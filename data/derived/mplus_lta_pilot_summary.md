# LTA Unconditional Model Parsing Summary

## Fit Summary

| model | n_states | run_type | loglikelihood_h0 | aic | bic | ssabic | entropy | best_loglikelihood_replicated | warnings |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| lta_3state_configural_pilot | 3 | pilot | -7119.082 | 14408.165 | 14742.406 | 14472.721 | 0.969 | True | local_independence_warning;fixed_transition_logits_empty_cells |
| lta_3state_invariant_pilot | 3 | pilot | -7265.790 | 14611.580 | 14768.869 | 14641.959 | 0.970 | True | local_independence_warning;fixed_transition_logits_empty_cells |
| lta_3state_invariant_smoke | 3 | smoke | -7265.790 | 14611.580 | 14768.869 | 14641.959 | 0.970 | True | local_independence_warning;fixed_transition_logits_empty_cells |
| lta_4state_configural_pilot | 4 | pilot | -6631.827 | 13511.655 | 13999.253 | 13605.831 | 0.968 | False | local_independence_warning;fixed_transition_logits_empty_cells;best_loglikelihood_not_replicated |
| lta_4state_invariant_pilot | 4 | pilot | -6807.015 | 13742.030 | 13993.693 | 13790.636 | 0.959 | True | local_independence_warning;fixed_transition_logits_empty_cells |
| lta_4state_invariant_smoke | 4 | smoke | -6807.015 | 13742.030 | 13993.693 | 13790.636 | 0.959 | True | local_independence_warning;fixed_transition_logits_empty_cells |

## Model Decision Notes

- The 4-state invariant pilot model improves information criteria substantially relative to the 3-state invariant pilot model.
- Both pilot models replicated the best loglikelihood and terminated normally.
- Both models fixed one or more transition logits, indicating empty or near-empty transition cells. This is not automatically fatal, but it weakens claims about rare transition paths.
- The local-independence warning is expected for the current diagonal latent-state model.
- Treat these as pilot results. A final model decision still needs full-start confirmation and substantive interpretation of class profiles and transition matrices.

## Class Proportions by Wave

