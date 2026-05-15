# =============================================================================
# sensitivity_lagged_mediation.R
#
# Sensitivity analysis #1 — Prompt-level autoregressive control on SI
# Sensitivity analysis #2 — Lagged mediation (stress_t-1 -> mediator_t -> SI_t+1)
# Sensitivity analysis #3 — ROPE-based decision for the C3-C2 indirect-effect
#                            null on the entrapment pathway
#
# Purpose: defend the within-person cascade against Ammerman 2025 (JPCS)
#          temporal-precedence critique, and provide rigorous null support
#          for the C3-C2 dissociation finding (manuscript main line).
#
# Author: Junlin Pu (with Claude Code assistance)
# Date:   2026-05-14
# =============================================================================

suppressPackageStartupMessages({
  library(tidyverse)
  library(brms)
  library(posterior)
  library(bayestestR)
  library(tidybayes)
})

# Choose backend: cmdstanr is faster on Windows once configured
USE_CMDSTANR <- requireNamespace("cmdstanr", quietly = TRUE)
if (USE_CMDSTANR) {
  options(brms.backend = "cmdstanr")
}
options(mc.cores = 4)

# ----- 1. Load data --------------------------------------------------------
DATA_LONG   <- "D:/R/research/study1_ema391_analysis_ready_long.csv"
DATA_SCALES <- "D:/R/research/all_scales_v5_FINAL.csv"
OUT_DIR     <- "D:/心理学/【0428小论文】/code/sensitivity_out"
dir.create(OUT_DIR, showWarnings = FALSE, recursive = TRUE)

ema    <- read_csv(DATA_LONG,   show_col_types = FALSE)
scales <- read_csv(DATA_SCALES, show_col_types = FALSE)

ema    <- ema    %>% mutate(pid = as.numeric(participant_id))
# scales already has `pid`; recode dominant_class3 1/2/3 → C1/C2/C3
scales <- scales %>%
  mutate(subtype = factor(paste0("C", dominant_class3),
                          levels = c("C1", "C2", "C3")))

df <- ema %>%
  left_join(scales %>% select(pid, subtype), by = "pid") %>%
  filter(!is.na(pid), !is.na(subtype))

cat(sprintf("Loaded %d prompts × %d participants × %d subtypes\n",
            nrow(df), n_distinct(df$pid), n_distinct(df$subtype)))

# ----- 2. Create mediator lag1 variables -----------------------------------
# Lag within (pid × wave) to avoid cross-wave contamination
df <- df %>%
  arrange(pid, wave, day_in_wave, planned_hour_filled) %>%
  group_by(pid, wave) %>%
  mutate(
    entrap_mean_lag1 = lag(entrap_mean),
    burden_mean_lag1 = lag(burden_mean),
    belong_mean_lag1 = lag(belong_mean),
    si_mean_lag1     = lag(si_mean)
  ) %>%
  ungroup()

# ----- 3. Within-person centering ------------------------------------------
center_wp <- function(d, vars) {
  for (v in vars) {
    pm <- d %>% group_by(pid) %>% summarise(pm = mean(.data[[v]], na.rm = TRUE), .groups = "drop")
    d  <- d %>% left_join(pm, by = "pid") %>%
      mutate(!!paste0(v, "_pm") := pm,
             !!paste0(v, "_wp") := .data[[v]] - pm) %>%
      select(-pm)
  }
  d
}

df <- center_wp(df, c(
  "stress_sum_intensity", "entrap_mean", "burden_mean", "belong_mean", "si_mean",
  "entrap_mean_lag1", "burden_mean_lag1", "belong_mean_lag1", "si_mean_lag1"
))

# Rename for readability
df <- df %>%
  rename(
    stress_wp        = stress_sum_intensity_wp,
    stress_pm        = stress_sum_intensity_pm,
    entrap_wp        = entrap_mean_wp,        entrap_pm = entrap_mean_pm,
    burden_wp        = burden_mean_wp,        burden_pm = burden_mean_pm,
    belong_wp        = belong_mean_wp,        belong_pm = belong_mean_pm,
    si_wp            = si_mean_wp,            si_pm     = si_mean_pm,
    entrap_lag1_wp   = entrap_mean_lag1_wp,
    burden_lag1_wp   = burden_mean_lag1_wp,
    belong_lag1_wp   = belong_mean_lag1_wp,
    si_lag1_wp       = si_mean_lag1_wp
  )

