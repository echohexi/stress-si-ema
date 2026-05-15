from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MPLUS_DIR = ROOT / "mplus" / "lta_unconditional"
OUT_DIR = ROOT / "data" / "derived"

INDICATORS = ["ST", "EN", "BU", "BE", "LO"]
INDICATOR_LABELS = {
    "ST": "stress",
    "EN": "entrapment",
    "BU": "burdensomeness",
    "BE": "belongingness",
    "LO": "loneliness",
}


def grab_float(text: str, pattern: str) -> float | None:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    return float(match.group(1)) if match else None


def grab_int(text: str, pattern: str) -> int | None:
    match = re.search(pattern, text, flags=re.IGNORECASE)
    return int(match.group(1)) if match else None


def parse_metadata(path: Path) -> dict[str, object]:
    match = re.search(r"lta_(\d+)state_([a-z]+)_([a-z]+)\.out$", path.name)
    if not match:
        return {"model": path.stem, "n_states": None, "constraint": None, "run_type": None}
    n_states, constraint, run_type = match.groups()
    return {
        "model": path.stem,
        "n_states": int(n_states),
        "constraint": constraint,
        "run_type": run_type,
    }


def parse_warning_summary(text: str) -> tuple[str, str]:
    warnings: list[str] = []
    if "All variables are uncorrelated with all other variables within class" in text:
        warnings.append("local_independence_warning")
    if "MULTINOMIAL LOGIT PARAMETERS WERE FIXED TO AVOID SINGULARITY" in text:
        warnings.append("fixed_transition_logits_empty_cells")
    if "THE BEST LOGLIKELIHOOD VALUE WAS NOT REPLICATED" in text:
        warnings.append("best_loglikelihood_not_replicated")
    if "NON-POSITIVE DEFINITE FIRST-ORDER DERIVATIVE PRODUCT MATRIX" in text:
        warnings.append("nonpositive_derivative_product_matrix")
    if "THE MODEL ESTIMATION TERMINATED NORMALLY" not in text:
        warnings.append("no_normal_termination_marker")

    fixed_params = re.findall(r"Parameter\s+\d+,\s+([^\r\n]+)", text)
    return ";".join(warnings) if warnings else "none", "; ".join(fixed_params)


def parse_fit(path: Path, text: str) -> dict[str, object]:
    row = parse_metadata(path)
    warnings, fixed_params = parse_warning_summary(text)
    row.update(
        {
            "n_observations": grab_int(text, r"Number of observations\s+(\d+)"),
            "n_free_parameters": grab_int(text, r"Number of Free Parameters\s+(\d+)"),
            "loglikelihood_h0": grab_float(text, r"H0 Value\s+(-?\d+\.\d+)"),
            "aic": grab_float(text, r"Akaike \(AIC\)\s+(-?\d+\.\d+)"),
            "bic": grab_float(text, r"Bayesian \(BIC\)\s+(-?\d+\.\d+)"),
            "ssabic": grab_float(text, r"Sample-Size Adjusted BIC\s+(-?\d+\.\d+)"),
            "entropy": grab_float(text, r"Entropy\s+(-?\d+\.\d+)"),
            "condition_number": grab_float(
                text,
                r"Condition Number for the Information Matrix\s+([0-9.]+E[+-]?\d+)",
            ),
            "best_loglikelihood_replicated": "THE BEST LOGLIKELIHOOD VALUE HAS BEEN REPLICATED" in text,
            "normal_termination": "THE MODEL ESTIMATION TERMINATED NORMALLY" in text,
            "warnings": warnings,
            "fixed_transition_parameters": fixed_params,
        }
    )
    return row


def parse_class_counts(text: str, model: str) -> list[dict[str, object]]:
    section_match = re.search(
        r"FINAL CLASS COUNTS AND PROPORTIONS FOR EACH LATENT CLASS VARIABLE\s+"
        r"BASED ON THE ESTIMATED MODEL(?P<section>.*?)LATENT TRANSITION PROBABILITIES",
        text,
        flags=re.DOTALL,
    )
    if not section_match:
        return []

    rows: list[dict[str, object]] = []
    current_wave: int | None = None
    for line in section_match.group("section").splitlines():
        match = re.match(r"\s*C(\d+)\s+(\d+)\s+([0-9.]+)\s+([0-9.]+)", line)
        if match:
            wave, klass, count, proportion = match.groups()
            current_wave = int(wave)
        else:
            match = re.match(r"\s+(\d+)\s+([0-9.]+)\s+([0-9.]+)", line)
            if not match or current_wave is None:
                continue
            klass, count, proportion = match.groups()
            wave = current_wave

        rows.append(
            {
                "model": model,
                "wave": int(wave),
                "class": int(klass),
                "estimated_n": float(count),
                "estimated_proportion": float(proportion),
            }
        )
    return rows


