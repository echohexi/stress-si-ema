# =============================================================================
# brms_main_analysis.R
# 论文: Risk and Resource Axes Jointly Shape the Within-Person Stress-to-SI
#       Cascade in College Students (4-wave EMA, n = 391)
#
# 主分析: 多层贝叶斯并行多重中介 + 风险-资源双轴 moderation + 三亚型对比
# 对应 OSF 预注册 H1-H7
#
# 作者: 蒲俊霖
# 日期: 2026-04-27 (locked-in version)
# 运行环境: R >= 4.3, brms >= 2.20, cmdstanr 后端推荐
# 预计运行时间: 全脚本 6-12 小时(取决于硬件,Apple M2 ~ 6 小时)
# =============================================================================

# ---- 1. 环境与依赖 ----------------------------------------------------------
suppressPackageStartupMessages({
  library(tidyverse)        # data wrangling
  library(brms)             # bayesian multilevel
  library(bayesplot)        # posterior plots
  library(tidybayes)        # tidy posterior extraction
  library(posterior)        # posterior summaries
  library(loo)              # model comparison
  library(emmeans)          # marginal effects
  library(broom.mixed)      # tidy summaries
})

# 推荐用 cmdstanr 后端(更快,需要先安装 cmdstanr)
# options(brms.backend = "cmdstanr", mc.cores = parallel::detectCores())
options(mc.cores = 4)

# 全局 brms 设置
BRM_ITER    <- 4000
BRM_WARMUP  <- 1000
BRM_CHAINS  <- 4
BRM_SEED    <- 20260427
BRM_CONTROL <- list(adapt_delta = 0.95, max_treedepth = 12)

# ---- 2. 数据加载与预处理 ----------------------------------------------------
DATA_DIR <- "/path/to/data"   # 改成你机器上的路径

# Person-level 量表(已修正反向计分,已并入 3 类亚型与 CTQ 五维度)
scales <- read_csv(file.path(DATA_DIR, "all_scales_v5_FINAL.csv"))

# EMA 长格式
ema    <- read_csv(file.path(DATA_DIR, "study1_ema391_analysis_ready_long.csv"))

# 合并
ema <- ema %>% mutate(pid = as.numeric(participant_id))
scales <- scales %>% rename(pid = raw_id_num)

df <- ema %>%
  left_join(scales, by = "pid") %>%
  filter(!is.na(pid), !is.na(CTQ_total_master), !is.na(dominant_class3))

cat(sprintf("分析样本: %d prompts × %d 被试\n", nrow(df), n_distinct(df$pid)))

# ---- 3. Within-person centering --------------------------------------------
# 关键:对每个 Level-1 变量同时计算 person-mean 和 person-mean-deviated,
# 这样可以无歧义地分离 between- 与 within-person 效应 (Curran & Bauer, 2011)
center_wp <- function(df, vars) {
  for (v in vars) {
    pm <- df %>% group_by(pid) %>% summarise(pm = mean(.data[[v]], na.rm = TRUE))
    df <- df %>%
      left_join(pm, by = "pid") %>%
      mutate(!!paste0(v, "_pm") := pm,
             !!paste0(v, "_wp") := .data[[v]] - pm) %>%
      select(-pm)
  }
  df
}

df <- center_wp(df, c("stress_sum_intensity", "entrap_mean", "burden_mean",
                       "belong_mean", "lonely_mean", "si_mean"))

# 重命名简化(与 brms 公式更易读)
df <- df %>%
  rename(stress_wp  = stress_sum_intensity_wp,
         stress_pm  = stress_sum_intensity_pm,
         entrap_wp  = entrap_mean_wp, entrap_pm = entrap_mean_pm,
         burden_wp  = burden_mean_wp, burden_pm = burden_mean_pm,
         belong_wp  = belong_mean_wp, belong_pm = belong_mean_pm,
         lonely_wp  = lonely_mean_wp, lonely_pm = lonely_mean_pm,
         si_wp      = si_mean_wp,     si_pm     = si_mean_pm)

