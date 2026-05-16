# Phase 4 — Reference Audit Report

> **Purpose**: Audit all in-text citations in Phase3_full_assembled.md against references.bib. 
> **Status**: 2026-05-16
> **Next step**: Take the MISSING list to Claude.ai → `paper-lookup` skill → bring back BibTeX → I integrate.

---

## Summary

| Category | Count |
|---|---|
| Entries in references.bib | 21 |
| Citations in manuscript | ~36 unique |
| **Matched (in BibTeX, correct year)** | **18** |
| **Year mismatch** | **1** |
| **Missing from BibTeX** | **15** |
| **Unused in BibTeX** | **3** |

---

## ✅ MATCHED (18) — no action needed

| In-text | BibTeX key | Section |
|---|---|---|
| Mortier et al., 2018 | Mortier2018FirstYear | §1.1 |
| O'Connor & Kirtley, 2018 | OConnor2018IMV | §1.2 |
| Van Orden et al., 2010 | VanOrden2010IPT | §1.2 |
| Klonsky et al., 2018 | Klonsky2018IdeationToAction | §1.2 |
| Czyz et al., 2019 | Czyz2019DailyDiary | §1.3, §4.2, §4.5 |
| Hallensleben et al., 2019 | Hallensleben2019Predicting | §1.3, §4.2, §4.5 |
| Kleiman et al., 2017 | Kleiman2017RealTimeSI | §1.3, §4.2, §4.5 |
| de Beurs et al., 2019 | deBeurs2019Network | §1.4 |
| Forkmann et al., 2018 | Forkmann2018EMAItems | §1.4 |
| Compas et al., 2017 | Compas2017Coping | §1.5, §4.3 |
| McLaughlin et al., 2020 | McLaughlin2020Mechanisms | §1.5, §4.3 |
| Liu et al., 2017 | Liu2017CTQMeta | §1.5, §4.3 |
| Masten, 2018 | Masten2018Resilience | §1.5, §4.3 |
| Houben et al., 2015 | Houben2015EmotionDynamics | §1.6, §4.2 |
| Kuppens et al., 2010 | Kuppens2010Inertia | §1.6, §4.2 |
| Bürkner, 2017 | Burkner2017brms | §1.7, §2.6, §4.4 |
| McNeish & Hamaker, 2020 | McNeish2020DSEM | §1.7, §2.6, §4.4 |
| Van Orden et al., 2012 | VanOrden2012INQ | §2.3 |

## ⚠️ YEAR MISMATCH (1) — fix in manuscript text

| Manuscript says | Actual (from BibTeX) | BibTeX key | Fix |
|---|---|---|---|
| (Li et al., **2023**) | (Li et al., **2014**) | Li2014SIChineseCollege | Change 2023 → 2014 in §1.1 |

## ❌ MISSING from BibTeX (15)

| In-text | Section | Description | Notes |
|---|---|---|---|
| Liu et al., **2022** | §1.1 | Chinese freshmen SI | ⚠️ Possibly hallucinated — needs real ref |
| Rogers & Joiner, 2017 | §1.4 | IPT conceptual review | Rogers & Joiner (2017) Curr Opin Psychol |
| Gilbert & Allan, 1998 | §2.3 | Entrapment Scale | Gilbert & Allan (1998) B J Clin Psychol |
| Osman et al., 1998 | §2.3 | PANSI | Osman et al. (1998) J Clin Psychol |
| Bernstein et al., 2003 | §2.4 | CTQ-SF | Bernstein et al. (2003) J Nerv Ment Dis |
| Smith et al., 2008 | §2.4 | BRS | Smith et al. (2008) Int J Behav Med |
| Lee et al., 2001 | §2.4 | Connectedness | Lee et al. (2001) J Couns Psychol |
| Gross & John, 2003 | §2.4 | ERQ | Gross & John (2003) J Pers Soc Psychol |
| Weekers et al., 2019 | §2.4 | LPFS-BF | Weekers et al. (2019) Assessment |
| Liu et al., 1997 | §2.3 | ASLEC | Liu et al. (1997) Chinese scale — may need Chinese-source lookup |
| Curran & Bauer, 2011 | §2.6 | Within-person centering | Curran & Bauer (2011) Psychol Methods |
| Kruschke, 2018 | §4.2 | ROPE / Bayesian estimation | Kruschke (2018) "Doing Bayesian Data Analysis" book |
| Lanius et al., 2010 | §4.3 | Dissociation/trauma | Lanius et al. (2010) J Trauma Stress |
| Nahum-Shani et al., 2018 | §4.6 | JITAI framework | Nahum-Shani et al. (2018) Ann Behav Med |

## ❌ UNUSED in BibTeX (3) — can remove or keep

| BibTeX key | Not cited in manuscript |
|---|---|
| Chang2024SIChineseChildren | Not used |
| Chu2017IPTMeta | Not used (Chu 2017 IPT meta-analysis) |
| Zheng2022Freshmen | Not used |

---

# Claude.ai TASK — copy this and paste into a new Claude.ai conversation

```
调用 paper-lookup skill。帮我找到以下 15 篇参考文献的完整 BibTeX 信息（Elsevier Harvard 格式，含 DOI）：

1. Liu et al. (1997) — Adolescent Self-Rating Life Events Checklist (ASLEC), Chinese scale
2. Gilbert & Allan (1998) — Entrapment Scale, British Journal of Clinical Psychology
3. Osman et al. (1998) — Positive and Negative Suicide Ideation Inventory (PANSI), J Clin Psychol
4. Bernstein et al. (2003) — Childhood Trauma Questionnaire (CTQ-SF), J Nerv Ment Dis
5. Gross & John (2003) — Emotion Regulation Questionnaire (ERQ), J Pers Soc Psychol
6. Smith et al. (2008) — Brief Resilience Scale (BRS), Int J Behav Med
7. Lee et al. (2001) — Connectedness Questionnaire / Social Connectedness Scale, J Couns Psychol
8. Rogers & Joiner (2017) — IPT conceptual review, Curr Opin Psychol
9. Weekers et al. (2019) — LPFS-BF, Assessment
10. Curran & Bauer (2011) — Within-person centering, Psychol Methods
11. Lanius et al. (2010) — Dissociation/trauma, J Trauma Stress
12. Nahum-Shani et al. (2018) — JITAI framework, Ann Behav Med
13. Kruschke (2018) — Doing Bayesian Data Analysis, book (Academic Press, 2nd ed.)
14. Van Orden et al. (2012) — INQ-15 validation, Psychol Assess (this one matches BibTeX key: VanOrden2012INQ)
15. Liu et al. (2022) — Chinese freshmen SI prevalence / college student SI — cannot find, try "Liu negative life events freshmen JAD 2022" (might be Zheng et al. 2022 already in BibTeX; if found, replace the in-text citation)

对每条输出 BibTeX @article{key, ...} 格式。如有 DOI 必须包含。

完成后把结果粘贴回 Claude Code。
```
