# LTA Indicator Strategy Evaluation

- Input: `data\derived\lta_person_wave_balanced_threshold8.csv`
- Rows: 1508
- Participants: 377
- Waves: 4

## Main Recommendation

- Primary strategy: use SI as a distal outcome, not a main state indicator.
- Primary state indicators: stress, entrapment, burdensomeness, belongingness, loneliness.
- Sensitivity strategy: include `si_mean` as a state indicator and check whether the transition story changes.

## SI Floor and Sparsity

- `si_mean` floor rate: 0.740
- `si_any_prompt_prop` zero rate: 0.740

## SI Any-Wave Rate

- Wave 1: 0.324
- Wave 2: 0.276
- Wave 3: 0.215
- Wave 4: 0.225

## Spearman Correlation With `si_mean`

- si_mean: 1.000
- si_any_prompt_prop: 0.997
- burdensomeness_mean: 0.441
- entrapment_mean: 0.432
- belongingness_mean: 0.403
- loneliness_mean: 0.320
- stress_sum_mean: 0.217
- morning_fatigue_mean: 0.171
- sleep_quality_mean: -0.168

## Indicator Distribution Summary

- stress_sum_mean: mean=2.233, sd=2.291, median=1.524, min=0.000, max=14.857, floor=0.102
- entrapment_mean: mean=1.401, sd=0.629, median=1.111, min=1.000, max=4.974, floor=0.296
- burdensomeness_mean: mean=1.279, sd=0.471, median=1.071, min=1.000, max=4.367, floor=0.351
- belongingness_mean: mean=1.352, sd=0.515, median=1.100, min=1.000, max=4.222, floor=0.281
- loneliness_mean: mean=1.504, sd=0.726, median=1.148, min=1.000, max=5.381, floor=0.180
- si_mean: mean=1.072, sd=0.256, median=1.000, min=1.000, max=3.933, floor=0.740
- si_any_prompt_prop: mean=0.072, sd=0.204, median=0.000, min=0.000, max=1.000, floor=0.740
- sleep_quality_mean: mean=4.785, sd=1.089, median=4.800, min=1.000, max=7.000, floor=0.002
- morning_fatigue_mean: mean=3.381, sd=1.158, median=3.420, min=1.000, max=7.000, floor=0.023
