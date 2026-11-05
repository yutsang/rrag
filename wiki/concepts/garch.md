---
title: "GARCH Models"
full_name: "Generalized Autoregressive Conditional Heteroscedasticity (GARCH)"
type: concept
tags: [time-series, econometrics, garch, arch, volatility, risk-management, finance]
created: "2026-04-10"
updated: "2026-04-14"
source: "wiki/sources/courses/financial-time-series"
confidence: high
---

## 概述

廣義自迴歸條件異質變異數模型（Generalized Autoregressive Conditional Heteroscedasticity, GARCH）是金融時間序列中建模時變波動率的核心工具族，由 Engle（1982）的 ARCH 與 Bollerslev（1986）的 GARCH 推廣而來。GARCH(1,1) 的核心方程式 $\sigma_t^2 = \alpha_0 + \alpha_1 a_{t-1}^2 + \beta_1 \sigma_{t-1}^2$ 以三個參數捕捉金融回報的波動率聚集效應——持續性量度 $\alpha_1 + \beta_1$ 在每日股票數據中通常達 0.95–0.99，意味著波動率衝擊的半衰期長達數週。當 $\alpha_1 + \beta_1 = 1$ 時退化為 IGARCH，即 RiskMetrics EWMA 模型的理論基礎。非對稱模型變體解決了基礎 GARCH 的對稱性缺陷：EGARCH 在對數空間建模 $\ln(\sigma_t^2)$ 以同時捕捉槓桿效應與自動滿足正值約束；TGARCH/GJR 則以指示函數直接量化負衝擊相對於正衝擊的額外波動率影響 $\gamma_1$，係數 $\gamma_1 > 0$ 是股票市場「壞消息放大波動」這一實證規律的直接度量。GARCH-M 在均值方程中引入條件標準差 $c \cdot \sigma_t$，為理論上的風險-回報正相關關係提供計量框架，但實證中 $c$ 往往統計上不顯著，構成金融學的「風險-回報之謎」。在運籌學與風險管理的接口上，GARCH 的多步波動率預測 $\hat{\sigma}_{t+h}^2 = V_L + (\alpha_1+\beta_1)^{h-1}(\sigma_{t+1}^2 - V_L)$ 是計算在險價值（VaR）與期望缺口（Expected Shortfall）的標準輸入；[[behavioral-economics|行為經濟學]]的損失厭惡理論為槓桿效應提供心理學解釋；多元 GARCH（DCC、BEKK）則延伸至 [[portfolio-theory|投資組合理論]] 中的動態相關係數估計。MSBD5006 課程以 SBUX、S&P 500、PG 及 USD/EUR 四個資產的逐步建模示範，涵蓋了從 ARCH 效應檢驗（McLeod-Li 檢驗）到非對稱模型比較的完整工作流程。

## Motivation: Stylized Facts of Financial Returns

Empirical analysis of asset returns reveals patterns that standard [[arma-models|ARMA models]] cannot capture:

- **Volatility clustering**: Large price changes (positive or negative) tend to be followed by large changes, and small changes by small changes. Formally, returns may be uncorrelated ($\rho_l \approx 0$) while squared returns show significant autocorrelation ($\rho_l(r_t^2) > 0$). The Ljung-Box test applied to squared residuals — sometimes called the **McLeod-Li test** (1983) — is the standard diagnostic for the presence of ARCH effects.
- **Heavy tails (leptokurtosis)**: The unconditional distribution of returns has excess kurtosis well above the Gaussian value of 3. Typical daily equity kurtosis is 5-15, and intraday data often exceed 20.
- **Leverage effect**: Negative returns tend to increase future volatility more than positive returns of equal magnitude, empirically documented since Black (1976) and typically attributed to financial leverage or to changing risk premia.
- **Long-memory volatility**: Shocks to volatility decay slowly; simple GARCH captures this via $\alpha_1 + \beta_1$ close to 1.

These observations motivate models where the **conditional variance** $\sigma_t^2 = \text{Var}(r_t | \mathcal{F}_{t-1})$ varies over time, even though the unconditional variance may be constant. The framework separates the **conditional mean equation** (ARMA for $r_t$) from the **conditional variance equation** (GARCH for $\sigma_t^2$).

