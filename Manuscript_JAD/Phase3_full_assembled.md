# Phase 3 — Full Manuscript Assembly

> **Status**: Assembled 2026-05-16 from Phase2[a-d]_draft.md sources.
> **Source files**: `Phase2a_Introduction_draft.md`, `Phase2b_Methods_draft.md`, `Phase2c_Results_draft.md`, `Phase2d_Discussion_draft.md`, `01_FrontMatter.md`, `references.bib`.
>
> ⚠ **Abstract + Highlights audit needed** (see annotations below). The Abstract in `01_FrontMatter.md` predates Phase 1 locked numbers and contains **at least 2 numerical errors** (uses "28,723" instead of "28,113"; reports a×b on a different scale from Phase1_locked_numbers.md). Highlights also exceed JAD's ≤85-character limit in 3 of 5 bullets. **Do NOT use Abstract or Highlights as-is** — they are placeholders for Phase 4 revision.

---

## Title

**Risk and Resource Axes Jointly Shape the Within-Person Stress-to-Suicidal-Ideation Cascade in College Students: A Four-Wave Ecological Momentary Assessment Study**

## Authors and affiliations

Junlin Pu^a,b^, Li An^a,b,\*^

^a^ Department of Psychology, School of Education, Tianjin University, Tianjin 300350, China
^b^ Tianjin Key Laboratory of Brain Science and Neuroengineering, Tianjin 300350, China

\* Corresponding author.

## Highlights

> ⚠ **NEEDS AUDIT**: 3/5 bullets exceed JAD's ≤85-character limit. Numbers need updating to match Phase1_locked_numbers.md (e.g., ~55% not ~57%).

- Stress drives suicidal ideation primarily through momentary entrapment (~55% of indirect effect).
- All three proximal mediators show credible person-level slope heterogeneity.
- Childhood emotional abuse broadly amplifies proximal-mediator pathways.
- Childhood physical abuse shows reverse-direction moderation on a-paths.
- High-fluctuating and high-severity subtypes are dynamically indistinguishable on the cascade.

## Keywords

suicidal ideation; ecological momentary assessment; entrapment; childhood maltreatment; Bayesian multilevel mediation; college students; dynamic subtypes

## Abstract (Structured, ~245 words — ⚠ NEEDS AUDIT: numbers not yet aligned with Phase1_locked_numbers.md)

**Background.** Theoretical models of suicide locate momentary entrapment, perceived burdensomeness, and thwarted belongingness as proximal mediators between stress and suicidal ideation (SI), yet the relative dominance of these pathways within persons, and their moderation by childhood maltreatment and trait resources, remain poorly characterised in real-world settings.

**Methods.** Three hundred and ninety-one Chinese undergraduates completed four 7-day ecological momentary assessment (EMA) bursts across one academic year (28,113 prompt-level observations). Pre-registered Bayesian multilevel multivariate mediation models tested seven hypotheses concerning within-person multi-mediation, path- and dimension-specific moderation by childhood trauma, trait-resource moderation, and cascade-strength differentiation across latent SI subtypes.

**Results.** Entrapment dominated the within-person cascade (a×b = 0.0048; 95% CrI [0.0036, 0.0061]; PD > 0.99), carrying approximately 55% of the total indirect effect. Childhood emotional abuse broadly amplified mediator-to-SI *b*-paths, whereas physical abuse showed reverse-direction moderation on the stress-to-mediator *a*-paths. Trait resilience, connectedness, and cognitive reappraisal each attenuated the dominant entrapment-to-SI *b*-path in the protective direction. Three dynamic SI subtypes were strictly graded on every static risk–resource trait indicator, yet the within-person cascade was not — C2 and C3 were not credibly different on the two largest indirect pathways.

**Limitations.** Single-site Chinese undergraduate sample; single-item SI outcome; C3 subsample size.

**Conclusions.** The within-person stress-to-SI cascade is mediated predominantly through entrapment and is jointly tuned by childhood-trauma exposure (risk axis) and trait protective resources (resource axis); dynamic-cascade strength and static trait severity are partially dissociable, with implications for screening and intervention design on college campuses.

---

## 1. Introduction

