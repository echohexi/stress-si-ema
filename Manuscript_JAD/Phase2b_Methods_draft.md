# 2. Methods

> **Status**: Draft from Claude Code (2026-05-16), based on `supervisor_briefing.md` and `code/brms_main_analysis.R`.
> **Next steps**: (1) Verify all scale names against `all_scales_v5_FINAL.csv`; (2) integrate into `Phase3_full_assembled.md`.

---

## 2.1 Participants and design

Participants were 391 first-year undergraduates from a public university in northern China (mean age 20.4 years, SD 1.6, range 17–25; 67.3% female; 92.6% Han ethnicity). Data were collected across four waves spanning one academic year, each wave comprising seven consecutive days of ecological momentary assessment (EMA) with three semi-random prompts per day (morning, midday, early evening). Each wave began with a self-report questionnaire battery. The study was preregistered on the Open Science Framework (OSF; blinded for review) and received ethics approval from the institutional review board (approval number TJUE2025-H-S-078).

## 2.2 EMA procedure and compliance

Participants received prompts via a mobile application and completed brief surveys on momentary stressors, cognitive–affective states, and suicidal ideation (SI) within 20 minutes of each prompt. The analytic dataset comprised 28,113 valid EMA prompts across 1,553 person-waves (median 72 prompts per participant). The overall prompt-level response rate was 76.4% (SD 11.2%). Of the 28,113 prompts, 46.3% reported at least one concurrent stressor and 6.9% reported momentary SI above the floor of the scale.

## 2.3 Momentary (EMA) measures

**Stressors.** Momentary stressor exposure was assessed at each prompt with an adapted version of the Adolescent Self-Rating Life Events Checklist (ASLEC; Liu et al., 1997). Participants indicated whether each of several common stressors (academic, interpersonal, financial, daily-hassle, and health domains) had occurred since the previous prompt. A total stress-sum intensity score was computed by summing the number of endorsed domains weighted by subjective severity (range 0–35), then within-person centred for analysis.

**Proximal mediators.** Three cognitive–affective states were measured at each prompt using single items adapted from the Interpersonal Needs Questionnaire (INQ-15; Van Orden et al., 2012) and the Entrapment Scale (Gilbert & Allan, 1998). *Entrapment* was assessed with the item "I feel trapped right now." *Perceived burdensomeness* was assessed with "I feel I am a burden to others right now." *Thwarted belongingness* was assessed with "I feel disconnected from others right now." Each item was rated on a 1 (not at all) to 5 (extremely) scale.

**Suicidal ideation.** Momentary SI was measured with a single item drawn from the Positive and Negative Suicide Ideation Inventory (PANSI-momentary; Osman et al., 1998): "Right now, I feel that life is not worth living," rated 1 (not at all) to 5 (extremely). This item was treated as an ordinal outcome (cumulative-logit link) in the primary models; Gaussian specifications were estimated as sensitivity checks and returned qualitatively identical patterns.

## 2.4 Person-level measures

**Childhood trauma.** The Childhood Trauma Questionnaire–Short Form (CTQ-SF; Bernstein et al., 2003) was administered at Wave 1. Its 25 clinical items yield scores for five dimensions: emotional abuse (EA), physical abuse (PA), sexual abuse (SA), emotional neglect (EN), and physical neglect (PN). All scores were z-standardised before analysis. One critical data-quality issue was identified during scale reconstruction: the original dataset's CTQ total score had **not applied the required reverse-scoring** for five positively framed items, producing a mean of 60.45 well above the normative range (sample means typically 32–40). The corrected total (mean 32.30) was used throughout; the corrected version correlated perfectly with the independently reconstructed score (*r* = 1.00).

