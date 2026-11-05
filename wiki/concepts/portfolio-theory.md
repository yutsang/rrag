---
title: "Portfolio Theory"
full_name: "Modern Portfolio Theory (MPT)"
type: concept
tags: [finance, portfolio-theory, investments, optimization]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/fina-investments"
confidence: high
---

## 概述

現代投資組合理論（Modern Portfolio Theory, MPT）由 Markowitz（1952）建立，將分散投資的直觀智慧轉化為嚴格的均值–變異數優化框架：投資組合方差 $\sigma_p^2 = w^T \Sigma w$ 在給定目標回報 $\mu_p$ 下最小化，其解析解沿有效前沿（Efficient Frontier）分佈。引入無風險資產後，有效前沿退化為一條直線——資本市場線（CML），與風險資產有效前沿的切點即為市場投資組合 $M$，此即二基金分離定理的幾何意義。CAPM（Sharpe, 1964; Lintner, 1965）在均衡假設下推導出期望回報的橫截面定價公式 $E[R_i] = R_f + \beta_i(E[R_M] - R_f)$，其中 $\beta_i = \text{Cov}(R_i, R_M)/\text{Var}(R_M)$ 是系統性風險的唯一定價因子，非系統性風險通過多元化消除後不獲補償。在運籌學中，均值–變異數優化本質上是帶線性約束（持倉限制、行業上限、換手率限制）的二次規劃（QP），可用 Gurobi 或 CPLEX 高效求解；進一步將目標替換為條件在險價值（CVaR）的最小化則轉化為線性規劃（Rockafellar-Uryasev, 2000）。Markowitz 框架的主要實踐挑戰在於估計誤差：均值 $\mu$ 的估計誤差遠大於 $\Sigma$ 的估計誤差，導致最優權重對輸入高度敏感；Black-Litterman 模型通過貝葉斯方式混合市場均衡與主觀觀點來緩解此問題。多因子擴展（Fama-French 三因子：市場、規模、價值）在實證上解釋了 CAPM $\alpha$ 的大部分截面變異，是學術資產定價研究的標準基準；[[garch|GARCH]] 模型提供的時變協方差矩陣估計則是動態投資組合再平衡的重要輸入，[[behavioral-economics|行為經濟學]]的損失厭惡與羊群效應則解釋了為何實際投資者的持倉往往顯著偏離均值–變異數最優解。

## What It Is

**Modern Portfolio Theory (MPT)**, introduced by Harry Markowitz (1952 Nobel Prize), formalizes the trade-off between expected return and risk (variance) for a portfolio of assets.

**Setup**: $n$ risky assets with expected returns $\mu_i$, variances $\sigma_i^2$, and pairwise covariances $\sigma_{ij}$. Portfolio weights $w = (w_1, \ldots, w_n)^T$ with $\sum_i w_i = 1$.

**Portfolio return**: $R_p = \sum_i w_i R_i$, so $E[R_p] = w^T \mu$

**Portfolio variance**: $\text{Var}(R_p) = w^T \Sigma w$ where $\Sigma$ is the covariance matrix

## Mean-Variance Optimization

The **efficient frontier** solves the quadratic program:
$$\min_{w} \; w^T \Sigma w \quad \text{s.t.} \quad w^T \mu = \mu_p, \; \mathbf{1}^T w = 1$$

for each target return $\mu_p$. Tracing over $\mu_p$ gives the frontier — the set of portfolios with minimum variance for each expected return level.

The **minimum variance portfolio** minimizes $w^T \Sigma w$ subject only to $\mathbf{1}^T w = 1$.

**Key insight — diversification**: $\text{Var}(R_p) = \sum_i w_i^2 \sigma_i^2 + \sum_{i \neq j} w_i w_j \sigma_{ij}$. If assets are not perfectly correlated, combining them reduces variance below the weighted average of individual variances.

**Two-fund separation theorem**: every efficient portfolio is a convex combination of any two distinct efficient portfolios (e.g., the minimum variance portfolio and the tangency portfolio). Investors only need to combine two "mutual funds."

## Capital Asset Pricing Model (CAPM)

Adding a **risk-free asset** (return $R_f$, zero variance): the efficient frontier with a riskless asset becomes a straight line — the **Capital Market Line (CML)** — tangent to the risky efficient frontier. The tangency portfolio = **market portfolio** $M$.

**CAPM pricing equation** (Sharpe 1964, Lintner 1965):
$$E[R_i] = R_f + \beta_i (E[R_M] - R_f)$$

where $\beta_i = \text{Cov}(R_i, R_M) / \text{Var}(R_M)$ measures systematic (market) risk.

**Interpretation**: only **systematic risk** (beta) is priced; **idiosyncratic risk** is diversified away and earns no premium.

$\beta > 1$: amplifies market moves (tech stocks)
$\beta < 0$: hedges market (gold, some utilities)
$\beta = 0$: uncorrelated with market (risk-free rate)

