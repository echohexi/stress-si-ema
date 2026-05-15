from __future__ import annotations

import json
from pathlib import Path

import pandas as pd


IN_CSV = Path("data/derived/lta_person_wave_balanced_threshold8.csv")
OUT_DIR = Path("mplus/lta_unconditional")
DATA_FILE = OUT_DIR / "lta_primary_z_wide.dat"
CODEBOOK_FILE = OUT_DIR / "lta_primary_z_codebook.json"

PRIMARY_INDICATORS = {
    "stress_sum_mean": "st",
    "entrapment_mean": "en",
    "burdensomeness_mean": "bu",
    "belongingness_mean": "be",
    "loneliness_mean": "lo",
}

DISTAL_OUTCOMES = {
    "si_mean": "si",
    "si_any_wave": "saw",
    "si_any_prompt_prop": "sap",
}


def zscore(series: pd.Series) -> pd.Series:
    return (series - series.mean()) / series.std(ddof=1)


def build_wide(df: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    df = df.copy()
    df["pid"] = pd.to_numeric(df["pid"], errors="coerce")

    standardization: dict[str, dict[str, float]] = {}
    for raw_col in PRIMARY_INDICATORS:
        standardization[raw_col] = {
            "mean": float(df[raw_col].mean()),
            "sd": float(df[raw_col].std(ddof=1)),
        }
        df[f"{raw_col}_z"] = zscore(df[raw_col])

    wide = pd.DataFrame({"id": sorted(df["pid"].unique())})
    for wave in [1, 2, 3, 4]:
        wdf = df[df["wave"].eq(wave)].copy()
        wave_cols = ["pid"]
        rename_map = {"pid": "id"}
        for raw_col, short in PRIMARY_INDICATORS.items():
            z_col = f"{raw_col}_z"
            out_col = f"{short}{wave}"
            wave_cols.append(z_col)
            rename_map[z_col] = out_col
        for raw_col, short in DISTAL_OUTCOMES.items():
            out_col = f"{short}{wave}"
            wave_cols.append(raw_col)
            rename_map[raw_col] = out_col
        wdf = wdf[wave_cols].rename(columns=rename_map)
        wide = wide.merge(wdf, on="id", how="inner")

    return wide, standardization


def invariant_model_block(n_states: int, indicators: list[str]) -> str:
    lines: list[str] = []
    # Equal residual variances across waves for each indicator.
    for ind in indicators:
        labels = " ".join(f"{ind}{wave}" for wave in [1, 2, 3, 4])
        lines.append(f"  {labels} (v{ind});")
    lines.append("")
    lines.append("  c2 ON c1;")
    lines.append("  c3 ON c2;")
    lines.append("  c4 ON c3;")
    lines.append("")

    for wave, c_name in enumerate(["c1", "c2", "c3", "c4"], start=1):
        lines.append(f"MODEL {c_name}:")
        for state in range(1, n_states + 1):
            lines.append(f"  %{c_name}#{state}%")
            for ind in indicators:
                lines.append(f"    [{ind}{wave}] (m{ind}{state});")
        lines.append("")
    return "\n".join(lines).rstrip()


def configural_model_block(n_states: int, indicators: list[str]) -> str:
    lines: list[str] = []
    for ind in indicators:
        labels = " ".join(f"{ind}{wave}" for wave in [1, 2, 3, 4])
        lines.append(f"  {labels} (v{ind});")
    lines.append("")
    lines.append("  c2 ON c1;")
    lines.append("  c3 ON c2;")
    lines.append("  c4 ON c3;")
    lines.append("")

    for wave, c_name in enumerate(["c1", "c2", "c3", "c4"], start=1):
        lines.append(f"MODEL {c_name}:")
        for state in range(1, n_states + 1):
            lines.append(f"  %{c_name}#{state}%")
            for ind in indicators:
                lines.append(f"    [{ind}{wave}];")
        lines.append("")
    return "\n".join(lines).rstrip()


def wrap_mplus_list(items: list[str], indent: str = "  ", per_line: int = 8) -> str:
    lines = []
    for i in range(0, len(items), per_line):
        lines.append(indent + " ".join(items[i : i + per_line]))
    return "\n".join(lines)


def mplus_input(
    n_states: int,
    invariant: bool,
    variable_names: list[str],
    *,
    starts: str = "1200 300",
    stiterations: int = 30,
    processors: int = 4,
    smoke: bool = False,
    run_label: str | None = None,
) -> str:
    indicators = ["st", "en", "bu", "be", "lo"]
    usevars = [f"{ind}{wave}" for wave in [1, 2, 3, 4] for ind in indicators]
    title_kind = "measurement-invariant" if invariant else "configural"
    if smoke and run_label is None:
        run_label = "smoke"
    title_prefix = ""
    if run_label == "smoke":
        title_prefix = "SMOKE TEST "
    elif run_label == "pilot":
        title_prefix = "PILOT "
    save_suffix = f"_{run_label}" if run_label else ""
    model_block = (
        invariant_model_block(n_states, indicators)
        if invariant
        else configural_model_block(n_states, indicators)
    )
    return f"""TITLE:
  {title_prefix}EMA-derived {n_states}-state unconditional LTA ({title_kind});

DATA:
  FILE IS lta_primary_z_wide.dat;

VARIABLE:
  NAMES ARE
{wrap_mplus_list(variable_names, indent='    ', per_line=8)};
  USEVARIABLES ARE
{wrap_mplus_list(usevars, indent='    ', per_line=8)};
  IDVARIABLE IS id;
  CLASSES = c1({n_states}) c2({n_states}) c3({n_states}) c4({n_states});
  MISSING ARE ALL (-999);

ANALYSIS:
  TYPE = MIXTURE;
  STARTS = {starts};
  STITERATIONS = {stiterations};
  PROCESSORS = {processors};

MODEL:
%OVERALL%
{model_block}

OUTPUT:
  TECH1 TECH4 TECH8 TECH15;

SAVEDATA:
  FILE IS lta_{n_states}state_{'invariant' if invariant else 'configural'}{save_suffix}_cprob.dat;
  SAVE = CPROBABILITIES;
"""


def main() -> None:
    if not IN_CSV.exists():
        raise FileNotFoundError(f"Missing input: {IN_CSV}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(IN_CSV)
    wide, standardization = build_wide(df)
    wide = wide.fillna(-999)

    variable_names = list(wide.columns)
    wide.to_csv(DATA_FILE, sep=" ", header=False, index=False, float_format="%.8f")

    codebook = {
        "input": str(IN_CSV),
        "data_file": str(DATA_FILE),
        "n_participants": int(wide["id"].nunique()),
        "n_rows": int(len(wide)),
        "primary_indicators_raw_to_short": PRIMARY_INDICATORS,
        "distal_outcomes_raw_to_short": DISTAL_OUTCOMES,
        "variable_names": variable_names,
        "standardization": standardization,
        "model_notes": [
            "Primary indicators were globally z-standardized across all balanced person-wave rows.",
            "SI variables are retained in the data file for later distal validation but are not used in unconditional LTA inputs.",
            "The primary unconditional LTA uses measurement-invariant class-specific means across waves to keep state labels comparable over time.",
        ],
    }
    CODEBOOK_FILE.write_text(json.dumps(codebook, ensure_ascii=False, indent=2), encoding="utf-8")

    for n_states in [3, 4]:
        for invariant in [True, False]:
            suffix = "invariant" if invariant else "configural"
            inp = OUT_DIR / f"lta_{n_states}state_{suffix}.inp"
            inp.write_text(mplus_input(n_states, invariant, variable_names), encoding="utf-8")
            smoke_inp = OUT_DIR / f"lta_{n_states}state_{suffix}_smoke.inp"
            smoke_inp.write_text(
                mplus_input(
                    n_states,
                    invariant,
                    variable_names,
                    starts="40 10",
                    stiterations=15,
                    processors=4,
                    run_label="smoke",
                ),
                encoding="utf-8",
            )
            pilot_inp = OUT_DIR / f"lta_{n_states}state_{suffix}_pilot.inp"
            pilot_inp.write_text(
                mplus_input(
                    n_states,
                    invariant,
                    variable_names,
                    starts="200 50",
                    stiterations=20,
                    processors=4,
                    run_label="pilot",
                ),
                encoding="utf-8",
            )

    print(f"Wrote {DATA_FILE}")
    print(f"Wrote {CODEBOOK_FILE}")
    for path in sorted(OUT_DIR.glob("*.inp")):
        print(f"Wrote {path}")
    print(json.dumps({k: codebook[k] for k in ["n_rows", "n_participants", "variable_names"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
