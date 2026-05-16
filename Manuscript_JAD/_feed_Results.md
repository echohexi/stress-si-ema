# Feeding Bundle: Results Drafting (for Claude.ai)

> **Purpose**: Single self-contained context bundle for drafting the **Results** section of the JAD manuscript on Claude.ai. Paste this whole file into a Claude.ai conversation, then ask Claude.ai to draft Results following the spec at the bottom.
>
> **Target journal**: *Journal of Affective Disorders* (JAD), 一区
> **Bundle generated**: 2026-05-16 by Claude Code
> **Narrative authority**: `Phase1d_C2_narrative_strategy.md` (locked 2026-05-16)

---

## §1. The paper in one sentence

A 4-wave EMA study (N = 391 college students, 28,113 prompts) using Bayesian multilevel multivariate mediation to test whether the within-person stress-to-SI cascade through entrapment, burdensomeness, and belongingness is jointly shaped by childhood trauma (risk axis) and trait resources (resource axis), and whether three dynamic subtypes (C1/C2/C3) dissociate from the static trait gradient.

## §2. Narrative spine for Results (LOCKED — do not re-derive)

The Results section must tell this story in exactly this order:

1. **H1-H3 (the cascade exists and is heterogeneous)**: All three indirect effects are credible. Entrapment dominates. Slopes vary across individuals. This establishes the basic phenomenon.
2. **H4 (the cascade is moderated, path- and dimension-specifically)**: CTQ moderation concentrates on the b-path. On the a-path, EA broadly amplifies, PA shows reverse-direction moderation relative to EA, neglect selectively targets relational mediators. PA on b-paths is near-null. Report the b-path pattern as primary; report PA reverse on a-path as a flat descriptive sentence (no mechanism speculation — that goes in Discussion).
3. **H5 (resources buffer the strongest b-path)**: BRS, Connectedness, and ERQ-Reappraisal all negatively moderate entrapment→SI in the protective direction.
4. **H6-H7 (the signature finding — static and dynamic dissociate)**: First report that C2 > C1 and C3 > C1 are credible. Then state that C3 > C2 strict monotonicity is NOT supported for entrapment or burdensomeness. Then immediately pivot: "However, this non-monotonicity dissociates from the strictly monotonic static trait gradient (H7)."

**Critical framing for H6**:
- Do NOT lead with "H6 failed." Lead with "The cascade was not uniformly distributed across subtypes: C2 and C3 were both credibly elevated above C1, but differed non-credibly from each other."
- Do NOT use "C2 > C3" — use "C2 and C3 were not credibly different."
- The dissociation (not the non-monotonicity) is the finding.

---

## §3. Sample flow

| Item | Number |
|---|---|
| Analytic sample | 391 first-year undergraduates |
| EMA prompts (analytic) | 28,113 |
| Person-waves | 1,553 |
| Age | 20.4 (SD 1.6), range 17–25 |
| Female | 67.3% |
| Han ethnicity | 92.6% |
| Response rate | 76.4% (SD 11.2%) |
| EMA design | 3 prompts/day × 7 days × 4 waves |
| Any momentary stressor | 46.3% of prompts |
| Any momentary SI (>1) | 6.9% of prompts |

## §4. H1-H3 — Descriptive statistics and basic cascade

### H1 — Within-person indirect effects (xlsx Table 3)

| Pathway | a×b median | 95% CrI | pd |
|---|---|---|---|
| Stress → Entrapment → SI | **0.0048** | [0.0036, 0.0061] | > 0.999 |
| Stress → Perceived burdensomeness → SI | **0.0023** | [0.0014, 0.0033] | > 0.999 |
| Stress → Thwarted belongingness → SI | **0.0012** | [0.0006, 0.0019] | > 0.999 |

All three 95% CrIs exclude zero; all pd > 0.975. H1 supported.
Approximately 55% of the total stress→SI effect was mediated via entrapment alone.

### H2 — Mediator dominance (xlsx Table 3 contrasts)

- P(entrap a×b > burden a×b) > 0.99
- P(entrap a×b > belong a×b) > 0.99
- H2 supported. Entrapment carries the dominant indirect effect.

### H3 — Random slope variance (xlsx Table 3 SD columns)

| Parameter | Posterior median SD | 95% CrI |
|---|---|---|
| a-path (stress→mediator) | 0.043–0.056 across mediators | Excludes zero |
| b-path (mediator→SI) | 0.073–0.124 across mediators | Excludes zero |

H3 supported. Individuals differ credibly in cascade strength.

