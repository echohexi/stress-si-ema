# Full dump of Study3_All_Tables.xlsx


## Overview  (rows=24, cols=2)

| Manuscript Table Catalog |  |
|  |  |
| Manuscript: | Subtype-specific within-person pathways from stress to suicidal ideation: Entrapment and interpersonal mechanisms in a four-wave ecological momentary assessment study |
| Sample: | 391 university students; 1,553 person-waves; 28,113 EMA prompts; 4 EMA waves. |
| Workbook contents: | Four main-text tables (Tables 1–4) plus six supplementary tables (S1–S6). |
|  |  |
| Sheet | Content |
| Table 1 | Sample characteristics and EMA descriptive statistics, overall and by subtype. |
| Table 2 | Overall within-person parallel mediation (H1): a-, b-, indirect paths and dominance contrasts. |
| Table 3 | Subtype-specific within-person path coefficients and indirect effects (H3); within-mediator subtype contrasts on indirect effects. |
| Table 4 | Within-person stress → SI slope before vs. after adjusting for the three proximal mediators, with subtype contrasts and attenuation (H4). |
| Table S1 | Posterior convergence diagnostics (R̂, ESS) for all fitted models. |
| Table S2 | Random-effects SDs from the H1 overall model, indexing between-person heterogeneity in within-person pathway strengths (H2). |
| Table S3 | Sample-composition check for the within-20-min sensitivity subsample. |
| Table S4 | H1 within-person indirect effects in the within-20-min sensitivity subsample. |
| Table S5 | Full subtype-specific a-, b-, c′-, and indirect paths (companion to Table 3). |
| Table S6 | Subtype contrasts on a-, b-, c′-, and indirect paths (companion to Table S5). |
|  |  |
| General notes: |  |
|  | All EMA variables were centered within participant × wave; person-wave means were entered as between-person stress. |
|  | Models adjusted for lagged momentary suicidal ideation, EMA wave (as a factor), and time of day; random intercepts and random within-person stress slopes were included for participant. |
|  | Bayesian estimation in brms / Stan with 4 chains × 4,000 iterations (1,000 warmup) per model. |
|  | CrI = 95% posterior credible interval; pd = posterior probability of direction; * indicates 95% CrI excludes zero. |
|  | C1 = low-stable subtype; C2 = low-to-moderate intensity with high fluctuation; C3 = high intensity, high frequency, and high fluctuation. |


## Table 1  (rows=18, cols=5)

| Table 1. Sample characteristics and ecological momentary assessment (EMA) descriptive statistics, overall and by suicidal ideation dynamic subtype. |  |  |  |  |
| Characteristic | Overall | C1 (Low-stable) | C2 (Low-mod / high-fluct) | C3 (High / high-fluct) |
| Sample structure |  |  |  |  |
| Unique participants contributing ≥1 person-wave to subtype, n | 391 | 367 | 128 | 37 |
| Person-waves, n (% of total) | 1,553 | 1,275 (82.1) | 199 (12.8) | 79 (5.1) |
| EMA prompts, n | 28,113 | 23,104 | 3,637 | 1,372 |
| Prompts per person-wave, M (SD) | 18.1 (2.4) | — | — | — |
| Waves per participant, M (SD) | 3.96 (0.26) | — | — | — |
| Prompt-level momentary indices, M (SD) |  |  |  |  |
| Stress sum intensity | 2.23 (3.20) | 1.99 (2.98) | 2.91 (3.72) | 4.36 (4.15) |
| Entrapment | 1.39 (0.78) | 1.28 (0.66) | 1.66 (0.93) | 2.59 (1.01) |
| Perceived burdensomeness | 1.27 (0.58) | 1.18 (0.45) | 1.49 (0.73) | 2.24 (0.94) |
| Thwarted belongingness | 1.34 (0.64) | 1.25 (0.54) | 1.56 (0.74) | 2.32 (0.92) |
| Suicidal ideation | 1.07 (0.30) | 1.00 (0.04) | 1.15 (0.39) | 1.99 (0.70) |
| Prompt-level prevalence, % |  |  |  |  |
| Any momentary stressor endorsed | 46.3 | 43.8 | 53.0 | 69.7 |
| Any momentary suicidal ideation (SI > 1) | 6.9 | 0.6 | 16.0 | 89.6 |
| Note. Subtype membership was assigned at the person-wave level; the same individual could occupy different subtypes across the four EMA waves, so subtype-specific participant counts sum to more than 391 across columns. Suicidal ideation and proximal psychological variables were measured on 5-point momentary scales (1 = not at all, 5 = extremely); stress sum intensity is the summed intensity across seven domains (range 0–35). Loneliness was treated as a supplementary construct because of its conceptual overlap with thwarted belongingness and was not included in the primary mediation models. C1 = low-stable subtype; C2 = low-to-moderate intensity with high fluctuation; C3 = high intensity, high frequency, and high fluctuation. |  |  |  |  |