## ARCH Model

The **ARCH(m)** model (Engle, 1982) was the first formalization of time-varying conditional variance:

$$a_t = \sigma_t \varepsilon_t, \qquad \varepsilon_t \overset{\text{iid}}{\sim} N(0, 1)$$

$$\sigma_t^2 = \alpha_0 + \alpha_1 a_{t-1}^2 + \alpha_2 a_{t-2}^2 + \cdots + \alpha_m a_{t-m}^2$$

where $a_t = r_t - \mu_t$ is the mean-corrected return (the "shock" or "innovation"), $\alpha_0 > 0$, and $\alpha_i \geq 0$ for all $i$. The constraint $\sum_{i=1}^m \alpha_i < 1$ ensures covariance stationarity. Conditional on $\mathcal{F}_{t-1}$, $a_t$ is Gaussian with variance $\sigma_t^2$; unconditionally, $a_t$ has heavy tails even when $\varepsilon_t$ is Gaussian.

### Testing for ARCH Effects

Before fitting an ARCH/GARCH model, test whether ARCH effects are present:

1. **Ljung-Box on squared residuals**: $Q(m)$ computed from $\{\hat{a}_t^2\}$ of an ARMA fit. Significant $Q(m)$ on squares (but not levels) indicates volatility clustering.
2. **Engle's LM test**: Regress $\hat{a}_t^2$ on a constant and $m$ lags of itself; $T \cdot R^2 \sim \chi^2(m)$ under the null of no ARCH effect.

### Properties of ARCH(m)

- **Unconditional variance**: $\text{Var}(a_t) = \alpha_0 / (1 - \alpha_1 - \cdots - \alpha_m)$
- **Excess kurtosis**: Even with Gaussian $\varepsilon_t$, the unconditional distribution of $a_t$ has kurtosis > 3. For ARCH(1) with Gaussian innovations, kurtosis $= 3(1 - \alpha_1^2)/(1 - 3\alpha_1^2)$, defined only when $3\alpha_1^2 < 1$ (i.e., $\alpha_1 < 1/\sqrt{3} \approx 0.577$).
- **Weakness**: Capturing persistent volatility requires many lags ($m$ large), leading to many parameters and non-parsimonious fits.

## GARCH(1,1) Model

The **GARCH(p,q)** model (Bollerslev, 1986) addresses ARCH's parsimony problem by adding lagged conditional variances as regressors:

$$\sigma_t^2 = \alpha_0 + \sum_{i=1}^m \alpha_i a_{t-i}^2 + \sum_{j=1}^s \beta_j \sigma_{t-j}^2$$

The workhorse **GARCH(1,1)** is:

$$\boxed{\sigma_t^2 = \alpha_0 + \alpha_1 a_{t-1}^2 + \beta_1 \sigma_{t-1}^2}$$

with constraints $\alpha_0 > 0$, $\alpha_1 \geq 0$, $\beta_1 \geq 0$ to ensure $\sigma_t^2 > 0$ almost surely.

### Stationarity and Persistence

- **Covariance stationarity**: Requires $\alpha_1 + \beta_1 < 1$.
- **Unconditional variance**: $\sigma^2 = \alpha_0 / (1 - \alpha_1 - \beta_1)$.
- **Persistence**: The sum $\alpha_1 + \beta_1$ measures volatility persistence. Values close to 1 indicate that shocks to volatility decay slowly. Typical daily equity estimates are $\alpha_1 \in [0.05, 0.15]$ and $\beta_1 \in [0.80, 0.95]$, giving persistence $0.95-0.99$ — implying half-lives of volatility shocks of 10-70 days.
- When $\alpha_1 + \beta_1 = 1$, the model is an **Integrated GARCH (IGARCH)**, where volatility shocks have permanent effects on forecasts. In IGARCH the unconditional variance is undefined; forecasts follow $\sigma_{t+h}^2 = \sigma_{t+1}^2 + (h-1)\alpha_0$, linear in $h$.

