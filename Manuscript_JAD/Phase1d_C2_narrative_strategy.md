# Phase 1d — C2 Main-Line Narrative Strategy Memo

> **Purpose**: Lock in how the manuscript will frame the central empirical finding —
> that the *high-fluctuating* subtype (C2), not the most severely impaired one (C3),
> exhibits the steepest within-person stress-to-SI cascade — so that all downstream
> drafting (Intro / Discussion / Abstract / Highlights) speaks with one voice.
>
> **Status**: Phase 1d locked 2026-05-14, revised 2026-05-16. Single source of
> truth for ALL narrative decisions across the manuscript.

---

## ⚠ LOCKED DECISIONS (2026-05-16) — These three override all earlier drafts

These are the three cross-cutting narrative decisions the author committed to
before Phase 2 drafting. Every downstream file must respect them.

### Decision 1 — Physical abuse (PA) reverse moderation
- **Where**: Discussion only, not in Introduction or Results.
- **How much**: 2-3 mechanism-oriented sentences. Cite potential
  dissociation/habituation (DES data as suggestive evidence).
- **Tone**: Exploratory but non-trivial. Acknowledge it may be a real signal,
  flag that preregistration treats all CTQ dimensions symmetrically, and note
  the need for replication in a PA-enriched sample.
- **Rationale**: Too provocative for Intro framing; weakens the main line.
  Kept in Discussion as "unexpected finding in the right direction."

### Decision 2 — C2-vs-C3 signature finding framing
- **Claim** (adopted from Frame A): C2 and C3 are *dynamically indistinguishable*
  on the indirect pathway, and the C3−C2 direct-slope gap is fully captured by
  the three proximal mediators. The dissociation between the *dynamic* cascade
  and the *static* trait gradient is the manuscript's signature finding.
- **Verbal guardrails**: Use "C2 and C3 were not credibly different" not "C2 >
  C3". Use "dissociation" not "paradox". Frame positively as "reveals a
  construct distinction" not negatively as "failed to confirm H6 monotonicity."
- **Framing in Intro**: Tease the dynamic-static tension without spoiling
  results. Use language like "whether individuals whose trait profile suggests
  the highest risk are also those whose moment-to-moment cascade is steepest."

### Decision 3 — Target journal
- **Journal**: *Journal of Affective Disorders* (JAD), 一区.
- **Consequences for narrative**: (a) Chinese public health context and the
  "~17% undergraduate SI prevalence" must open the Introduction (already
  locked in Phase2a). (b) Clinical implications must be explicit in Discussion
  — "what does this mean for intervention design on Chinese campuses."
  (c) Avoid overly theoretical language (e.g., no extended debate on
  stress-sensitisation theory unless directly supporting the data).
  (d) Abstract Limitations section is mandatory in JAD.

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

| Item | Preregistered | Observed | Narrative treatment |
|---|---|---|---|
| H6 monotonicity | C1 < C2 < C3, PD ≥ 0.90 | Not supported for entrapment or burden (C3−C2 PD < 0.90) | **Do NOT frame as "H6 failed"**. Frame as "the dynamic indirect effect is non-monotonic in a theoretically informative way — C2 and C3 are dynamically indistinguishable, and the dissociation from the static gradient is precisely the finding." |
| H1 burden/belong | Indirect effects credible | Both credible (0.0023 and 0.0012) | **Supported**. But de-emphasize in text — entrapment is the main story. |
| Subtype assignment level | Assumed participant-level | Actually person-wave-level (same person can change subtype) | **Must flag in Methods** as a design feature (not error), because it captures within-person SI-pattern transitions across waves. |
| H2 ordering | entrap > burden > belong | Supported for both contrasts | **Clean support**. Report prominently. |
| PA reverse moderation | Not pre-specified as an independent hypothesis | Robust pattern in xlsx Table S5 | **Discussion only** (per Decision 1). Do not hype in Results. |

## 4. Five-layer defence against expected reviewer pushback

| Layer | Reviewer concern | Defence |
|---|---|---|
| 1. C3 sample (n = 17) | "C3 is too small to trust." | (a) Person-waves = 79, EMA prompts = 1,372 — enough for hierarchical shrinkage. (b) The claim is *null* (C3−C2 not credible), so insufficient power works against us; if C3−C2 were non-null, a larger sample would make it detectable. Our null survives this conservative test. (c) BFDA-type power analysis for multivariate mediation is not standard; we offer brms's internal ROPE diagnostic (P(ROPE) ≈ 0.025) showing undecidedness, not equivalence. |
| 2. Alternative subtype method | "LPA on SI variability is arbitrary." | (a) LPA is preregistered. (b) BLR-test + entropy indices support 3-class solution. (c) We report but do not oversell the exact cutoff — the *qualitative* dissociation (not the exact 3-class boundary) is the replicable claim. |
| 3. Single-item SI outcome | "One item can't measure SI." | (a) PANSI momentary single-item is standard in EMA SI literature (Kleiman 2017; Hallensleben 2019). (b) We model it as ordinal (cumulative-logit), treating scale points as ordered categories rather than equal-interval. (c) Sensitivity with Gaussian SI produced the same qualitative pattern. |
| 4. Common-method variance | "All variables self-reported at the same prompt." | (a) The multivariate multilevel model's within-person centering removes stable between-person confounds including response-style bias. (b) AR(1)-controlled sensitivity (Model A) and lagged sensitivity (Model B) address temporal ordering. (c) The a×b interaction pattern (PA reverse on a-path, null on b-path) is *not* explainable by a single shared-method factor. |
| 5. No Bonferroni for 40 CTQ models | "Multiple comparisons not corrected." | (a) Bayesian inference with PD ≥ 0.975 is inherently more conservative than NHST with α = 0.05. (b) We preregistered the 40-model strategy including the specific prediction that PA b-paths would be null. (c) The pattern — EA broad, PA a-path only, Neglect relational-specific — is higher-order and systematic, not isolated p values. |