## Table 2  (rows=19, cols=4)

| Table 2. Overall within-person parallel mediation from momentary stress to momentary suicidal ideation through three proximal psychological pathways, and dominance contrasts among the three indirect effects. |  |  |  |
| Path | Posterior median | 95% CrI | pd |
| a-paths: Stress → Mediator |  |  |  |
| Stress → Entrapment | 0.068 | [0.061, 0.074] | > 0.999 |
| Stress → Perceived burdensomeness | 0.041 | [0.036, 0.046] | > 0.999 |
| Stress → Thwarted belongingness | 0.044 | [0.039, 0.049] | > 0.999 |
| b-paths: Mediator → Suicidal ideation |  |  |  |
| Entrapment → SI | 0.037 | [0.027, 0.048] | > 0.999 |
| Perceived burdensomeness → SI | 0.041 | [0.023, 0.058] | > 0.999 |
| Thwarted belongingness → SI | 0.025 | [0.013, 0.038] | > 0.999 |
| Within-person indirect effects (a × b) |  |  |  |
| Stress → Entrapment → SI | 0.0025 | [0.0018, 0.0033] | > 0.999 |
| Stress → Perceived burdensomeness → SI | 0.0016 | [0.0009, 0.0024] | > 0.999 |
| Stress → Thwarted belongingness → SI | 0.0011 | [0.0006, 0.0017] | > 0.999 |
| Dominance contrasts among indirect effects |  |  |  |
| Entrapment − Perceived burdensomeness | 0.0009 | [−0.0002, 0.0020] | 0.944 |
| Entrapment − Thwarted belongingness | 0.0014 | [0.0005, 0.0024] | 0.998 |
| Perceived burdensomeness − Thwarted belongingness | 0.0005 | [−0.0004, 0.0015] | 0.867 |
| Note. CrI = posterior credible interval; pd = posterior probability of direction. All EMA variables were centered within participant × wave. The model adjusted for between-person stress (participant × wave mean), lagged suicidal ideation, EMA wave, and time of day, with random intercepts and random stress slopes. Indirect effects were computed at the posterior-draw level. Subtype-specific c′ direct paths are reported in Supplementary Table S5. |  |  |  |


## Table 3  (rows=24, cols=4)

