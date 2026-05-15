# LTA Step 1 Checkpoint: Data Audit and Wave-Level State Screening

## What Was Completed

- Located the prompt-level EMA file: `D:/R/research/study1_ema391_analysis_ready_long.csv`.
- Built a de-identified person-wave candidate table from raw EMA indicators.
- Created threshold-based LTA analysis sets.
- Screened 2-5 class wave-specific latent state solutions using two theory-driven indicator sets.
- Removed the dissertation's existing LPA class variables from the new small-paper data build.

## Generated Files

- `data/derived/lta_person_wave_candidates.csv`
- `data/derived/lta_person_wave_qa.md`
- `data/derived/lta_person_wave_threshold8.csv`
- `data/derived/lta_person_wave_balanced_threshold8.csv`
- `data/derived/lta_person_wave_balanced_baseline_covariate_threshold8.csv`
- `data/derived/lta_wide_balanced_threshold8.csv`
- `data/derived/lta_indicator_descriptives_threshold8.csv`
- `data/derived/lta_indicator_correlations_threshold8.csv`
- `data/derived/wave_profile_screen_fit_indices.csv`
- `data/derived/wave_profile_screen_class_profiles.csv`

## Key Sample Facts

- Prompt-level EMA rows in the located raw file: 29,704.
- EMA participants in the located raw file: 389.
- Person-wave rows: 1,556.
- Balanced four-wave sample with at least 8 valid prompts per wave: 377 participants.
- Balanced four-wave sample with at least 8 valid prompts per wave plus baseline covariate match: 366 participants.
- The scale file has 931 participant records, but only 378 match the EMA file and have the baseline covariates needed for candidate transition predictors.

## Important Discrepancy to Resolve

Current manuscript materials mention 391 participants and, in some places, 28,723 prompt-level observations. The raw EMA file located through the analysis scripts contains 389 participants and 29,704 prompt-level rows.

This must be resolved before preregistration, methods writing, or final LTA reporting. For the small paper, the safest current wording is:

```text
The preliminary LTA data build used the available prompt-level EMA file containing 29,704 observations from 389 participants. After requiring at least 8 valid prompts in each of four EMA waves, the balanced analytic sample contained 377 participants.
```

## Indicator Sets Screened

Primary suicide-risk state set:

```text
stress_sum_mean
entrapment_mean
burdensomeness_mean
belongingness_mean
si_mean
```

Alternative state set with SI reserved as a distal outcome:

```text
stress_sum_mean
entrapment_mean
burdensomeness_mean
belongingness_mean
loneliness_mean
```

## Screening Interpretation

BIC continued to improve through 5 classes in both indicator sets and all four waves. This suggests strong distributional heterogeneity, but it does not automatically justify a 5-state LTA.

The 3-state solutions are interpretable as low, moderate, and high risk. The 4-state solutions usually separate an additional very-low or intermediate-risk state. The 5-state solutions often split severity gradients further, which may make the transition matrix harder to interpret and less stable.

## Recommended Next Modeling Decision

Proceed to formal LTA with the 4-state solution as the leading candidate, while retaining 3-state as the conservative comparison.

Use this hierarchy:

1. Fit 3-state LTA.
2. Fit 4-state LTA.
3. Only fit 5-state LTA as a sensitivity check if convergence is acceptable and the transition matrix remains interpretable.

## Recommended Manuscript Position After Step 1

The small paper should not claim that the latent states are already finalized. The defensible current claim is:

```text
Preliminary wave-specific profile screening based only on newly derived EMA indicators indicated reproducible low-to-high daily-life risk-state structure across four EMA waves. A 4-state LTA appears theoretically promising because it preserves severity differentiation without overcomplicating the transition matrix.
```
