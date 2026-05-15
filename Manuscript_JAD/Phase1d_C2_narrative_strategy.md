# Phase 1d — C2 Main-Line Narrative Strategy Memo

> **Purpose**: Lock in how the manuscript will frame the central empirical finding —
> that the *high-fluctuating* subtype (C2), not the most severely impaired one (C3),
> exhibits the steepest within-person stress-to-SI cascade — so that all downstream
> drafting (Intro / Discussion / Abstract / Highlights) speaks with one voice.
>
> **Status**: Phase 1d locked 2026-05-14, revised 2026-05-15. Single source of
> truth for C2-framing decisions across the manuscript.

---

## 1. The empirical pattern, stated minimally

Across the three within-person mediators (entrapment, perceived burdensomeness,
thwarted belongingness), the subtype-specific indirect-effect medians from the
main brms model (xlsx Table 3) and from the AR(1)-controlled sensitivity Model C
(`sensitivity_out/summary_modelC_subtype_AR1_indirect.csv`) agree on the same
qualitative pattern:

| Mediator | C1 a×b | C2 a×b | C3 a×b | C3 − C2 95% CrI | C3 − C2 PD |
|---|---|---|---|---|---|
| Entrapment (main) | 0.0012 | 0.0162 | 0.0191 | [−0.0011, 0.0071] | < 0.90 |
| Burdensomeness (main) | 0.0008 | 0.0128 | 0.0113 | [−0.0045, 0.0016] | < 0.90 (sign reversed) |
| Belongingness (main) | 0.0008 | 0.0101 | 0.0146 | [0.0014, 0.0079] | ≥ 0.975 |
| Entrapment (Model C, AR1) | 0.00217 | 0.01780 | 0.02030 | [−0.0079, 0.0147] | 0.66 |

Five jointly true statements drive the narrative:

1. **C2 > C1 and C3 > C1** are credible across all three mediators (95% CrIs exclude zero); the cascade is unambiguously *not* uniformly low.
2. **C3 > C2 strict monotonicity is not credible** for entrapment or burdensomeness; for burdensomeness the point estimate is in the wrong direction.
3. **The C3 − C2 contrast lives in a high-uncertainty zone**: 95% HDI spans both signs; PD ≈ 0.66 (close to a coin flip); ROPE-probability ≈ 0.025 (so equivalence *cannot* be asserted either — only undecidedness).
4. **In raw stress→SI slope (xlsx Table 4)** the order *is* monotonic: C1 ≈ 0, C2 = 0.0327, C3 = 0.0437, with credible C3 − C2 = 0.0110 [0.0055, 0.0163]. The non-monotonicity is *specific to the indirect (a×b) pathway*, not to the raw cascade. This is a tighter, more defensible claim than the version that conflates the two.
5. **Static trait profiles (H7, xlsx not yet dumped for that table but per Figure 1) are strictly monotonic** C1 < C2 < C3 on every risk indicator and inversely monotonic on every resource indicator. The dynamic-cascade non-monotonicity therefore *dissociates from* the static trait gradient — this dissociation is the manuscript's signature finding.

## 2. Three candidate interpretive frames

Three substantive readings of the C2-vs-C3 pattern are *not* mutually exclusive,
but they make different testable predictions and place different demands on the
text. We commit to **Frame A as the lead** and treat B and C as Discussion
candidates, in that order of textual weight.

### Frame A — Dynamic-vs-static dissociation (LEAD)

**Claim**: The strength of the within-person stress-to-SI cascade and the
person's static trait severity index different latent constructs. Trait
severity is gradient (C1 < C2 < C3); cascade reactivity has a non-monotonic
profile peaking in the high-fluctuating subtype.

**Mechanism vocabulary**: stress reactivity (Bonanno 2004; Selby & Joiner 2009);
emotional inertia and variability as risk markers independent of mean level
(Houben et al. 2015; Kuppens et al. 2010); dynamic phenotype vs. severity
phenotype (Schiepek 2009; Olthof et al. 2020).

**Why this frame leads**: (i) it accounts for *all five* facts in Section 1
without forcing the C3 − C2 contrast to be credible, (ii) it is theoretically
generative for clinical translation ("high-fluctuating profiles may benefit
from different micro-interventions than high-severity profiles"), (iii) it
maps onto Compas/Masten resource-axis literature already used in the
preregistration, and (iv) it survives the lagged-sensitivity caveat
because it makes no temporal-causal commitment.

### Frame B — Ceiling / saturation in C3 (SECONDARY)

**Claim**: C3 participants are already near the upper bound of momentary SI on a
non-trivial share of prompts (Table 1: 89.6% any-SI > 1 in C3 vs. 16.0% in C2),
so the *marginal* SI response to incremental stress is compressed by the
truncation of the response scale.

**Strengths**: parsimonious; testable via examining whether the C3 b-paths
flatten at high stress (post-hoc spline; defer to Discussion only).

**Weaknesses**: the C3 b-paths in xlsx Table 3 are *largest* of the three
subtypes (entrap b = 0.261; burden b = 0.243; belong b = 0.197), which is
the opposite of what a hard-ceiling account predicts. The ceiling is at most
partial.

### Frame C — Habituation / desensitisation in C3 (TERTIARY)

**Claim**: Repeated severe SI episodes blunt the within-person *coupling*
between stress and proximal mediators, so the a-paths in C3 (entrap = 0.073,
burden = 0.047) are attenuated relative to C2 (entrap = 0.100, burden = 0.070).
This is consistent with stress-sensitisation theory inverted at the high end
(an "inverted-U" reactivity-by-severity function).

**Strengths**: matches the xlsx S5 pattern that C3 a-paths *are* numerically
smaller than C2 a-paths even though c′-paths are larger.

**Weaknesses**: depends on cross-sectional inference; cannot adjudicate
between habituation and other reasons C3 might have weaker a-paths
(e.g., sampling-window effects; baseline-difference selection effects).

## 3. Pre-registration deviation: what we promised vs. what we found

(to fill — Section 3)

## 4. Five-layer defence against expected reviewer pushback

(to fill — Section 4)

## 5. Concrete writing rules for Intro / Discussion / Abstract / Highlights

(to fill — Section 5)

## 6. Fallback positions if a reviewer rejects the main framing

(to fill — Section 6)
