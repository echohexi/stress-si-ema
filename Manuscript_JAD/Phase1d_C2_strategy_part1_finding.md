# Phase 1d (part 1/3) — The C2 Finding, Stated Precisely

> **Purpose of this memo (parts 1–3):** lock the *interpretive* default for the manuscript's most counter-intuitive result — that the highest within-person stress→SI cascade strength sits in the *high-fluctuating* subtype (C2), not in the *highest-severity* subtype (C3). Every sentence in Intro / Results / Discussion that touches subtypes must be consistent with parts 1–3.

---

## 1. The empirical fact (no interpretation yet)

From `Study3_All_Tables.xlsx`, Table 3 (canonical):

| Subtype | n (PW) | Entrap a-path | Entrap b-path | **Entrap a×b** |
|---|---|---|---|---|
| C1 Low-stable | 1,275 | 0.061 [0.055, 0.068] | 0.019 [0.006, 0.032] | **0.0012** [0.0004, 0.0020] |
| C2 Low-mod / **high-fluct** | 199 | **0.100** [0.091, 0.109] | 0.162 [0.145, 0.179] | **0.0162** [0.0141, 0.0185] |
| C3 High / high-fluct | 79 | 0.073 [0.059, 0.088] | **0.261** [0.234, 0.288] | **0.0191** [0.0150, 0.0235] |

Subtype contrast on indirect effect:
- C2 − C1: 0.0151 [0.0131, 0.0171] **\*** (credible)
- C3 − C1: 0.0179 [0.0138, 0.0223] **\*** (credible)
- **C3 − C2: 0.0029 [−0.0011, 0.0071]** — CI crosses zero, **NOT credible**

Sensitivity (Model C, AR1-controlled, `sensitivity_out/summary_modelC_subtype_AR1_indirect.csv`):
- ind_C1 = 0.00217, ind_C2 = 0.01780, ind_C3 = 0.02030
- C3 − C2 contrast: 0.0025 [−0.0079, 0.0147], **PD = 0.66**, **2.5% in ROPE [−0.0002, 0.0002]**

**Numerical reading:** C3 is *numerically* slightly higher than C2 (0.0191 vs 0.0162; or 0.0203 vs 0.0178 under AR1). The contrast is *not credibly* different from zero. ROPE 2.5% says we also *cannot* claim equivalence (would need ≥ 95% in ROPE). The honest verdict is: **C2 and C3 are indistinguishable in cascade strength at the current sample, and both are credibly above C1.**

---

## 2. What this finding is NOT

These framings would be **factually wrong** and must never appear in the manuscript:

- ❌ "C2 has the steepest cascade." — C3 is numerically higher; the contrast is null.
- ❌ "C3 has the steepest cascade." — Same reason in reverse.
- ❌ "C2 and C3 are equivalent." — ROPE test does not support equivalence (P_in_ROPE = 0.025).
- ❌ "The cascade strengthens monotonically with severity." — This is the pre-registered H6 prediction, and it is **not supported** (C3 − C2 PD < 0.90).
- ❌ "Sample size in C3 explains the result." — The C3 95% CI [0.0150, 0.0235] **does not include the C2 median 0.0162**, so this is not a power issue.

---

## 3. What this finding IS

The only defensible reading from the data alone is:

> **A high-fluctuating SI profile (regardless of mean intensity) is sufficient to produce a credibly elevated stress→SI cascade. Adding high mean intensity on top (C3) does not credibly strengthen the cascade further.**

This is a *dynamic-static dissociation* claim, not a *C2 supremacy* claim. The dissociation is between:
- the **dynamic** axis (within-person cascade strength), which appears to **saturate** at C2 ≈ C3 ≫ C1
- the **static** axis (between-subtype trait severity, Table 1 + H7), which is **monotonically graded** C1 < C2 < C3 across every CTQ-EA, CTQ-EN, LPFS-BF, PANSI-Neg, BRS, connectedness contrast

Both axes are real. Saying so is the entire interpretive contribution.

---

*(Continued in part 2: pre-registration deviation framing and competing explanations.)*
