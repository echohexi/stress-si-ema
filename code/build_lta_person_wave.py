from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd


EMA_LONG = Path("D:/R/research/study1_ema391_analysis_ready_long.csv")
SCALES = Path("all_scales_v5_FINAL.csv")
OUT_DIR = Path("data/derived")
OUT_CSV = OUT_DIR / "lta_person_wave_candidates.csv"
OUT_QA_JSON = OUT_DIR / "lta_person_wave_qa.json"
OUT_QA_MD = OUT_DIR / "lta_person_wave_qa.md"


EMA_REQUIRED = [
    "participant_id",
    "wave",
    "day_in_wave",
    "planned_hour_filled",
    "stress_any",
    "stress_count",
    "stress_sum_intensity",
    "stress_max_intensity",
    "belong_mean",
    "burden_mean",
    "entrap_mean",
    "lonely_mean",
    "si_passive",
    "si_active",
    "si_mean",
    "sleep_quality",
    "morning_fatigue",
    "expected_prompts",
    "prompts_answered",
    "response_rate",
]

SCALE_KEEP = [
    "pid",
    "CTQ_total_master",
    "CTQ_EA_master",
    "CTQ_PA_master",
    "CTQ_SA_master",
    "CTQ_EN_master",
    "CTQ_PN_master",
    "PANSI_neg_T1",
    "PANSI_total_risk_T1",
    "SuicideHist_T1_anyLifetime",
    "SuicideHist_T1_lastQuarter",
    "NSSI_count_T1",
    "NSSI_sum_T1",
    "BSS5_total_T1",
    "DASS_anx_T1",
    "DASS_dep_T1",
    "DASS_total_T1",
    "ES_total_T1",
    "CERQ_maladaptive_T1",
    "CERQ_adaptive_T1",
    "Lonely_total_T1",
    "PSQI_raw_sum_T1",
    "Connect_total_T2",
    "ERQ_reapp_T3",
    "ERQ_suppr_T3",
    "LPFS_total_T3",
    "BRS_total_T3",
]


def require_columns(df: pd.DataFrame, required: list[str], label: str) -> None:
    missing = [col for col in required if col not in df.columns]
    if missing:
        raise ValueError(f"{label} is missing required columns: {missing}")


def sd(series: pd.Series) -> float:
    return float(series.std(ddof=1)) if series.notna().sum() >= 2 else np.nan


def rmssd(series: pd.Series) -> float:
    values = series.dropna().to_numpy(dtype=float)
    if values.size < 2:
        return np.nan
    diffs = np.diff(values)
    return float(np.sqrt(np.mean(diffs**2)))


def wave_summary(group: pd.DataFrame) -> pd.Series:
    ordered = group.sort_values(["day_in_wave", "planned_hour_filled"])
    si_any_prompt = (
        (ordered["si_passive"] > 1)
        | (ordered["si_active"] > 1)
        | (ordered["si_mean"] > 1)
    )

    expected_prompts = ordered["expected_prompts"].max(skipna=True)
    if pd.isna(expected_prompts) or expected_prompts <= 0:
        expected_prompts = 21

    n_valid = int(len(ordered))
    response_rate = n_valid / float(expected_prompts)

    return pd.Series(
        {
            "n_valid_prompts": n_valid,
            "n_days_observed": int(ordered["day_in_wave"].nunique()),
            "expected_prompts": float(expected_prompts),
            "response_rate_wave": response_rate,
            "source_response_rate_max": ordered["response_rate"].max(skipna=True),
            "stress_any_prop": ordered["stress_any"].mean(skipna=True),
            "stress_count_mean": ordered["stress_count"].mean(skipna=True),
            "stress_sum_mean": ordered["stress_sum_intensity"].mean(skipna=True),
            "stress_sum_sd": sd(ordered["stress_sum_intensity"]),
            "stress_sum_rmssd": rmssd(ordered["stress_sum_intensity"]),
            "stress_max_mean": ordered["stress_max_intensity"].mean(skipna=True),
            "entrapment_mean": ordered["entrap_mean"].mean(skipna=True),
            "entrapment_sd": sd(ordered["entrap_mean"]),
            "burdensomeness_mean": ordered["burden_mean"].mean(skipna=True),
            "burdensomeness_sd": sd(ordered["burden_mean"]),
            "belongingness_mean": ordered["belong_mean"].mean(skipna=True),
            "belongingness_sd": sd(ordered["belong_mean"]),
            "loneliness_mean": ordered["lonely_mean"].mean(skipna=True),
            "loneliness_sd": sd(ordered["lonely_mean"]),
            "si_mean": ordered["si_mean"].mean(skipna=True),
            "si_sd": sd(ordered["si_mean"]),
            "si_rmssd": rmssd(ordered["si_mean"]),
            "si_any_prompt_prop": si_any_prompt.mean(),
            "si_any_wave": int(si_any_prompt.any()),
            "sleep_quality_mean": ordered["sleep_quality"].mean(skipna=True),
            "morning_fatigue_mean": ordered["morning_fatigue"].mean(skipna=True),
            "valid_threshold_6": int(n_valid >= 6),
            "valid_threshold_8": int(n_valid >= 8),
            "valid_threshold_10": int(n_valid >= 10),
        }
    )


