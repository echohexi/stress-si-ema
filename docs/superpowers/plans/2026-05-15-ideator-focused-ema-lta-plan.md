# Ideator-Focused EMA-LTA Small Paper Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evaluate and implement a JAD-inspired ideator-focused EMA analysis route that excludes students with no suicidal ideation during EMA from the latent-state modeling sample, while retaining them as a reference group for descriptive and validation comparisons.

**Architecture:** This plan separates the paper into two nested analytic layers. First, all EMA participants are used to define the sampling frame and compare never-SI versus ever-SI students. Second, latent profile/transition modeling is conducted only among students who reported at least one EMA suicidal ideation episode. The approach avoids using the dissertation LPA classes and derives all states freshly from EMA and baseline data.

**Tech Stack:** Python/pandas for data preparation and descriptive tables; Mplus for LPA/LTA; CSV/Markdown outputs for model comparison and manuscript tables.

---

## Core Decision

This is not a simple sample-size reduction. It changes the research question.

Original full-sample question:

> Across all students, what latent daily-life suicide-risk states exist, and how do students transition among them?

Ideator-focused question:

> Among students who experienced suicidal ideation during EMA, what latent suicidal-ideation dynamic states exist, and how do these states persist, remit, or intensify across waves?

The ideator-focused route is defensible only if the paper clearly states that the target population is **EMA-identified ideators**, not all college students.

## Current Data Implication

Using the balanced threshold-8 person-wave data:

- Full balanced analytic sample: 377 participants, 1508 person-waves.
- Ever-SI participants during EMA: 193 participants, 772 person-waves.
- Never-SI participants during EMA: 184 participants.
- Within the 193 ever-SI participants, 392 person-waves are SI-positive and 380 person-waves are SI-negative.

This means the ideator-focused route keeps a clinically meaningful sample, but it does not remove all SI sparsity. Many retained participants still have SI-negative waves, which is useful for studying remission/reappearance but risky for over-complex LTA.

## Recommended Manuscript Positioning

Working title:

> Dynamic profiles of suicidal ideation among college students identified through ecological momentary assessment

One-sentence research question:

> Among college students who reported suicidal ideation during EMA, do distinct profiles of momentary suicidal-ideation burden and proximal psychological risk emerge across waves, and how do students transition among these profiles over time?

Primary novelty:

> Instead of classifying all students by broad distress states, this paper focuses on students with observed suicidal ideation and examines whether SI intensity, persistence, and proximal interpersonal-cognitive risk form dynamic states across repeated EMA waves.

Do not claim:

> This model describes the latent risk-state structure of all college students.

Safe claim:

> This model describes heterogeneity among students with EMA-observed suicidal ideation; never-SI students are retained as a reference group for sample characterization and external validation.

## Analysis Strategy Overview

### Route A: Full-Sample Risk-State LTA

Purpose:

Use all 377 balanced participants to identify broad daily-life risk states from stress, entrapment, burdensomeness, belongingness-related risk, and loneliness.

Current status:

- 4-state invariant LTA is the strongest stable pilot candidate.
- Main concern: small extreme-risk state and sparse transition paths.

Role in final project:

Keep as the original main route unless the ideator-focused route gives a clearer and more publishable story.

### Route B: Ideator-Focused SI-Dynamic Modeling

Purpose:

Use only the 193 ever-SI participants for latent profile/transition modeling.

Recommended status:

Treat this as the strongest alternative route. It is more clinically focused and closer to the 2025 JAD paper logic, but it should start with simpler models.

Critical rule:

Do not begin with 4-state LTA in the 193-person ideator sample. Start with 2-state and 3-state models.

## Indicator Strategy

### Primary SI-Dynamic Indicator Set

Use indicators that describe SI burden during each EMA wave:

- `si_mean`: average SI intensity during the wave.
- `si_any_prompt_prop`: proportion of prompts with SI endorsement.
- `si_sd` or `si_rmssd`: instability/variability of SI when available.
- `stress_sum_mean`: wave-level stress exposure.
- `entrapment_mean`: proximal cognitive risk.
- `burdensomeness_mean`: interpersonal suicide-risk cognition.

