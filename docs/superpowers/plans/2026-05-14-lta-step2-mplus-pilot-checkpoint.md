# LTA Step 2 Checkpoint: Unconditional Mplus Pilot Models

Date: 2026-05-14

## Purpose

This checkpoint evaluates whether the EMA-derived LTA small-paper plan is empirically feasible and whether the current model results are likely to be acceptable for a publishable manuscript.

The analysis remains independent from the dissertation LPA classes. The LTA indicators are freshly derived from multi-wave EMA person-wave summaries:

- stress
- entrapment
- burdensomeness
- belongingness / belongingness-related risk
- loneliness

Suicidal ideation variables are retained for later distal validation, not used as primary class indicators in the unconditional LTA.

## Files Produced

- `data/derived/mplus_lta_fit_summary.csv`
- `data/derived/mplus_lta_class_proportions.csv`
- `data/derived/mplus_lta_transition_probabilities.csv`
- `data/derived/mplus_lta_class_means.csv`
- `data/derived/mplus_lta_pilot_summary.md`
- `code/parse_mplus_lta_outputs.py`

## Pilot Model Fit

| Model | N | Free parameters | LL | AIC | BIC | ssaBIC | Entropy | Replicated |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| 3-state invariant pilot | 377 | 40 | -7265.790 | 14611.580 | 14768.869 | 14641.959 | 0.970 | Yes |
| 4-state invariant pilot | 377 | 64 | -6807.015 | 13742.030 | 13993.693 | 13790.636 | 0.959 | Yes |

Relative to the 3-state model, the 4-state model improves:

- AIC by 869.550 points
- BIC by 775.176 points
- sample-size adjusted BIC by 851.323 points

This is a very large information-criterion improvement. On fit alone, the 4-state solution is the stronger candidate.

## 4-State Profile Interpretation

Estimated invariant class means are z-standardized.

| Class | Stress | Entrapment | Burdensomeness | Belongingness-related risk | Loneliness | Provisional label |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| 1 | -0.354 | -0.475 | -0.471 | -0.529 | -0.484 | Low-risk regulated |
| 3 | 0.381 | 0.244 | 0.204 | 0.408 | 0.464 | Moderate interpersonal distress |
| 2 | 0.896 | 1.509 | 1.466 | 1.615 | 1.458 | Elevated entrapment-interpersonal risk |
| 4 | 2.030 | 3.199 | 3.473 | 3.027 | 2.360 | Extreme diffuse risk |

The 4-state model is substantively interpretable. It separates a large low-risk state, a moderate interpersonal distress state, an elevated risk state, and a very high-risk state.

## Class Size Concern

The high-risk Class 4 is small:

| Wave | Class 4 estimated n | Class 4 proportion |
| ---: | ---: | ---: |
| 1 | 15.44 | 4.09% |
| 2 | 10.44 | 2.77% |
| 3 | 12.00 | 3.18% |
| 4 | 14.41 | 3.82% |

This does not make the model unusable, but it is the main acceptability risk. Reviewers may question whether the extreme class is stable enough to support detailed transition claims.

## Transition Pattern

The 4-state model shows strong stability in low-risk states and moderate stability in higher-risk states:

- Class 1 stability: 0.931, 1.000, 0.958
- Class 2 stability: 0.510, 0.651, 0.636
- Class 3 stability: 0.564, 0.560, 0.806
- Class 4 stability: 0.319, 0.720, 0.500

The extreme-risk state is not simply persistent. It shows partial movement into elevated or moderate states, which could become the main substantive story: high-risk states are rare but dynamically unstable.

However, several transition logits were fixed because of empty or near-empty cells. Therefore, rare transition paths should not be overinterpreted.

## Feasibility Judgment

Feasibility is acceptable.

Reasons:

- The balanced analytic sample contains 377 participants across four EMA waves.
- Both 3-state and 4-state invariant pilot models terminated normally.
- The best loglikelihood was replicated in both pilot models.
- Entropy is high in both solutions.
- The 4-state profiles are theoretically interpretable.

Main technical limitations:

- The 4-state model has a small extreme-risk class.
- The 4-state model fixed more transition logits than the 3-state model, suggesting sparse transition cells.
- Current outputs are pilot runs, not final full-start confirmation.
- The current invariant model should still be compared with configural or partially invariant alternatives before final Methods/Results writing.

## Paper Acceptability Judgment

The paper is potentially acceptable if framed cautiously.

Most defensible framing:

> We identified EMA-derived daily-life risk states and examined transitions among these states across four waves. The model suggested a dominant low-risk state, two intermediate risk states, and a rare but clinically meaningful extreme-risk state. Because rare transition cells were sparse, transition findings involving the extreme-risk state were interpreted cautiously and tested in sensitivity analyses.

Avoid this framing:

> We discovered a definitive high-risk subgroup and precisely estimated all transition paths.

The second framing is too strong for the current evidence.

## Decision for Next Step

Treat the 4-state invariant model as the main candidate, but not yet the final model.

## Configural Pilot Follow-up

Configural pilot models were run after the first invariant checkpoint.

| Model | Free parameters | LL | AIC | BIC | ssaBIC | Entropy | Replicated | Key issue |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- | --- |
| 3-state configural pilot | 85 | -7119.082 | 14408.165 | 14742.406 | 14472.721 | 0.969 | Yes | Some sparse transition cells |
| 4-state configural pilot | 124 | -6631.827 | 13511.655 | 13999.253 | 13605.831 | 0.968 | No | Local maximum / unstable SE warning / sparse cells |

Interpretation:

- The 3-state configural model improves BIC over the 3-state invariant model, but it still fits worse than the 4-state invariant model.
- The 4-state configural model has lower AIC and ssaBIC than the 4-state invariant model, but BIC is slightly worse and the best loglikelihood was not replicated.
- The 4-state configural model also produced a non-positive definite first-order derivative product matrix warning, so it is not trustworthy as a main model at this stage.
- Therefore, the configural comparison does not currently overturn the 4-state invariant candidate. It mainly shows that fully unconstrained 4-state LTA is too unstable for the current sample and sparse transitions.

Updated model decision:

> Use the 4-state invariant solution as the primary candidate because it has the best BIC among stable replicated models and has interpretable state profiles. Keep the 3-state configural or 3-state invariant model as a conservative sensitivity model. Do not use the 4-state configural model as the main model unless a higher-start rerun replicates and resolves the standard-error warning.

Next actions:

1. Run full-start 3-state and 4-state invariant models after the input file naming fix.
2. Add SI as a distal validation outcome. The extreme and elevated risk states should show higher SI burden if the state interpretation is valid.
3. Prepare a sensitivity table that compares 3-state invariant, 3-state configural, 4-state invariant, and 4-state configural models.
4. Keep the 3-state model as the conservative fallback if the 4-state solution remains sparse or unstable under full-start and distal-validation checks.

## Current Bottom Line

The LTA small-paper idea is feasible and has a credible empirical signal. The strongest current model is the 4-state invariant solution, but the publishable version must emphasize cautious interpretation, robustness checks, and distal SI validation rather than only superior fit indices.