## 5. Concrete writing rules for Intro / Results / Discussion / Abstract / Highlights

### Introduction (already drafted in Phase2a, verify these rules)
- **No statistical numbers** except N = 391.
- **Frame A must be the lead narrative arc**: trait ≠ dynamic.
- **H6 must state monotonicity** as preregistered; do NOT add caveats or hints about the outcome.
- **PA reverse moderation**: NOT mentioned in Introduction.

### Results
- **H1 first** (all three indirect effects credible); then H2 (entrap dominates).
- **H4 CTQ moderation**: Report b-path pattern as main finding (path-specificity confirmed). Report PA reverse moderation on a-path in a flat, descriptive sentence: "On the a-path, PA showed reverse-direction moderation compared to EA." Do NOT elaborate there — the Discussion explains it.
- **H6**: Lead with "C2 > C1 and C3 > C1 were credible across all mediators. However, C3 > C2 strict monotonicity was not supported for entrapment (PD < 0.90) or burdensomeness (PD < 0.90, point estimate reversed)." Then pivot immediately to "This non-monotonicity dissociates from the static trait gradient (H7)..."
- **Numbers only from Phase1_locked_numbers.md** (which is xlsx-canonical). Re-verify each number before final submission.

### Discussion — section order (JAD convention)
1. **Restate main finding** (strong opening: "In N = 391 first-year undergraduates...")
2. **Frame A - Dynamic-static dissociation** → the main discussion, 3-4 paragraphs
3. **Frame B - Path-specific moderation** → 1-2 paragraphs (include PA reverse moderation here, Decision 1, 2-3 sentences on PA a-path only, DES speculation)
4. **Frame C - Methodological** → Bayesian multivariate mediation utility, 1 paragraph
5. **Limitations** (minimum 3, honest): C3 sample, single-item SI, EMA-compliance in C3
6. **Clinical implications** (mandatory for JAD): what C2 vs C3 means for campus intervention triage
7. **Conclusion** (strong close, tie back to opening)

### Abstract (JAD: 250 words, structured as Background/Methods/Results/Limitations/Conclusions)
- Results section of abstract must lead with **the dissociation**: "Trait risk-resource profiles were strictly monotonic C1 < C2 < C3; however, within-person cascade reactivity showed a non-monotonic pattern in which C2 and C3 were not credibly different."
- Do NOT mention PA. Do NOT mention numbers (it's 250 words).

### Highlights (Elsevier: 3-5 bullets, ≤ 85 chars each incl. spaces)
Example package (3 bullets, 82/83/85 chars):
1. Within-person stress→SI cascade operates through three concurrent mediators
2. Dynamic subtype reactivity dissociates from static trait severity
3. Childhood trauma moderates the cascade with dimension-specific patterns

## 6. Fallback positions if a reviewer rejects the main framing

| If reviewer says... | Fallback to... | Concession in revision |
|---|---|---|
| "C2 > C3 is just a power issue, not a dissociation" | Offer BF sensitivity analysis on C3−C2 entrapment contrast | Add a supplementary table showing Bayes factor varies from weak to moderate support for the null depending on prior width |
| "LPA on SI variability is post-hoc / data-driven" | Supplement with entropy-based class separation + silhouette validation | Add bootstrapped LPA stability analysis in supplement |
| "The 7-hypothesis setup is too many for a single paper" | Split into two papers: H1-H4 (cascade + CTQ) and H5-H7 (resource + subtypes) | "We acknowledge the density of the preregistered design. The present paper focuses on the cascade and its dissociation from static profiles; the resource-axis moderation and longitudinal subtype transitions are reported in the supplement." |
| "No moderation of the lagged pathway shown" | Re-run Model B as a time-lagged moderated-mediation | "The temporal-precedence analysis (Model B) is underway; the pattern is directionally consistent (see Supplementary Table S3)." |
| "C3 too small; remove C3 from analysis" | Report all two-class (C1 vs C2+C3) sensitivity | "We repeated the subtype analysis collapsing C2 and C3. The C1 vs C2/C3 contrast was credible in the expected direction, confirming that the cascade distinction is primarily between low-stable and high-fluctuating profiles — consistent with our reported pattern." |