Rationale:

This route should not merely reproduce broad distress classes. It should define states by SI burden plus theoretically proximal risk processes.

### Alternative Smaller Indicator Set

Use if the primary set creates unstable profiles:

- `si_mean`
- `si_any_prompt_prop`
- `entrapment_mean`
- `burdensomeness_mean`
- `stress_sum_mean`

Rationale:

The ideator sample is smaller, so the model should avoid too many correlated indicators.

### Variables Reserved for Validation or Prediction

Do not use these as state indicators in the first ideator-focused model:

- baseline PANSI negative
- depression/anxiety
- CTQ
- NSSI history
- suicide history
- resilience / connectedness / cognitive reappraisal

Use them later to test whether classes differ meaningfully or predict transition risk.

## Model-Building Plan

### Task 1: Create Ideator-Focused Analysis Dataset

**Files:**

- Read: `data/derived/lta_person_wave_balanced_threshold8.csv`
- Create: `data/derived/lta_person_wave_balanced_threshold8_ever_si.csv`
- Create: `data/derived/lta_person_wave_balanced_threshold8_never_si_reference.csv`
- Create: `data/derived/ever_si_sample_qa.md`

- [ ] Identify each participant's EMA-ever-SI status.
- [ ] Keep participants with `max(si_any_wave) > 0` in the ideator modeling sample.
- [ ] Store participants with `max(si_any_wave) == 0` as the reference group.
- [ ] Summarize retained versus excluded participants by baseline vulnerability and EMA response quality.

Decision gate:

Proceed only if the ever-SI sample remains near the current count of 193 participants and has all four waves for most or all participants.

### Task 2: Compare Ever-SI and Never-SI Groups

**Files:**

- Create: `data/derived/ever_vs_never_si_baseline_comparison.csv`
- Create: `data/derived/ever_vs_never_si_baseline_comparison.md`

- [ ] Compare demographics, baseline PANSI, depression/anxiety, NSSI, suicide history, and EMA response counts.
- [ ] Report standardized mean differences, not only p-values.
- [ ] Use this table to show what population the ideator-focused model applies to.

Decision gate:

If ever-SI and never-SI groups differ strongly on baseline severity, frame the ideator analysis as clinically enriched and not population-representative.

### Task 3: Descriptive SI-Dynamic Audit

**Files:**

- Create: `data/derived/ever_si_indicator_descriptives.csv`
- Create: `data/derived/ever_si_indicator_correlations.csv`
- Create: `data/derived/ever_si_indicator_strategy.md`

- [ ] Inspect floor effects for `si_mean` and `si_any_prompt_prop` within the ever-SI sample.
- [ ] Check whether `si_mean` and `si_any_prompt_prop` are almost redundant.
- [ ] Check correlations among entrapment, burdensomeness, belongingness, loneliness, and stress.
- [ ] Decide whether to use the primary or smaller indicator set.

Decision gate:

If SI indicators remain extremely sparse even within ever-SI students, use SI as the central class indicator but keep the number of states small.

### Task 4: Wave-Specific LPA Screening

**Files:**

- Create: `data/derived/ever_si_wave_profile_screen.csv`
- Create: `data/derived/ever_si_wave_profile_screen.md`

- [ ] Fit 2-, 3-, and 4-profile models separately at each wave.
- [ ] Compare BIC, ssaBIC, entropy, smallest class size, and interpretability.
- [ ] Reject 4-profile solutions if any wave has a class below roughly 5% or fewer than 10 estimated participants.

Decision gate:

Expected best candidate is 2 or 3 profiles. A 4-profile solution should be treated as exploratory only.

### Task 5: Ideator-Focused LTA

**Files:**