| model | wave | class | estimated_n | estimated_proportion |
| --- | --- | --- | --- | --- |
| lta_3state_configural_pilot | 1 | 1 | 30.419 | 0.081 |
| lta_3state_configural_pilot | 1 | 2 | 75.765 | 0.201 |
| lta_3state_configural_pilot | 1 | 3 | 270.817 | 0.718 |
| lta_3state_configural_pilot | 2 | 1 | 29.923 | 0.079 |
| lta_3state_configural_pilot | 2 | 2 | 77.977 | 0.207 |
| lta_3state_configural_pilot | 2 | 3 | 269.099 | 0.714 |
| lta_3state_configural_pilot | 3 | 1 | 27.426 | 0.073 |
| lta_3state_configural_pilot | 3 | 2 | 291.363 | 0.773 |
| lta_3state_configural_pilot | 3 | 3 | 58.212 | 0.154 |
| lta_3state_configural_pilot | 4 | 1 | 16.996 | 0.045 |
| lta_3state_configural_pilot | 4 | 2 | 68.999 | 0.183 |
| lta_3state_configural_pilot | 4 | 3 | 291.005 | 0.772 |
| lta_3state_invariant_pilot | 1 | 1 | 263.338 | 0.699 |
| lta_3state_invariant_pilot | 1 | 2 | 32.295 | 0.086 |
| lta_3state_invariant_pilot | 1 | 3 | 81.367 | 0.216 |
| lta_3state_invariant_pilot | 2 | 1 | 282.863 | 0.750 |
| lta_3state_invariant_pilot | 2 | 2 | 25.660 | 0.068 |
| lta_3state_invariant_pilot | 2 | 3 | 68.477 | 0.182 |
| lta_3state_invariant_pilot | 3 | 1 | 296.463 | 0.786 |
| lta_3state_invariant_pilot | 3 | 2 | 22.114 | 0.059 |
| lta_3state_invariant_pilot | 3 | 3 | 58.422 | 0.155 |
| lta_3state_invariant_pilot | 4 | 1 | 288.573 | 0.765 |
| lta_3state_invariant_pilot | 4 | 2 | 24.596 | 0.065 |
| lta_3state_invariant_pilot | 4 | 3 | 63.832 | 0.169 |
| lta_3state_invariant_smoke | 1 | 1 | 263.338 | 0.699 |
| lta_3state_invariant_smoke | 1 | 2 | 81.367 | 0.216 |
| lta_3state_invariant_smoke | 1 | 3 | 32.295 | 0.086 |
| lta_3state_invariant_smoke | 2 | 1 | 282.863 | 0.750 |
| lta_3state_invariant_smoke | 2 | 2 | 68.477 | 0.182 |
| lta_3state_invariant_smoke | 2 | 3 | 25.660 | 0.068 |
| lta_3state_invariant_smoke | 3 | 1 | 296.463 | 0.786 |
| lta_3state_invariant_smoke | 3 | 2 | 58.422 | 0.155 |
| lta_3state_invariant_smoke | 3 | 3 | 22.114 | 0.059 |
| lta_3state_invariant_smoke | 4 | 1 | 288.573 | 0.765 |
| lta_3state_invariant_smoke | 4 | 2 | 63.832 | 0.169 |
| lta_3state_invariant_smoke | 4 | 3 | 24.596 | 0.065 |
| lta_4state_configural_pilot | 1 | 1 | 252.730 | 0.670 |
| lta_4state_configural_pilot | 1 | 2 | 66.577 | 0.177 |
| lta_4state_configural_pilot | 1 | 3 | 45.857 | 0.122 |
| lta_4state_configural_pilot | 1 | 4 | 11.836 | 0.031 |
| lta_4state_configural_pilot | 2 | 1 | 3.000 | 0.008 |
| lta_4state_configural_pilot | 2 | 2 | 89.062 | 0.236 |
| lta_4state_configural_pilot | 2 | 3 | 37.629 | 0.100 |
| lta_4state_configural_pilot | 2 | 4 | 247.309 | 0.656 |
| lta_4state_configural_pilot | 3 | 1 | 13.023 | 0.035 |
| lta_4state_configural_pilot | 3 | 2 | 271.739 | 0.721 |
| lta_4state_configural_pilot | 3 | 3 | 37.835 | 0.100 |
| lta_4state_configural_pilot | 3 | 4 | 54.402 | 0.144 |
| lta_4state_configural_pilot | 4 | 1 | 12.979 | 0.034 |
| lta_4state_configural_pilot | 4 | 2 | 63.164 | 0.168 |
| lta_4state_configural_pilot | 4 | 3 | 34.676 | 0.092 |
| lta_4state_configural_pilot | 4 | 4 | 266.182 | 0.706 |
| lta_4state_invariant_pilot | 1 | 1 | 230.989 | 0.613 |
| lta_4state_invariant_pilot | 1 | 2 | 51.367 | 0.136 |
| lta_4state_invariant_pilot | 1 | 3 | 79.209 | 0.210 |
| lta_4state_invariant_pilot | 1 | 4 | 15.435 | 0.041 |
| lta_4state_invariant_pilot | 2 | 1 | 244.047 | 0.647 |
| lta_4state_invariant_pilot | 2 | 2 | 39.027 | 0.104 |
| lta_4state_invariant_pilot | 2 | 3 | 83.481 | 0.221 |
| lta_4state_invariant_pilot | 2 | 4 | 10.445 | 0.028 |
| lta_4state_invariant_pilot | 3 | 1 | 271.716 | 0.721 |
| lta_4state_invariant_pilot | 3 | 2 | 37.409 | 0.099 |
| lta_4state_invariant_pilot | 3 | 3 | 55.877 | 0.148 |
| lta_4state_invariant_pilot | 3 | 4 | 11.998 | 0.032 |
| lta_4state_invariant_pilot | 4 | 1 | 266.108 | 0.706 |
| lta_4state_invariant_pilot | 4 | 2 | 34.936 | 0.093 |
| lta_4state_invariant_pilot | 4 | 3 | 61.549 | 0.163 |
| lta_4state_invariant_pilot | 4 | 4 | 14.408 | 0.038 |
| lta_4state_invariant_smoke | 1 | 1 | 230.989 | 0.613 |
| lta_4state_invariant_smoke | 1 | 2 | 51.367 | 0.136 |
| lta_4state_invariant_smoke | 1 | 3 | 79.209 | 0.210 |
| lta_4state_invariant_smoke | 1 | 4 | 15.435 | 0.041 |
| lta_4state_invariant_smoke | 2 | 1 | 244.047 | 0.647 |
| lta_4state_invariant_smoke | 2 | 2 | 39.027 | 0.104 |
| lta_4state_invariant_smoke | 2 | 3 | 83.481 | 0.221 |
| lta_4state_invariant_smoke | 2 | 4 | 10.445 | 0.028 |
| lta_4state_invariant_smoke | 3 | 1 | 271.716 | 0.721 |
| lta_4state_invariant_smoke | 3 | 2 | 37.409 | 0.099 |
| lta_4state_invariant_smoke | 3 | 3 | 55.877 | 0.148 |
| lta_4state_invariant_smoke | 3 | 4 | 11.998 | 0.032 |
| lta_4state_invariant_smoke | 4 | 1 | 266.108 | 0.706 |
| lta_4state_invariant_smoke | 4 | 2 | 34.936 | 0.093 |
| lta_4state_invariant_smoke | 4 | 3 | 61.549 | 0.163 |
| lta_4state_invariant_smoke | 4 | 4 | 14.408 | 0.038 |