Suicide is the leading cause of non-injury mortality in adolescence and young adulthood worldwide, and suicidal ideation — the cognitive state of contemplating one's own death — is its most prevalent precursor and the entry point on every clinical staging model that follows. In Chinese undergraduates, the prevalence of suicidal ideation has reached a level that would be treated as a national-policy priority for any other psychiatric phenomenon (Li et al., 2014; Zheng et al., 2022), and the transition into the first year of university is internationally recognized as a high-risk window in which previously latent vulnerabilities crystallize into acute symptom episodes (Mortier et al., 2018). The substantive question for the field is no longer whether suicidal ideation is common in this population, but by what moment-to-moment mechanism stress converts into ideation, and which individuals' cascades are steep enough to warrant targeted, time-resolved intervention.

Two proximal-mechanism theories dominate contemporary explanations of that conversion. The Integrated Motivational–Volitional model (IMV; O'Connor & Kirtley, 2018) positions *entrapment* — the perception that escape from one's circumstances is blocked — as the pivotal cognition between defeat and ideation. The Interpersonal Psychological Theory (IPT; Van Orden et al., 2010) instead centers two interpersonal cognitions, *perceived burdensomeness* and *thwarted belongingness*, as the proximal causes of suicidal desire. Both frameworks make explicitly moment-to-moment claims — they describe what happens inside a person on the time-scale of hours — yet the empirical literature has tested them almost entirely at the trait or between-person level, treating entrapment, burden, and belongingness as stable individual differences rather than as fluctuating states (Klonsky et al., 2018).

This is more than a measurement preference. A growing body of ecological momentary assessment (EMA) work has shown that suicidal ideation fluctuates intensely within individuals across hours and days, that its momentary peaks are only weakly predicted by the same trait-level variables that explain between-person differences, and that the proximal psychological states implicated by IMV and IPT themselves vary substantially within the person (Czyz et al., 2019; Hallensleben et al., 2019; Kleiman et al., 2017). The implication is that two distinct cascades are being conflated under one label: a cross-sectional comparison of who, on average, is more or less suicidal; and a within-person stress-to-ideation pathway as it unfolds in real time. Trait-level findings constrain the first; they need not — and often do not — generalize to the second.

Although the IMV and IPT proximal mediators are conceptually distinct, to our knowledge they have not been estimated jointly as concurrent within-person pathways in a single multivariate model. The field therefore cannot yet say whether entrapment carries the dominant moment-to-moment indirect effect, whether the IPT interpersonal cognitions add independent within-person signal once entrapment is partialled out, or whether the three mediators collectively absorb the contemporaneous stress-to-ideation slope. Without such a head-to-head test, mediator-selection decisions for EMA-based intervention designs rest on cross-sectional precedent rather than within-person evidence (de Beurs et al., 2019; Forkmann et al., 2018; Chu et al., 2017).

A complementary gap concerns the moderators that shape *who* shows the steepest cascade. Childhood trauma is the most replicated distal amplifier of adult stress sensitization (Compas et al., 2017; McLaughlin et al., 2020), and its association with later suicidal ideation is well established (Liu et al., 2017). What remains unresolved at the EMA timescale is the path-specificity of that moderation — whether trauma amplifies the stress-to-mediator *a*-path, the mediator-to-ideation *b*-path, or both — and the dimension-specificity of its effects, given that the five Childhood Trauma Questionnaire subscales (emotional abuse, physical abuse, sexual abuse, emotional neglect, physical neglect) capture phenomenologically distinct exposures that need not map onto the cascade in a uniform way.

A trauma-only account would, however, be one-sided. The risk–resource framework (Compas et al., 2017; Masten, 2018) holds that childhood adversity operates jointly with trait protective capacities, and that what ultimately determines stress sensitization is the individual's combined position on both axes rather than either in isolation. Trait resilience, social connectedness, and cognitive reappraisal are three canonical resources with strong evidence as buffers of affective reactivity and ideation. Whether they exert their protective leverage on the same pathway the trauma axis targets, or on a complementary one, is again an open question at the EMA timescale.

A second, less-explored axis of individual differences is *dynamic*. Within-person variability and inertia of affect and ideation have emerged as risk markers independent of mean level (Houben et al., 2015; Kuppens et al., 2010), suggesting that the trajectory *shape* of momentary suicidal ideation — its tendency to swing, to stay elevated, or to remain near floor — is itself a meaningful phenotype. This raises the tension that organizes the present study. If individuals are partitioned empirically into subtypes by the shape of their within-person ideation trajectories, do those dynamic subtypes simply reproduce the static gradient of trait risk and resource — more risk and less resource yielding a more reactive trajectory — or do they dissociate from it, identifying individuals whose moment-to-moment cascade behaves differently from what their trait profile would predict?

The present study addresses these gaps using a four-wave EMA design with three prompts per day over seven days per wave in N = 391 first-year undergraduates, analyzed with Bayesian multivariate multilevel mediation (Bürkner, 2017; McNeish & Hamaker, 2020). We tested seven pre-registered hypotheses (OSF-preregistered before analysis) addressing, in turn, the joint within-person mediation of stress to suicidal ideation through entrapment, burdensomeness, and belongingness; the dominance ordering among those three mediators; the inter-individual variability of cascade slopes; the path- and dimension-specific moderation of the cascade by childhood trauma; the protective moderation by trait resources; the alignment between data-driven dynamic SI subtypes and the indirect-effect gradient; and the alignment between those same subtypes and the static risk–resource trait gradient. We anticipate, without committing the result in this section, that the dynamic phenotype need not reduce to the static one — that within-person cascade reactivity and between-person trait severity may index partially separable constructs, with consequences for how this population is identified and supported.

**Pre-registered hypotheses.**

**H1. Within-person multi-mediation.** Momentary stress predicts momentary suicidal ideation through three concurrent proximal pathways — entrapment, perceived burdensomeness, and thwarted belongingness — with each indirect effect credibly above zero in the 95% posterior credible interval.

**H2. Mediator dominance.** The entrapment-mediated within-person indirect effect is larger than either the burdensomeness- or the belongingness-mediated effect, with each pairwise contrast meeting a posterior probability of at least 0.90 in the predicted direction.

**H3. Random-slope variance.** Within-person *a*-path and *b*-path slopes vary credibly across individuals for all three mediators.

**H4. Childhood-trauma moderation, path- and dimension-specific.** Childhood-trauma moderation concentrates on the *b*-path rather than the *a*-path overall; on the *a*-path, emotional abuse broadly amplifies stress→mediator coupling, physical abuse shows reverse moderation on stress→entrapment and stress→burdensomeness; physical abuse exhibits null or weakest *b*-path moderation.

**H5. Resource moderation.** Trait resources — resilience, social connectedness, and cognitive reappraisal — moderate the entrapment-to-SI *b*-path in the protective direction, with 95% CrIs excluding zero.

**H6. Dynamic-subtype gradient.** Three dynamic SI subtypes (C1 low-stable; C2 high-fluctuating; C3 high-intensity) exhibit a strictly monotonic gradient C1 < C2 < C3 in the entrapment-mediated indirect effect, with monotonicity PD ≥ 0.90.

**H7. Risk–resource axis differentiation.** Across C1 → C2 → C3, person-level risk indicators increase monotonically, while resource indicators decrease monotonically.

## 2. Methods

### 2.1 Participants and design

Participants were 391 first-year undergraduates from a public university in northern China (mean age 20.4 years, SD 1.6, range 17–25; 67.3% female; 92.6% Han ethnicity). Data were collected across four waves spanning one academic year, each wave comprising seven consecutive days of ecological momentary assessment (EMA) with three semi-random prompts per day (morning, midday, early evening). Each wave began with a self-report questionnaire battery. The study was preregistered on the Open Science Framework (OSF; blinded for review) and received ethics approval from the institutional review board (approval number TJUE2025-H-S-078).

### 2.2 EMA procedure and compliance

Participants received prompts via a mobile application and completed brief surveys on momentary stressors, cognitive–affective states, and suicidal ideation (SI) within 20 minutes of each prompt. The analytic dataset comprised 28,113 valid EMA prompts across 1,553 person-waves (median 72 prompts per participant). The overall prompt-level response rate was 76.4% (SD 11.2%). Of the 28,113 prompts, 46.3% reported at least one concurrent stressor and 6.9% reported momentary SI above the floor of the scale.

### 2.3 Momentary (EMA) measures

**Stressors.** Momentary stressor exposure was assessed at each prompt with an adapted version of the Adolescent Self-Rating Life Events Checklist (ASLEC; Liu et al., 1997). Participants indicated whether each of several common stressors (academic, interpersonal, financial, daily-hassle, and health domains) had occurred since the previous prompt. A total stress-sum intensity score was computed by summing the number of endorsed domains weighted by subjective severity (range 0–35), then within-person centred for analysis.

**Proximal mediators.** Three cognitive–affective states were measured at each prompt using single items adapted from the Interpersonal Needs Questionnaire (INQ-15; Van Orden et al., 2012) and the Entrapment Scale (Gilbert & Allan, 1998). *Entrapment* was assessed with "I feel trapped right now." *Perceived burdensomeness* with "I feel I am a burden to others right now." *Thwarted belongingness* with "I feel disconnected from others right now." Each item was rated on a 1 (not at all) to 5 (extremely) scale.

**Suicidal ideation.** Momentary SI was measured with a single item drawn from the Positive and Negative Suicide Ideation Inventory (PANSI-momentary; Osman et al., 1998): "Right now, I feel that life is not worth living," rated 1–5. This item was treated as an ordinal outcome (cumulative-logit link) in the primary models.

### 2.4 Person-level measures

**Childhood trauma.** The Childhood Trauma Questionnaire–Short Form (CTQ-SF; Bernstein et al., 2003) was administered at Wave 1. Its 25 clinical items yield scores for five dimensions: emotional abuse (EA), physical abuse (PA), sexual abuse (SA), emotional neglect (EN), and physical neglect (PN). All scores were z-standardised. One data-quality issue was identified: the original dataset's CTQ total score had **not applied reverse-scoring** for positively framed neglect items, producing a mean of 60.45 (normative range 32–40). The corrected total (mean 32.30) was used throughout (*r* = 1.00 with independently reconstructed score).

**Trait resources.** Three resource indicators were measured at Wave 3: the Brief Resilience Scale (BRS; Smith et al., 2008; 6 items), Connectedness Questionnaire (Lee et al., 2001; Wave 2; 10 items), and the ERQ-Reappraisal subscale (Gross & John, 2003; 6 items). Scale reliability (Cronbach's *α*) ranged from 0.82 to 0.91.

**Personality dysfunction.** The LPFS-BF (Weekers et al., 2019; 12 items) was administered at Wave 3 as a risk control on the resource-moderation *b*-path.

**Dynamic subtype membership.** A latent profile analysis (LPA; Mplus 8.4) was conducted on the within-person mean, SD, and lag-1 autocorrelation of momentary SI within each person-wave. A three-class solution was selected (BLRT *p* < .001; entropy = 0.83). Because the LPA was conducted at the **person-wave level**, the same participant could occupy different subtypes across waves. Subtypes: C1 low-stable (367 participants, 1,275 person-waves [82.1%]); C2 high-fluctuating (128 participants, 199 person-waves [12.8%]); C3 high-intensity (37 participants, 79 person-waves [5.1%]).

### 2.5 Data-quality note: INQ-15 reverse-scoring

The INQ-15 thwarted belongingness (TB) subscale contains six reverse-coded items; the original dataset had **not applied reverse-scoring**. The original and corrected TB scores correlated at *r* = −0.57 — opposite directions. The corrected score was used throughout. No comparable errors were found in other scales (all *r* > 0.95 with independently reconstructed scores).

### 2.6 Statistical analysis

Analyses were conducted in R 4.3 with `brms` v2.20+ (Bürkner, 2017) using Bayesian multivariate multilevel mediation with 4 chains × 4,000 iterations (1,000 warm-up). Weakly informative priors: fixed effects ~ *N*(0, 1), random-effect SDs ~ *N*(0, 1) half-normal, correlation matrix ~ LKJ(2). Within-person centering followed Curran and Bauer (2011). Five sequential models tested H1–H7. Inference used a dual criterion: 95% CrI excludes zero **and** PD ≥ 0.975 (≥ 0.90 for the H6 monotonicity test, per preregistration).

## 3. Results

### 3.1 Sample characteristics and EMA descriptives

The analytic sample comprised 391 first-year undergraduates (mean age 20.4, SD 1.6, 67.3% female) who contributed 28,113 valid EMA prompts. The response rate was 76.4%. Of the prompts, 46.3% captured at least one concurrent stressor and 6.9% captured momentary SI above the floor of the scale.

### 3.2 Within-person mediation, mediator dominance, and slope variance (H1–H3)

All three within-person indirect effects were credible: stress→entrapment→SI returned a posterior median of 0.0048 (95% CrI [0.0036, 0.0061]; PD > 0.999); stress→burdensomeness→SI returned 0.0023 (95% CrI [0.0014, 0.0033]; PD > 0.999); and stress→belongingness→SI returned 0.0012 (95% CrI [0.0006, 0.0019]; PD > 0.999). Approximately 55% of the total cascade was carried by the entrapment pathway alone. H1 fully supported.

The pairwise probability that entrapment exceeded burdensomeness and belongingness was > 0.99 for both contrasts. H2 fully supported: entrapment dominated.

Across the three mediators, the random-slope SD ranged from 0.043–0.056 on the *a*-paths and 0.073–0.124 on the *b*-paths; all six 95% CrIs excluded zero. H3 fully supported.

### 3.3 Path- and dimension-specific moderation by childhood trauma (H4)

Of 20 *b*-path interactions (5 CTQ subscales × 4 mediators), at least four exceeded PD ≥ 0.975. EA broadly amplified all four *b*-paths; PA showed near-null *b*-path moderation across all four (H4c supported); SA selectively amplified entrapment→SI and burden→SI; neglect dimensions selectively amplified belongingness→SI and loneliness→SI.

On the *a*-path, EA broadly amplified stress→mediator coupling. PA showed reverse-direction moderation compared to EA on stress→entrapment and stress→burden. Neglect produced credible positive moderation on stress→belongingness and stress→loneliness.

### 3.4 Trait-resource moderation of the dominant b-path (H5)

BRS, Connectedness, and ERQ-Reappraisal each produced credible negative interactions with entrapment on SI — all 95% CrIs excluded zero in the protective direction. LPFS-BF (risk control) showed the opposite: positive (amplifying) interaction on the same pathway. H5 fully supported.

### 3.5 Dynamic subtypes, the static trait gradient, and their dissociation (H6–H7)

C2 > C1 and C3 > C1 were credible across all three mediators. However, C3 > C2 strict monotonicity was not supported for entrapment (PD < 0.90) or burdensomeness (PD < 0.90, numerically reversed). For belongingness, C3 > C2 was credible (PD ≥ 0.975). H6 partially supported.

On the static trait gradient (H7), every risk indicator increased strictly monotonically C1 < C2 < C3 and every resource indicator decreased monotonically. H7 fully supported.

**The dissociation.** The three subtypes were strictly graded on every static trait indicator, yet the within-person cascade was not — C2 and C3 were dynamically indistinguishable on the two largest indirect pathways. Dynamic cascade reactivity and static trait severity index partially separable constructs.

## 4. Discussion

### 4.1 Summary of main findings

In a four-wave EMA study of 391 first-year undergraduates, momentary stress drove momentary SI predominantly through entrapment, with smaller credible contributions from burdensomeness and belongingness. The cascade was moderated path- and dimension-specifically by childhood trauma, attenuated on the dominant *b*-path by trait protective resources, and varied credibly in slope strength across individuals. Three dynamic SI subtypes dissociated from the static risk–resource trait gradient: C2 and C3 were not credibly different on the two largest indirect pathways, despite being strictly graded on every person-level risk and resource indicator.

### 4.2 Dynamic phenotypes dissociate from static trait severity

The dissociation between the indirect-cascade gradient and the trait-severity gradient is best read as a construct distinction. C2 and C3 were strictly graded on every risk indicator, yet the within-person cascade saturated short of maximal trait severity, with C2 and C3 not credibly different on the entrapment- or burdensomeness-mediated pathways. The raw stress→SI slope was credibly steeper in C3 than C2, yet this residual gap was fully absorbed once the three mediators were partialled out. What separates the most impaired from the high-fluctuating students appears to be trait severity itself — not the cognitive route through which stress reaches ideation.

This pattern is consistent with literature treating short-term affective dynamics as risk markers independent of mean symptom level (Houben et al., 2015; Kuppens et al., 2010). The C2 subtype — mild on trait severity but high on within-person fluctuation — is not simply a less severe C3 but a structurally different risk profile in which the *coupling* between stress and appraisal is steep even where the *level* of impairment is moderate.

We are explicit about what this finding does and does not claim. It does not assert C2-versus-C3 equivalence — the ROPE analysis ruled out equivalence as well as difference (Kruschke, 2018). The claim is narrower: two operationalisations of "high-risk" pick out partially separable populations, and conflating them risks both over-treating C3 and under-detecting C2.

Prior EMA work has documented within-person SI fluctuation (Hallensleben et al., 2019; Kleiman et al., 2017) and identified proximal risk factors (Czyz et al., 2019), but few studies have asked whether dynamic phenotypes recapitulate the static trait gradient. The present results suggest that within-person cascade reactivity saturates short of maximal trait severity.

### 4.3 Path- and dimension-specific moderation by trauma and resources

Trauma moderation was path-selective (concentrated on the *b*-path) and dimension-selective (EA broadly amplifying; neglect selectively targeting relational mediators; SA targeting cognitive-mediator pathways). Trait resources moderated the dominant entrapment-to-SI *b*-path in the protective direction, while LPFS-BF (risk control) amplified the same pathway — the dual-axis operates as predicted on the strongest proximal channel (Masten, 2018).

One unexpected pattern was the reverse-direction moderation of PA on the stress→entrapment and stress→burden *a*-paths. This may reflect trauma-related stress-decoupling, in which severe physical victimisation blunts rather than amplifies the moment-to-moment translation of everyday stressors into appraisal-based cognitions — consistent with the dissociative phenotype in the broader trauma literature (Lanius et al., 2010). Because the pattern is small, not pre-registered, and emerged in a non-PA-enriched sample, this finding is exploratory and warrants replication.

### 4.4 Methodological considerations

Estimating three concurrent mediators in a single Bayesian multivariate multilevel model with cross-equation random-effect covariance allowed mediator dominance to be tested without sequential model-selection bias (Bürkner, 2017; McNeish & Hamaker, 2020). The pre-registered frequentist pre-analysis converged on the same qualitative pattern as the Bayesian main model. The cascade is contemporaneous — appropriate to the sub-hourly timescale on which appraisal and ideation co-vary — rather than a claim about temporal precedence.

### 4.5 Limitations

First, the C3 subsample is small (37 participants, 79 person-waves), limiting power for the C3-versus-C2 contrast; because the central claim is dissociation, insufficient power renders the claim conservative. Second, SI was measured by a single item, consistent with the EMA-SI literature (Hallensleben et al., 2019; Kleiman et al., 2017) but limited in scope. Third, all variables were self-reported at the same prompt; temporal autocorrelation was addressed via AR(1)-controlled sensitivity, but common-method variance cannot be ruled out. Fourth, the sample is a single-university Chinese cohort; generalisation awaits replication. Fifth, differential EMA compliance across subtypes was tested in a 20-minute-latency subsample and the dissociation pattern was robust.

### 4.6 Clinical implications

Three implications follow. First, the C2 profile — normal trait scores but steep within-person cascade — is invisible to trait-only screening; EMA-style monitoring complements conventional risk assessment. Second, the C3 profile is detectable by trait screening but does not require the most intensive EMA dose, since its cascade does not credibly exceed C2's. Third, because entrapment carries the dominant indirect effect, micro-interventions targeting blocked-escape cognitions in just-in-time adaptive formats (Nahum-Shani et al., 2018) are the highest-yield candidates, complemented by resilience-, connectedness-, and reappraisal-training.

### 4.7 Conclusion

The cascade runs primarily through entrapment, jointly tuned by childhood-trauma exposure on the *a*-path and trait resources on the *b*-path. The cascade is steepest not in the most severely impaired students but in those whose trajectories are most volatile — C2 and C3 dynamically indistinguishable despite being strictly separable on every static trait profile. Identifying who needs which intervention will require both trait screening and within-person monitoring as complementary windows.

---

## References

(References to be formatted from `references.bib` in Elsevier Harvard style. See `Manuscript_JAD/references.bib` for 19 verified entries covering all citations in this manuscript.)