### Interpretation as Weighted Average

GARCH(1,1) can be rewritten to reveal its structure as a weighted average:

$$\sigma_t^2 = (1 - \alpha_1 - \beta_1) V_L + \alpha_1 a_{t-1}^2 + \beta_1 \sigma_{t-1}^2$$

where $V_L = \alpha_0 / (1 - \alpha_1 - \beta_1)$ is the long-run variance. The conditional variance is a convex combination of the long-run mean variance, the most recent squared shock, and the previous variance forecast. Equivalently:

$$\sigma_t^2 = \alpha_0 + (\alpha_1 + \beta_1)\sigma_{t-1}^2 + \alpha_1(a_{t-1}^2 - \sigma_{t-1}^2)$$

which isolates the "surprise" component $a_{t-1}^2 - \sigma_{t-1}^2$. RiskMetrics' EWMA variance forecast is a restricted GARCH(1,1) with $\alpha_0 = 0$ and $\alpha_1 + \beta_1 = 1$ (typically $\beta_1 = 0.94$ for daily data).

### Multi-Step Volatility Forecast

The h-step-ahead GARCH(1,1) variance forecast is:

$$\hat{\sigma}_{t+h}^2 = V_L + (\alpha_1 + \beta_1)^{h-1} (\sigma_{t+1}^2 - V_L)$$

which decays geometrically toward the long-run variance at rate $\alpha_1 + \beta_1$.

### Advantages and Weaknesses

**Advantages**:

- **Parsimonious**: Three parameters capture rich volatility dynamics.
- Generates heavy-tailed unconditional distributions even with Gaussian innovations.
- Naturally produces volatility clustering.
- Easy to integrate with ARMA mean equations and VaR computation.

**Weaknesses**:

- **Symmetric response**: Treats positive and negative shocks identically (they enter as $a_{t-1}^2$).
- **Non-negativity constraints**: Parameters must be non-negative, which can be binding in estimation.
- **No structural interpretation**: Offers no explanation of *why* volatility clusters.
- **Not sufficiently adaptive**: Linear structure may underreact to extreme events.

## Asymmetric GARCH Variants

### EGARCH (Nelson, 1991)

The **Exponential GARCH** model addresses both the symmetry and non-negativity issues by modeling the log of conditional variance:

$$\ln(\sigma_t^2) = \alpha_0 + \beta_1 \ln(\sigma_{t-1}^2) + \alpha_1 g(\varepsilon_{t-1})$$

where

$$g(\varepsilon_t) = \theta \varepsilon_t + \gamma (|\varepsilon_t| - E|\varepsilon_t|)$$

The function $g(\varepsilon_t)$ has two components: the **sign effect** $\theta \varepsilon_t$ and the **magnitude effect** $\gamma (|\varepsilon_t| - E|\varepsilon_t|)$, with $E[g(\varepsilon_t)] = 0$. Under Gaussian innovations $E|\varepsilon_t| = \sqrt{2/\pi}$. Rewriting $g$ piecewise makes the asymmetry explicit:

$$g(\varepsilon_t) = \begin{cases} (\theta + \gamma)\varepsilon_t - \gamma E|\varepsilon_t| & \text{if } \varepsilon_t \geq 0 \\ (\theta - \gamma)\varepsilon_t - \gamma E|\varepsilon_t| & \text{if } \varepsilon_t < 0 \end{cases}$$

When $\theta < 0$, negative shocks generate larger variance responses than positive shocks of equal magnitude, capturing the **leverage effect**. Since the model operates on $\ln(\sigma_t^2)$, no non-negativity constraints on parameters are needed; $\sigma_t^2 > 0$ is automatic.

### TGARCH / GJR-GARCH (Glosten, Jagannathan, Runkle, 1993)

The **Threshold GARCH** (also known as GJR-GARCH) uses an indicator function to achieve asymmetry:

$$\sigma_t^2 = \alpha_0 + \alpha_1 a_{t-1}^2 + \gamma_1 N_{t-1} a_{t-1}^2 + \beta_1 \sigma_{t-1}^2$$

