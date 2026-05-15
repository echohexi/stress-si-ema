# Phase 1 — Locked Authoritative Numbers (v2: xlsx canonical + sensitivity)

> **CANONICAL SOURCE HIERARCHY** (read this every time before quoting a number):
> 1. **First-tier truth**: `Table/Study3_All_Tables.xlsx` — 11 sheets (Overview + Table 1–4 + Table S1–S6). When any other document disagrees, **xlsx wins**.
> 2. **Second-tier truth (sensitivity)**: `code/sensitivity_out/{summary_modelA,B,C}_*.csv` for AR1-controlled, fully-lagged, and subtype+AR1+ROPE specifications.
> 3. **Provisional** (not for citation in manuscript): `Figure/Study3_main/Figure_*_source_data.csv` — basis of v1; agrees with xlsx on every checked number, but xlsx is the formal lock.
>
> **Files that are now KNOWN to contain wrong numbers** (see §10 audit log) and must NOT be quoted from until corrected:
> - `Results_JAD_Style.md` — at least 5 numerical errors
> - `01_FrontMatter.md` Abstract + Highlights — at least 2 numerical errors
>
> Phase 2 drafting must replace the conflicting numbers against this document.
>
> *Locked: 2026-05-15. Supersedes v1 (2026-05-13).*

---

## 1. Sample, design, and EMA parameters (xlsx Overview + Table 1)

| Parameter | LOCKED VALUE | Source |
|---|---|---|
| Analytic participants, N | **391** | xlsx Overview |
| Total person-waves (PW) | **1,553** | xlsx Overview, Table 1 |
| Total EMA prompts | **28,113** | xlsx Overview, Table 1 |
| EMA waves | **4** | xlsx Overview |
| Mean prompts per person-wave | 18.1 (SD 2.4) | xlsx Table 1 |
| Mean waves per participant | 3.96 (SD 0.26) | xlsx Table 1 |
| Response rate | 76.4% (SD 11.2%) | supervisor briefing |
| Age | 20.4 (SD 1.6), range 17–25 | Methods.md cross-check |
| % female | 67.3% | Methods.md cross-check |
| % Han ethnicity | 92.6% | Methods.md cross-check |
| Any momentary stressor (%) | 46.3 of prompts | xlsx Table 1 |
| Any momentary SI (SI > 1) (%) | 6.9 of prompts | xlsx Table 1 |
| Mean stress sum intensity | 2.23 (SD 3.20), 0–35 scale | xlsx Table 1 |

**The "28,723" figure** in Phase1_v1, Results_JAD_Style.md, and supervisor_briefing.md is **superseded** by xlsx's **28,113**.

**Schedule reconciliation:** Earlier "8 prompts/day, 12 days" in Results_JAD_Style.md §3.1 is **arithmetically inconsistent** with 28,113 prompts at 76.4% response (would predict ~150k max). "3/day × 7 days" (Methods.md, supervisor briefing) yields ~33k max — consistent. **Use 3 prompts/day × 7 days × 4 waves throughout.**

---

## 2. Subtype structure (xlsx Table 1) — PRE-REGISTRATION DEVIATION

Subtype membership was assigned **at the person-wave level**, not at the participant level. The same individual may occupy different subtypes across the four EMA waves. As a result, **subtype-specific participant counts sum to more than 391**.

| Subtype | Participants, n | Person-waves, n (% of total) | EMA prompts, n |
|---|---|---|---|
| C1 Low-stable | 367 | 1,275 (82.1%) | 23,104 |
| C2 Low-mod / **high-fluct** | 128 | 199 (12.8%) | 3,637 |
| C3 High / high-fluct | 37 | 79 (5.1%) | 1,372 |
| **Sum across columns** | **532** | **1,553** | **28,113** |