# Level-2 z-score 化
z <- function(x) (x - mean(x, na.rm=TRUE)) / sd(x, na.rm=TRUE)
df <- df %>% mutate(
  CTQ_total_z = z(CTQ_total_master),
  CTQ_EA_z    = z(CTQ_EA_master),
  CTQ_PA_z    = z(CTQ_PA_master),
  CTQ_SA_z    = z(CTQ_SA_master),
  CTQ_EN_z    = z(CTQ_EN_master),
  CTQ_PN_z    = z(CTQ_PN_master),
  BRS_z       = z(BRS_total_T3),
  Connect_z   = z(Connect_total_T2),
  LPFS_z      = z(LPFS_total_T3),
  ERQ_reapp_z = z(ERQ_reapp_T3),
  CERQ_adapt_z= z(CERQ_adaptive_T1),
  CERQ_mal_z  = z(CERQ_maladaptive_T1),
  class3      = factor(dominant_class3, levels = c(1,2,3),
                       labels = c("C1_lowstable","C2_lowmod","C3_high"))
)

# SI 作为 ordinal(主模型);备份 Gaussian 版本(敏感性分析)
df <- df %>% mutate(si_ord = ordered(round(pmin(pmax(si_mean, 1), 5))))

# 保存预处理后数据
saveRDS(df, file.path(DATA_DIR, "df_preprocessed.rds"))

# =============================================================================
# Model 1 — Parallel multi-mediation (H1, H2, H3)
# =============================================================================
cat("\n=== Model 1: Parallel multi-mediation ===\n")

# 三个 mediator 公式 + 一个 SI 公式
# 注意 (... | p | pid) 中的 'p' 标识符让 random effects 在四个公式间共享 cov 矩阵
bf_entrap <- bf(entrap_mean ~ stress_wp + stress_pm + 
                  (1 + stress_wp | p | pid))
bf_burden <- bf(burden_mean ~ stress_wp + stress_pm + 
                  (1 + stress_wp | p | pid))
bf_belong <- bf(belong_mean ~ stress_wp + stress_pm + 
                  (1 + stress_wp | p | pid))
bf_si     <- bf(si_ord ~ entrap_wp + burden_wp + belong_wp +
                          entrap_pm + burden_pm + belong_pm +
                          stress_wp + stress_pm +
                          (1 + entrap_wp + burden_wp + belong_wp + stress_wp | p | pid))

# Priors
priors_M1 <- c(
  prior(normal(0, 1), class = "b"),                           # 系数
  prior(normal(0, 1), class = "Intercept", resp = "entrapmean"),
  prior(normal(0, 1), class = "Intercept", resp = "burdenmean"),
  prior(normal(0, 1), class = "Intercept", resp = "belongmean"),
  prior(half_normal(0, 1), class = "sd"),                     # random effect SDs
  prior(lkj(2), class = "L")                                  # correlation matrix
)

m1 <- brm(
  bf_entrap + bf_burden + bf_belong + bf_si + set_rescor(FALSE),
  data    = df,
  family  = list(gaussian(), gaussian(), gaussian(), cumulative("logit")),
  prior   = priors_M1,
  iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
  control = BRM_CONTROL,
  seed    = BRM_SEED,
  file    = file.path(DATA_DIR, "m1_parallel_mediation")
)
print(summary(m1))

# H1, H2: 计算 within-person indirect 效应 a×b
# 提取 stress_wp 对每个 mediator 的系数(a), 每个 mediator_wp 对 si 的系数(b)
post_m1 <- as_draws_df(m1)
indirect_entrap <- post_m1$b_entrapmean_stress_wp * post_m1$b_si_entrap_wp
indirect_burden <- post_m1$b_burdenmean_stress_wp * post_m1$b_si_burden_wp
indirect_belong <- post_m1$b_belongmean_stress_wp * post_m1$b_si_belong_wp

cat("\n--- H1 indirect effects (95% CI) ---\n")
cat(sprintf("entrap a×b: median=%.4f, 95%% CI=[%.4f, %.4f]\n",
    median(indirect_entrap),
    quantile(indirect_entrap, 0.025), quantile(indirect_entrap, 0.975)))
cat(sprintf("burden a×b: median=%.4f, 95%% CI=[%.4f, %.4f]\n",
    median(indirect_burden),
    quantile(indirect_burden, 0.025), quantile(indirect_burden, 0.975)))
cat(sprintf("belong a×b: median=%.4f, 95%% CI=[%.4f, %.4f]\n",
    median(indirect_belong),
    quantile(indirect_belong, 0.025), quantile(indirect_belong, 0.975)))