- Create: `mplus/lta_ever_si/lta_ever_si_2state_invariant.inp`
- Create: `mplus/lta_ever_si/lta_ever_si_3state_invariant.inp`
- Create: `mplus/lta_ever_si/lta_ever_si_2state_configural.inp`
- Create: `mplus/lta_ever_si/lta_ever_si_3state_configural.inp`
- Create: `data/derived/ever_si_lta_fit_summary.csv`
- Create: `data/derived/ever_si_lta_transition_summary.csv`

- [ ] Run 2-state invariant LTA.
- [ ] Run 3-state invariant LTA.
- [ ] Run 2-state configural LTA.
- [ ] Run 3-state configural LTA.
- [ ] Do not run 4-state LTA until 2- and 3-state models are stable.

Decision gate:

Choose the model with the best balance of:

- replicated best loglikelihood
- no severe standard-error warnings
- acceptable smallest class size
- interpretable SI burden gradient
- transition matrix without excessive empty cells

### Task 6: Validate Classes Against External Risk

**Files:**

- Create: `data/derived/ever_si_class_validation.csv`
- Create: `data/derived/ever_si_class_validation.md`

- [ ] Compare classes on baseline PANSI negative, NSSI, prior suicide history, depression/anxiety, CTQ, and resources.
- [ ] Test whether higher SI-dynamic classes show higher baseline risk and lower protective resources.
- [ ] Check whether class membership predicts future wave SI burden.

Decision gate:

If classes do not differ on SI burden or external risk markers, do not use this route as the main paper.

### Task 7: Compare Route A and Route B

**Files:**

- Create: `docs/superpowers/plans/2026-05-15-route-comparison-decision.md`

- [ ] Compare full-sample LTA and ideator-focused LTA on model stability.
- [ ] Compare interpretability of class profiles.
- [ ] Compare manuscript novelty.
- [ ] Compare likely reviewer objections.
- [ ] Choose one main paper route and one supplementary route.

Decision rule:

Use Route B as the main paper only if it produces a stable 2- or 3-state model with clear SI burden differences and a stronger clinical story than the full-sample LTA.

## Recommended Final Design if Route B Works

Main analytic sample:

- 193 EMA-ever-SI students.

Reference sample:

- 184 EMA-never-SI students, used only for descriptive comparison and external positioning.

Primary model:

- 2- or 3-state ideator-focused invariant LTA.

Candidate state labels:

- Low/past or intermittent SI burden
- Moderate persistent SI-risk state
- High SI burden with entrapment-interpersonal risk

Main outcomes:

- Initial latent state prevalence.
- Transition probabilities across four EMA waves.
- Probability of persistence, remission, and escalation.
- Baseline predictors of high-risk persistence or escalation.

Main manuscript claim:

> Among students with EMA-observed suicidal ideation, latent SI-dynamic states differed in ideation burden and proximal interpersonal-cognitive risk. Transitions suggested that SI risk was not static: some students remitted, some persisted, and a smaller group escalated or remained high-risk.

## Reviewer Risk Assessment

### Strengths

- More clinically focused than broad distress-state LTA.
- Avoids letting never-SI participants dominate class formation.
- Directly models heterogeneity among students who actually experienced SI.
- Easier to connect to intervention relevance.

### Risks

- Reduced sample size from 377 to 193.
- Results no longer generalize to all students.
- Four-wave LTA may still have sparse transition cells.
- If too many SI indicators are used, classes may become simple severity splits.
- Excluding never-SI participants can be criticized unless they are retained as a reference group.

### Mitigation

- Present never-SI students as a reference/control group.
- Use 2- and 3-state models first.
- Use full-sample LTA as a sensitivity or alternative analysis.
- Emphasize clinical enrichment rather than population prevalence.
- Report class size and transition sparsity transparently.

## Final Recommendation

Do not abandon the original full-sample LTA yet.

Run this ideator-focused route as a serious alternative. It is likely more publishable if the model stabilizes at 2 or 3 states and validates clearly against SI burden and baseline risk. It is likely less publishable if it requires 4 states or produces sparse/unstable transitions.

The safest strategic posture is:

> Develop both routes through the unconditional-model stage, then choose the route with the clearest balance of stability, interpretability, and clinical contribution.