| Table 3. Subtype-specific within-person path coefficients and indirect effects from momentary stress to momentary suicidal ideation through entrapment, perceived burdensomeness, and thwarted belongingness, with within-mediator subtype contrasts on the indirect effect. |  |  |  |
| Mediator / Subtype or contrast | a-path: Stress → M | b-path: M → SI | Indirect (a × b) |
| Entrapment |  |  |  |
| C1 (Low-stable) | 0.061 [0.055, 0.068] | 0.019 [0.006, 0.032] | 0.0012 [0.0004, 0.0020] |
| C2 (Low-mod / high-fluct) | 0.100 [0.091, 0.109] | 0.162 [0.145, 0.179] | 0.0162 [0.0141, 0.0185] |
| C3 (High / high-fluct) | 0.073 [0.059, 0.088] | 0.261 [0.234, 0.288] | 0.0191 [0.0150, 0.0235] |
| Indirect contrast: C2 − C1 | — | — | 0.0151 [0.0131, 0.0171]* |
| Indirect contrast: C3 − C1 | — | — | 0.0179 [0.0138, 0.0223]* |
| Indirect contrast: C3 − C2 | — | — | 0.0029 [−0.0011, 0.0071] |
| Perceived burdensomeness |  |  |  |
| C1 | 0.034 [0.029, 0.039] | 0.023 [0.005, 0.042] | 0.0008 [0.0002, 0.0014] |
| C2 | 0.070 [0.063, 0.077] | 0.183 [0.160, 0.206] | 0.0128 [0.0109, 0.0149] |
| C3 | 0.047 [0.035, 0.058] | 0.243 [0.209, 0.276] | 0.0113 [0.0083, 0.0145] |
| Indirect contrast: C2 − C1 | — | — | 0.0120 [0.0103, 0.0139]* |
| Indirect contrast: C3 − C1 | — | — | 0.0105 [0.0075, 0.0137]* |
| Indirect contrast: C3 − C2 | — | — | −0.0015 [−0.0045, 0.0016] |
| Thwarted belongingness |  |  |  |
| C1 | 0.037 [0.032, 0.042] | 0.021 [0.005, 0.037] | 0.0008 [0.0002, 0.0014] |
| C2 | 0.066 [0.058, 0.073] | 0.154 [0.132, 0.174] | 0.0101 [0.0083, 0.0119] |
| C3 | 0.075 [0.063, 0.087] | 0.197 [0.164, 0.229] | 0.0146 [0.0114, 0.0183] |
| Indirect contrast: C2 − C1 | — | — | 0.0093 [0.0078, 0.0109]* |
| Indirect contrast: C3 − C1 | — | — | 0.0139 [0.0108, 0.0174]* |
| Indirect contrast: C3 − C2 | — | — | 0.0046 [0.0014, 0.0079]* |
| Note. Posterior medians [95% CrI]. * indicates that the 95% CrI excludes zero. The C3 − C2 indirect-effect contrast credibly excludes zero only for the thwarted-belongingness mediator. Contrasts on the a-, b-, and c′-paths and the c′-path estimates themselves are reported in Supplementary Tables S5 and S6. |  |  |  |


## Table 4  (rows=11, cols=4)

| Table 4. Within-person stress → suicidal ideation slopes by subtype, before and after adjustment for the three concurrent proximal mediators, with subtype contrasts and attenuations. |  |  |  |
|  | Before mediators | After mediators | Attenuation (Before − After) |
| Within-class stress → SI slope |  |  |  |
| C1 (Low-stable) | 0.0012 [−0.0007, 0.0030] | 0.0004 [−0.0010, 0.0017] | 0.0008 [−0.0015, 0.0031] |
| C2 (Low-mod / high-fluct) | 0.0327 [0.0298, 0.0357]* | 0.0096 [0.0070, 0.0122]* | 0.0231 [0.0191, 0.0270]* |
| C3 (High / high-fluct) | 0.0437 [0.0385, 0.0486]* | 0.0126 [0.0083, 0.0168]* | 0.0311 [0.0245, 0.0376]* |
| Subtype contrasts on stress → SI slope |  |  |  |
| C2 − C1 | 0.0316 [0.0286, 0.0345]* | 0.0093 [0.0065, 0.0121]* | 0.0223 [0.0182, 0.0264]* |
| C3 − C1 | 0.0425 [0.0372, 0.0477]* | 0.0122 [0.0078, 0.0167]* | 0.0303 [0.0235, 0.0371]* |
| C3 − C2 | 0.0110 [0.0055, 0.0163]* | 0.0030 [−0.0018, 0.0077] | 0.0080 [0.0009, 0.0151]* |
| Note. Posterior medians [95% CrI]. * indicates that the 95% CrI excludes zero. The C3 − C2 contrast on the within-person stress → SI slope was credibly positive without mediators but was substantially attenuated and no longer credibly different from zero after adjustment for the three proximal mediators. The Before-mediators model included subtype × stress interactions and standard covariates; the After-mediators model additionally included subtype × entrapment, subtype × burdensomeness, and subtype × thwarted-belongingness interactions. |  |  |  |


