# Feeding Bundle: Discussion Drafting (for Claude.ai)

> **Purpose**: Single self-contained context bundle for drafting the **Discussion** section of the JAD manuscript on Claude.ai. Paste this whole file into a Claude.ai conversation, then ask Claude.ai to draft Discussion following the spec at the bottom.
>
> **Target journal**: *Journal of Affective Disorders* (JAD), 一区
> **Bundle generated**: 2026-05-16 by Claude Code
> **Narrative authority**: `Phase1d_C2_narrative_strategy.md` (locked 2026-05-16)

---

## §1. The paper in one sentence

A 4-wave EMA study (N = 391 college students, 28,113 prompts) using Bayesian multilevel multivariate mediation to test whether the within-person stress-to-SI cascade through entrapment, burdensomeness, and belongingness is jointly shaped by childhood trauma (risk axis) and trait resources (resource axis), and whether three dynamic subtypes (C1/C2/C3) dissociate from the static trait gradient.

## §2. Narrative spine for Discussion (LOCKED — do not re-order)

From `Phase1d_C2_narrative_strategy.md` §5. Discussion must follow this exact section order (JAD convention):

1. **Restate main finding** (strong opening paragraph): "In N = 391 first-year undergraduates with 28,113 EMA prompts..."
2. **Frame A — Dynamic-static dissociation** (3-4 paragraphs, THE MAIN DISCUSSION)
3. **Frame B — Path-specific moderation** (1-2 paragraphs, includes PA reverse moderation)
4. **Frame C — Methodological contribution** (1 paragraph: Bayesian multivariate mediation)
5. **Limitations** (minimum 3, honest)
6. **Clinical implications** (mandatory for JAD)
7. **Conclusion** (strong close, tie back to opening)

## §3. Three narrative frames (from Phase1d_C2_narrative_strategy.md)

### Frame A — Dynamic-vs-static dissociation (LEAD, 3-4 paragraphs)

**Claim**: The strength of the within-person stress-to-SI cascade and the person's static trait severity index are partially separable constructs. Trait severity is strictly graded (C1 < C2 < C3); cascade reactivity has a non-monotonic profile in which C2 and C3 are dynamically indistinguishable.

**Mechanism vocabulary**: stress reactivity (Bonanno 2004; Selby & Joiner 2009); emotional inertia and variability as risk markers independent of mean level (Houben et al. 2015; Kuppens et al. 2010); dynamic phenotype vs. severity phenotype.

**This frame accounts for ALL five empirical facts** (from Phase1d §1):
1. C2 > C1 and C3 > C1 are credible across all three mediators.
2. C3 > C2 strict monotonicity is NOT credible for entrapment or burdensomeness (burden point estimate in wrong direction).
3. C3 − C2 lives in high-uncertainty zone (95% HDI spans both signs; PD ≈ 0.66; ROPE ≈ 0.025).
4. In RAW stress→SI slope, C3 − C2 IS credible (0.0110\*) — the non-monotonicity is specific to the *indirect* (a×b) pathway, not to the raw cascade.
5. Static trait profiles are strictly monotonic C1 < C2 < C3 on every risk indicator and inversely monotonic on every resource indicator.

**Key verbal guardrails**:
- Use "C2 and C3 were not credibly different" NOT "C2 > C3"
- Use "dissociation" NOT "paradox"
- Frame positively as "reveals a construct distinction" NOT negatively as "H6 failed"

### Frame B — Path-specific moderation (SECONDARY, 1-2 paragraphs)

- CTQ moderation is dimension-specific: EA broad, SA selective on entrapment/burden, neglect on relational mediators.
- **PA reverse moderation**: 2-3 mechanism sentences. EA amplifies a-path broadly; PA shows reverse-direction moderation on the same a-path. Potential mechanism: PA-related dissociation (DES data as suggestive). Exploratory finding needing replication in PA-enriched sample.
- Resource moderation and CTQ moderation operate on complementary pathways (resource on b-path, trauma on a-path in part), consistent with dual-axis framework.

### Frame C — Methodological (TERTIARY, 1 paragraph)

- Bayesian multivariate multilevel mediation with cross-equation random-effect covariance matrix.
- Simultaneous estimation of three mediators avoids model-selection bias.
- Replicates frequentist pre-analysis; method-independent validation.
- Implications for future EMA-SI research using similar designs.

## §4. Key locked facts and numbers (for reference — Discussion does NOT report new numbers)

Discussion refers back to Results numbers. Do NOT re-report them. The following are context only:

- H1: entrap a×b = 0.0048 [0.0036, 0.0061], burden = 0.0023, belong = 0.0012
- H2: P(entrap > burden) > 0.99, P(entrap > belong) > 0.99
- H4: ≥ 4 of 20 b-path interactions met PD ≥ 0.975
- H6: C3−C2 entrap PD < 0.90, burden PD < 0.90 (reversed), belong PD ≥ 0.975
- H7: Strictly monotonic on ALL risk/resource indicators
- Dissociation: Dynamic cascade ≠ static trait gradient
- Subtype sizes: C1 n=367, C2 n=128, C3 n=37

## §5. Limitations (minimum 3, must be honest)

1. **C3 sample size (n=37 participants, 79 person-waves)**: Limits statistical power for detecting C3−C2 contrasts. However, note that the claim is null (no credible difference), insufficient power makes this conservative, and the ROPE diagnostic confirms undecidedness rather than equivalence.
2. **Single-item SI outcome**: Standard in EMA-SI literature (Kleiman 2017, Hallensleben 2019) but lacks multi-faceted assessment. Compositive SI tools may capture additional variance.
3. **Self-report common-method variance**: All within-person variables measured at same prompt. Between-person confounds removed by within-person centering; AR(1)-controlled sensitivity addresses temporal autocorrelation.
4. **College convenience sample**: First-year Tianjin University undergraduates; generalizability to community, clinical, or non-college young-adult populations is untested.
5. **EMA compliance in C3**: If C3 participants systematically differ in response rate, missing-data mechanisms could bias subtype comparisons (tested via 20-min latency subsample — robust).

## §6. Clinical implications (mandatory for JAD, 1 full paragraph)

Must explicitly address what the findings mean for intervention design on Chinese college campuses:
- C2 profile: relatively normal trait profile but steep cascade → missing in trait-only screening → EMA monitoring needed
- C3 profile: high on every severity indicator but dynamic cascade not steeper than C2 → already captured by trait screening but may not need the most intensive EMA
- Entrapment as dominant mediator → target entrapment in micro-interventions (ACT-based defusion, re-appraisal of blocked escape)
- Dual-axis → address trauma AND build resources
- Dynamic-static dissociation → screening and monitoring are complementary, not redundant

## §7. Length and style rules

- JAD Discussion: no hard cap; typical JAD Discussions are 1500–2000 words. Stay within this range.
- Tone: interpretive but measured. Do NOT over-claim — use "suggest", "may reflect", "consistent with".
- Bayesian language throughout: "credible", "posterior probability", "95% CrI". Avoid "significant", "marginally significant".
- **PA reverse moderation**: 2-3 mechanism sentences MAX (Decision 1). Do NOT expand into a full subsection.
- **Do NOT invent findings**: Discussion refers only to numbers from Phase1_locked_numbers.md / Phase2c_Results_draft.md.
- **End strong**: Conclusion paragraph that ties back to the opening question: "What is the moment-to-moment cascade, and whose cascade is steepest?"

## §8. Files you may want Claude.ai to consult (upload to Project knowledge)

- This bundle (`_feed_Discussion.md`)
- `Phase1d_C2_narrative_strategy.md` (full narrative memo with reviewer defences in §4)
- `Phase2c_Results_draft.md` (Results draft to reference numbers)
- `Phase2a_Introduction_draft.md` (to ensure Discussion mirrors Introduction)
- `references.bib` (to auto-complete citations)

---

# DRAFTING SPEC (paste this to Claude.ai as the final instruction)

> Using the bundle above, draft the Discussion for a *Journal of Affective Disorders* submission of this paper. Constraints:
> 1. Follow §2 section order EXACTLY: restate finding → Frame A (3-4 para) → Frame B including PA (1-2 para) → Frame C (1 para) → Limitations (≥3) → Clinical implications (mandatory) → Conclusion.
> 2. Frame A is the LEAD narrative. DO NOT start with methodological fine-print or limitations.
> 3. PA reverse moderation: MAX 3 sentences in Frame B. Descriptive mechanism speculation allowed (dissociation/habituation) but keep brief. Do NOT put PA in its own subsection.
> 4. Do NOT re-report statistical numbers. Discussion refers, not reports.
> 5. 1500-2000 words total.
> 6. Tone: Interpretive, measured. Use "credible" not "significant". Bayesian language.
> 7. Conclusion must tie back to the opening question: by what moment-to-moment mechanism does stress convert into ideation.
> 8. Return the draft as one markdown block, ready for me to paste back into Claude Code for landing.