## §5. H4 — CTQ path × dimension moderation (xlsx Table 2 + Table S5)

### b-path (mediator → SI) — primary finding

Out of 20 b-path interactions (5 CTQ subscales × 4 mediators), ≥ 4 exceeded PD ≥ 0.975. H4a supported — trauma moderation concentrates on the b-path.

**b-path pattern summary (narrative, not full table)**:
- **Emotional abuse (EA)**: Positive moderation across all four b-paths. Broadest amplifier.
- **Physical abuse (PA)**: Near-null or weakest moderation across all b-paths. H4c supported.
- **Sexual abuse (SA)**: Selective positive moderation on entrapment→SI and burden→SI b-paths.
- **Emotional neglect (EN)**: Selective positive moderation on belongingness→SI and loneliness→SI b-paths.
- **Physical neglect (PN)**: Similar to EN pattern but weaker.

### a-path (stress → mediator) — secondary finding

Report descriptively. One sentence on each:
- **EA**: Positive interaction on all four a-paths (amplifies stress→mediator coupling broadly).
- **PA**: **Reverse-direction moderation** compared to EA on stress→entrapment and stress→burden (negative interaction coefficients). Report as empirical fact: "PA showed a reverse pattern relative to EA on the stress→entrapment and stress→burden a-paths." Do NOT explain or speculate. That goes in Discussion.
- **Neglect (EN + PN)**: Positive moderation on stress→belongingness and stress→loneliness, consistent with the relational-specificity hypothesis.

## §6. H5 — Resource moderation (xlsx Table S6)

All three resource indicators moderate the entrapment → SI b-path in the protective (negative) direction:

| Resource indicator | Interaction direction | Posterior support |
|---|---|---|
| BRS (resilience) | Negative | 95% CrI excludes zero |
| Connectedness | Negative | 95% CrI excludes zero |
| ERQ-Reappraisal | Negative | 95% CrI excludes zero |

H5 supported. The resource axis attenuates the dominant proximal pathway. LPFS (personality dysfunction) entered as a risk control; its interaction direction was positive (amplifying) as expected, confirming the risk-resource dual-axis framework operates as predicted on the same pathway.

## §7. H6-H7 — Subtype cascade and the dissociation (THE SIGNATURE FINDING)

### Subtype structure

Subtype membership assigned at the **person-wave level** (same individual can occupy different subtypes across waves). See Phase1_locked_numbers.md §2 for full table.

| Subtype | Participants, n | Person-waves, n (%) | EMA prompts, n |
|---|---|---|---|
| C1 Low-stable | 367 | 1,275 (82.1%) | 23,104 |
| C2 Low-mod / high-fluct | 128 | 199 (12.8%) | 3,637 |
| C3 High / high-fluct | 37 | 79 (5.1%) | 1,372 |

### H6 — Subtype-specific indirect effects (xlsx Table 3)

| Mediator | C1 a×b | C2 a×b | C3 a×b | C3 − C2 95% CrI | C3 > C2 PD |
|---|---|---|---|---|---|
| Entrapment | 0.0012 | **0.0162** | **0.0191** | [−0.0011, 0.0071] | < 0.90 |
| Burdensomeness | 0.0008 | **0.0128** | 0.0113 | [−0.0045, 0.0016] | < 0.90 |
| Belongingness | 0.0008 | **0.0101** | **0.0146** | [0.0014, 0.0079] | ≥ 0.975 |

**Narrative template (COPY VERBATIM into Results paragraph)**:
> "C2 > C1 and C3 > C1 contrasts were credible across all three mediators (95% CrIs excluded zero). However, C3 > C2 strict monotonicity was not supported for entrapment (PD < 0.90) or burdensomeness (PD < 0.90, with burdensomeness showing a numerically reversed point estimate). For belongingness, the C3 > C2 contrast was credible (PD ≥ 0.975). Taken together, the indirect effect gradient was not strictly monotonic: C2 and C3 were not credibly different on the two largest indirect pathways."

### H7 — Static trait gradient (Figure 1 source data)

Across C1 → C2 → C3, all risk indicators increase monotonically and all resource indicators decrease monotonically:

| Indicator | Direction | Pattern |
|---|---|---|
| CTQ-EA (emotional abuse) | C1 < C2 < C3 | Strict monotonic |
| CTQ-EN (emotional neglect) | C1 < C2 < C3 | Strict monotonic |
| LPFS-BF (personality dysfunction) | C1 < C2 < C3 | Strict monotonic |
| BRS (resilience) | C1 > C2 > C3 | Strict monotonic (inverse) |
| Connectedness | C1 > C2 > C3 | Strict monotonic (inverse) |

