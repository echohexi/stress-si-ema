# Phase 1d (part 3/3) — Locked Phrases & Recursion-Proofing

> Every line in this file is a phrase the **next-stage Claude session** must reuse verbatim (or paraphrase only as marked). The goal is to keep the C2 main line consistent across Intro, Results, Discussion, Abstract, and Highlights — even if the drafting session reconnects after a network drop and only has access to these memo files.

---

## 7. Five locked phrases (for direct paste)

**A. Title-level positioning (used in working title only, NOT in body):**
> "the high-fluctuating, not the most severely impaired, subtype shows the steepest within-person cascade"

This is already in `01_FrontMatter.md` Highlights #5. Keep.

**B. Abstract — one Results sentence:**
> "A high-fluctuating subtype, rather than the most severely impaired one, exhibited the steepest cascade, dissociating dynamic strength from static trait severity."

This is already in `01_FrontMatter.md` Abstract. Keep.

**C. Results §3.5 — the H6 sentence (mandatory wording):**
> "Hypothesis 6 was not supported: the C3 versus C2 contrast credibly excluded zero in neither the entrapment nor the burdensomeness indirect-effect pathway (Table 3; entrapment C3 − C2 = 0.0029, 95% CI [−0.0011, 0.0071]; burdensomeness C3 − C2 = −0.0015, 95% CI [−0.0045, 0.0016])."

**D. Discussion §4.3 — the dissociation paragraph topic sentence:**
> "Within-person cascade strength and between-person trait severity were partially dissociable: trait severity increased strictly monotonically across the three subtypes (H7 supported), whereas dynamic cascade strength saturated at the high-fluctuating subtype (H6 not supported)."

**E. Limitations — the C3 sample-size sentence:**
> "Confirmation that the cascade truly plateaus rather than continues to rise with severity will require a larger high-severity subsample than the 37 participants (79 person-waves) available here."

---

## 8. Forbidden phrases (will misrepresent the data)

Reject any draft that contains:
- "C2 had the strongest cascade" → factually wrong (C3 numerically higher)
- "C3 had the strongest cascade" → factually wrong (C3 − C2 contrast not credible)
- "C2 and C3 were equivalent" → ROPE evidence does not support equivalence
- "The cascade was attenuated in C3" → no — it was *not credibly different*; "attenuated" implies a directional effect we do not have
- "Sample size in C3 likely accounts for…" → ruled out in part 2 §5.3
- "Strictly monotonic gradient across subtypes" — wrong direction; we got near-monotonic on traits, plateaued on dynamics
- "The cascade is causally driven by entrapment" → Model B reversal does not allow causal-temporal claims; use "concurrently mediated by" or "primarily channelled through"

---

## 9. Recursion-proofing rules for any future session drafting Intro / Discussion

1. Before writing any subtype sentence, re-read **part 1 §1 (the empirical table)** and verify the numbers match. The xlsx is canonical; if Results_JAD_Style.md disagrees (and it does), xlsx wins.
2. Before writing any cascade-causation sentence, check **part 2 §6**. The cascade is *contemporaneous*; never write "stress at time t predicts SI at time t+1 through entrapment" — that is the Model B specification and it gave the opposite sign.
3. Before writing any subtype-severity claim, distinguish:
   - **Trait-severity axis** (Table 1 means; H7) → monotonic C1 < C2 < C3 → can say "graded"
   - **Dynamic-cascade axis** (Table 3 a×b; H6) → saturated at C2 ≈ C3 ≫ C1 → cannot say "graded"
4. Every figure caption referencing subtype must spell out the n at the **person-wave level** (1,275 / 199 / 79) AND at the **participant level** (367 / 128 / 37), and note that the same individual may occupy different subtypes across waves (this is in Table 1's note already).
5. Discussion §4.3 must conclude that the dissociation is *the* novel finding of the paper. Not the parallel mediation (H1 — confirmatory), not the dimension-specific CTQ moderation (H4 — already well-trodden). The dissociation is what distinguishes this manuscript from existing JAD EMA studies on subtypes (Portillo-Van Diest 2025; Mandel 2024).

---

## 10. Decision: what to do if a reviewer rejects the C2 framing

Three pre-prepared fallbacks, in increasing order of concession:

**F1 (preferred): defend the dissociation framing.**
- Show the ROPE result: P_in_ROPE = 0.025 → "we explicitly do not claim equivalence; we claim the cascade gradient saturates beyond C2".
- Cite Glenn 2017 and Czyz 2019 for prior evidence of within-person reactivity peaking below maximal severity.

**F2 (compromise): re-frame as "C2 and C3 jointly form a high-cascade cluster" without ranking them.**
- Drop the "high-fluctuating, not the most severely impaired" language from Abstract; replace with "two-tier cascade structure: a low-cascade subtype (C1) and a credibly higher-cascade cluster (C2/C3) with no detectable internal gradient".
- This is honest but loses the dissociation novelty.

**F3 (last resort, if reviewer insists on strict monotonicity): report H6 as null and shift main contribution to H4 (CTQ-EA × CTQ-PA dimension-specific moderation) + H1/H2 (entrapment dominance).**
- Demote subtype analysis to Supplementary.
- This loses ~30% of the manuscript's distinctiveness; only invoke if F1+F2 both fail across two reviewers.

---

## 11. End-of-memo invariant

The most important sentence in this entire memo, to keep visible during drafting:

> **C3 is numerically larger than C2. The C3 − C2 contrast is not credibly different from zero. We claim *dissociation* between dynamic-cascade strength and static-trait severity, not C2 supremacy.**

If the manuscript ever drifts from this invariant, stop drafting and reread parts 1–3.

---

*Phase 1d locked: 2026-05-15.*
*Source data verified against `Study3_All_Tables.xlsx` Table 3 and `code/sensitivity_out/summary_modelC_subtype_AR1_indirect.csv`.*
*Phase 1c (Phase1_locked_numbers.md rewrite) supersedes any numerical claim that conflicts with this file.*
