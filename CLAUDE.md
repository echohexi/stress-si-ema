# Project: Stress→SI Cascade EMA Paper (JAD submission)

Pu Junlin's psychology paper — 391 college students, 4-wave EMA, within-person stress→suicidal ideation cascade, brms Bayesian multilevel models.

## Network resilience rules (because user's connection drops with ECONNRESET)

Apply these **without being asked**, on every relevant action:

### Before any long-running analysis (brms, PyMC, simulation, large data ETL)
1. **Commit pending changes first** if this is a git repo (`git status` → if dirty, ask user whether to commit before proceeding).
2. **Cache model output to disk.** For brms always pass `file = "models/<name>.rds"` so re-running skips MCMC. For PyMC use `arviz.to_netcdf()` immediately after sampling. For Python scripts producing large objects, `pickle.dump` or `joblib.dump` at every checkpoint.
3. **Make scripts idempotent.** Re-running a half-finished pipeline must not redo expensive steps that already produced output files. Check `if file.exists()` / `if (file.exists())` before recomputing.
4. **Print progress to stdout frequently** so the user (and the agent on reconnect) can see exactly where a run stopped.

### Long bash commands
- Anything expected to take > 1 minute → run with `run_in_background: true`. Reconnecting after a drop can then resume by reading the output file.
- Save logs explicitly: `... 2>&1 | tee logs/<step>_$(date +%Y%m%d_%H%M%S).log`.

### Conversation hygiene
- Use TodoWrite for any task > 3 steps so progress survives disconnects.
- Before starting a new long sub-task, briefly state the rollback / resume point in plain text — so if the session dies, the next session can pick up from the message history.
- After writing files, commit small focused changes rather than batching — small commits are easier to recover from than uncommitted work.

### What NOT to do
- Don't run `Rscript brms_main_analysis.R` from scratch without checking `models/*.rds` cache first.
- Don't keep large intermediate objects only in conversation context.
- Don't start a 10-minute job in foreground when background + `tee` is available.
- **Never let cmdstanr write CSVs to Windows %TEMP%.** Confirmed loss on 2026-05-15: after 13 h of successful sampling on `sensitivity_lagged_8000iter.R`, Windows Storage Sense cleaned `C:\Users\…\Temp\Rtmp*` before brms could read them, and all samples were lost (`read_cmdstan_csv` fread error, execution halted, zero output). **Every long brms+cmdstanr script must set `Sys.setenv(TMPDIR = "D:/心理学/【0428小论文】/code/_cmdstan_csv")` (or equivalent project-local path) BEFORE loading brms/cmdstanr.**

### Chunked write rule (avoid socket close on large outputs)
- Large single Write/Edit calls (> ~1500 words of new text in one tool call) tend to trigger `API Error: The socket connection was closed unexpectedly`.
- **Always split long manuscript-style outputs into chunks of ≤ ~800 words per Write/Edit call.**
- Use the workflow: Write minimal skeleton first, then Edit incrementally section-by-section, each Edit appending one logical block.
- After every chunk, the file on disk is a valid checkpoint — if the socket drops, the next session resumes from the last written chunk, not from zero.

## Project specifics

- Data: `all_scales_v5_FINAL.csv` (391 subjects × multi-wave EMA)
- Preregistration: `preregistration_final.pdf` (7 hypotheses)
- Main R script: `code/brms_main_analysis.R`
- Figure generation: `code/generate_study3_main_figures_matplotlib.py`
- Target journal: JAD (Journal of Affective Disorders), 一区
- Manuscript draft: `Risk and Resource Axes Jointly Shape...docx`
- Methods/Results in JAD style: `Methods_JAD_Style.md`, `Results_JAD_Style.md`

## Dual-track workflow: Claude.ai × Claude Code

**Why:** User's network is unstable; long single-response generation in Claude Code triggers `API Error: socket closed unexpectedly`. Claude.ai's web streaming protocol auto-reconnects and is robust to this. Split work accordingly.

### Routing rule (the only one to remember)
> **Does the task need to touch anything besides keyboard text?**
> - Touches files / runs commands / git ops → **Claude Code (here)**
> - Pure text in, pure text out → **Claude.ai**

### Concretely

| Task | Where | Reason |
|---|---|---|
| Drafting Introduction / Discussion long prose | Claude.ai | Single 2000+ word output, no file IO needed |
| Cover Letter, Response to Reviewers | Claude.ai | Polished prose, sensitive to socket drops |
| Reading 67 article PDFs for citation hunting | Claude.ai (Projects upload) | Robust file ingest vs. local Read |
| Web search for recent literature | Claude.ai | Built-in search tool |
| Locking numbers (Phase 1 §9, §10) | Claude Code | Needs xlsx parsing, Edit, git commit |
| Fixing wrong numbers in `Results_JAD_Style.md` etc. | Claude Code | Needs git diff audit + chunked Edit |
| brms / R / Python script writing & running | Claude Code | Needs Bash execution |
| Figure generation & debugging | Claude Code | Needs stderr + PNG inspection |
| Pure narrative brainstorming (C2/C3 framing etc.) | Claude.ai | No files touched |
| Landing brainstormed text into Manuscript_JAD/ | Claude Code | I Write/Edit, you paste the text |

### Handoff protocol

**Claude.ai → Claude Code (text inbound):**
- User pastes Claude.ai output into Claude Code chat.
- Claude Code Writes to `Manuscript_JAD/Phase2[a-d]_<Section>_draft.md`.
- Claude Code immediately `git add` + commit so the draft is checkpointed.

**Claude Code → Claude.ai (context outbound):**
- Claude Code packages "feeding bundles" (locked numbers + narrative spine + key refs) as a single markdown.
- User copies the markdown into Claude.ai's chat or Claude.ai Project knowledge.
- Naming: `Manuscript_JAD/_feed_<topic>.md` (underscore prefix marks "scratch/feed" files).

### Naming convention for manuscript drafts

```
Manuscript_JAD/
├── Phase0_JAD_profile.md             (existing — journal target)
├── Phase1_locked_numbers.md          (existing — number-of-truth)
├── Phase1d_C2_narrative_strategy.md  (existing — narrative spine)
├── Phase2a_Introduction_draft.md     (Claude.ai output lands here)
├── Phase2b_Methods_draft.md          (Claude.ai output lands here)
├── Phase2c_Results_draft.md          (Claude.ai output lands here)
├── Phase2d_Discussion_draft.md       (Claude.ai output lands here)
├── Phase3_full_assembled.md          (Claude Code stitches all Phase 2 drafts)
└── _feed_<topic>.md                  (Claude Code → Claude.ai context bundles)
```

### What Claude Code should proactively do
- When user asks for "write a 1000+ word section" → suggest moving to Claude.ai, offer to prepare a feeding bundle instead.
- When user pastes Claude.ai output → Write to the correct `Phase2*` file + git commit immediately.
- After each Claude.ai-sourced commit, briefly state: "Bundle committed at `<file>` — if Claude.ai session drops, this version survives."

## Supervisor context
Advisor: An Li (安莉), Tianjin University. See `supervisor_briefing.md` for current state.
