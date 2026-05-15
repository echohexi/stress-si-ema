from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


IN_CSV = Path("data/derived/lta_person_wave_candidates.csv")
OUT_DIR = Path("data/derived")
LONG_THRESHOLD8 = OUT_DIR / "lta_person_wave_threshold8.csv"
LONG_BALANCED_THRESHOLD8 = OUT_DIR / "lta_person_wave_balanced_threshold8.csv"
LONG_BALANCED_BASELINE_COVARIATE_THRESHOLD8 = (
    OUT_DIR / "lta_person_wave_balanced_baseline_covariate_threshold8.csv"
)
WIDE_BALANCED_THRESHOLD8 = OUT_DIR / "lta_wide_balanced_threshold8.csv"
INDICATOR_DESC = OUT_DIR / "lta_indicator_descriptives_threshold8.csv"
INDICATOR_CORR = OUT_DIR / "lta_indicator_correlations_threshold8.csv"
OUT_QA = OUT_DIR / "lta_analysis_sets_qa.json"
OUT_MD = OUT_DIR / "lta_analysis_sets_qa.md"


INDICATORS = [
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


def main() -> None:
    if not IN_CSV.exists():
        raise FileNotFoundError(f"Run build_lta_person_wave.py first: {IN_CSV}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(IN_CSV)

    threshold8 = df[df["valid_threshold_8"].eq(1)].copy()

    wave_counts = threshold8.groupby("pid")["wave"].nunique()
    balanced_pids = wave_counts[wave_counts.eq(4)].index
    balanced = threshold8[threshold8["pid"].isin(balanced_pids)].copy()

    baseline_covariate_wave_counts = threshold8[
        threshold8["has_baseline_covariates"].eq(1)
    ].groupby("pid")["wave"].nunique()
    baseline_covariate_pids = baseline_covariate_wave_counts[
        baseline_covariate_wave_counts.eq(4)
    ].index
    balanced_baseline_covariate = threshold8[
        threshold8["pid"].isin(baseline_covariate_pids)
    ].copy()

    threshold8.to_csv(LONG_THRESHOLD8, index=False, encoding="utf-8-sig")
    balanced.to_csv(LONG_BALANCED_THRESHOLD8, index=False, encoding="utf-8-sig")
    balanced_baseline_covariate.to_csv(
        LONG_BALANCED_BASELINE_COVARIATE_THRESHOLD8, index=False, encoding="utf-8-sig"
    )

    wide_parts = []
    for wave in sorted(balanced["wave"].unique()):
        wave_df = balanced[balanced["wave"].eq(wave)].copy()
        cols = ["pid"] + INDICATORS
        wave_df = wave_df[cols]
        wave_df = wave_df.rename(
            columns={col: f"{col}_w{int(wave)}" for col in INDICATORS}
        )
        wide_parts.append(wave_df)

    wide = wide_parts[0]
    for part in wide_parts[1:]:
        wide = wide.merge(part, on="pid", how="inner")

    wide.to_csv(WIDE_BALANCED_THRESHOLD8, index=False, encoding="utf-8-sig")

    desc = (
        threshold8.groupby("wave")[INDICATORS]
        .agg(["count", "mean", "std", "min", "median", "max"])
        .round(4)
    )
    desc.columns = ["_".join(col).strip() for col in desc.columns.to_flat_index()]
    desc.reset_index().to_csv(INDICATOR_DESC, index=False, encoding="utf-8-sig")

    corr = threshold8[INDICATORS].corr().round(4)
    corr.to_csv(INDICATOR_CORR, encoding="utf-8-sig")

    qa = {
        "inputs": str(IN_CSV),
        "outputs": {
            "long_threshold8": str(LONG_THRESHOLD8),
            "long_balanced_threshold8": str(LONG_BALANCED_THRESHOLD8),
            "long_balanced_baseline_covariate_threshold8": str(
                LONG_BALANCED_BASELINE_COVARIATE_THRESHOLD8
            ),
            "wide_balanced_threshold8": str(WIDE_BALANCED_THRESHOLD8),
            "indicator_descriptives": str(INDICATOR_DESC),
            "indicator_correlations": str(INDICATOR_CORR),
        },
        "rows": {
            "candidate": int(len(df)),
            "threshold8": int(len(threshold8)),
            "balanced_threshold8": int(len(balanced)),
            "balanced_baseline_covariate_threshold8": int(len(balanced_baseline_covariate)),
            "wide_balanced_threshold8": int(len(wide)),
        },
        "participants": {
            "candidate": int(df["pid"].nunique()),
            "threshold8_any_wave": int(threshold8["pid"].nunique()),
            "balanced_threshold8": int(balanced["pid"].nunique()),
            "balanced_baseline_covariate_threshold8": int(
                balanced_baseline_covariate["pid"].nunique()
            ),
            "wide_balanced_threshold8": int(wide["pid"].nunique()),
        },
        "rows_by_wave_threshold8": {
            str(int(k)): int(v) for k, v in threshold8.groupby("wave").size().items()
        },
        "rows_by_wave_balanced_threshold8": {
            str(int(k)): int(v) for k, v in balanced.groupby("wave").size().items()
        },
        "candidate_indicators": INDICATORS,
    }

    OUT_QA.write_text(json.dumps(qa, ensure_ascii=False, indent=2), encoding="utf-8")

    md = [
        "# LTA Analysis Sets QA",
        "",
        "## Rows",
        "",
    ]
    for key, value in qa["rows"].items():
        md.append(f"- {key}: {value}")
    md.extend(["", "## Participants", ""])
    for key, value in qa["participants"].items():
        md.append(f"- {key}: {value}")
    md.extend(["", "## Threshold-8 Rows by Wave", ""])
    for wave, value in qa["rows_by_wave_threshold8"].items():
        md.append(f"- Wave {wave}: {value}")
    md.extend(["", "## Balanced Threshold-8 Rows by Wave", ""])
    for wave, value in qa["rows_by_wave_balanced_threshold8"].items():
        md.append(f"- Wave {wave}: {value}")
    md.extend(["", "## Candidate Indicators", ""])
    for indicator in INDICATORS:
        md.append(f"- {indicator}")
    md.append("")

    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    print(json.dumps(qa, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