# H2: posterior probability that entrap > burden, entrap > belong
cat(sprintf("\nH2: P(entrap a×b > burden a×b) = %.3f\n",
            mean(indirect_entrap > indirect_burden)))
cat(sprintf("    P(entrap a×b > belong a×b) = %.3f\n",
            mean(indirect_entrap > indirect_belong)))

# H3: random slope variance
# 检查 sd(stress_wp), sd(entrap_wp) 等是否 95% CI 远离 0(默认 brms 已经这样)
ranefs <- VarCorr(m1)
print(ranefs$pid$sd)

# =============================================================================
# Model 2 — CTQ × path × dimension moderation (H4)
# =============================================================================
cat("\n=== Model 2: CTQ path × dimension moderation ===\n")

dims <- c("EA","PA","SA","EN","PN","total")
mediators <- c("entrap","burden","belong","lonely")
results_M2 <- list()

for (dim in dims) {
  zvar <- if (dim == "total") "CTQ_total_z" else paste0("CTQ_", dim, "_z")
  
  for (med in mediators) {
    cat(sprintf("\n  CTQ-%s × %s\n", dim, med))
    med_wp <- paste0(med, "_wp")
    med_pm <- paste0(med, "_pm")
    
    # a-path moderation: stress_wp × CTQ_dim → mediator_wp
    f_a <- bf(reformulate(c(sprintf("stress_wp * %s", zvar), "stress_pm",
                             sprintf("(1 + stress_wp | pid)")),
                           response = paste0(med, "_mean")))
    
    m_a <- brm(f_a, data = df,
               prior   = c(prior(normal(0,1), class="b"),
                            prior(half_normal(0,1), class="sd")),
               iter    = 2000, warmup = 500, chains = 2,  # 单变量,可减半
               control = BRM_CONTROL, seed = BRM_SEED,
               file    = file.path(DATA_DIR, sprintf("m2_apath_%s_%s", dim, med)))
    
    # b-path moderation: mediator_wp × CTQ_dim → si_ord
    f_b <- bf(reformulate(c(sprintf("%s * %s", med_wp, zvar),
                             "stress_wp", "stress_pm", med_pm,
                             sprintf("(1 + %s | pid)", med_wp)),
                           response = "si_ord"))
    
    m_b <- brm(f_b, data = df, family = cumulative("logit"),
               prior   = c(prior(normal(0,1), class="b"),
                            prior(half_normal(0,1), class="sd")),
               iter    = 2000, warmup = 500, chains = 2,
               control = BRM_CONTROL, seed = BRM_SEED,
               file    = file.path(DATA_DIR, sprintf("m2_bpath_%s_%s", dim, med)))
    
    # 提取交互项的 PD
    int_a <- sprintf("b_stress_wp:%s", zvar)
    int_b <- sprintf("b_%s:%s", med_wp, zvar)
    
    pa <- as_draws_df(m_a)[[int_a]]
    pb <- as_draws_df(m_b)[[int_b]]
    
    pd_a <- max(mean(pa > 0), mean(pa < 0))
    pd_b <- max(mean(pb > 0), mean(pb < 0))
    
    results_M2[[paste(dim, med, sep="_")]] <- list(
      a_median = median(pa), a_pd = pd_a,
      b_median = median(pb), b_pd = pd_b
    )
    cat(sprintf("    a-path: median = %+.4f, PD = %.3f\n", median(pa), pd_a))
    cat(sprintf("    b-path: median = %+.4f, PD = %.3f\n", median(pb), pd_b))
  }
}

# 整理为 5×4 矩阵
df_M2 <- bind_rows(lapply(names(results_M2), function(k) {
  parts <- strsplit(k, "_")[[1]]
  tibble(dim = parts[1], mediator = parts[2],
         a_b = results_M2[[k]]$a_median, a_PD = results_M2[[k]]$a_pd,
         b_b = results_M2[[k]]$b_median, b_PD = results_M2[[k]]$b_pd)
}))
write_csv(df_M2, file.path(DATA_DIR, "M2_CTQ_5dim_results.csv"))

