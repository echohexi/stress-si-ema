install.packages("rstan", dependencies = TRUE, repos = "https://cloud.r-project.org")
# 加载 rstan
library(rstan)

# 启用并行计算
options(mc.cores = parallel::detectCores())

# 启用编译结果缓存以避免重复编译
rstan_options(auto_write = TRUE)

# 验证 rstan 版本
packageVersion("rstan")
# 一个最小的 Stan 模型测试
test_code <- "
data {
  int<lower=0> N;
  vector[N] y;
}
parameters {
  real mu;
  real<lower=0> sigma;
}
model {
  y ~ normal(mu, sigma);
}
"

test_data <- list(N = 100, y = rnorm(100))

# 编译并采样
test_fit <- stan(model_code = test_code, data = test_data,
                 chains = 2, iter = 500, refresh = 0)

# 查看摘要
print(test_fit, pars = c("mu", "sigma"))

install.packages(c("brms", "tidyverse", "bayesplot", "tidybayes",
                   "posterior", "loo", "emmeans", "broom.mixed"),
                 dependencies = TRUE, repos = "https://cloud.r-project.org")

library(brms)
options(brms.backend = "rstan", mc.cores = parallel::detectCores())

library(brms)
options(brms.backend = "rstan", mc.cores = parallel::detectCores())

test_data <- data.frame(y = rnorm(100), x = rnorm(100))
test_fit <- brm(y ~ x, data = test_data, chains = 2, iter = 500,
                refresh = 100)
summary(test_fit)