**Pre-registered counts** (participant-level): C1 = 337, C2 = 37, C3 = 17. **This is a structural deviation** — the analytic plan was reframed during analysis to assign subtypes at the PW level (each wave's 7-day trajectory clusters independently). Every Methods/Results sentence mentioning subtype N must:
1. Quote the PW-level n by default (1,275 / 199 / 79)
2. Disclose participant-level n in parentheses (367 / 128 / 37)
3. Note that participants are not nested within a single subtype

**Locked phrasing (use verbatim):**
> "Subtype membership was assigned at the person-wave level, so a single participant could occupy different subtypes across the four EMA waves; subtype-specific participant counts therefore sum to more than 391 (Table 1)."

---

## 3. Prompt-level descriptive statistics (xlsx Table 1)

| Construct | Overall | C1 | C2 | C3 |
|---|---|---|---|---|
| Stress sum intensity, M (SD) | 2.23 (3.20) | 1.99 (2.98) | 2.91 (3.72) | 4.36 (4.15) |
| Entrapment | — | 1.28 (0.66) | 1.66 (0.93) | 2.59 (1.01) |
| Perceived burdensomeness | — | 1.18 (0.45) | 1.49 (0.73) | 2.24 (0.94) |
| Thwarted belongingness | — | 1.25 (0.54) | 1.56 (0.74) | 2.32 (0.92) |
| Suicidal ideation | — | 1.00 (0.04) | 1.15 (0.39) | 1.99 (0.70) |
| Any momentary stressor (%) | 46.3 | 43.8 | 53.0 | 69.7 |
| Any momentary SI > 1 (%) | 6.9 | 0.6 | 16.0 | 89.6 |

All EMA constructs on 1–5 momentary scales (except stress sum: 0–35, sum of 7 domains).

---

## 4. Overall within-person parallel mediation, H1 + H2 (xlsx Table 2)

| Path | Posterior median | 95% CrI | pd |
|---|---|---|---|
| **a-paths: Stress → Mediator** | | | |
| Stress → Entrapment | 0.068 | [0.061, 0.074] | > 0.999 |
| Stress → Perceived burdensomeness | 0.041 | [0.036, 0.046] | > 0.999 |
| Stress → Thwarted belongingness | 0.044 | [0.039, 0.049] | > 0.999 |
| **b-paths: Mediator → SI** | | | |
| Entrapment → SI | 0.037 | [0.027, 0.048] | > 0.999 |
| Perceived burdensomeness → SI | 0.041 | [0.023, 0.058] | > 0.999 |
| Thwarted belongingness → SI | 0.025 | [0.013, 0.038] | > 0.999 |
| **Within-person indirect effects (a × b)** | | | |
| Stress → Entrapment → SI | **0.0025** | [0.0018, 0.0033] | > 0.999 |
| Stress → Perceived burdensomeness → SI | **0.0016** | [0.0009, 0.0024] | > 0.999 |
| Stress → Thwarted belongingness → SI | **0.0011** | [0.0006, 0.0017] | > 0.999 |
| **Dominance contrasts** | | | |
| Entrap − Burden | 0.0009 | [−0.0002, 0.0020] | 0.944 |
| Entrap − Belong | 0.0014 | [0.0005, 0.0024] | 0.998 |
| Burden − Belong | 0.0005 | [−0.0004, 0.0015] | 0.867 |

**Entrapment share of total indirect** = 0.0025 / (0.0025 + 0.0016 + 0.0011) = **48%** (NOT 57%; see §10 audit).

**H1 status: SUPPORTED.** All three indirect-effect CIs exclude zero.
**H2 status: SUPPORTED at pre-reg PD ≥ 0.90 threshold.** Entrap − Burden PD = 0.944 (passes 0.90, fails 0.975); Entrap − Belong PD = 0.998 (passes both). Burden − Belong PD = 0.867 not credible.

---

## 5. Random-slope variance, H3 (xlsx Table S2)

All six within-person path SDs are **credibly > 0**:

| Random-effect term | Posterior median | 95% CrI | pd |
|---|---|---|---|
| a-path SD: Stress → Entrapment | 0.0560 | [0.0513, 0.0614] | > 0.999 |
| a-path SD: Stress → Burdensomeness | 0.0430 | [0.0392, 0.0472] | > 0.999 |
| a-path SD: Stress → Belongingness | 0.0431 | [0.0392, 0.0473] | > 0.999 |
| b-path SD: Entrapment → SI | 0.0732 | [0.0643, 0.0830] | > 0.999 |
| b-path SD: Burdensomeness → SI | 0.1237 | [0.1097, 0.1391] | > 0.999 |
| b-path SD: Belongingness → SI | 0.0853 | [0.0744, 0.0978] | > 0.999 |

a-path SD range: **0.043–0.056**; b-path SD range: **0.073–0.124**. The earlier draft `Results_JAD_Style.md` quoted "0.602 to 0.806" for b-path SDs — **wrong by ~10×; see §10 audit**.

**H3 status: SUPPORTED.** All six within-person path SDs credibly non-zero.

---

## 6. Subtype-specific mediation, H6 (xlsx Table 3) — **THE C2/C3 DISSOCIATION**

| Mediator / Subtype | a-path | b-path | Indirect (a × b) |
|---|---|---|---|
| **Entrapment** | | | |
| C1 (Low-stable) | 0.061 [0.055, 0.068] | 0.019 [0.006, 0.032] | 0.0012 [0.0004, 0.0020] |
| **C2 (Low-mod / high-fluct)** | **0.100** [0.091, 0.109] | 0.162 [0.145, 0.179] | **0.0162** [0.0141, 0.0185] |
| C3 (High / high-fluct) | 0.073 [0.059, 0.088] | **0.261** [0.234, 0.288] | **0.0191** [0.0150, 0.0235] |
| **Contrasts (Entrap a×b)** | | | |
| C2 − C1 | — | — | 0.0151 [0.0131, 0.0171] **\*** |
| C3 − C1 | — | — | 0.0179 [0.0138, 0.0223] **\*** |
| C3 − C2 | — | — | **0.0029** [−0.0011, 0.0071] **NOT credible** |
| **Perceived burdensomeness** | | | |
| C1 | 0.034 [0.029, 0.039] | 0.023 [0.005, 0.042] | 0.0008 [0.0002, 0.0014] |
| C2 | 0.070 [0.063, 0.077] | 0.183 [0.160, 0.206] | 0.0128 [0.0109, 0.0149] |
| C3 | 0.047 [0.035, 0.058] | 0.243 [0.209, 0.276] | 0.0113 [0.0083, 0.0145] |
| **Contrasts (Burden a×b)** | | | |
| C3 − C2 | — | — | **−0.0015** [−0.0045, 0.0016] **NOT credible** (sign reversed) |
| **Thwarted belongingness** | | | |
| C1 | 0.037 [0.032, 0.042] | 0.021 [0.005, 0.037] | 0.0008 [0.0002, 0.0014] |
| C2 | 0.066 [0.058, 0.073] | 0.154 [0.132, 0.174] | 0.0101 [0.0083, 0.0119] |
| C3 | 0.075 [0.063, 0.087] | 0.197 [0.164, 0.229] | 0.0146 [0.0114, 0.0183] |
| **Contrasts (Belong a×b)** | | | |
| C3 − C2 | — | — | 0.0046 [0.0014, 0.0079] **\* credible** |

**H6 status: NOT SUPPORTED.** Pre-reg demanded strict monotonicity C1 < C2 < C3 with monotonicity PD ≥ 0.90. Realised: only belongingness shows credible C3 > C2; entrapment C3 − C2 is null, burdensomeness C3 − C2 is null with reversed sign. See `Phase1d_C2_strategy_part1_finding.md` for the full interpretive frame.

---

*(continued §7–§10)*