# ----- 4. brms settings (reduced for sensitivity) --------------------------
BRM_ITER    <- 2000
BRM_WARMUP  <- 500
BRM_CHAINS  <- 4
BRM_SEED    <- 20260514
BRM_CONTROL <- list(adapt_delta = 0.95, max_treedepth = 12)

# Wide priors but informative for stability
PRIORS_AR  <- c(
  prior(normal(0, 1), class = "b"),
  prior(normal(0, 1), class = "sd")
)

# ----- 5. Model A: AR(1)-controlled H1 overall mediation -------------------
# Outcome model adds si_lag1_wp to control for prompt-to-prompt SI persistence.
# Mediator models add own lag1 to control for mediator autocorrelation.
cat("\n=== Model A: AR(1)-controlled H1 mediation ===\n")

df_A <- df %>% drop_na(stress_wp, entrap_wp, burden_wp, belong_wp,
                        si_mean, si_lag1_wp,
                        entrap_lag1_wp, burden_lag1_wp, belong_lag1_wp)
cat(sprintf("Model A analytic prompts: %d\n", nrow(df_A)))

m_entrap_A <- bf(entrap_wp ~ stress_wp + stress_pm + entrap_lag1_wp + (1 + stress_wp | p | pid))
m_burden_A <- bf(burden_wp ~ stress_wp + stress_pm + burden_lag1_wp + (1 + stress_wp | p | pid))
m_belong_A <- bf(belong_wp ~ stress_wp + stress_pm + belong_lag1_wp + (1 + stress_wp | p | pid))
m_si_A     <- bf(si_mean ~ stress_wp + stress_pm +
                          entrap_wp + burden_wp + belong_wp +
                          si_lag1_wp +
                          (1 + stress_wp + entrap_wp + burden_wp + belong_wp | p | pid))

fit_A <- brm(
  m_entrap_A + m_burden_A + m_belong_A + m_si_A + set_rescor(FALSE),
  data    = df_A,
  iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
  seed    = BRM_SEED, control = BRM_CONTROL,
  file    = file.path(OUT_DIR, "fit_modelA_AR1_overall")
)

saveRDS(fit_A, file.path(OUT_DIR, "fit_modelA_AR1_overall.rds"))

# Extract a-, b-, and indirect-effect posteriors for Model A
draws_A <- as_draws_df(fit_A)
indirect_A <- tibble(
  entrap_indirect = draws_A$b_entrapwp_stress_wp * draws_A$b_simean_entrap_wp,
  burden_indirect = draws_A$b_burdenwp_stress_wp * draws_A$b_simean_burden_wp,
  belong_indirect = draws_A$b_belongwp_stress_wp * draws_A$b_simean_belong_wp
)

summarise_indirect <- function(x, label) {
  q <- quantile(x, c(0.025, 0.5, 0.975))
  pd <- mean(x > 0); pd <- max(pd, 1 - pd)
  tibble(pathway = label,
         median  = q[2], lo = q[1], hi = q[3], pd = pd)
}

summary_A <- bind_rows(
  summarise_indirect(indirect_A$entrap_indirect, "Stress → Entrapment → SI"),
  summarise_indirect(indirect_A$burden_indirect, "Stress → Burdensomeness → SI"),
  summarise_indirect(indirect_A$belong_indirect, "Stress → Belongingness → SI")
)

write_csv(summary_A,
          file.path(OUT_DIR, "summary_modelA_AR1_overall_indirect.csv"))
cat("\n--- Model A indirect effects (AR1-controlled) ---\n")
print(summary_A)

# ----- 6. Model B: Lagged mediation (stress_t-1 -> mediator_t -> SI_t+1) ---
# Best causal-precedence sensitivity. Requires further lagging on the SI side.
cat("\n=== Model B: Lagged mediation ===\n")