def parse_transition_probabilities(text: str, model: str) -> list[dict[str, object]]:
    section_match = re.search(
        r"LATENT TRANSITION PROBABILITIES BASED ON THE ESTIMATED MODEL(?P<section>.*?)"
        r"FINAL CLASS COUNTS AND PROPORTIONS FOR THE LATENT CLASS PATTERNS",
        text,
        flags=re.DOTALL,
    )
    if not section_match:
        return []

    rows: list[dict[str, object]] = []
    current_from_wave: int | None = None
    current_to_wave: int | None = None
    to_classes: list[int] = []

    for line in section_match.group("section").splitlines():
        header = re.search(r"C(\d+) Classes \(Rows\) by C(\d+) Classes \(Columns\)", line)
        if header:
            current_from_wave = int(header.group(1))
            current_to_wave = int(header.group(2))
            to_classes = []
            continue

        if current_from_wave is None or current_to_wave is None:
            continue

        col_header = re.match(r"\s+((?:\d+\s*)+)$", line)
        if col_header:
            to_classes = [int(x) for x in col_header.group(1).split()]
            continue

        values = re.match(r"\s+(\d+)\s+(.+)$", line)
        if values and to_classes:
            from_class = int(values.group(1))
            probs = [float(x) for x in values.group(2).split()]
            for to_class, prob in zip(to_classes, probs, strict=False):
                rows.append(
                    {
                        "model": model,
                        "from_wave": current_from_wave,
                        "to_wave": current_to_wave,
                        "from_class": from_class,
                        "to_class": to_class,
                        "probability": prob,
                    }
                )
    return rows


def parse_class_means(text: str, model: str, n_states: int | None) -> list[dict[str, object]]:
    if n_states is None:
        return []

    rows: list[dict[str, object]] = []
    for klass in range(1, n_states + 1):
        pattern = " ".join(["1", "1", "1", str(klass)])
        section_match = re.search(
            rf"Latent Class Pattern {re.escape(pattern)}\s+Means(?P<section>.*?)\s+Variances",
            text,
            flags=re.DOTALL,
        )
        if not section_match:
            continue

        section = section_match.group("section")
        for indicator in INDICATORS:
            mean = grab_float(section, rf"\b{indicator}4\s+(-?\d+\.\d+)")
            if mean is not None:
                rows.append(
                    {
                        "model": model,
                        "class": klass,
                        "indicator": INDICATOR_LABELS[indicator],
                        "z_mean": mean,
                    }
                )
    return rows


def write_csv(path: Path, rows: list[dict[str, object]]) -> None:
    if not rows:
        path.write_text("", encoding="utf-8")
        return
    with path.open("w", newline="", encoding="utf-8-sig") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def markdown_table(rows: list[dict[str, object]], columns: list[str]) -> str:
    def fmt(value: object) -> str:
        if isinstance(value, float):
            return f"{value:.3f}"
        return str(value)

    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(fmt(row.get(col, "")) for col in columns) + " |")
    return "\n".join(lines)


def build_markdown(fit_rows: list[dict[str, object]], class_rows: list[dict[str, object]]) -> str:
    fit_cols = [
        "model",
        "n_states",
        "run_type",
        "loglikelihood_h0",
        "aic",
        "bic",
        "ssabic",
        "entropy",
        "best_loglikelihood_replicated",
        "warnings",
    ]

    lines = [
        "# LTA Unconditional Model Parsing Summary",
        "",
        "## Fit Summary",
        "",
        markdown_table(fit_rows, fit_cols),
        "",
        "## Model Decision Notes",
        "",
        "- The 4-state invariant pilot model improves information criteria substantially relative to the 3-state invariant pilot model.",
        "- Both pilot models replicated the best loglikelihood and terminated normally.",
        "- Both models fixed one or more transition logits, indicating empty or near-empty transition cells. This is not automatically fatal, but it weakens claims about rare transition paths.",
        "- The local-independence warning is expected for the current diagonal latent-state model.",
        "- Treat these as pilot results. A final model decision still needs full-start confirmation and substantive interpretation of class profiles and transition matrices.",
        "",
        "## Class Proportions by Wave",
        "",
        markdown_table(
            class_rows,
            ["model", "wave", "class", "estimated_n", "estimated_proportion"],
        ),
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    out_files = sorted(MPLUS_DIR.glob("lta_*state_*_*.out"))
    fit_rows: list[dict[str, object]] = []
    class_rows: list[dict[str, object]] = []
    transition_rows: list[dict[str, object]] = []
    mean_rows: list[dict[str, object]] = []

    for path in out_files:
        text = path.read_text(encoding="utf-8", errors="replace")
        fit = parse_fit(path, text)
        fit_rows.append(fit)
        class_rows.extend(parse_class_counts(text, str(fit["model"])))
        transition_rows.extend(parse_transition_probabilities(text, str(fit["model"])))
        mean_rows.extend(parse_class_means(text, str(fit["model"]), fit.get("n_states")))

    write_csv(OUT_DIR / "mplus_lta_fit_summary.csv", fit_rows)
    write_csv(OUT_DIR / "mplus_lta_class_proportions.csv", class_rows)
    write_csv(OUT_DIR / "mplus_lta_transition_probabilities.csv", transition_rows)
    write_csv(OUT_DIR / "mplus_lta_class_means.csv", mean_rows)
    (OUT_DIR / "mplus_lta_pilot_summary.md").write_text(
        build_markdown(fit_rows, class_rows),
        encoding="utf-8",
    )

    print(f"Parsed {len(out_files)} Mplus output files.")
    print(f"Wrote summaries to {OUT_DIR}.")


if __name__ == "__main__":
    main()