## Table S1  (rows=11, cols=8)

| Supplementary Table S1. Posterior convergence diagnostics for all fitted Bayesian multivariate multilevel models. |  |  |  |  |  |  |  |
| Model | No. of parameters | Max R̂ | No. with R̂ > 1.01 | No. with R̂ > 1.05 | Min Bulk ESS | Min Tail ESS | No. with Bulk ESS < 400 |
| H1: overall parallel mediation | 4358 | 1.0095 | 0 | 0 | 266 | 548 | 1 |
| H3: entrapment × subtype mediation | 1994 | 1.0038 | 0 | 0 | 845 | 1872 | 0 |
| H3: perceived-burdensomeness × subtype mediation | 1994 | 1.0044 | 0 | 0 | 745 | 1539 | 0 |
| H3: thwarted-belongingness × subtype mediation | 1994 | 1.0112 | 1 | 0 | 672 | 1817 | 0 |
| H4: no-mediator (stress × subtype only) | 801 | 1.0026 | 0 | 0 | 971 | 2085 | 0 |
| H4: with three concurrent mediators | 1986 | 1.0029 | 0 | 0 | 663 | 1387 | 0 |
| Supplementary: loneliness × subtype mediation | 1994 | 1.0030 | 0 | 0 | 896 | 1656 | 0 |
| Sensitivity: within-20-min subsample H1 | 4358 | 1.0115 | 1 | 0 | 427 | 893 | 0 |
| Note. R̂ = potential scale reduction factor across chains; Bulk ESS and Tail ESS = effective sample sizes for posterior bulk and tail estimation, respectively. All models were fit with 4 chains × 4,000 iterations (1,000 warmup) for 12,000 post-warmup draws. Convergence was acceptable in all models, with R̂ < 1.05 throughout and no more than one parameter per model exhibiting R̂ > 1.01. |  |  |  |  |  |  |  |


## Table S2  (rows=14, cols=5)

| Supplementary Table S2. Random-effects standard deviations from the H1 overall within-person parallel mediation model, indexing between-person heterogeneity in within-person pathway strengths (H2). |  |  |  |  |
| Random-effect term | Posterior median | Posterior mean | 95% CrI | pd |
| Random intercept SD: entrapment | 0.0018 | 0.0021 | [0.0001, 0.0060] | > 0.999 |
| Random slope SD: stress → entrapment | 0.0560 | 0.0561 | [0.0513, 0.0614] | > 0.999 |
| Random intercept SD: perceived burdensomeness | 0.0014 | 0.0016 | [0.0001, 0.0046] | > 0.999 |
| Random slope SD: stress → perceived burdensomeness | 0.0430 | 0.0431 | [0.0392, 0.0472] | > 0.999 |
| Random intercept SD: thwarted belongingness | 0.0015 | 0.0018 | [0.0001, 0.0051] | > 0.999 |
| Random slope SD: stress → thwarted belongingness | 0.0431 | 0.0432 | [0.0392, 0.0473] | > 0.999 |
| Random intercept SD: suicidal ideation | 0.1610 | 0.1612 | [0.1501, 0.1734] | > 0.999 |
| Random slope SD: stress → SI (c′ path) | 0.0078 | 0.0078 | [0.0064, 0.0092] | > 0.999 |
| Random slope SD: entrapment → SI | 0.0732 | 0.0733 | [0.0643, 0.0830] | > 0.999 |
| Random slope SD: perceived burdensomeness → SI | 0.1237 | 0.1239 | [0.1097, 0.1391] | > 0.999 |
| Random slope SD: thwarted belongingness → SI | 0.0853 | 0.0855 | [0.0744, 0.0978] | > 0.999 |
| Note. SDs are on the original scale of the corresponding outcome. CrI = posterior credible interval; pd = posterior probability of direction (here the probability that the SD is greater than zero). Random slopes were specified independently of random intercepts (||) within each outcome equation. All six within-person pathway SDs (stress → mediator a-paths and mediator → SI b-paths) are clearly above zero, supporting substantial between-person heterogeneity in within-person pathway strength. |  |  |  |  |


