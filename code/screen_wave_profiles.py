from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd


IN_CSV = Path("data/derived/lta_person_wave_balanced_threshold8.csv")
OUT_DIR = Path("data/derived")
FIT_OUT = OUT_DIR / "wave_profile_screen_fit_indices.csv"
PROFILE_OUT = OUT_DIR / "wave_profile_screen_class_profiles.csv"


MODEL_SPECS = {
    "imv_ipt_with_si": [
        "stress_sum_mean",
        "entrapment_mean",
        "burdensomeness_mean",
        "belongingness_mean",
        "si_mean",
    ],
    "imv_ipt_with_loneliness_no_si": [
        "stress_sum_mean",
        "entrapment_mean",
        "burdensomeness_mean",
        "belongingness_mean",
        "loneliness_mean",
    ],
}


@dataclass
class GmmResult:
    weights: np.ndarray
    means: np.ndarray
    variances: np.ndarray
    responsibilities: np.ndarray
    loglik: float
    n_iter: int


def logsumexp(a: np.ndarray, axis: int = 1) -> np.ndarray:
    amax = np.max(a, axis=axis, keepdims=True)
    return (amax + np.log(np.sum(np.exp(a - amax), axis=axis, keepdims=True))).squeeze(axis)


def fit_diag_gmm(
    x: np.ndarray,
    k: int,
    *,
    n_starts: int = 80,
    max_iter: int = 500,
    tol: float = 1e-6,
    seed: int = 20260514,
) -> GmmResult:
    rng = np.random.default_rng(seed + k)
    n, d = x.shape
    best: GmmResult | None = None
    var_floor = 1e-4

    for _ in range(n_starts):
        init_idx = rng.choice(n, size=k, replace=False)
        means = x[init_idx].copy()
        variances = np.tile(np.var(x, axis=0) + var_floor, (k, 1))
        weights = np.repeat(1 / k, k)
        previous_loglik = -np.inf

        for iteration in range(1, max_iter + 1):
            log_prob = np.empty((n, k))
            for cls in range(k):
                var = np.maximum(variances[cls], var_floor)
                log_det = np.sum(np.log(var))
                sq = np.sum(((x - means[cls]) ** 2) / var, axis=1)
                log_prob[:, cls] = (
                    np.log(weights[cls] + 1e-12)
                    - 0.5 * (d * np.log(2 * np.pi) + log_det + sq)
                )

            row_lse = logsumexp(log_prob, axis=1)
            loglik = float(np.sum(row_lse))
            resp = np.exp(log_prob - row_lse[:, None])

            nk = np.maximum(resp.sum(axis=0), 1e-8)
            weights = nk / n
            means = (resp.T @ x) / nk[:, None]
            for cls in range(k):
                diff = x - means[cls]
                variances[cls] = (resp[:, cls][:, None] * diff**2).sum(axis=0) / nk[cls]
            variances = np.maximum(variances, var_floor)

            if abs(loglik - previous_loglik) < tol:
                break
            previous_loglik = loglik

        result = GmmResult(weights, means, variances, resp, loglik, iteration)
        if best is None or result.loglik > best.loglik:
            best = result

    assert best is not None
    return best


def standardize(frame: pd.DataFrame, cols: list[str]) -> tuple[np.ndarray, pd.Series, pd.Series]:
    means = frame[cols].mean()
    sds = frame[cols].std(ddof=1).replace(0, np.nan)
    z = (frame[cols] - means) / sds
    if z.isna().any().any():
        raise ValueError(f"Missing or constant values in columns: {cols}")
    return z.to_numpy(dtype=float), means, sds


def normalized_entropy(resp: np.ndarray) -> float:
    n, k = resp.shape
    if k <= 1:
        return 1.0
    raw = -np.sum(resp * np.log(resp + 1e-12))
    return float(1 - raw / (n * np.log(k)))


def main() -> None:
    if not IN_CSV.exists():
        raise FileNotFoundError(f"Run prepare_lta_analysis_sets.py first: {IN_CSV}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(IN_CSV)

    fit_rows: list[dict] = []
    profile_rows: list[dict] = []

    for model_name, indicators in MODEL_SPECS.items():
        for wave in sorted(df["wave"].unique()):
            wave_df = df[df["wave"].eq(wave)].copy()
            wave_df = wave_df.dropna(subset=indicators)
            x, _, _ = standardize(wave_df, indicators)
            n, d = x.shape

            for k in range(2, 6):
                result = fit_diag_gmm(x, k, seed=20260514 + int(wave) * 100)
                assigned = result.responsibilities.argmax(axis=1)
                counts = np.bincount(assigned, minlength=k)
                min_class_n = int(counts.min())
                min_class_pct = float(counts.min() / n)
                entropy = normalized_entropy(result.responsibilities)
                appa = float(result.responsibilities.max(axis=1).mean())
                n_params = (k - 1) + k * d + k * d
                bic = float(n_params * np.log(n) - 2 * result.loglik)
                aic = float(2 * n_params - 2 * result.loglik)

                fit_rows.append(
                    {
                        "model": model_name,
                        "wave": int(wave),
                        "n_classes": k,
                        "n": n,
                        "n_indicators": d,
                        "loglik": result.loglik,
                        "n_parameters": n_params,
                        "aic": aic,
                        "bic": bic,
                        "entropy": entropy,
                        "appa": appa,
                        "smallest_class_n": min_class_n,
                        "smallest_class_pct": min_class_pct,
                        "n_iter_best_start": result.n_iter,
                    }
                )

                tmp = wave_df[["pid", "wave"] + indicators].copy()
                tmp["class"] = assigned + 1
                for cls in range(k):
                    cls_df = tmp[tmp["class"].eq(cls + 1)]
                    profile = {
                        "model": model_name,
                        "wave": int(wave),
                        "n_classes": k,
                        "class": cls + 1,
                        "class_n": int(len(cls_df)),
                        "class_pct": float(len(cls_df) / n),
                    }
                    for col in indicators:
                        profile[f"{col}_raw_mean"] = float(cls_df[col].mean())
                    profile_rows.append(profile)

    pd.DataFrame(fit_rows).sort_values(
        ["model", "wave", "n_classes"]
    ).to_csv(FIT_OUT, index=False, encoding="utf-8-sig")
    pd.DataFrame(profile_rows).sort_values(
        ["model", "wave", "n_classes", "class"]
    ).to_csv(PROFILE_OUT, index=False, encoding="utf-8-sig")

    print(f"Wrote {FIT_OUT}")
    print(f"Wrote {PROFILE_OUT}")
    print(pd.DataFrame(fit_rows).sort_values(["model", "wave", "bic"]).groupby(["model", "wave"]).head(2).to_string(index=False))


if __name__ == "__main__":
    main()