**H7 supported.** The static risk-resource profile is strictly graded.

### The dissociation (THIS IS THE FINDING)

From Phase1d_C2_narrative_strategy.md §1, fact 5:
> "Static trait profiles are strictly monotonic C1 < C2 < C3 on every risk indicator and inversely monotonic on every resource indicator. The dynamic-cascade non-monotonicity therefore **dissociates from** the static trait gradient — this dissociation is the manuscript's signature finding."

**Write this as the closing paragraph of H6-H7 subsection**:
> "Thus, the dynamic cascade reactivity and the static trait severity index are not redundant. The three subtypes were strictly graded on every person-level risk and resource indicator (H7), yet the within-person indirect effect gradient was not — C2 and C3, despite their distinct trait profiles, were dynamically indistinguishable on the two largest indirect pathways."

---

## §8. Writing rules for Results (LOCKED from Phase1d_C2_narrative_strategy.md §5)

1. **H1 first** (all three indirect effects credible); then H2 (entrap dominates).
2. **H4 CTQ moderation**: Report b-path pattern as main finding. Report PA reverse moderation on a-path in one flat, descriptive sentence: "On the a-path, PA showed reverse-direction moderation compared to EA on stress→entrapment and stress→burden." Do NOT elaborate or speculate there — the Discussion §3 explains it.
3. **H6**: Lead with "C2 > C1 and C3 > C1 were credible across all mediators. However, C3 > C2 strict monotonicity was not supported for entrapment (PD < 0.90) or burdensomeness (PD < 0.90)." Then pivot: "This non-monotonicity dissociates from the static trait gradient (H7)..." Use the template in §7 verbatim.
4. **Numbers only from this feed**, which is xlsx-canonical via Phase1_locked_numbers.md.
5. **JAD style**: Results narrate, do NOT interpret. Interpretation goes in Discussion. Use "credible" not "significant". Report 95% CrI not CI/p-value. Report pd when relevant.
6. **Length**: No formal JAD limit for Results section. Estimate ~1500-2000 words total for all subsections combined.
7. **Acronyms**: Re-introduce on first Results use (assume reader jumped from Methods, may not have read Intro).

## §9. Table correspondence

| Manuscript table | Feed section | xlsx sheet |
|---|---|---|
| Table 1 — Sample + EMA descriptives | §3 | Overview + Table 1 |
| Table 2 — H1 indirect effects + H2 contrasts | §4 | Table 3 |
| Table 3 — H4 CTQ × path moderation | §5 | Table 2 + S5 |
| Table 4 — H6-H7 subtype cascade + trait gradient | §7 | Table 3 + Figure 1 source data |

## §10. Supplementary tables referenced

| Table | Content | xlsx sheet |
|---|---|---|
| Table S1 | Descriptive statistics per wave | Table 1 |
| Table S2 | AR(1)-controlled H1 sensitivity | S3 |
| Table S3 | Lagged mediation sensitivity | S4 |
| Table S4 | Within-20-min latency sensitivity | S3-S4 |
| Table S5 | Full 40-model CTQ a-path + b-path interaction matrix | Table 2 |
| Table S6 | Resource moderation full coefficients | S6 |
| Table S7 | Random-slope SD full matrix | S2 |

---

# DRAFTING SPEC (paste this to Claude.ai as the final instruction)

> Using the feeding bundle above, draft the Results section for a *Journal of Affective Disorders* submission. Constraints:
> 1. Follow §2 narrative spine order exactly. Do NOT reorder.
> 2. Use the H6 narrative template from §7 **verbatim** — those are locked phrases.
> 3. For PA reverse moderation in §5 (H4 a-path), write ONE flat descriptive sentence only: "On the a-path, PA showed reverse-direction moderation compared to EA on stress→entrapment and stress→burden." Do NOT add mechanism speculation there.
> 4. The closing paragraph of H6-H7 must state the dissociation explicitly (use the lock phrase in §7).
> 5. Numbers only from this bundle — do not invent or round differently.
> 6. Tone: narrative, not interpretive. JAD-house style. Use "credible" not "significant". Report 95% CrI. Report pd when relevant.
> 7. ~1500-2000 words total. Each subsection (H1-H3, H4, H5, H6-H7) should be 3-6 paragraphs.
> 8. Return the draft as one markdown block, ready for me to paste back into Claude Code for landing.