# H4 评估
n_b_strict <- sum(df_M2$b_PD >= .975 & df_M2$dim != "PA")  # PA 排除
cat(sprintf("\nH4a 评估: %d / 16 个非PA b-path interaction PD >= .975\n", n_b_strict))
cat("H4c 评估: PA 各路径中 b-path PD 应较低 (n.s. pattern)\n")
print(df_M2 %>% filter(dim == "PA"))

# =============================================================================
# Model 3 — Risk-Resource trait moderation (H5)
# =============================================================================
cat("\n=== Model 3: Risk-Resource dual-axis moderation ===\n")

# 包含 BRS, Connect, ERQ_reapp 三个 resource moderators(同时入模)
# 加入 LPFS_z 作为 risk control
bf_M3 <- bf(si_ord ~ entrap_wp * (BRS_z + Connect_z + ERQ_reapp_z + LPFS_z) +
                       stress_wp + stress_pm + entrap_pm + burden_wp + belong_wp +
                       (1 + entrap_wp | pid))

m3 <- brm(bf_M3, data = df, family = cumulative("logit"),
          prior   = c(prior(normal(0,1), class = "b"),
                       prior(half_normal(0,1), class = "sd")),
          iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
          control = BRM_CONTROL, seed = BRM_SEED,
          file    = file.path(DATA_DIR, "m3_dual_axis_moderation"))
print(summary(m3))

# H5 评估
post_m3 <- as_draws_df(m3)
for (mod in c("BRS_z","Connect_z","ERQ_reapp_z","LPFS_z")) {
  col <- paste0("b_entrap_wp:", mod)
  if (col %in% names(post_m3)) {
    v <- post_m3[[col]]
    pd <- max(mean(v > 0), mean(v < 0))
    cat(sprintf("entrap × %s: median = %+.4f, 95%% CI = [%+.4f, %+.4f], PD = %.3f\n",
                mod, median(v), quantile(v, 0.025), quantile(v, 0.975), pd))
  }
}

# =============================================================================
# Model 4 — Subtype-specific cascade (H6)
# =============================================================================
cat("\n=== Model 4: Subtype-specific cascade ===\n")

# 方法 A: subtype × stress_wp 交互项
bf_M4_a <- bf(entrap_mean ~ stress_wp * class3 + stress_pm +
                              (1 + stress_wp | pid))
bf_M4_b <- bf(si_ord ~ entrap_wp * class3 + stress_wp + stress_pm + entrap_pm +
                         (1 + entrap_wp | pid))

m4a <- brm(bf_M4_a, data = df,
           prior   = c(prior(normal(0,1), class="b"),
                        prior(half_normal(0,1), class="sd")),
           iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
           control = BRM_CONTROL, seed = BRM_SEED,
           file    = file.path(DATA_DIR, "m4a_subtype_apath"))

m4b <- brm(bf_M4_b, data = df, family = cumulative("logit"),
           prior   = c(prior(normal(0,1), class="b"),
                        prior(half_normal(0,1), class="sd")),
           iter    = BRM_ITER, warmup = BRM_WARMUP, chains = BRM_CHAINS,
           control = BRM_CONTROL, seed = BRM_SEED,
           file    = file.path(DATA_DIR, "m4b_subtype_bpath"))

print(summary(m4a))
print(summary(m4b))

# H6 monotonicity test
post_m4a <- as_draws_df(m4a)
post_m4b <- as_draws_df(m4b)

a_C1 <- post_m4a$b_stress_wp
a_C2 <- post_m4a$b_stress_wp + post_m4a$`b_stress_wp:class3C2_lowmod`
a_C3 <- post_m4a$b_stress_wp + post_m4a$`b_stress_wp:class3C3_high`

b_C1 <- post_m4b$b_entrap_wp
b_C2 <- post_m4b$b_entrap_wp + post_m4b$`b_entrap_wp:class3C2_lowmod`
b_C3 <- post_m4b$b_entrap_wp + post_m4b$`b_entrap_wp:class3C3_high`

# Indirect effects per subtype
ind_C1 <- a_C1 * b_C1
ind_C2 <- a_C2 * b_C2
ind_C3 <- a_C3 * b_C3

