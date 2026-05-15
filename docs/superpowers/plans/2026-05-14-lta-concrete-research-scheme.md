# EMA-LTA Concrete Research Scheme

## Applied Skills

- `research-idea-incubator`: used to convert the broad idea into a publishable paper path.
- `scientific-critical-thinking`: used to check whether the design avoids circularity, overclaiming, and post-hoc subtype validation.
- `statistical-analysis`: used to evaluate indicator distributions, floor effects, and modeling choices.
- `executing-plans`: used to advance the existing plan task by task.

## Stage Classification

`paper/design`

The study has existing data and a general method direction, but the scientific contribution and statistical specification must be locked before formal LTA modeling.

## One-Sentence Reconstruction

This study will use raw four-wave EMA data to freshly derive latent daily-life risk states among college students, estimate transitions among those states across the academic year, and test whether baseline vulnerabilities and resources predict escalation, persistence, or recovery.

## Core Judgment

`worth pursuing`

The idea is publishable if it stays independent from the dissertation LPA classes and makes state transition, not static subtype description, the core contribution.

## Feasibility Matrix

| Dimension | Judgment | Reason |
|---|---|---|
| Theory | strong | IMV/IPT indicators map cleanly onto entrapment, burdensomeness, belongingness, loneliness, and stress exposure. |
| Data | medium-strong | The raw EMA file has 29,704 prompt-level rows; the balanced four-wave threshold-8 sample has 377 participants. |
| Method | medium | LTA is appropriate for four wave-level states, but formal estimation must be done in Mplus/R or another dedicated mixture-modeling tool. |
| Ethics | medium | Suicide-related variables require cautious wording; avoid individual prediction claims and clinical decision claims. |
| Novelty | medium-strong | The stronger contribution is modeling movement among EMA-derived daily-life states, not identifying classes per se. |
| Publishability | medium-strong | The paper is plausible for affective-disorder, suicide-risk, or digital-phenotyping outlets if transitions predict SI or are predicted by meaningful vulnerabilities/resources. |

## Main Design Decision

Use SI as a distal validation outcome in the primary model, not as a primary state indicator.

### Evidence

From `data/derived/lta_indicator_strategy_eval.md`:

- `si_mean` floor rate across balanced person-waves: 0.740.
- `si_any_prompt_prop` zero rate: 0.740.
- Any-SI wave rate declines from Wave 1 to Wave 4: 0.324, 0.276, 0.215, 0.225.
- SI correlates with the proximal indicators but is sparse enough to risk dominating class separation if included directly.

### Primary State Indicators

```text
stress_sum_mean
entrapment_mean
burdensomeness_mean
belongingness_mean
loneliness_mean
```

### Distal Outcomes

```text
si_mean
si_any_wave
si_any_prompt_prop
```

### Baseline Predictors

Use a small predictor set first:

```text
CTQ_total_master
DASS_total_T1
PANSI_neg_T1
PSQI_raw_sum_T1
CERQ_maladaptive_T1
CERQ_adaptive_T1
```

Then add resource predictors as a second block if the first model is stable:

```text
Connect_total_T2
ERQ_reapp_T3
BRS_total_T3
LPFS_total_T3
```

## Primary Model Path

### Model 1: Wave-Specific State Screening

Purpose: confirm that the same broad state structure appears across all four waves.

Use the primary indicator set:

```text
stress_sum_mean
entrapment_mean
burdensomeness_mean
belongingness_mean
loneliness_mean
```

Compare 3-state and 4-state solutions as the main candidates.

Interpretation rule:

```text
Prefer 4 states only if it produces a substantively distinct state beyond simple severity splitting and all states remain interpretable across waves.
```

### Model 2: Unconditional LTA

Purpose: estimate transition probabilities without predictors.

Main comparison:

```text
3-state LTA vs 4-state LTA
```

Primary outputs:

```text
state prevalence by wave
transition matrix W1->W2
transition matrix W2->W3
transition matrix W3->W4
stable low-risk proportion
persistent high-risk proportion
escalation proportion
recovery proportion
```

