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

## Supervisor context
Advisor: An Li (安莉), Tianjin University. See `supervisor_briefing.md` for current state.