**Trait protective resources.** Three resource indicators were measured: the Brief Resilience Scale (BRS; Smith et al., 2008) at Wave 3 (6 items); the Connectedness Questionnaire (Lee et al., 2001) at Wave 2 (10 items); and the cognitive reappraisal subscale of the Emotion Regulation Questionnaire (ERQ-Reappraisal; Gross & John, 2003) at Wave 3 (6 items). All composites were scored by unit-weighting items after reverse-coding where necessary. Scale reliability (Cronbach's *α*) in the present sample ranged from 0.82 to 0.91.

**Personality dysfunction.** The Level of Personality Functioning Scale–Brief Form (LPFS-BF; Weekers et al., 2019) was administered at Wave 3 (12 items). It was entered as a risk control on the resource-moderation *b*-path.

**Dynamic subtype membership.** Prior to hypothesis testing, a latent profile analysis (LPA; Mplus 8.4; Masyn, 2013) was conducted on the within-person mean, variability (within-person SD), and autocorrelation (lag-1) of momentary SI aggregated within each person-wave. A three-class solution was selected based on the bootstrap likelihood-ratio test (BLRT; *p* < .001), entropy (0.83), and conceptual interpretability. Because the LPA was conducted at the **person-wave level**, the same participant could occupy different subtypes across the four EMA waves — capturing that an individual's SI-dynamic profile may shift across the academic year. Subtype labels are C1 (low-stable; 367 participants, 1,275 person-waves [82.1%]), C2 (low-to-moderate, high-fluctuating; 128 participants, 199 person-waves [12.8%]), and C3 (high-intensity, high-fluctuating; 37 participants, 79 person-waves [5.1%]).

## 2.5 Data-quality note: INQ-15 reverse-scoring correction

A critical data-quality finding concerned the Interpersonal Needs Questionnaire (INQ-15). The thwarted belongingness (TB) subscale contains six reverse-coded items; the original dataset had **not applied reverse-scoring** to these items. The correlation between the original (incorrect) and the corrected TB score was *r* = −0.57 — the original version was correlated in the opposite direction to the correct version. This error affected several earlier reports using the same dataset, including related thesis chapters by the first author. The present study used the corrected TB score throughout; the issue is disclosed in the Discussion as a limitation of prior work. No comparable scoring errors were found in the BRS, Connectedness, LPFS-BF, ERQ, or CERQ scales (all *r* > 0.95 with independently reconstructed scores).

## 2.6 Statistical analysis

Analyses were conducted in R 4.3 with the `brms` package (v2.20+; Bürkner, 2017), using a Bayesian multivariate multilevel mediation framework with four chains of 4,000 iterations each (1,000 warm-up) and the `cmdstanr` back-end. All models used weakly informative priors: fixed effects ~ *N*(0, 1), random-effect SDs ~ *N*(0, 1) with a half-normal lower bound, and the random-effect correlation matrix ~ LKJ(2). Within-person centering followed Curran and Bauer (2011): every Level-1 predictor was decomposed into a person-mean (*pm*) and a person-mean-deviated component (*wp*), cleanly separating between- and within-person variance. All Level-2 moderators were grand-mean standardised.

Five sequential models tested the seven pre-registered hypotheses:

- **Model 1 (H1–H3).** A multivariate multilevel mediation model simultaneously estimating three Gaussian mediator equations (entrapment, burdensomeness, belongingness) and one cumulative-logit ordinal SI equation, linked by a shared random-effect covariance matrix via the `(… | p | pid)` syntax. Within-person indirect effects (a × b) were computed from the joint posterior.
- **Model 2 (H4).** A 5 (CTQ dimension) × 4 (mediator) × 2 (a-path, b-path) factorial specification producing 40 sub-models, testing path- and dimension-specific moderation.
- **Model 3 (H5).** The entrapment × BRS, entrapment × Connectedness, and entrapment × ERQ-Reappraisal interactions on the b-path, with LPFS-BF as a risk control.
- **Model 4 (H6).** Subtype × stress_wp interactions on the indirect-effect pathways, testing the monotonicity of C1 < C2 < C3.
- **Model 5 (H7).** A person-level Bayesian ANOVA testing trait-level differentiation across the three subtypes.

**Inference criteria.** A hypothesis was supported if the 95% posterior credible interval (CrI) excluded zero *and* the posterior probability of the predicted direction (PD) was ≥ 0.975. This dual criterion is more conservative than either criterion alone and corresponds approximately to a one-sided Bayesian *p* < .025. For the H6 monotonicity test, the PD threshold was set at ≥ 0.90 per the preregistration.