### Model 3: Distal SI Validation

Purpose: test whether newly derived state membership and transition patterns have suicide-risk meaning.

Primary contrasts:

```text
high-risk state vs low-risk state on si_mean
escalation vs stable-low on later si_any_wave
recovery vs persistent-high on later si_any_wave
```

This model supports construct validity but does not justify causal language.

### Model 4: Transition Predictors

Purpose: test who escalates and who recovers.

Primary transition outcomes:

```text
low/intermediate -> higher-risk escalation
higher-risk -> lower-risk recovery
persistent high-risk vs recovery
```

Predictor blocks:

1. Baseline vulnerability: childhood trauma, baseline distress, baseline SI, sleep.
2. Cognitive/emotional regulation: maladaptive and adaptive CERQ.
3. Resources: connectedness, reappraisal, resilience, personality functioning.

## Three Optimized Versions

### Conservative Version

Title direction:

```text
Latent daily-life risk states and their stability across four EMA waves
```

Analysis:

```text
3-state LTA; SI only as distal outcome; baseline predictors exploratory.
```

Use if the 4-state model is unstable or hard to interpret.

### Stronger Version

Title direction:

```text
Escalation and recovery in EMA-derived daily-life suicide-risk states
```

Analysis:

```text
4-state LTA; SI distal validation; baseline vulnerability and resource predictors of transition.
```

This is the recommended main path.

### Bold Version

Title direction:

```text
Dynamic reorganization of interpersonal-cognitive suicide-risk states across an academic year
```

Analysis:

```text
4-state or 5-state LTA; transition predictors; transition-to-SI distal outcomes; visualization as alluvial/Sankey flow.
```

Use only if the formal LTA is stable and state labels are consistent across waves.

## Main Failure Modes

- The 4-state solution may split severity without adding theory.
- SI may be too sparse for strong distal validation.
- Transition predictors may be weak after accounting for baseline SI/distress.
- Four waves may not support overly complex transition structures.
- If state labels shift across waves, transition interpretation becomes fragile.
- Because the design is observational, predictors of transition cannot be described as causes.

## Minimum Viable Validation

Before running a full predictor LTA, complete these checks:

1. Confirm 3-state and 4-state wave-specific profiles are interpretable across all waves.
2. Confirm the unconditional LTA transition matrix is not dominated by one nearly absorbing state.
3. Confirm higher-risk states have higher later SI than lower-risk states.
4. Confirm escalation is associated with later SI elevation compared with stable-low status.

Supportive result:

```text
Newly derived states are stable enough to label, transitions occur at nontrivial rates, and escalation predicts later SI.
```

Weakening result:

```text
States are interpretable but transitions are rare or not associated with SI.
```

Kill criterion:

```text
State labels are inconsistent across waves and no transition pattern has interpretable relation to SI.
```

## Paper Path

### Working Title

```text
Escalation and recovery in EMA-derived daily-life suicide-risk states across one academic year
```

### Research Questions

1. What latent daily-life risk states can be derived from repeated EMA indicators of stress, entrapment, burdensomeness, belongingness, and loneliness?
2. How stable are these states across four EMA waves?
3. Do transitions into higher-risk states predict later suicidal ideation?
4. Which baseline vulnerability and resource factors predict escalation or recovery?

### Hypotheses

H1. Three or four interpretable daily-life risk states will emerge across waves.

H2. Most students will remain in low-risk or intermediate-risk states, but a meaningful subgroup will show escalation or recovery.

H3. Escalation into higher-risk states will be associated with higher later SI.

H4. Higher baseline vulnerability and lower resources will predict escalation and reduce recovery probability.

### Figure Plan

1. Profile plot of the selected states across indicators.
2. Alluvial/Sankey plot of state transitions across four waves.
3. Predicted probability plot for escalation/recovery predictors.
4. Distal SI plot by transition pattern.

## Next Concrete Action

Prepare formal 3-state and 4-state unconditional LTA inputs using the primary indicator set, then run the model in the available formal mixture-modeling environment.