where $N_{t-1} = \mathbf{1}\{a_{t-1} < 0\}$. A positive $\gamma_1$ means negative shocks have a larger impact ($\alpha_1 + \gamma_1$) than positive shocks ($\alpha_1$). Under symmetric innovations the stationarity condition becomes $\alpha_1 + \gamma_1/2 + \beta_1 < 1$. Zakoian (1994) proposed a closely related TGARCH formulation on $\sigma_t$ (not $\sigma_t^2$).

### Choosing Between Variants

| Model | Asymmetry | Positivity | Interpretation |
|-------|-----------|------------|----------------|
| ARCH(m) | None | Via $\alpha_i \geq 0$ | Historical baseline |
| GARCH(1,1) | None | Via constraints | Parsimonious baseline |
| IGARCH | None | Via constraints | Permanent shock effects |
| EGARCH | Via $\theta$ (sign effect) | Automatic (log) | Best for leverage effect, no positivity issues |
| TGARCH/GJR | Via $\gamma_1$ (indicator) | Via constraints | Direct asymmetric threshold impact |
| GARCH-M | None | Via constraints | Embeds risk premium in mean |

Empirically, TGARCH/GJR often outperforms GARCH for equity indices, and EGARCH is preferred when the data push against the non-negativity constraints. Likelihood-ratio tests nest GARCH within TGARCH via $\gamma_1 = 0$.

## GARCH-M: Risk Premium in the Mean

The **GARCH-in-Mean** model (Engle, Lilien, Robins 1987) adds the conditional variance (or standard deviation) directly into the mean equation:

$$r_t = \mu + c \cdot \sigma_t^2 + a_t, \qquad a_t = \sigma_t \varepsilon_t$$

or alternatively $r_t = \mu + c \cdot \sigma_t + a_t$ or $r_t = \mu + c \cdot \ln(\sigma_t^2) + a_t$. This captures the finance-theoretic intuition that higher risk should command a higher expected return; $c$ represents the risk premium per unit of variance (or volatility). Empirical estimates of $c$ are often statistically insignificant, which has generated a substantial literature on the risk-return puzzle.

## Combined ARMA-GARCH Models

In practice, the mean and variance equations are estimated *jointly*:

- **Mean equation**: $r_t = \phi_0 + \sum_{i=1}^p \phi_i r_{t-i} + a_t - \sum_{j=1}^q \theta_j a_{t-j}$ (ARMA)
- **Variance equation**: $\sigma_t^2 = \alpha_0 + \sum_{i=1}^m \alpha_i a_{t-i}^2 + \sum_{j=1}^s \beta_j \sigma_{t-j}^2$ (GARCH)

This is the **ARMA(p,q)-GARCH(m,s)** framework. For non-stationary series, **ARIMA-GARCH** applies differencing first: $\phi(B)(1 - B) \log P_t = \theta(B) a_t$ with $a_t = \sigma_t \varepsilon_t$. The R package `fGarch` fits these models via `garchFit()`, specifying both mean and variance orders.

## Estimation: Conditional Maximum Likelihood

GARCH models are estimated by **conditional MLE**. Consider the AR(1)-GARCH(1,1) specification:

$$r_t = \phi r_{t-1} + a_t, \qquad a_t = \sigma_t \varepsilon_t, \qquad \sigma_t^2 = \alpha_0 + \alpha_1 a_{t-1}^2 + \beta_1 \sigma_{t-1}^2$$

Given $\mathcal{F}_{t-1}$, the conditional density of $r_t$ under Gaussian $\varepsilon_t$ is

$$f(r_t | \mathcal{F}_{t-1}) = \frac{1}{\sqrt{2\pi \sigma_t^2}} \exp\left(-\frac{(r_t - \phi r_{t-1})^2}{2\sigma_t^2}\right)$$

The conditional log-likelihood decomposes as a sum:

$$\ell(\lambda) = \sum_{t=1}^T \ell_t = -\frac{T}{2}\ln(2\pi) - \frac{1}{2}\sum_{t=1}^T\left[\ln \sigma_t^2(\lambda) + \frac{a_t^2(\phi)}{\sigma_t^2(\lambda)}\right]$$

