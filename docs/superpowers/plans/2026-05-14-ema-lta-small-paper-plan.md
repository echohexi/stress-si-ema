# EMA-LTA Small Paper Research Plan

> **For research execution:** use this as a staged analysis and writing checklist. Each task should be completed in order, because later modeling decisions depend on the earlier conceptual and data audits.

**Goal:** Build a small paper that uses the four-wave EMA data to answer a new longitudinal transition question from the raw data, without using the dissertation's existing LPA classes as input, validation target, or interpretive anchor.

**Core Positioning:** The dissertation focuses on within-person stress-to-suicidal-ideation cascades and static/dynamic subtype differentiation. The small paper should focus on latent state transitions: which daily-life psychological states exist across EMA waves, how students move between them, and what predicts risk escalation or recovery.

**Available Evidence From Current Workspace:** The current project materials report a four-wave EMA design. For this small paper, the analysis must start from the raw prompt-level EMA file and freshly derive wave-level indicators. Existing dissertation LPA classes must not be used for sample eligibility, model fitting, class naming, hypothesis construction, or primary interpretation.

---

## Recommended Paper Positioning

**Working title:** Latent transitions in daily-life suicide-risk states across four EMA waves among college students

**One-sentence research question:** Across four EMA waves, do students show distinct latent daily-life risk states, how stable or changeable are these states over time, and which baseline or time-varying factors predict escalation, persistence, or recovery?

**What makes it different from the dissertation:** This paper does not ask whether previously identified SI trajectory classes differ in cascade strength, and it does not reuse those classes. It asks whether momentary psychological risk configurations can be newly identified from EMA indicators and whether these configurations change across time.

**Preferred conceptual frame:** Dynamic risk-state transition. Use IMV/IPT variables as state indicators, and use trauma, resources, sleep, loneliness, depression/anxiety, and life events as predictors or distal outcomes depending on temporal order.

---

## Task 1: Lock the New Research Question

- [ ] Define the target phenomenon as "latent risk-state transition", not "LPA subtype validation" and not "extension of existing dissertation classes".
- [ ] Decide whether the main outcome is suicide-specific risk, broad affective distress, or interpersonal suicide-risk state.
- [ ] Use this primary wording unless the supervisor requests a different emphasis:

```text
This study used four-wave ecological momentary assessment data to identify latent daily-life suicide-risk states and examine transitions among these states over one academic year. We further tested whether distal vulnerabilities and proximal resources predicted risk-state escalation, persistence, or recovery.
```

- [ ] State the novelty in the introduction as a time-dynamic question:

```text
Prior EMA studies have clarified short-term within-person associations among stress, proximal interpersonal-cognitive states, and suicidal ideation. Less is known about whether these momentary risk configurations form recurrent latent states that remain stable, worsen, or remit across repeated EMA bursts.
```

**Decision rule:** If a paragraph sounds like "we confirmed the dissertation subtypes" or "we found three types of people", revise it. The small paper should sound like "we derived daily-life states from EMA indicators and examined movement among them".

---

## Task 2: Audit the Data Structure

- [ ] Locate the raw prompt-level EMA dataset used to produce the 28,723 observations.
- [ ] Confirm the exact time variables available:
  - participant ID
  - wave number
  - day within wave
  - prompt number or timestamp
  - EMA indicators for stress, entrapment, perceived burdensomeness, thwarted belongingness, loneliness, affect, and suicidal ideation
- [ ] Confirm whether each wave can be summarized into one person-wave record.
- [ ] Create a person-wave analysis table with one row per participant per wave.

Minimum table structure:

```text
pid
wave
n_prompts_valid
response_rate_wave
stress_mean
stress_variability
entrapment_mean
burdensomeness_mean
belongingness_mean
si_mean
si_any
si_variability
loneliness_mean
negative_affect_mean
positive_affect_mean
sleep_or_daily_functioning_if_available
```

- [ ] Exclude person-wave rows with insufficient EMA data before modeling.

Recommended exclusion rule:

```text
Retain a person-wave record if it contains at least 8 valid prompts within that wave. Test 6-prompt and 10-prompt thresholds in sensitivity analyses.
```

**Decision rule:** Do not run LTA directly on every prompt as a separate wave. Four academic waves are appropriate for LTA; thousands of prompts are better used to construct reliable person-wave indicators.

---

## Task 3: Choose the Latent State Indicators

Use a small, theory-driven indicator set. Avoid overloading LTA with too many highly correlated variables.

Primary indicator set:

```text
stress_mean
entrapment_mean
burdensomeness_mean
belongingness_mean
si_mean or si_any
```

Alternative indicator set if affect variables are central:

```text
negative_affect_mean
positive_affect_mean
loneliness_mean
stress_mean
si_mean or si_any
```

Preferred recommendation:

```text
Use the IMV/IPT set as the main model, because it connects cleanly to the dissertation while answering a different longitudinal question.
```

- [ ] Standardize continuous indicators within the analytic sample.
- [ ] Treat SI carefully because of low base rate. Compare continuous SI mean with binary any-SI as a sensitivity check.
- [ ] Inspect distributions for floor effects before deciding whether SI should be an indicator or distal outcome.

**Decision rule:** If SI is too sparse and dominates class separation, move SI to a distal outcome and define states using stress, entrapment, burdensomeness, belongingness, loneliness, and affect.

---

## Task 4: Fit Measurement Models Before LTA

- [ ] Fit separate latent profile models at each wave with 2, 3, 4, and 5 classes.
- [ ] Compare BIC, sample-size-adjusted BIC, entropy, average posterior probabilities, smallest class size, and interpretability.
- [ ] Reject class solutions with tiny unstable classes unless they are theoretically essential and reproducible across waves.

Minimum reporting table:

```text
wave
n_classes
BIC
ssaBIC
entropy
smallest_class_n
smallest_class_percent
interpretability_rating
```

- [ ] Test whether the same number and meaning of states can be retained across waves.
- [ ] Name states by profiles, not severity alone.

Possible state labels:

```text
Low-risk regulated
Interpersonal distress
Entrapment-dominant risk
High-risk diffuse distress
```

**Decision rule:** Prefer a 3-class or 4-class solution if it is stable and interpretable. Avoid a 5-class solution unless it clearly adds a theoretically distinct state and not just a split of severity.

---

## Task 5: Fit the LTA Model

- [ ] Fit unconditional LTA first.
- [ ] Estimate class prevalence at each wave.
- [ ] Estimate transition probabilities from Wave 1 to Wave 2, Wave 2 to Wave 3, and Wave 3 to Wave 4.
- [ ] Summarize the main transition types:

```text
stable low risk
persistent high risk
escalation
recovery
fluctuating or recurrent risk
```

- [ ] Visualize transitions with a Sankey plot or alluvial plot.

Primary interpretation target:

```text
The central result is not only which states exist, but whether movement into and out of high-risk states is common, asymmetric, and predictable.
```

**Decision rule:** If class labels shift across waves, do not force strong transition interpretation. Revisit measurement invariance or use a simpler model.

---

## Task 6: Add Predictors of Transition

Use predictors only after the unconditional LTA is stable.

Baseline vulnerability predictors:

```text
CTQ dimensions
baseline PANSI negative
baseline depression/anxiety
baseline loneliness
suicide history
NSSI history
```

Resource predictors:

```text
cognitive reappraisal
connectedness
resilience
adaptive personality functioning
sleep quality
```

Time-varying predictors if available by wave:

```text
wave-level life events
wave-level sleep quality
wave-level loneliness
wave-level depression/anxiety
```

- [ ] Model predictors as transition covariates, not merely class-membership covariates.
- [ ] Prioritize two transition contrasts:

```text
low-risk to higher-risk escalation
higher-risk to lower-risk recovery
```

**Decision rule:** Do not include every available scale in the main model. Use a small predictor set that maps onto vulnerability and resource axes.

---

## Task 7: Run Robustness Checks