df_B <- df %>%
  arrange(pid, wave, day_in_wave, planned_hour_filled) %>%
  group_by(pid, wave) %>%
  mutate(
    si_lead1 = lead(si_mean),
    entrap_wp_lag1 = entrap_lag1_wp,
    burden_wp_lag1 = burden_lag1_wp,
    belong_wp_lag1 = belong_lag1_wp
  ) %>%
  ungroup() %>%
  drop_na(stress_sum_wp_lag1, entrap_wp, burden_wp, belong_wp,
          si_lead1, si_lag1_wp)
cat(sprintf("Model B analytic prompts: %d\n", nrow(df_B)))

m_entrap_B <- bf(entrap_wp ~ stress_sum_wp_lag1 + stress_pm +
                            entrap_lag1_wp + (1 + stress_sum_wp_lag1 | p | pid))
m_burden_B <- bf(burden_wp ~ stress_sum_wp_lag1 + stress_pm +
                            burden_lag1_wp + (1 + stress_sum_wp_lag1 | p | pid))
m_belong_B <- bf(belong_wp ~ stress_sum_wp_lag1 + stress_pm +
                            belong_lag1_wp + (1 + stress_sum_wp_lag1 | p | pid))
m_si_B     <- bf(si_lead1 ~ stress_sum_wp_lag1 + stress_pm +
                            entrap_wp + burden_wp + belong_wp +
                            si_lag1_wp +
                            (1 + stress_sum_wp_lag1 + entrap_wp + burden_wp + belong_wp | p | pid))

fit_B <- brm(
  m_entrap_B + m_burden_B + m_belong_B + m_si_B + set_rescor(FALSE),
  data    = df_B,
  iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
  seed    = BRM_SEED, control = BRM_CONTROL,
  file    = file.path(OUT_DIR, "fit_modelB_lagged_overall")
)

saveRDS(fit_B, file.path(OUT_DIR, "fit_modelB_lagged_overall.rds"))

draws_B <- as_draws_df(fit_B)
indirect_B <- tibble(
  entrap_indirect = draws_B$b_entrapwp_stress_sum_wp_lag1 *
                    draws_B$b_silead1_entrap_wp,
  burden_indirect = draws_B$b_burdenwp_stress_sum_wp_lag1 *
                    draws_B$b_silead1_burden_wp,
  belong_indirect = draws_B$b_belongwp_stress_sum_wp_lag1 *
                    draws_B$b_silead1_belong_wp
)

summary_B <- bind_rows(
  summarise_indirect(indirect_B$entrap_indirect, "Stress(t-1) → Entrapment(t) → SI(t+1)"),
  summarise_indirect(indirect_B$burden_indirect, "Stress(t-1) → Burdensomeness(t) → SI(t+1)"),
  summarise_indirect(indirect_B$belong_indirect, "Stress(t-1) → Belongingness(t) → SI(t+1)")
)

write_csv(summary_B,
          file.path(OUT_DIR, "summary_modelB_lagged_overall_indirect.csv"))
cat("\n--- Model B indirect effects (lagged) ---\n")
print(summary_B)

# ----- 7. Model C: Subtype × AR(1) mediation for C3-C2 ROPE ----------------
# Re-estimate the H3 subtype-stratified entrapment cascade with AR(1) control,
# then compute ROPE-based decision and 95%/89% HDIs on the C3-C2 contrast.
cat("\n=== Model C: Subtype-stratified entrapment cascade (AR1-controlled) ===\n")

df_C <- df_A   # subtype factor (C1/C2/C3) already attached via join in section 1
cat(sprintf("Model C participants by subtype:\n"))
print(df_C %>% distinct(pid, subtype) %>% count(subtype))

m_entrap_C <- bf(entrap_wp ~ 0 + subtype + stress_wp:subtype + stress_pm +
                              entrap_lag1_wp +
                              (1 + stress_wp | p | pid))
m_si_C     <- bf(si_mean ~ 0 + subtype + stress_wp:subtype + entrap_wp:subtype +
                            stress_pm + si_lag1_wp +
                            (1 + stress_wp + entrap_wp | p | pid))

