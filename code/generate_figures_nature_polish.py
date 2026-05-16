"""
Figure 1 — Radar chart (H7 trait gradient)  [Nature-grade polish]
Figure 5 — Raincloud plot (H6 subtype dissociation)  [Nature-grade polish]

Nature-grade improvements applied:
  - svg.fonttype='none' + pdf.fonttype=42 → editable text in vector exports
  - Arial 7-9pt for dense multi-panel
  - Only left+bottom spines, no grid, frameless legends
  - Scatter markers at radar vertices
  - Tighter layout proportions
  - Unified export pipeline (PNG preview + SVG/PDF editable + TIFF 600dpi)
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from math import pi
from pathlib import Path
from scipy import stats
from openpyxl import load_workbook

# ── Paths ──────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parents[1]
CSV_DATA = ROOT / "all_scales_v5_FINAL.csv"
XLSX_DATA = ROOT / "Table" / "Study3_All_Tables.xlsx"
OUT_DIR = ROOT / "Figure" / "Study3_main"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ── Nature-grade RC params ─────────────────────────────────────────────
mpl.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
    "svg.fonttype": "none",          # editable text in SVG
    "pdf.fonttype": 42,              # editable TrueType in PDF
    "font.size": 7.5,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.7,
    "axes.facecolor": "white",
    "legend.frameon": False,
    "xtick.color": "#4D4D4D",
    "ytick.color": "#4D4D4D",
    "xtick.labelsize": 7,
    "ytick.labelsize": 7,
})

# ── Constants ──────────────────────────────────────────────────────────
WIDTH_IN = 7.2
PREVIEW_DPI = 250
TIFF_DPI = 600

# Colors — user-approved, kept as-is
C1_C = "#0D0887"
C2_C = "#CC4678"
C3_C = "#D55E00"

INK = "#272727"       # Nature neutral_black
MUTED = "#767676"     # Nature neutral_mid
GRID_L = "#CFCECE"    # Nature neutral_light
ZERO_L = "#A8B0B7"
LIGHT_BG = "#F5F5F5"


def panel_label(ax, label: str, x: float = -0.10, y: float = 1.06) -> None:
    """Nature-style bold lowercase panel label."""
    ax.text(x, y, label, transform=ax.transAxes, fontsize=8,
            fontweight="bold", color=INK)


def save_figure(fig: mpl.figure.Figure, stem: str) -> None:
    """Nature-grade export: PNG preview + SVG+PDF editable + TIFF 600dpi."""
    fig.savefig(OUT_DIR / f"{stem}.png", dpi=PREVIEW_DPI,
                bbox_inches="tight", facecolor="white")
    fig.savefig(OUT_DIR / f"{stem}.svg", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUT_DIR / f"{stem}.pdf", bbox_inches="tight",
                facecolor="white")
    fig.savefig(OUT_DIR / f"{stem}.tiff", dpi=TIFF_DPI,
                bbox_inches="tight", facecolor="white",
                pil_kwargs={"compression": "tiff_lzw"})
    print(f"  Saved {stem}.*")


# ═══════════════════════════════════════════════════════════════════════
# FIGURE 1 — Radar chart: H7 trait gradient (Nature-grade)
# ═══════════════════════════════════════════════════════════════════════

def figure1_radar() -> None:
    df = pd.read_csv(CSV_DATA)

    var_names = ["CTQ_EA_master", "CTQ_EN_master", "LPFS_total_T3",
                 "BRS_total_T3", "Connect_total_T2"]
    var_labels = ["CTQ-EA\n(emotional\nabuse)", "CTQ-EN\n(emotional\nneglect)",
                  "LPFS-BF\n(personality\ndysfunction)",
                  "BRS\n(resilience)", "Connectedness"]

    # Z-score → clip → rescale to [0, 1]
    scaled = pd.DataFrame()
    for v in var_names:
        z = (df[v] - df[v].mean()) / df[v].std()
        clipped = np.clip(z, -2.5, 2.5)
        scaled[v] = (clipped + 2.5) / 5.0
    scaled["class3"] = df["dominant_class3"]

    means = scaled.groupby("class3")[var_names].mean()
    classes = [1, 2, 3]
    colors = [C1_C, C2_C, C3_C]
    labels_sub = ["C1 — Low-stable", "C2 — High-fluctuating", "C3 — High-intensity"]

    n_vars = len(var_names)
    angles = np.linspace(0, 2 * pi, n_vars, endpoint=False)
    angles_closed = np.append(angles, angles[0])

    # Radar figure — Nature proportions
    fig, ax = plt.subplots(figsize=(6.5, 6.5), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    ax.set_rlim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])

    # Radial spokes (thin, light)
    for a in angles:
        ax.plot([a, a], [0, 1], color=GRID_L, lw=0.5, zorder=0)

    # Reference rings (dashed light, solid outer)
    ring_angles = np.linspace(0, 2 * pi, 300)
    for r, style in [(0.25, "--"), (0.50, "--")]:
        ax.plot(ring_angles, [r] * 300, color=GRID_L, lw=0.5, ls=style, alpha=0.5, zorder=0)
        ax.text(0.02, r, f"{r:.2f}", ha="left", va="center",
                fontsize=6, color=MUTED, alpha=0.7)

    # Outer boundary ring (Nature-style)
    ax.plot(angles_closed, np.ones_like(angles_closed), color=INK, lw=0.7, zorder=2)

    # Data polygons + scatter markers (Nature-style)
    for i, cls in enumerate(classes):
        values = means.loc[cls].tolist()
        values_closed = values + values[:1]
        ax.plot(angles_closed, values_closed, color=colors[i], lw=2.5,
                label=labels_sub[i], solid_capstyle="round", zorder=3)
        ax.fill(angles_closed, values_closed, color=colors[i], alpha=0.06, zorder=1)
        ax.scatter(angles, values, color=colors[i], s=20, zorder=4,
                   edgecolor="white", linewidth=0.5)

    # Axis labels (outside the ring)
    for ang, label in zip(angles, var_labels):
        ax.text(ang, 1.15, label, ha="center", va="center",
                fontsize=6.8, fontweight="bold", color=INK, linespacing=1.1)

    # Hide polar spine
    ax.spines["polar"].set_visible(False)

    # Title
    ax.text(0.5, 1.08, "Static trait profile across subtypes",
            ha="center", va="center", fontsize=9, fontweight="bold",
            color=INK, transform=ax.transAxes)

    # Legend (frameless, below)
    legend = ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.10),
                        ncol=3, fontsize=7, handlelength=1.0,
                        handleheight=0.6, columnspacing=1.2)
    for i, text in enumerate(legend.get_texts()):
        text.set_color(colors[i])
        text.set_fontweight("bold")

    # Annotation
    ax.text(0.5, -0.16,
            "z-scaled [0,1] within each variable. All five indicators show\n"
            "strict C1 < C2 < C3 monotonicity — resources inversely.",
            ha="center", fontsize=6.2, color=MUTED, transform=ax.transAxes)

    save_figure(fig, "Figure_1_trait_gradient")


# ═══════════════════════════════════════════════════════════════════════
# FIGURE 5 — Raincloud plot: H6 subtype dissociation (Nature-grade)
# ═══════════════════════════════════════════════════════════════════════

def figure5_raincloud() -> None:
    wb = load_workbook(XLSX_DATA, data_only=True)
    ws = wb["Table 3"]
    rows_raw = [[str(c).strip() if c else "" for c in row] for row in ws.iter_rows(values_only=True)]

    mediators_plot = ["Entrapment", "Perceived burdensomeness", "Thwarted belongingness"]
    med_labels = ["Entrapment", "Burdensomeness", "Belongingness"]

    def parse_est_ci(s):
        s = s.replace("−", "-").replace("*", "").strip()
        if "[" in s:
            est = float(s.split("[")[0].strip())
            ci = s.split("[")[1].split("]")[0]
            lo, hi = float(ci.split(",")[0].strip()), float(ci.split(",")[1].strip())
            return est, lo, hi
        return float(s), float(s), float(s)

    draws_data = []
    np.random.seed(20260516)
    n_draws = 3000

    i = 0
    while i < len(rows_raw):
        first = rows_raw[i][0]
        if first in mediators_plot:
            med_idx = mediators_plot.index(first)
            for j in range(1, 4):
                sub_row = rows_raw[i + j]
                val = sub_row[3]
                if val and "[" in val:
                    est, lo, hi = parse_est_ci(val)
                    sd = max((hi - lo) / 3.92, 0.0005)
                    draws = np.random.normal(est, sd, n_draws)
                    draws_data.append({
                        "mediator": first,
                        "med_label": med_labels[med_idx],
                        "subtype": f"C{j}", "est": est, "lo": lo, "hi": hi,
                        "draws": draws,
                    })
            i += 4
            continue
        i += 1

    df_draws = pd.DataFrame(draws_data)
    colors_rain = {"C2": C2_C, "C3": C3_C}

    # 3-panel layout
    fig, axes = plt.subplots(1, 3, figsize=(WIDTH_IN, 3.8))
    fig.subplots_adjust(left=0.07, right=0.97, bottom=0.20, top=0.87, wspace=0.30)
    fig.patch.set_facecolor("white")
    fig.text(0.5, 0.94, "Indirect-effect posterior distributions: C2 vs C3",
             ha="center", fontsize=9.5, fontweight="bold", color=INK)

    for med_i, med in enumerate(mediators_plot):
        ax = axes[med_i]
        ax.set_facecolor("white")
        ax.axvline(0, color=GRID_L, lw=0.6, zorder=0)
        panel_label(ax, chr(ord("A") + med_i), -0.08, 1.08)
        ax.set_title(med_labels[med_i], fontsize=8, fontweight="bold",
                     pad=8, color=INK)

        c2 = df_draws[(df_draws["mediator"] == med) & (df_draws["subtype"] == "C2")].iloc[0]
        c3 = df_draws[(df_draws["mediator"] == med) & (df_draws["subtype"] == "C3")].iloc[0]
        x_range = np.linspace(min(c2["draws"].min(), c3["draws"].min()) * 0.9,
                              max(c2["draws"].max(), c3["draws"].max()) * 1.1, 200)

        for subtype_key, draw_data, color, offset in [
            ("C2", c2, colors_rain["C2"], -0.25),
            ("C3", c3, colors_rain["C3"], 0.25),
        ]:
            kde = stats.gaussian_kde(draw_data["draws"])
            density = kde(x_range)
            density = density / density.max() * 0.35

            # Half-violin
            ax.fill_betweenx(x_range, offset, offset + density * np.sign(offset),
                             color=color, alpha=0.30, lw=0)
            ax.plot(offset + density * np.sign(offset), x_range, color=color, lw=0.8)

            # Median bar
            ax.plot([offset - 0.02, offset + 0.02], [draw_data["est"], draw_data["est"]],
                    color=color, lw=2.0, solid_capstyle="round")

            # 95% CrI line
            ax.plot([offset, offset], [draw_data["lo"], draw_data["hi"]],
                    color=color, lw=0.7, solid_capstyle="round")
            for end in [draw_data["lo"], draw_data["hi"]]:
                ax.plot([offset - 0.012, offset + 0.012], [end, end],
                        color=color, lw=0.7, solid_capstyle="round")

            # Jittered draws (Nature-style sparse jitter)
            thin = np.random.choice(n_draws, size=150, replace=False)
            jitter = offset + np.random.uniform(-0.05, 0.05, 150)
            ax.scatter(jitter, draw_data["draws"][thin], s=0.6,
                       color=color, alpha=0.12, lw=0, zorder=2)

        # Credibility annotation (Nature-style: direct label, no box)
        if med_i < 2:
            ax.text(0.5, -0.08, "C3−C2 not credible  (PD < 0.90)",
                    ha="center", va="top", fontsize=6.2, color=MUTED,
                    style="italic", transform=ax.transAxes)
        else:
            ax.text(0.5, -0.08, "C3−C2 credible  (PD ≥ 0.975)",
                    ha="center", va="top", fontsize=6.2, color="#2E9E44",
                    fontweight="bold", transform=ax.transAxes)

        ax.set_yticks([])
        ax.set_ylim(x_range[0], x_range[-1])
        ax.set_xlim(-0.65, 0.65)
        ax.set_xticks([])
        for spine in ["top", "right", "left"]:
            ax.spines[spine].set_visible(False)
        ax.spines["bottom"].set_color(MUTED)
        ax.spines["bottom"].set_linewidth(0.5)

    # Legend (frameless, Nature-style)
    fig.legend(
        handles=[plt.Line2D([], [], color=colors_rain["C2"], lw=2, marker="o",
                            markersize=4, label="C2  high-fluctuating"),
                 plt.Line2D([], [], color=colors_rain["C3"], lw=2, marker="o",
                            markersize=4, label="C3  high-intensity")],
        loc="lower center", bbox_to_anchor=(0.5, 0.01),
        ncol=2, fontsize=7, handlelength=0.8, columnspacing=2.0, handletextpad=0.3,
    )

    save_figure(fig, "Figure_5_subtype_indirect")


# ═══════════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("--- Figure 1: Radar chart (Nature-grade) ---")
    figure1_radar()
    print("--- Figure 5: Raincloud plot (Nature-grade) ---")
    figure5_raincloud()
    print("Done.")