where $\lambda = (\phi, \alpha_0, \alpha_1, \beta_1)'$ and recursions are initialized with $\sigma_1^2 = \text{Var}(r_t)$. Optimization uses numerical methods (BFGS, L-BFGS-B, Nelder-Mead). Under regularity conditions and $E\varepsilon_t^4 < \infty$:

$$\sqrt{T}(\hat{\lambda} - \lambda_0) \xrightarrow{d} N(0, \hat{\Omega})$$

with $\hat{\Omega}$ estimated from the outer product of scores (OPG) or the Hessian.

### Non-Gaussian Innovations

For heavy-tailed data, **Student-$t$** or **GED** (generalized error distribution) innovations replace the Gaussian. For $\varepsilon_t \sim t_\nu$ standardized to unit variance, the conditional log-likelihood contribution is:

$$\ell_t = \ln \Gamma\left(\frac{\nu+1}{2}\right) - \ln\Gamma\left(\frac{\nu}{2}\right) - \frac{1}{2}\ln[(\nu-2)\pi] - \frac{1}{2}\ln \sigma_t^2 - \frac{\nu+1}{2}\ln\left[1 + \frac{a_t^2}{(\nu-2)\sigma_t^2}\right]$$

with smaller $\nu$ giving heavier tails. The degrees of freedom $\nu$ is estimated jointly with the GARCH parameters.

## Diagnostic Checking

After fitting a GARCH model, check the **standardized residuals** $\tilde{e}_t = \hat{a}_t / \hat{\sigma}_t$:

1. **Ljung-Box on $\tilde{e}_t$**: Tests for remaining serial correlation in the conditional mean. If significant, the ARMA mean equation is inadequate.
2. **Ljung-Box on $\tilde{e}_t^2$**: Tests for remaining ARCH effects in the conditional variance. If significant, the variance model is inadequate — consider more GARCH lags, asymmetric variants, or non-Gaussian innovations.
3. **QQ-plot**: Checks the distributional assumption (Gaussian, Student-$t$, GED).
4. **Sign-bias tests** (Engle & Ng 1993): Regress $\tilde{e}_t^2$ on $N_{t-1}$, $N_{t-1} \tilde{e}_{t-1}$, and $(1 - N_{t-1})\tilde{e}_{t-1}$ to diagnose residual asymmetry that a symmetric GARCH may have missed.

## R Implementation

```r
library(fGarch)

# ARMA(1,0)-GARCH(1,1) with Student-t innovations
fit <- garchFit(~arma(1,0) + garch(1,1),
                data=sp500_ret,
                cond.dist="std",        # Student-t
                trace=FALSE)
summary(fit)                             # Ljung-Box, Jarque-Bera, ARCH-LM

# Extract standardized residuals
res <- residuals(fit, standardize=TRUE)
Box.test(res,   lag=10, type="Ljung-Box")   # mean adequacy
Box.test(res^2, lag=10, type="Ljung-Box")   # variance adequacy

# Conditional volatility series
sigma_t <- volatility(fit, type="sigma")

# Forecast 5 steps ahead
fc <- predict(fit, n.ahead=5, plot=TRUE)
# fc$meanForecast and fc$standardDeviation give r-hat and sigma-hat

# EGARCH / TGARCH via rugarch for more flexibility
library(rugarch)
spec <- ugarchspec(
  variance.model = list(model="eGARCH", garchOrder=c(1,1)),
  mean.model     = list(armaOrder=c(1,0)),
  distribution.model = "std")
fit2 <- ugarchfit(spec, data=sp500_ret)
```

## Worked Examples

These worked examples are drawn from MSBD5006 HW3 (see [[financial-time-series|MSBD5006]] for the dataset catalog). Each fits a different GARCH variant on daily or monthly percentage log returns of a named asset and highlights the resulting parameter estimates and diagnostics.

### Starbucks (SBUX) Daily Log Returns: GARCH(1,1) + Leverage Checks

