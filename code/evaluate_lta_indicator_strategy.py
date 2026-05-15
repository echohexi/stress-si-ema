from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


IN_CSV = Path("data/derived/lta_person_wave_balanced_threshold8.csv")
OUT_DIR = Path("data/derived")
OUT_JSON = OUT_DIR / "lta_indicator_strategy_eval.json"
OUT_MD = OUT_DIR / "lta_indicator_strategy_eval.md"


CORE = [
    "stress_sum_mean",
    "entrapment_mean",
    "burdensomeness_mean",
    "belongingness_mean",
    "loneliness_mean",
    "si_mean",
    "si_any_prompt_prop",
    "sleep_quality_mean",
    "morning_fatigue_mean",
]


def summarize_distribution(df: pd.DataFrame, col: str) -> dict:
    s = df[col].dropna()
    return {
        "n": int(s.size),
        "mean": float(s.mean()),
        "sd": float(s.std(ddof=1)),
        "min": float(s.min()),
        "p25": float(s.quantile(0.25)),
        "median": float(s.median()),
        "p75": float(s.quantile(0.75)),
        "max": float(s.max()),
        "floor_rate_at_min": float((s == s.min()).mean()),
        "zero_rate": float((s == 0).mean()),
    }


def main() -> None:
    if not IN_CSV.exists():
        raise FileNotFoundError(f"Missing input: {IN_CSV}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(IN_CSV)

    dist = {
        col: summarize_distribution(df, col)
        for col in CORE
        if col in df.columns
    }

    by_wave = {}
    for wave, g in df.groupby("wave"):
        by_wave[str(int(wave))] = {
            col: summarize_distribution(g, col)
            for col in CORE
            if col in g.columns
        }

    corr = df[CORE].corr(method="spearman").round(3)
    si_corr = corr["si_mean"].sort_values(ascending=False).to_dict()

    si_floor = dist["si_mean"]["floor_rate_at_min"]
    si_any_zero = dist["si_any_prompt_prop"]["zero_rate"]
    si_any_wave_rate = {
        str(int(w)): float(v)
        for w, v in df.groupby("wave")["si_any_wave"].mean().items()
    }

    recommendation = {
        "primary_indicator_strategy": "use_si_as_distal_outcome",
        "primary_state_indicators": [
            "stress_sum_mean",
            "entrapment_mean",
            "burdensomeness_mean",
            "belongingness_mean",
            "loneliness_mean",
        ],
        "sensitivity_indicator_strategy": "include_si_mean_as_state_indicator",
        "rationale": [
            "SI has strong floor concentration and should not be allowed to dominate state formation in the main model.",
            "The IMV/IPT proximal indicators plus loneliness define daily-life risk states while preserving SI for outcome validation.",
            "Including SI as a state indicator remains important as a sensitivity check because suicide-risk state labels should predict SI.",
        ],
    }

    qa = {
        "input": str(IN_CSV),
        "n_rows": int(len(df)),
        "n_participants": int(df["pid"].nunique()),
        "n_waves": int(df["wave"].nunique()),
        "overall_distribution": dist,
        "by_wave_distribution": by_wave,
        "spearman_correlation_with_si_mean": si_corr,
        "si_floor_rate": si_floor,
        "si_any_prompt_zero_rate": si_any_zero,
        "si_any_wave_rate": si_any_wave_rate,
        "recommendation": recommendation,
    }

    OUT_JSON.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    lines = [
        "# LTA Indicator Strategy Evaluation",
        "",
        f"- Input: `{IN_CSV}`",
        f"- Rows: {qa['n_rows']}",
        f"- Participants: {qa['n_participants']}",
        f"- Waves: {qa['n_waves']}",
        "",
        "## Main Recommendation",
        "",
        "- Primary strategy: use SI as a distal outcome, not a main state indicator.",
        "- Primary state indicators: stress, entrapment, burdensomeness, belongingness, loneliness.",
        "- Sensitivity strategy: include `si_mean` as a state indicator and check whether the transition story changes.",
        "",
        "## SI Floor and Sparsity",
        "",
        f"- `si_mean` floor rate: {si_floor:.3f}",
        f"- `si_any_prompt_prop` zero rate: {si_any_zero:.3f}",
        "",
        "## SI Any-Wave Rate",
        "",
    ]
    for wave, rate in si_any_wave_rate.items():
        lines.append(f"- Wave {wave}: {rate:.3f}")

    lines.extend(["", "## Spearman Correlation With `si_mean`", ""])
    for key, value in si_corr.items():
        lines.append(f"- {key}: {value:.3f}")

    lines.extend(["", "## Indicator Distribution Summary", ""])
    for col, values in dist.items():
        lines.append(
            f"- {col}: mean={values['mean']:.3f}, sd={values['sd']:.3f}, "
            f"median={values['median']:.3f}, min={values['min']:.3f}, "
            f"max={values['max']:.3f}, floor={values['floor_rate_at_min']:.3f}"
        )
    lines.append("")

    OUT_MD.write_text("\n".join(lines), encoding="utf-8")

    print(f"Wrote {OUT_JSON}")
    print(f"Wrote {OUT_MD}")
    print("\n".join(lines[:36]))


if __name__ == "__main__":
    main()
