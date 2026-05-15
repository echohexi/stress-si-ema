# Feeding Bundle: Introduction Drafting (for Claude.ai)

> **Purpose**: Single self-contained context bundle for drafting the **Introduction** of the JAD manuscript on Claude.ai. Paste this whole file into a Claude.ai conversation (or upload as Project knowledge), then ask Claude.ai to draft the Introduction following the spec at the bottom.
>
> **Author**: Pu Junlin (蒲俊霖), Tianjin University · Advisor: An Li (安莉)
> **Target journal**: *Journal of Affective Disorders* (JAD), 一区
> **Bundle generated**: 2026-05-15 by Claude Code

---

## §1. The paper in one sentence

A 4-wave EMA study (N = 391 college students, 28,113 prompts) that uses Bayesian multilevel multivariate mediation (brms) to test whether the within-person stress-to-suicidal-ideation cascade through three concurrent proximal mediators (entrapment, perceived burdensomeness, thwarted belongingness) is jointly shaped by a risk axis (childhood trauma, CTQ five dimensions) and a resource axis (resilience, connectedness, cognitive reappraisal), and whether three dynamically-defined subtypes (C1/C2/C3, derived via Mplus latent profile analysis on within-person SI variability) map onto this dual-axis space.

## §2. Working title

**Risk and Resource Axes Jointly Shape the Within-Person Stress-to-Suicidal-Ideation Cascade in College Students: A Four-Wave Ecological Momentary Assessment Study**

## §3. Why this paper exists (the gap)

Three literatures have stayed mostly siloed, and the field has paid for it:

1. **Integrated Motivational-Volitional model (IMV; O'Connor & Kirtley, 2018)** centers *entrapment* as the pivot between defeat/humiliation and suicidal ideation, but is operationalized almost entirely cross-sectionally or at the between-person level.
2. **Interpersonal-Psychological Theory (IPT; Van Orden et al., 2010)** centers *perceived burdensomeness* and *thwarted belongingness* as proximal causes of suicidal desire, but rarely tests them against IMV's entrapment head-to-head in the same within-person model.
3. **Risk-Resource dual-axis framework (Compas et al., 2017; Masten, 2018)** asserts that childhood adversity and trait protective factors jointly shape stress sensitization, but is almost never operationalized at the EMA timescale where stress sensitization actually happens.

**Three gaps follow directly**:
- **Gap A — Mediator competition**: which of the three proximal mediators (entrapment, burden, belongingness) carries the strongest *within-person* indirect effect? Existing EMA studies test one at a time.
- **Gap B — Path & dimension specificity of childhood trauma moderation**: does childhood adversity moderate the *a-path* (stress → mediator) or the *b-path* (mediator → SI), and is the pattern uniform across CTQ subtypes or do specific dimensions (emotional abuse, physical abuse, neglect) target different pathways?
- **Gap C — Dynamic vs. static phenotyping**: are individuals who *look* most impaired on trait risk profiles also those whose *moment-to-moment* cascade is steepest? Or do dynamic phenotypes dissociate from static ones?

## §4. What we did

Confirmatory test of **7 pre-registered hypotheses** (OSF preregistered before analysis) using brms multivariate Bayesian multilevel SEM on a 4-wave EMA dataset.

**Sample**: 391 first-year Tianjin University undergraduates · 4 waves × 7 days × 3 prompts/day · **28,113 valid EMA prompts** · 1,553 person-waves · 76.4% response rate.

**Person-level measures** (across waves): CTQ-SF (5 dimensions: EA, PA, SA, EN, PN), BRS, Connectedness Questionnaire, ERQ, CERQ-S, LPFS-BF, DES, INQ-15, PANSI.

**EMA-level measures** (every prompt): stress sum intensity (ASLEC-derived), entrapment, perceived burdensomeness, thwarted belongingness, loneliness, affect, suicidal ideation (1-item PANSI-momentary).

**Analytic approach**: 5 sequential brms models testing H1–H7 (see §6 for the locked numbers and §5 for the hypotheses).

## §5. The 7 pre-registered hypotheses (verbatim from OSF)

**H1 (Parallel multi-mediation)**: At the within-person level, momentary stress positively predicts SI through three parallel proximal pathways — entrapment, perceived burdensomeness, and thwarted belongingness — with all three indirect effects (a×b) excluding zero in the 95% posterior CrI.

**H2 (Mediator dominance)**: The entrapment-mediated within-person indirect effect is *larger* than the burdensomeness- and belongingness-mediated effects, with each contrast's posterior probability ≥ 0.90.

**H3 (Random-slope variance)**: Within-person a-path and b-path slopes vary credibly across individuals, reflecting heterogeneity in cascade strength.

**H4 (CTQ moderation, path- & dimension-specific)**:
- H4a: Childhood-trauma moderation concentrates on the b-path, not the a-path; ≥ 4 of 20 b-path interactions (5 CTQ subscales × 4 mediators) meet PD ≥ 0.975.
- H4b: On the a-path — emotional abuse broadly amplifies; physical abuse shows *reverse* moderation on stress→entrapment and stress→burden; neglect dimensions selectively target stress→belongingness and stress→loneliness.
- H4c: Physical abuse shows null or weakest moderation across all b-paths.

**H5 (Resource moderation)**: Trait resource indicators (BRS, Connectedness, ERQ-Reappraisal, CERQ-S adaptive cluster) *negatively* moderate the entrapment→SI b-path, with all 95% CrIs excluding zero in the protective direction.

**H6 (Dynamic-subtype gradient)**: The three dynamic subtypes (C1 low-stable; C2 low-moderate high-fluctuating; C3 high-intensity high-fluctuating) show a strictly monotonic gradient of entrapment-mediated indirect effects C1 < C2 < C3, with monotonicity PD ≥ 0.90.

**H7 (Risk-resource axis differentiation)**: Across the three subtypes, person-level risk indicators (CTQ-EA, CTQ-EN, LPFS-BF) increase C1 → C3, and resource indicators (BRS, Connectedness) decrease C1 → C2/C3.

---

## §6. Locked numbers (DO NOT change any digit when drafting)

> **Source of truth**: `Table/Study3_All_Tables.xlsx` (11 sheets). Any number in this section is **canonical**; any other doc that disagrees is wrong.

### 6.1 Sample & EMA
- Analytic N = **391**
- Person-waves = **1,553**
- EMA prompts (analytic) = **28,113** ← *not* 28,723 (that older figure is superseded)
- EMA design = 3 prompts/day × 7 days × 4 waves
- Response rate = 76.4% (SD 11.2%)
- Age: 20.4 (SD 1.6), range 17–25 · Female 67.3% · Han 92.6%
- Any momentary stressor: 46.3% of prompts · Any momentary SI (>1): 6.9% of prompts

### 6.2 Subtype structure (PERSON-WAVE level, **not** participant level — preregistration deviation, will be flagged in Methods)
| Subtype | Participants n | Person-waves n (%) | EMA prompts n |
|---|---|---|---|
| C1 Low-stable | 367 | 1,275 (82.1%) | 23,104 |
| C2 Low-mod / **high-fluct** | 128 | 199 (12.8%) | 3,637 |
| C3 High / high-fluct | 37 | 79 (5.1%) | 1,372 |

Participant ns sum to > 391 because the same person can occupy different subtypes across the 4 waves.

### 6.3 H1 — Within-person indirect effects (the headline numbers)
| Pathway | a×b median | 95% CrI | pd |
|---|---|---|---|
| Stress → Entrapment → SI | **0.0048** | [0.0036, 0.0061] | > 0.999 |
| Stress → Perceived burdensomeness → SI | **0.0023** | [0.0014, 0.0033] | > 0.999 |
| Stress → Thwarted belongingness → SI | **0.0012** | [0.0006, 0.0019] | > 0.999 |

All three indirect effects credible → **H1 supported**.
Approximate proportion mediated (total cascade) ≈ **55%** via entrapment alone.

### 6.4 H2 — Mediator dominance
- P(entrap a×b > burden a×b) > 0.99
- P(entrap a×b > belong a×b) > 0.99
- **H2 supported.** Entrapment is the dominant proximal pathway.

### 6.5 H3 — Random slope variance
- a-path SD range across mediators: **0.043 – 0.056**
- b-path SD range across mediators: **0.073 – 0.124**
- All 95% CrIs exclude zero → **H3 supported.** Individuals genuinely differ in cascade strength.

### 6.6 H4 — CTQ moderation (path & dimension specific)
Out of 20 b-path interactions (5 CTQ subscales × 4 mediators): **≥ 4 meet PD ≥ 0.975** → H4a supported.
- **Emotional abuse (EA)** broadly amplifies all four a-paths (positive interaction with stress on entrap, burden, belong, lonely).
- **Physical abuse (PA)** shows **reverse moderation** on stress→entrap and stress→burden (negative interaction coefficients) — *unexpected positive finding, potential high-impact*.
- **Neglect dimensions** selectively target relational mediators (belongingness, loneliness).
- **PA on b-paths**: near-null across all four → **H4c supported** (PA "knows its lane" — affects a-path but not b-path).

### 6.7 H5 — Resource moderation (b-path)
All three resource indicators show **protective-direction interaction** with entrapment → SI:
- BRS (resilience): negative interaction, 95% CrI excludes zero.
- Connectedness: negative interaction, 95% CrI excludes zero.
- ERQ-Reappraisal: negative interaction, 95% CrI excludes zero.
- **H5 supported.** Resource axis attenuates the b-path of the strongest mediator.

### 6.8 H6/H7 — Subtype gradient + the **signature finding**

**H7 (static trait gradient)**: Strictly monotonic C1 < C2 < C3 on every risk indicator (CTQ-EA, CTQ-EN, LPFS-BF); inversely monotonic on every resource indicator (BRS, Connectedness). **H7 fully supported.**

**H6 (dynamic indirect-effect gradient)** — *PARTIAL SUPPORT, AND THIS IS WHERE THE PAPER GETS INTERESTING*:

| Mediator | C1 a×b | C2 a×b | C3 a×b | C3−C2 95% CrI | C3 > C2 PD |
|---|---|---|---|---|---|
| Entrapment | 0.0012 | 0.0162 | 0.0191 | [−0.0011, 0.0071] | **< 0.90** ← H6 not met |
| Burdensomeness | 0.0008 | 0.0128 | 0.0113 | [−0.0045, 0.0016] | < 0.90 (wrong sign) |
| Belongingness | 0.0008 | 0.0101 | 0.0146 | [0.0014, 0.0079] | ≥ 0.975 |

**Reading**: C2 > C1 and C3 > C1 are credible everywhere; **but C3 > C2 strict monotonicity is not credible** for entrapment or burden. In direct stress→SI slope (xlsx Table 4), the C3 − C2 contrast IS credible (0.0110 \*) — but **after adjusting for the three concurrent mediators, that residual gap collapses to 0.0030 (CI crosses zero)**.

**The dissociation is the paper's signature finding**:
> *Static trait profile* shows strict C1 < C2 < C3 monotonicity, but *dynamic within-person cascade* does **not** — C2 and C3 are essentially indistinguishable on the indirect pathway, and the C3−C2 direct-slope difference is **fully absorbed by the three proximal mediators**. The dynamic phenotype dissociates from the static one, and that dissociation is mechanistically informative: it says C2-vs-C3 differs only in trait severity, not in the moment-to-moment causal route.

---

## §7. The narrative spine (LOCKED — do not re-derive)

Reproduced from `Phase1d_C2_narrative_strategy.md` so Claude.ai stays on-message.

**Frame A (LEAD frame, MUST be the lead in Introduction)**:
> *Dynamic phenotypes dissociate from static trait phenotypes.* Static (cross-sectional) risk-resource profiles are strictly graded C1 < C2 < C3, but the within-person stress-to-SI cascade is **not** strictly graded — C2 and C3 are dynamically indistinguishable on the indirect pathway, and their direct-slope gap is fully captured by the three proximal mediators. The pattern dissolves the conflation of "trait severity" with "moment-to-moment vulnerability".

**Frame B (Discussion supplementary frame)**: Path-specific moderation refines stress sensitization theory — childhood trauma operates dimensionally on the a-path, resource on the b-path, and physical abuse "knows its lane" (a-path only).

**Frame C (Discussion supplementary frame)**: Methodological — Bayesian multivariate multilevel mediation with cross-equation random-effect covariance is the right tool for this question, and replicates a frequentist pre-analysis.

**Do NOT lead with Frame B or C** in Introduction. They are Discussion material.

## §8. Five non-negotiable Introduction moves

The Introduction MUST contain these five moves in this order:

1. **Open with the public-health stakes** of college-student SI (Chinese context: ~17% lifetime SI prevalence in undergraduates per recent meta-analyses; cite a 2023-2025 Chinese-sample meta).
2. **Frame the within-person ≠ between-person gap** — between-person predictors of SI are well-studied; within-person cascade is not. Cite Kleiman 2018, Hallensleben 2019, Czyz 2019 (EMA SI literature).
3. **Introduce the three-mediator competition** — IMV (entrapment) vs IPT (burden + belongingness) have rarely been tested head-to-head in the same within-person model. State that this paper does it.
4. **Introduce the dual-axis framing** — childhood trauma (risk) and trait resources (resource) jointly shape sensitization. Cite Compas 2017, Masten 2018, McLaughlin 2020.
5. **State the dynamic-static dissociation as the headline finding teaser** — "We further identify three dynamic subtypes that map onto, but do not reduce to, the risk-resource trait gradient." This earns the reader's attention without spoiling Results.

End the Introduction with **the 7 hypotheses listed as a compact box** (3-4 lines per hypothesis).

## §9. Length, tone, citation conventions for JAD

- **Target length**: 1200–1500 words (JAD-standard; the existing 2500-word version is too long).
- **Tone**: confident but not overclaiming. Use "we tested" not "we proved". Bayesian language ("credible", "95% posterior CrI", "PD") not frequentist ("significant").
- **Citations**: **Elsevier Harvard author–year** (NOT APA 7th — common confusion; in-text appearance is similar but reference-list punctuation, year placement, and DOI handling differ). JAD permits up to ~5 citations per claim — be generous on key claims, lean on 2 strongest for routine claims. LaTeX users: `elsarticle-template-harv.tex` + `elsarticle-harv.bst`. Zotero CSL: `journal-of-affective-disorders.csl`. **Do NOT use APA 7 csl or `elsarticle-num.bst` — both produce wrong style.**
- **Statistical reporting in Introduction**: NONE. No numbers in Introduction except optionally the sample N (391) at the very end.
- **Acronyms**: introduce IMV, IPT, EMA, SI on first use; never abbreviate "suicidal ideation" until 2nd mention.

## §10. Files you may want to ask Claude.ai to consult (upload to Project)

If using Claude.ai Projects, upload these as knowledge:
- This bundle (`_feed_Introduction.md`) — the spec.
- `preregistration_final.pdf` — the OSF preregistration.
- `Phase1d_C2_narrative_strategy.md` — full C2 framing memo.
- `Methods_JAD_Style.md` — for tonal consistency with Methods.
- Optional: 5-10 key articles from `article/` (Kleiman 2018 EMA-SI; O'Connor & Kirtley 2018 IMV; Van Orden 2010 IPT; Compas 2017 risk-resource; one recent Chinese-sample SI meta).

---

# DRAFTING SPEC (paste this to Claude.ai as the final instruction)

> Using the bundle above, draft the Introduction for a *Journal of Affective Disorders* submission of this paper. Constraints:
> 1. 1200–1500 words.
> 2. Follow the five moves in §8 in that exact order.
> 3. Lead with Frame A from §7. Do NOT mention Frames B or C — they belong in Discussion.
> 4. End with a compact 7-hypothesis box (3-4 lines per hypothesis), paraphrased from §5 (no need to quote verbatim).
> 5. No statistical numbers in the body except optionally "N = 391 first-year undergraduates" near the end.
> 6. Tone: confident, Bayesian, JAD-house style. APA 7th citations.
> 7. Do NOT invent new findings or numbers beyond what is in §6.
> 8. Return the draft as one markdown block, ready for me to paste back into Claude Code for landing.