Using daily SBUX simple returns 1996-2006 converted to percentage log returns, the McLeod-Li test (Ljung-Box on squared returns, lag 10) detects significant ARCH effects with LM statistic $\approx 39.34$ and $p \approx 2.2\times10^{-5}$. A Gaussian $\text{GARCH}(1,1)$ fit passes standard diagnostics: residual Ljung-Box $p > 0.05$ on both levels and squares (ARCH-LM on residuals $p = 0.87$). Extending to $\text{GARCH}(1,1)\text{-M}$ gives a marginally significant mean $\hat\mu = 0.1181$ ($p = 0.017$) but an insignificant ARCH-in-mean parameter ($p = 0.163$) — the risk-premium embedding is not supported in this sample. Fitting $\text{EGARCH}(1,1)$ yields $\hat\beta_1 = 0.9963$ (very persistent) and a leverage parameter that is only **marginally insignificant** at 5%, consistent with a mild but not decisive asymmetry in SBUX volatility response to negative news. This example is useful pedagogically because it shows the GARCH-M and EGARCH refinements *failing to reject* the null — a reminder that asymmetric variants are not automatic improvements.

### S&P 500 Daily Log Returns: IGARCH(1,1)

Applying the same procedure to the daily S&P 500 simple returns over 1996-2006 (log-transformed to percentage) produces no significant serial correlation in the mean (Ljung-Box $p > 0.05$) but overwhelming ARCH effects. An $\text{IGARCH}(1,1)$ fit with Gaussian innovations yields:

$$r_t = 0.0394 + a_t, \qquad a_t = \sigma_t \varepsilon_t, \qquad \sigma_t^2 = 0.00607 + 0.0620\, a_{t-1}^2 + 0.9309\, \sigma_{t-1}^2$$

with log-likelihood $-2003$, AIC $= 4014$, and persistence $\alpha_1 + \beta_1 = 0.9929$ — essentially at the integrated-variance boundary. The multi-step forecast behaves as expected: the mean-equation forecast stays at $\hat\mu \approx 0.039\%$ while forecast variance grows linearly in the horizon, matching the IGARCH closed-form $\sigma_{t+h}^2 = \sigma_{t+1}^2 + (h-1)\alpha_0$. This is the canonical RiskMetrics-adjacent case: **daily equity index returns with near-unit-root variance dynamics**.

### Procter & Gamble Monthly Returns: GARCH(1,1)

Monthly log returns of PG (1956-2006) fitted with a plain Gaussian $\text{GARCH}(1,1)$ give a mean of $\hat\mu \approx 0.0855\%$ per month and a 5-step 95% prediction interval of roughly $[-0.49\%, +0.66\%]$. Two lessons: (1) at monthly frequency the GARCH variance dynamics exist but are much less dramatic than daily, and (2) the unconditional variance estimate $\hat\sigma^2 = \hat\alpha_0 / (1-\hat\alpha_1-\hat\beta_1)$ is stable enough that forecast intervals remain roughly constant — the ratio of conditional to unconditional variance tightens faster at monthly frequency than daily.

### USD/EUR FX Daily Returns: Constant-Mean IGARCH

Daily USD/EUR log returns 1999-2007 show no mean-level serial correlation (LB $p = 0.29$), yet the McLeod-Li test rejects no-ARCH at $p \approx 0.003$ after demeaning. A constant-mean $\text{IGARCH}(1,1)$ fit yields stable forecasts of $\hat\mu \approx 0.0109\%$ and $\hat\sigma^2 \approx 0.1467$ across the first four horizons. FX rates are a textbook case where the conditional mean is essentially a martingale ($\mu \approx 0$) while the conditional variance is persistent — the original motivation for the EWMA volatility target used by the RiskMetrics methodology.

### R: Reproducing the SBUX Example

