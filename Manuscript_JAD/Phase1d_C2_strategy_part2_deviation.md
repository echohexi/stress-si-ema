# Phase 1d (part 2/3) — Pre-registration Deviation Framing & Competing Explanations

---

## 4. Pre-registration deviation: explicit acknowledgement

Pre-reg H6 stated: *"three subtypes show strictly monotonic C1 < C2 < C3 indirect effects (entrapment), posterior monotonicity probability ≥ 0.90."*

**Status: NOT supported.** Posterior monotonicity probability for entrapment a×b is well below 0.90 because of the C2 ↔ C3 ambiguity. This is a deviation we must report transparently.

**Locked wording for Results §3.5 (one sentence):**
> "Hypothesis 6 — that the within-person indirect effect would increase strictly monotonically across subtypes — was not supported: the C2 vs C3 contrast credibly excluded zero in neither the entrapment nor the perceived-burdensomeness pathway (Table 3)."

**Locked wording for Discussion §4.3 opening (one sentence):**
> "We had pre-registered a strictly monotonic gradient of cascade strength across the three SI subtypes; instead, the gradient saturated at the high-fluctuating subtype, with the highest-intensity subtype showing no credible further increase."

---

## 5. Three competing explanations (must all appear in Discussion §4.3)

For honesty and to pre-empt reviewer probes, all three must be named even though we only commit to one as primary.

### 5.1 Habituation / saturation (PRIMARY interpretation)

Above some threshold of chronic SI intensity, the proximal mechanism (entrapment-driven momentary spikes) saturates. Beyond saturation, additional severity expresses itself in *trait* metrics (CTQ-EA exposure, LPFS-BF dysfunction, lower BRS) rather than in *dynamic* sensitivity.

Mechanistic anchor:
- Clinical literature on suicidal-mode "kindling" (Beck): repeated activation lowers threshold but the within-event slope plateaus.
- Compatible with Glenn et al. (2017, *JCCP*) showing within-person reactivity peaks below the most chronically affected group.

This is the version we lead with. It is testable in future work (e.g., piecewise SEM with threshold knots).

### 5.2 Ceiling on SI scale measurement

The momentary SI item is rated 1–5; C3 mean SI = 1.99 (Table 1), so C3 person-waves are already non-trivially above floor. Higher stress cannot push SI past the upper end of the response scale, mechanically compressing the b-path slope.

Argument for: scale arithmetic alone limits available variance for the slope.
Argument against: C3 b-path estimates are *higher* than C2's (0.261 vs 0.162), not lower — so the slope itself is not flat. Only the *combined* a×b ends up similar because C3's a-path is *lower* (0.073 vs 0.100). The ceiling story does not naturally explain this asymmetry.

We mention this explanation, then note its incomplete fit.

### 5.3 Sample-size–driven instability for C3

C3 has 37 participants and 79 person-waves. With brms-style shrinkage, the C3 estimate is partially pulled toward the grand mean.

Argument against: even after pooling, the C3 a×b 95% CI [0.0150, 0.0235] does not include the C2 median (0.0162). If the gap were purely a power artefact, the C3 CI should be wide enough to *contain* the C2 estimate. It does not — they overlap, but C3's lower CI bound is 0.0150 < 0.0162. This argues that the C3 estimate is reasonably stable; the **contrast** is uncertain primarily because the *difference* is small (≈ 0.003), not because C3 itself is poorly identified.

Mention; rule out as primary; flag that confirmation in a larger high-severity sample is needed in Limitations.

---

## 6. What about Model B (the lagged-mediation reversal)?

Model B (`sensitivity_out/summary_modelB_lagged_overall_indirect.csv`) shows *all three* indirect effects flip to small negative values with CIs excluding zero when modelled as stress(t−1) → mediator(t) → SI(t+1):

| Pathway | a×b lag | 95% CI | PD |
|---|---|---|---|
| Entrap | −0.00014 | [−0.000285, −0.0000229] | 0.991 |
| Burden | −0.00015 | [−0.000273, −0.0000506] | 1.000 |
| Belong | −0.00014 | [−0.000267, −0.0000395] | 0.997 |

This **is not a contradiction** of the main C2 story. The main analysis and Model A (contemporaneous, AR1-controlled) both give positive cascades; only the *fully* lagged version reverses. Three plausible reasons:

1. **Mean reversion / regression-to-the-mean artefact**: high-stress prompts coincide with elevated mediators; the next prompt naturally drifts back to baseline, taking SI with it → spurious negative cross-time partial.
2. **Wrong time scale**: stress→SI cascades operate on a sub-hourly scale; ~5 h between prompts is past the natural window of mechanistic carryover.
3. **AR1-conditioning artefact**: once si_lag1 is partialled out, the residual SI variance reflects *recovery* signal rather than *new* arousal.

**Locked manuscript stance:** the cascade is **contemporaneous** (within-prompt), not delayed across prompts. We will say so explicitly in Methods §statistical-analyses and Limitations. This is also a *protective* framing — it tells reviewers up-front not to over-interpret the cascade as classical cross-lagged causation.

The Discussion §4.4 paragraph should be exactly one paragraph and end with: *"Within-prompt co-occurrence does not establish causal direction; the contemporaneous nature of the cascade is a feature of the design, not a claim about temporal precedence."*

---

*(Continued in part 3: locked words/phrases for the manuscript and recursion-proofing.)*