cat("\n--- H6 subtype indirect effects (medians + 95% CI) ---\n")
for (cls in c("C1","C2","C3")) {
  v <- get(paste0("ind_", cls))
  cat(sprintf("%s: median=%.4f, 95%% CI=[%.4f, %.4f]\n",
              cls, median(v), quantile(v, 0.025), quantile(v, 0.975)))
}

# Monotonicity: P(C1 < C2 < C3)
mono_prob <- mean(ind_C1 < ind_C2 & ind_C2 < ind_C3)
cat(sprintf("\nP(C1 < C2 < C3, monotonic) = %.3f\n", mono_prob))

# =============================================================================
# Model 5 — H7: Risk-resource axis differentiation across subtypes
# =============================================================================
cat("\n=== Model 5: H7 — Trait differentiation by subtype ===\n")

# Person-level 数据
person_df <- df %>% 
  group_by(pid, class3) %>%
  summarise(across(c(CTQ_EA_master, CTQ_EN_master, LPFS_total_T3,
                      BRS_total_T3, Connect_total_T2, PANSI_neg_T1),
                    ~ first(na.omit(.x))),
            .groups = "drop") %>%
  drop_na(class3)

trait_vars <- c("CTQ_EA_master","CTQ_EN_master","LPFS_total_T3",
                "BRS_total_T3","Connect_total_T2","PANSI_neg_T1")

bayes_anova_results <- list()
for (v in trait_vars) {
  cat(sprintf("\n  --- %s ---\n", v))
  f <- as.formula(paste(v, "~ class3"))
  m_anv <- brm(f, data = person_df,
               prior = c(prior(normal(0,5), class="b"),
                          prior(half_normal(0,5), class="sigma")),
               iter = 2000, chains = 2, seed = BRM_SEED,
               file = file.path(DATA_DIR, sprintf("m5_anova_%s", v)))
  print(summary(m_anv))
  bayes_anova_results[[v]] <- m_anv
}

# =============================================================================
# 6. 模型诊断与可视化
# =============================================================================
cat("\n=== Diagnostics & Visualization ===\n")

# Trace plots, posterior predictive checks (例 m1)
pdf(file.path(DATA_DIR, "diagnostics_m1.pdf"), width = 11, height = 8)
plot(m1)
pp_check(m1, resp = "siord", type = "bars") + ggtitle("PPC: SI ordinal")
dev.off()

# Forest plot of all key indirect effects
ind_summary <- tibble(
  effect = c("Entrap (overall)", "Burden (overall)", "Belong (overall)",
             "Indirect C1", "Indirect C2", "Indirect C3"),
  median = c(median(indirect_entrap), median(indirect_burden), median(indirect_belong),
             median(ind_C1), median(ind_C2), median(ind_C3)),
  lower  = c(quantile(indirect_entrap, .025), quantile(indirect_burden, .025),
             quantile(indirect_belong, .025),
             quantile(ind_C1, .025), quantile(ind_C2, .025), quantile(ind_C3, .025)),
  upper  = c(quantile(indirect_entrap, .975), quantile(indirect_burden, .975),
             quantile(indirect_belong, .975),
             quantile(ind_C1, .975), quantile(ind_C2, .975), quantile(ind_C3, .975))
)

p_forest <- ind_summary %>%
  ggplot(aes(x = median, y = effect)) +
  geom_pointrange(aes(xmin = lower, xmax = upper)) +
  geom_vline(xintercept = 0, linetype = "dashed", color = "gray") +
  labs(x = "Posterior median (95% CI) of indirect effect a×b",
       y = NULL,
       title = "Within-person indirect effects: overall and by subtype") +
  theme_minimal(base_size = 11)
ggsave(file.path(DATA_DIR, "forest_indirect_effects.pdf"), p_forest, width = 9, height = 5)

# 保存 final summary
saveRDS(list(M1 = m1, M3 = m3, M4a = m4a, M4b = m4b),
        file.path(DATA_DIR, "all_models.rds"))

cat("\n=== Analysis complete. ===\n")
cat(sprintf("All models, posteriors, and figures saved to:\n  %s\n", DATA_DIR))

# =============================================================================
# 7. (Optional) Exploratory analyses — non-confirmatory
# =============================================================================
# - Lagged within-person mediation
# - PA reverse-moderation mechanism via DES
# - Three-way interactions (CTQ × subtype × stress)
# 这些在主分析后单独跑,代码不在本文件中