```r
library(rugarch)
spec <- ugarchspec(
  variance.model = list(model = "sGARCH",  garchOrder = c(1, 1)),
  mean.model     = list(armaOrder = c(0, 0), include.mean = TRUE),
  distribution.model = "norm")
fit <- ugarchfit(spec, data = sbux_logret)
fit                                 # coefficient table + LB, JB, LM tests
# Leverage test: re-fit with eGARCH and compare likelihood
spec_e <- ugarchspec(
  variance.model = list(model = "eGARCH", garchOrder = c(1, 1)),
  mean.model     = list(armaOrder = c(0, 0)),
  distribution.model = "norm")
fit_e <- ugarchfit(spec_e, data = sbux_logret)
2 * (likelihood(fit_e) - likelihood(fit))   # LR statistic, ~chi-sq(1)
```

### Important HW3 Caveats (from TA feedback)

- When running an ARCH-LM / Ljung-Box test on squared returns, **demean first**: if the mean is large, raw squared returns can mask genuine ARCH effects.
- For GARCH-type models with $p = q = 1$, do *not* zero out insignificant variance parameters — once $\omega$, $\alpha_1$, or $\beta_1$ is forced to zero the model is no longer a GARCH(1,1). The mean $\mu$ may still be zeroed if insignificant.
- R's `ugarchforecast` supports **rolling forecasts** and **bootstrap forecasts** that give more accurate multi-step variance bands than the closed-form recursion, especially for short horizons where parameter uncertainty dominates.
- R and SAS parameterize the MA component with opposite signs from most textbook conventions; always map coefficients explicitly to the notes before reporting.

## Beyond Standard GARCH

- **Stochastic Volatility (SV)**: Treats $\ln \sigma_t^2$ as a latent AR(1) process with its own independent innovation, offering more flexibility but requiring simulation-based estimation (MCMC, particle filters, or quasi-maximum likelihood via Kalman filtering on a log-squared transformation).
- **Realized Volatility (RV)**: Uses high-frequency intraday returns to compute a non-parametric estimate of daily integrated volatility, $RV_t = \sum_{i=1}^M r_{t,i}^2$, bypassing parametric GARCH entirely. HAR-RV models (Corsi 2009) forecast RV using daily, weekly, and monthly averages.
- **Multivariate GARCH**: Extends to vector settings — BEKK, DCC (Dynamic Conditional Correlation, Engle 2002), CCC (Constant Conditional Correlation, Bollerslev 1990), and factor GARCH. See [[cointegration|multivariate time series]] for broader vector framework.
- **HEAVY models** (Shephard & Sheppard 2010): Combines daily returns and realized measures for improved forecasting.

## Related Concepts

- [[arma-models|ARMA Models]] -- Provides the conditional mean equation paired with GARCH for variance
- [[cointegration|Cointegration and Multivariate Time Series]] -- Multivariate GARCH (DCC, BEKK) extends volatility modeling to vector settings
- [[linear-regression|Linear Regression]] -- Engle's LM test for ARCH effects is an auxiliary regression; GARCH mean equation reduces to OLS when $\sigma_t^2$ is constant
- [[financial-ratios|Financial Ratios]] -- Volatility estimates feed into risk metrics (VaR, Expected Shortfall, Sharpe ratio)
- [[behavioral-economics|Behavioral Economics]] -- Leverage effect and asymmetric volatility connect to investor psychology, loss aversion, and market microstructure
- [[pca|Principal Component Analysis]] -- Used for dimension reduction in high-dimensional multivariate GARCH (principal volatility components)
- [[revenue-management|Revenue Management]] -- Demand and price volatility drives protection levels and overbooking cushions; GARCH-style conditional variance is the natural input for dynamic pricing under time-varying risk
- [[ab-testing|A/B Testing]] -- Heteroskedasticity invalidates constant-variance assumptions in experiment analysis; ARCH effects in metric time series motivate robust standard errors and longer pre-test windows
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Financial Time Series and Econometrics)

## Source Materials

- [[wiki/sources/courses/financial-time-series|MSBD5006 Quantitative Analysis of Financial Time Series]]
- Lecture 4-5: Conditional Heteroscedastic Models
- Lecture 6: ARCH Testing and GARCH Variants
- Lecture 7: ARMA-GARCH and EGARCH
- R: GARCH Simulation