## Table S3  (rows=6, cols=3)

| Supplementary Table S3. Composition of the within-20-min sensitivity subsample for the H1 within-person parallel mediation model. |  |  |
| Index | Primary analytic sample | Within-20-min subsample |
| EMA prompts, n | 28,113 | 20,867 |
| Participants, n | 391 | 391 |
| Person-waves, n | 1,553 | 1,553 |
| Note. The within-20-min subsample retained only EMA prompts answered within 20 minutes of the scheduled prompt delivery time, as a sensitivity check against potential recall distortion at longer response latencies. |  |  |


## Table S4  (rows=6, cols=4)

| Supplementary Table S4. H1 within-person indirect effects in the within-20-min sensitivity subsample. |  |  |  |
| Indirect pathway | Posterior median | 95% CrI | pd |
| Stress → Entrapment → SI | 0.0025 | [0.0017, 0.0035] | > 0.999 |
| Stress → Perceived burdensomeness → SI | 0.0018 | [0.0010, 0.0027] | > 0.999 |
| Stress → Thwarted belongingness → SI | 0.0009 | [0.0004, 0.0015] | 1.000 |
| Note. Within-person indirect effects (a × b) computed from the H1 parallel mediation model refit on the within-20-min subsample (n = 20,867 prompts; see Supplementary Table S3). CrI = posterior credible interval; pd = posterior probability of direction. All three pathways remained credibly positive and comparable in magnitude to the primary-sample estimates reported in Table 2. |  |  |  |


## Table S5  (rows=18, cols=4)

| Supplementary Table S5. Full subtype-specific within-person path coefficients (a, b, c′) and indirect effects from momentary stress to momentary suicidal ideation through each of the three proximal psychological mediators. |  |  |  |
| Mediator / Path | C1 (Low-stable) | C2 (Low-mod / high-fluct) | C3 (High / high-fluct) |
| Entrapment |  |  |  |
| a-path: Stress → Mediator | 0.061 [0.055, 0.068] * | 0.100 [0.091, 0.109] * | 0.073 [0.059, 0.088] * |
| b-path: Mediator → SI | 0.019 [0.006, 0.032] * | 0.162 [0.145, 0.179] * | 0.261 [0.234, 0.288] * |
| c′-path: Stress → SI (direct) | 0.0005 [−0.0009, 0.0020] | 0.0148 [0.0121, 0.0175] * | 0.0186 [0.0144, 0.0229] * |
| Indirect: Stress → Mediator → SI (a × b) | 0.0012 [0.0004, 0.0020] * | 0.0162 [0.0141, 0.0185] * | 0.0191 [0.0150, 0.0235] * |
| Perceived burdensomeness |  |  |  |
| a-path: Stress → Mediator | 0.034 [0.029, 0.039] * | 0.070 [0.063, 0.077] * | 0.047 [0.035, 0.058] * |
| b-path: Mediator → SI | 0.023 [0.005, 0.042] * | 0.183 [0.160, 0.206] * | 0.243 [0.209, 0.276] * |
| c′-path: Stress → SI (direct) | 0.0005 [−0.0009, 0.0019] | 0.0175 [0.0149, 0.0201] * | 0.0290 [0.0248, 0.0331] * |
| Indirect: Stress → Mediator → SI (a × b) | 0.0008 [0.0002, 0.0014] * | 0.0128 [0.0109, 0.0149] * | 0.0113 [0.0083, 0.0145] * |
| Thwarted belongingness |  |  |  |
| a-path: Stress → Mediator | 0.037 [0.032, 0.042] * | 0.066 [0.058, 0.073] * | 0.075 [0.063, 0.087] * |
| b-path: Mediator → SI | 0.021 [0.005, 0.037] * | 0.154 [0.132, 0.174] * | 0.197 [0.164, 0.229] * |
| c′-path: Stress → SI (direct) | 0.0007 [−0.0008, 0.0021] | 0.0211 [0.0184, 0.0238] * | 0.0243 [0.0197, 0.0288] * |
| Indirect: Stress → Mediator → SI (a × b) | 0.0008 [0.0002, 0.0014] * | 0.0101 [0.0083, 0.0119] * | 0.0146 [0.0114, 0.0183] * |
| Note. Posterior medians [95% CrI]. * indicates that the 95% CrI excludes zero. Each subtype-specific model was a Bayesian bivariate multilevel model in which the mediator and momentary suicidal ideation were jointly modelled with stress × subtype and mediator × subtype interactions, lagged SI, between-person stress, EMA wave, and time-of-day covariates, and random intercepts and random slopes for the within-person stress and within-person mediator predictors. a-path = stress → mediator; b-path = mediator → SI; c′-path = stress → SI controlling for the mediator; indirect = posterior product a × b. Subtype contrasts on each path are reported in Supplementary Table S6. |  |  |  |