- [ ] Refit LTA with SI as an indicator.
- [ ] Refit LTA with SI as a distal outcome.
- [ ] Refit using different minimum valid-prompt thresholds per wave.
- [ ] Check whether class solution changes when response rate is included as a covariate.
- [ ] Check whether transition findings remain when participants with very low compliance are excluded.
- [ ] If class sizes are small, report transition estimates cautiously and avoid overclaiming rare transitions.

**Decision rule:** The paper is publishable if the broad transition story is stable. It does not require every exact class boundary to be identical across robustness checks.

---

## Task 8: Decide the Main Manuscript Claim

Use one of these claims after results are known.

If transitions are frequent:

```text
Daily-life suicide-risk states were dynamic across the academic year, with a meaningful subgroup showing escalation into high-risk states and another subgroup showing recovery.
```

If stability dominates:

```text
Daily-life suicide-risk states showed substantial stability across EMA waves, suggesting that momentary risk configurations can operate as persistent dynamic phenotypes.
```

If predictors are strong:

```text
Risk and resource factors distinguished not only who occupied high-risk states, but who escalated into or recovered from them over time.
```

If predictors are weak:

```text
Latent state transitions were identifiable, but common trait vulnerability and resource measures showed limited ability to predict movement between states.
```

**Decision rule:** Let the result decide the claim. Do not promise "mechanism" unless transition predictors are temporally ordered and robust.

---

## Task 9: Draft the Paper

Recommended structure:

```text
Introduction
1. EMA captures short-term suicide-risk dynamics.
2. Existing work identifies within-person processes but less often models latent state transitions.
3. LTA can test stability, escalation, and recovery across repeated EMA bursts.
4. Present study: four-wave EMA, latent risk states, transition probabilities, predictors.

Methods
1. Participants and EMA design.
2. EMA state indicators and person-wave aggregation.
3. Person-level and wave-level predictors.
4. Latent profile and latent transition analysis.
5. Missing data and sensitivity analyses.

Results
1. Descriptives and compliance.
2. Wave-specific latent state solutions.
3. Unconditional LTA transitions.
4. Predictors of escalation and recovery.
5. Sensitivity analyses.

Discussion
1. Main transition pattern.
2. Theoretical meaning for dynamic suicide-risk models.
3. Why this differs from the dissertation subtype paper.
4. Practical implications for monitoring and prevention.
5. Limitations.
```

- [ ] Keep the manuscript focused on one central contribution: dynamic transition.
- [ ] Avoid reusing the dissertation's full mediation framework except as background.
- [ ] Do not use the dissertation LPA findings in the primary analysis or Discussion argument. If mentioned at all, they should appear only in a brief limitation/context sentence after the new LTA findings are fully established.

---

## Task 10: Supervisor Discussion Checklist

Ask the supervisor to decide these points before full modeling:

- [ ] Should the LTA states be suicide-specific or broader affective-interpersonal states?
- [ ] Should SI be an indicator of states or a distal outcome predicted by states?
- [ ] Should predictors emphasize childhood trauma, current resources, or wave-level proximal changes?
- [ ] What is the acceptable minimum person-wave EMA compliance threshold?
- [ ] Is the target outlet a suicide/affective-disorder journal or a methods/digital-phenotyping journal?

Recommended proposal to supervisor:

```text
I plan to use the four EMA waves to freshly derive person-wave latent risk states and model transitions across the academic year. This will be independent of the dissertation LPA work: existing dissertation classes will not be used as predictors, outcomes, filters, labels, or validation targets. I will first test whether stable wave-level latent states can be identified from EMA indicators, then estimate transition probabilities, and finally test a small set of vulnerability and resource predictors.
```

---

## Immediate Next Actions

- [ ] Find the raw prompt-level EMA dataset.
- [ ] Build the person-wave table.
- [ ] Run descriptive checks for each candidate indicator.
- [ ] Fit wave-specific 2-5 class models.
- [ ] Select the class count and state labels.
- [ ] Fit unconditional LTA.
- [ ] Add a small predictor set only after the unconditional model is stable.