fit_C <- brm(
  m_entrap_C + m_si_C + set_rescor(FALSE),
  data    = df_C,
  iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
  seed    = BRM_SEED, control = BRM_CONTROL,
  file    = file.path(OUT_DIR, "fit_modelC_subtype_AR1")
)

saveRDS(fit_C, file.path(OUT_DIR, "fit_modelC_subtype_AR1.rds"))

draws_C <- as_draws_df(fit_C)

# Indirect by subtype
ind_C1 <- draws_C[["b_entrapwp_subtypeC1:stress_wp"]] *
          draws_C[["b_simean_subtypeC1:entrap_wp"]]
ind_C2 <- draws_C[["b_entrapwp_subtypeC2:stress_wp"]] *
          draws_C[["b_simean_subtypeC2:entrap_wp"]]
ind_C3 <- draws_C[["b_entrapwp_subtypeC3:stress_wp"]] *
          draws_C[["b_simean_subtypeC3:entrap_wp"]]

contrast_C3_C2 <- ind_C3 - ind_C2

# ROPE definition: ±0.5 × SD of overall entrapment indirect from Model A
# (a defensible "negligibly small" cutoff)
rope_sd  <- sd(indirect_A$entrap_indirect)
rope_lo  <- -0.5 * rope_sd
rope_hi  <-  0.5 * rope_sd

rope_pct <- mean(contrast_C3_C2 > rope_lo & contrast_C3_C2 < rope_hi)

hdi89 <- bayestestR::hdi(contrast_C3_C2, ci = 0.89)
hdi95 <- bayestestR::hdi(contrast_C3_C2, ci = 0.95)
pd_C3_C2 <- max(mean(contrast_C3_C2 > 0), mean(contrast_C3_C2 < 0))

cat(sprintf("\nC3-C2 entrapment indirect contrast:\n  median = %.4f\n  89%% HDI = [%.4f, %.4f]\n  95%% HDI = [%.4f, %.4f]\n  PD = %.3f\n  ROPE = [%.4f, %.4f]\n  P(contrast in ROPE) = %.3f\n",
            median(contrast_C3_C2),
            hdi89$CI_low, hdi89$CI_high,
            hdi95$CI_low, hdi95$CI_high,
            pd_C3_C2,
            rope_lo, rope_hi, rope_pct))

summary_C <- tibble(
  quantity     = c("ind_C1", "ind_C2", "ind_C3", "C3 - C2 contrast"),
  median       = c(median(ind_C1), median(ind_C2), median(ind_C3),
                   median(contrast_C3_C2)),
  q025         = c(quantile(ind_C1, .025), quantile(ind_C2, .025),
                   quantile(ind_C3, .025), quantile(contrast_C3_C2, .025)),
  q975         = c(quantile(ind_C1, .975), quantile(ind_C2, .975),
                   quantile(ind_C3, .975), quantile(contrast_C3_C2, .975)),
  pd           = c(NA, NA, NA, pd_C3_C2),
  p_in_ROPE    = c(NA, NA, NA, rope_pct)
)
write_csv(summary_C,
          file.path(OUT_DIR, "summary_modelC_subtype_AR1_indirect.csv"))
cat("\n--- Model C subtype indirect summary ---\n")
print(summary_C)

# ----- 8. Convergence diagnostics ------------------------------------------
write_csv(
  tibble(model = c("A","B","C"),
         max_rhat = c(max(rhat(fit_A), na.rm = TRUE),
                      max(rhat(fit_B), na.rm = TRUE),
                      max(rhat(fit_C), na.rm = TRUE)),
         min_ess_bulk = c(min(neff_ratio(fit_A), na.rm = TRUE),
                          min(neff_ratio(fit_B), na.rm = TRUE),
                          min(neff_ratio(fit_C), na.rm = TRUE))),
  file.path(OUT_DIR, "convergence_diagnostics.csv")
)

cat("\n\nAll sensitivity models complete. Outputs in:\n")
cat(OUT_DIR, "\n")