## Table S6  (rows=18, cols=4)

| Supplementary Table S6. Subtype contrasts (C2 − C1, C3 − C1, C3 − C2) on a-, b-, c′-, and indirect paths from each H3 subtype-specific within-person mediation model. |  |  |  |
| Mediator / Path | C2 − C1 | C3 − C1 | C3 − C2 |
| Entrapment |  |  |  |
| a-path: Stress → Mediator | 0.039 [0.031, 0.047] * | 0.012 [−0.002, 0.027] | −0.027 [−0.041, −0.012] * |
| b-path: Mediator → SI | 0.143 [0.128, 0.158] * | 0.242 [0.215, 0.269] * | 0.099 [0.072, 0.125] * |
| c′-path: Stress → SI (direct) | 0.0143 [0.0114, 0.0172] * | 0.0180 [0.0136, 0.0225] * | 0.0038 [−0.0010, 0.0087] |
| Indirect: Stress → Mediator → SI (a × b) | 0.0151 [0.0131, 0.0171] * | 0.0179 [0.0138, 0.0223] * | 0.0029 [−0.0011, 0.0071] |
| Perceived burdensomeness |  |  |  |
| a-path: Stress → Mediator | 0.036 [0.030, 0.042] * | 0.013 [0.001, 0.023] * | −0.023 [−0.035, −0.013] * |
| b-path: Mediator → SI | 0.159 [0.140, 0.179] * | 0.219 [0.187, 0.251] * | 0.060 [0.029, 0.091] * |
| c′-path: Stress → SI (direct) | 0.0170 [0.0143, 0.0198] * | 0.0285 [0.0241, 0.0328] * | 0.0115 [0.0068, 0.0162] * |
| Indirect: Stress → Mediator → SI (a × b) | 0.0120 [0.0103, 0.0139] * | 0.0105 [0.0075, 0.0137] * | −0.0015 [−0.0045, 0.0016] |
| Thwarted belongingness |  |  |  |
| a-path: Stress → Mediator | 0.029 [0.022, 0.035] * | 0.038 [0.026, 0.050] * | 0.009 [−0.003, 0.021] |
| b-path: Mediator → SI | 0.133 [0.114, 0.151] * | 0.176 [0.145, 0.207] * | 0.043 [0.013, 0.074] * |
| c′-path: Stress → SI (direct) | 0.0204 [0.0176, 0.0232] * | 0.0236 [0.0189, 0.0283] * | 0.0032 [−0.0018, 0.0082] |
| Indirect: Stress → Mediator → SI (a × b) | 0.0093 [0.0078, 0.0109] * | 0.0139 [0.0108, 0.0174] * | 0.0046 [0.0014, 0.0079] * |
| Note. Posterior medians of subtype contrasts on each path, with 95% CrI in brackets. * indicates that the 95% CrI excludes zero. Each contrast is the within-mediator difference in the path coefficient between two subtypes, computed at the posterior-draw level. a-path = stress → mediator; b-path = mediator → SI; c′-path = stress → SI controlling for the mediator; indirect = a × b. Subtype-specific point estimates appear in Supplementary Table S5. |  |  |  |
