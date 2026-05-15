# Phase 0 — Journal of Affective Disorders Submission Profile

**Fetched**: 2026-05-13 · **Refreshed v2**: 2026-05-15 (via Claude.ai `journal-intelligence` skill)
**Article type targeted**: Full-Length Research Paper
**Source**: Elsevier ScienceDirect Guide for Authors + Elsevier Highlights spec

---

## ⚠ v2 corrections (2026-05-15) — these override v1 wherever they conflict

Three critical changes since v1 (2026-05-13). Apply to all downstream files.

### Correction 1 — AI disclosure section TITLE changed (Elsevier-wide, Sep 2025)
- **OLD (v1, NOW WRONG)**: "Declaration of generative AI and AI-assisted technologies **in the manuscript preparation process**"
- **NEW (v2, AUTHORITATIVE)**: "Declaration of generative AI and AI-assisted technologies **in the writing process**"
- **Severity**: CRITICAL — Editorial Manager checks the section title literally.

### Correction 2 — AI disclosure TEMPLATE final phrase changed
- **OLD (v1, NOW WRONG)**: "...take(s) full responsibility for the content of the **published article**."
- **NEW (v2, AUTHORITATIVE)**: "...take(s) full responsibility for the content of the **publication**."
- **Severity**: MAJOR — required wording.

### Correction 3 — Citation style downstream confusion
- The earlier `_feed_Introduction.md` (now superseded) said citations are "APA 7th". **WRONG.**
- JAD uses **Elsevier Harvard (author–year)**. NOT APA, NOT Vancouver-numbered.
- In-text appearance is similar to APA; reference-list punctuation, year placement, and DOI handling DIFFER.
- LaTeX users: start from `elsarticle-template-harv.tex` + `elsarticle-harv.bst` (the `-num` variant gives wrong style).
- `_feed_Introduction.md` §9 has been corrected in commit (see git log).

### Other v2 refinements
- Abstract: structured format (Background / Methods / Results / Limitations / Conclusions) is **JAD convention**, not a hard rule. The official spec is unstructured ≤250 words. **Drafting decision unchanged** — keep structured because every JAD paper uses it.
- Keywords: official count is **1–7** (not "3–6").
- Introduction word limit: no per-section cap; falls under the 5,000-word main-text budget. The 1200–1500 internal target is reasonable.

---

## Length & format limits

| Item | Limit |
|---|---|
| Main text | ≤ **5,000 words** (excluding references) |
| Figures + tables, combined | ≤ **6** |
| Abstract | ≤ **250 words** (concise & factual: purpose, principal results, major conclusions) |
| Highlights | **3–5 bullets**, ≤ **85 characters each** (incl. spaces) |
| Manuscript file format | `.docx` or `.tex` (PDF NOT acceptable as source) |
| Review process | **Single anonymized** (single-blind) |

## Reference style (CRITICAL CORRECTION)

- **Harvard author–year**, NOT Vancouver numbered.
- In-text: `(Author, 2013)` or `(Devoret and Schoelkopf, 2013; Xu, 2013)`.
- Bibliography: lastname + initials, year, title, container, volume, pages.
- Zotero CSL available: `journal-of-affective-disorders.csl`.
- ⚠️ My earlier `01_FrontMatter.md` used numbered `[1]` placeholders — **must be regenerated** with Harvard.

## AI / LLM disclosure (mandatory) — v2 wording

New section titled "**Declaration of generative AI and AI-assisted technologies in the writing process**" (← title changed Sep 2025), placed **immediately before References**, using EXACTLY this template:

> "During the preparation of this work the author(s) used [NAME OF TOOL / SERVICE] in order to [REASON]. After using this tool/service, the author(s) reviewed and edited the content as needed and take(s) full responsibility for the content of the publication." (← final phrase changed Sep 2025)

**Must document**: tool name (e.g. "Claude Opus 4"), purpose ("to improve language clarity"), extent of human oversight.
**Other rules**: AI cannot be author/co-author; AI-generated images not permitted (except as documented methodology); pure grammar/spell-check needs no disclosure; reviewer use of AI is forbidden (confidentiality).

## Highlights spec (Elsevier-wide)

- 3 to 5 bullets.
- ≤ 85 characters/bullet incl. spaces.
- Avoid jargon, acronyms, abbreviations.
- "Elevator pitch" for SEO discoverability.
- Submit as separate Word doc with "Highlights" file type at final-files stage.

## Items NOT fully extracted from the live guide (need second pass at Phase 6)

- Exact ethics statement wording (assume standard "approved by [IRB] under [#]; informed consent obtained" suffices).
- Exact data availability statement options (assume Elsevier four standard options: deposited / available on request / not applicable / contained in supplementary).
- Cover letter explicit requirements (treat as: novelty, fit, no concurrent submission, suggested reviewers).

## Sources

- [JAD Guide for Authors (Elsevier ScienceDirect)](https://www.sciencedirect.com/journal/journal-of-affective-disorders/publish/guide-for-authors)
- [Elsevier Highlights guidance](https://www.elsevier.com/researcher/author/tools-and-resources/highlights)
- [Journal of Affective Disorders citation style — Paperpile](https://paperpile.com/s/journal-of-affective-disorders-citation-style/)
- [JAD Zotero CSL — zotero.org](https://www.zotero.org/styles/journal-of-affective-disorders)