def main() -> None:
    if not EMA_LONG.exists():
        raise FileNotFoundError(f"EMA long file not found: {EMA_LONG}")
    if not SCALES.exists():
        raise FileNotFoundError(f"Scale file not found: {SCALES}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)

    ema = pd.read_csv(EMA_LONG, usecols=EMA_REQUIRED, low_memory=False)
    scales = pd.read_csv(SCALES, low_memory=False)

    require_columns(ema, EMA_REQUIRED, "EMA long file")
    require_columns(scales, SCALE_KEEP, "scale file")

    ema["pid"] = pd.to_numeric(ema["participant_id"], errors="coerce")
    scales["pid"] = pd.to_numeric(scales["pid"], errors="coerce")

    person_wave = (
        ema.dropna(subset=["pid", "wave"])
        .groupby(["pid", "wave"], as_index=False)
        .apply(wave_summary, include_groups=False)
        .reset_index(drop=True)
    )

    keep_scales = [col for col in SCALE_KEEP if col in scales.columns]
    merged = person_wave.merge(scales[keep_scales], on="pid", how="left")
    merged["has_baseline_covariates"] = (
        merged.get("CTQ_total_master", pd.Series(index=merged.index, dtype=float)).notna()
        & merged.get("PANSI_neg_T1", pd.Series(index=merged.index, dtype=float)).notna()
        & merged.get("DASS_total_T1", pd.Series(index=merged.index, dtype=float)).notna()
    ).astype(int)
    merged["eligible_lta_threshold8"] = (merged["n_valid_prompts"] >= 8).astype(int)
    merged["eligible_lta_baseline_covariate_threshold8"] = (
        (merged["n_valid_prompts"] >= 8) & (merged["has_baseline_covariates"] == 1)
    ).astype(int)
    merged = merged.sort_values(["pid", "wave"]).reset_index(drop=True)

    merged.to_csv(OUT_CSV, index=False, encoding="utf-8-sig")

    indicator_cols = [
        "stress_sum_mean",
        "entrapment_mean",
        "burdensomeness_mean",
        "belongingness_mean",
        "loneliness_mean",
        "si_mean",
        "sleep_quality_mean",
        "morning_fatigue_mean",
    ]

    qa = {
        "inputs": {
            "ema_long": str(EMA_LONG),
            "scales": str(SCALES),
        },
        "output": str(OUT_CSV),
        "prompt_rows": int(len(ema)),
        "participants_in_ema": int(ema["pid"].nunique()),
        "participants_in_scales": int(scales["pid"].nunique()),
        "person_wave_rows": int(len(merged)),
        "participants_in_person_wave": int(merged["pid"].nunique()),
        "person_wave_rows_without_baseline_covariate_match": int(
            merged["CTQ_total_master"].isna().sum()
            if "CTQ_total_master" in merged.columns
            else -1
        ),
        "participants_in_scales_not_in_ema": int(
            len(set(scales["pid"].dropna()) - set(ema["pid"].dropna()))
        ),
        "participants_in_ema_not_in_scales": int(
            len(set(ema["pid"].dropna()) - set(scales["pid"].dropna()))
        ),
        "waves": sorted(int(w) for w in merged["wave"].dropna().unique()),
        "rows_by_wave": {
            str(int(k)): int(v) for k, v in merged.groupby("wave").size().items()
        },
        "valid_prompt_thresholds": {
            "at_least_6": int(merged["valid_threshold_6"].sum()),
            "at_least_8": int(merged["valid_threshold_8"].sum()),
            "at_least_10": int(merged["valid_threshold_10"].sum()),
        },
        "eligible_participants": {
            "ema_any_wave": int(merged["pid"].nunique()),
            "all_four_waves_threshold8": int(
                merged.groupby("pid")["eligible_lta_threshold8"].sum().eq(4).sum()
            ),
            "all_four_waves_threshold8_with_baseline_covariates": int(
                merged.groupby("pid")["eligible_lta_baseline_covariate_threshold8"].sum().eq(4).sum()
            ),
            "with_baseline_covariates_any_wave": int(
                merged.loc[merged["has_baseline_covariates"].eq(1), "pid"].nunique()
            ),
        },
        "si_any_wave_rate_by_wave": {
            str(int(k)): float(v)
            for k, v in merged.groupby("wave")["si_any_wave"].mean().items()
        },
        "missing_rate_core_indicators": {
            col: float(merged[col].isna().mean()) for col in indicator_cols
        },
        "response_rate_wave_summary": {
            "mean": float(merged["response_rate_wave"].mean()),
            "sd": float(merged["response_rate_wave"].std(ddof=1)),
            "min": float(merged["response_rate_wave"].min()),
            "median": float(merged["response_rate_wave"].median()),
            "max": float(merged["response_rate_wave"].max()),
        },
    }

    OUT_QA_JSON.write_text(
        json.dumps(qa, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    md = [
        "# LTA Person-Wave QA",
        "",
        f"- Prompt-level rows: {qa['prompt_rows']}",
        f"- EMA participants: {qa['participants_in_ema']}",
        f"- Scale-file participants: {qa['participants_in_scales']}",
        f"- Person-wave rows: {qa['person_wave_rows']}",
        f"- Person-wave participants: {qa['participants_in_person_wave']}",
        f"- Person-wave rows without baseline covariate match: {qa['person_wave_rows_without_baseline_covariate_match']}",
        f"- Scale participants not in EMA: {qa['participants_in_scales_not_in_ema']}",
        f"- EMA participants not in scales: {qa['participants_in_ema_not_in_scales']}",
        f"- Waves: {', '.join(map(str, qa['waves']))}",
        "",
        "## Rows by Wave",
        "",
    ]
    for wave, n in qa["rows_by_wave"].items():
        md.append(f"- Wave {wave}: {n}")
    md.extend(["", "## Valid Prompt Thresholds", ""])
    for key, n in qa["valid_prompt_thresholds"].items():
        md.append(f"- {key}: {n}")
    md.extend(["", "## Eligible Participants", ""])
    for key, n in qa["eligible_participants"].items():
        md.append(f"- {key}: {n}")
    md.extend(["", "## SI Any-Wave Rate", ""])
    for wave, rate in qa["si_any_wave_rate_by_wave"].items():
        md.append(f"- Wave {wave}: {rate:.3f}")
    md.extend(["", "## Missing Rate: Core Indicators", ""])
    for col, rate in qa["missing_rate_core_indicators"].items():
        md.append(f"- {col}: {rate:.3f}")
    md.extend(["", "## Response Rate Summary", ""])
    for key, value in qa["response_rate_wave_summary"].items():
        md.append(f"- {key}: {value:.3f}")
    md.append("")

    OUT_QA_MD.write_text("\n".join(md), encoding="utf-8")

    print(f"Wrote {OUT_CSV}")
    print(f"Wrote {OUT_QA_JSON}")
    print(f"Wrote {OUT_QA_MD}")
    print(json.dumps(qa, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