## Performance Metrics

**Sharpe ratio**: $(E[R_p] - R_f) / \sigma_p$ — excess return per unit of total risk. Higher is better. Tangency portfolio maximizes Sharpe ratio.

**Jensen's alpha** ($\alpha$): $R_p - [R_f + \beta_p(R_M - R_f)]$ — return above CAPM prediction. Positive alpha = manager skill (or luck).

**Treynor ratio**: $(E[R_p] - R_f) / \beta_p$ — excess return per unit of systematic risk.

**Information ratio**: active return / tracking error — measures active management efficiency.

## Assumptions and Limitations

**Core assumptions**:
1. Investors maximize expected utility of end-of-period wealth; preferences fully captured by mean and variance (i.e., either quadratic utility or normally distributed returns).
2. Returns are jointly elliptically distributed — in practice, return distributions are leptokurtic (fat-tailed) and exhibit negative skewness, especially in crises.
3. All investors share the same beliefs (homogeneous expectations) and the same investment horizon.
4. Markets are frictionless: no transaction costs, taxes, short-selling restrictions, or liquidity constraints.
5. $\mu$ and $\Sigma$ are known and stable — violated severely in practice: estimation error in $\mu$ dominates that in $\Sigma$, and both vary over time.

**Limitations**:
- **Estimation error**: with $n$ assets, estimating $\Sigma$ requires $n(n+1)/2$ parameters. For $n = 100$, that is 5,050 covariance estimates from limited history. Mean estimates are even noisier — the Michaud (1989) critique shows that mean-variance optimization amplifies rather than diversifies estimation error.
- **Non-normality**: [[behavioral-economics|behavioral]] and empirical evidence confirms fat tails and crash risk; CVaR minimization (an LP) provides a more robust alternative under non-normal return distributions.
- **Time-varying covariances**: $\Sigma$ is not constant — [[garch|GARCH]]-DCC models estimate a dynamic $\Sigma_t$ for use in rolling portfolio optimization.
- **Ignores illiquidity**: optimal weights may require positions that cannot be unwound quickly without market impact.

**Extensions**:
- **Black-Litterman model**: combines CAPM equilibrium returns with investor views via Bayesian updating; produces more stable and intuitive weights than direct Markowitz optimization.
- **Risk parity**: weight assets by inverse volatility contribution ($w_i \propto 1/\sigma_i$) rather than mean-variance; avoids mean estimation entirely.
- **Factor models** (Fama-French three-factor: market, size $SMB$, value $HML$; Carhart four-factor adds momentum): explain cross-sectional return variation and provide a parsimonious structure for $\Sigma$.
- **Robust optimization**: min-max formulation over an uncertainty set for $(\mu, \Sigma)$; protects against worst-case estimation error.

## Connections to OR

Portfolio optimization is a **quadratic program (QP)** — a special case of [[optimization]] with quadratic objective and linear constraints. Gurobi/CPLEX solve large instances in seconds.

Mean-variance optimization with constraints (long-only, sector limits, turnover) is standard in quantitative asset management. Extension to CVaR (conditional value-at-risk) minimization is an LP (Rockafellar-Uryasev).

## Related Concepts

- [[optimization|Optimization]] — Mean-variance optimization is a QP; CVaR minimization is an LP
- [[linear-programming|Linear Programming]] — CVaR portfolio optimization (Rockafellar-Uryasev) reformulated as LP
- [[financial-ratios|Financial Ratios]] — Sharpe ratio, Treynor ratio, Jensen's alpha are portfolio performance metrics
- [[garch|GARCH Models]] — Dynamic conditional correlation (DCC-GARCH) provides time-varying $\Sigma_t$ for rolling optimization
- [[cointegration|Cointegration]] — Cointegration-based portfolios exploit stationary spreads; related to stat-arb strategies
- [[behavioral-economics|Behavioral Economics]] — Explains why actual holdings deviate from mean-variance optimal (loss aversion, home bias)
- [[options-pricing|Options Pricing]] — Options extend portfolio analysis to non-linear payoffs; put options as portfolio insurance
- [[fixed-income|Fixed Income]] — Bond-equity portfolio allocation; duration-adjusted multi-asset optimization
- [[corporate-finance|Corporate Finance]] — WACC and CAPM connect firm-level discount rates to portfolio theory
- [[stochastic-calculus|Stochastic Calculus]] — Continuous-time Merton portfolio problem solved via HJB equation
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/financial-engineering|Financial Engineering MOC]]

## Source Materials

- [[wiki/sources/courses/fina-investments|FINA3103 Investments]]
- [[wiki/sources/courses/fina-financial-management|FINA2303 Financial Management]]
- [[wiki/sources/courses/hkust-financial-mathematics|MATH4424/4514 Financial Mathematics]]
