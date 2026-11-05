---
title: "Fixed Income"
full_name: "Fixed Income Securities"
type: concept
tags: [finance, fixed-income, bonds, interest-rates]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/fina-investments"
confidence: high
---

## 概述

固定收益證券（Fixed Income Securities）以債券為主體，是全球規模最大的資產類別，承諾在約定日期支付固定票息並於到期日返還面值。債券定價公式 $P = C \cdot \frac{1-(1+y)^{-T}}{y} + \frac{F}{(1+y)^T}$ 本質上是 [[time-value-of-money|TVM]] 折現計算的直接應用，到期殖利率（YTM）則等同於 [[irr|IRR]] 的概念；價格與殖利率的反向關係，加上不同票面率與期限的債券對殖利率變動敏感度不同，催生了利率風險管理的核心工具——Macaulay 存續期 $D = \frac{\sum_t t \cdot PV(CF_t)}{P}$ 與修正存續期 $D^* = D/(1+y)$（每升息 1% 損失 $D^*\%$），以及捕捉非線性的凸性修正 $\frac{1}{2}\text{Convexity} \cdot (\Delta y)^2$。殖利率曲線（利率期限結構）的形狀——正斜率（常態）、平坦或倒掛——是預測景氣循環最受重視的宏觀指標，倒掛殖利率曲線在歷史上多次領先預示經濟衰退；其理論解釋涉及預期假說（長期利率為未來短期利率的幾何平均）、流動性溢價與市場區隔假說三個競爭性框架。信用風險方面，信用差距（Credit Spread）由風險中性默約密度 $\lambda$ 與回收率 $R$ 共同決定（$\text{spread} \approx \lambda(1-R)$），信用違約互換（CDS）提供了市場化的違約保護定價，是連接固定收益分析與衍生品的橋樑。在運籌學應用中，固定收益組合最優化（在存續期、凸性與信用約束下最大化殖利率）是二次或線性規劃問題；養老基金的免疫策略（資產存續期匹配負債存續期）是利率風險中性化的優化決策；[[cointegration|共整合]]理論則為殖利率曲線不同期限之間的長期均衡關係（利差的定態性）提供了計量基礎，是利率衍生品套利策略的學術支撐。

## What It Is

**Fixed income** securities promise specified cash flows on specified dates. **Bonds** are the primary instrument: the issuer (government, corporation) promises periodic **coupon payments** and repayment of **face value (par)** at **maturity**.

Types:
- **Government bonds**: Treasury bills (T-bills, < 1yr), Treasury notes (2-10yr), Treasury bonds (10-30yr); default-free in domestic currency
- **Corporate bonds**: credit risk; rated by Moody's/S&P/Fitch (investment grade: BBB-/Baa3 and above; high yield / junk: below)
- **Mortgage-backed securities (MBS)**: pools of mortgages; prepayment risk
- **Zero-coupon bonds**: single payment at maturity; no intermediate coupons

## Bond Pricing

**Price** = present value of all cash flows discounted at yield to maturity $y$:

$$P = \sum_{t=1}^{T} \frac{C}{(1+y)^t} + \frac{F}{(1+y)^T} = C \cdot \underbrace{\frac{1-(1+y)^{-T}}{y}}_{\text{annuity factor}} + \frac{F}{(1+y)^T}$$

where $C$ = periodic coupon, $F$ = face value, $T$ = periods to maturity.

**Inverse relationship**: price and yield move in opposite directions. If $y >$ coupon rate, bond trades at a **discount** ($P < F$); if $y <$ coupon rate, at a **premium** ($P > F$).

**Yield to Maturity (YTM)**: the internal rate of return — the single discount rate $y$ that equates price to PV of cash flows. See [[irr]].

**Current yield**: $C/P$ (annual coupon / price) — simpler approximation.

## Duration

**Macaulay duration** $D$ = weighted average time to receive cash flows:
$$D = \frac{\sum_{t=1}^{T} t \cdot PV(CF_t)}{P}$$

Duration measures **interest rate sensitivity**: $\frac{dP}{P} \approx -D^* \cdot dy$

where $D^* = D/(1+y)$ is **modified duration**.

**Interpretation**: a bond with duration 7 loses approximately 7% of value if yields rise 1%.

**Properties**:
- Zero-coupon bond: $D = T$ (duration equals maturity)
- Higher coupon → lower duration (earlier cash flows receive more weight)
- Higher yield → lower duration
- Longer maturity → higher duration (but bounded for perpetuity: $D \to (1+y)/y$)

## Convexity

Duration is a linear approximation; **convexity** captures the curvature:
$$\frac{\Delta P}{P} \approx -D^* \Delta y + \frac{1}{2} \text{Convexity} \cdot (\Delta y)^2$$

**Positive convexity** is valuable: for a given yield change, the gain when yields fall exceeds the loss when yields rise by the same amount. Investors pay for convexity (lower yield).

MBS exhibit **negative convexity** due to prepayment options — when rates fall, homeowners refinance, cutting off the upside.

## Yield Curve

The **yield curve** (term structure) plots YTM vs. maturity for bonds of the same credit quality.

**Shapes**:
- **Normal (upward sloping)**: long rates > short rates — typical
- **Flat**: short ≈ long rates
- **Inverted (downward sloping)**: short rates > long rates — historically predicts recession

**Theories**:
- **Expectations theory**: long rate = geometric average of expected future short rates
- **Liquidity preference**: investors demand term premium for holding longer maturities
- **Market segmentation**: supply/demand in each maturity segment independently

**Forward rates**: implied future short rates. $f(T_1, T_2) = [(1+y_2)^{T_2}/(1+y_1)^{T_1}]^{1/(T_2-T_1)} - 1$.

## Credit Risk

**Credit spread**: yield difference between corporate bond and equivalent Treasury. Compensates for default probability and recovery uncertainty.

**Default probability** from bond prices (risk-neutral): spread $\approx \lambda(1 - R)$ where $\lambda$ = risk-neutral default intensity, $R$ = recovery rate.

**Credit default swap (CDS)**: insurance contract paying face value if bond defaults. CDS spread ≈ bond spread (by no-arbitrage).

**Credit ratings**: Moody's (Aaa/Baa/Caa), S&P (AAA/BBB/CCC). Investment grade spreads: 50-200 bps; high yield: 300-1000+ bps.

## Connections to OR

- **Duration matching (immunization)**: match duration of assets to liabilities — eliminates interest rate risk for a pension fund; an [[optimization]] problem
- **Bond portfolio optimization**: maximize yield subject to duration, convexity, credit constraints — variant of [[portfolio-theory]]
- **Yield curve modeling**: [[arma-models]] and [[cointegration]] applied to short/long rate dynamics
- **Interest rate models** for pricing interest rate derivatives use SDE framework: see [[stochastic-calculus]]

## Assumptions and Limitations

- **YTM assumes hold-to-maturity and coupon reinvestment at YTM**: if rates change between now and maturity, realized return will differ. Duration-based immunization only neutralizes parallel yield-curve shifts; non-parallel shifts (twists, butterflies) require key-rate durations.
- **Duration is a linear approximation**: accurate only for small yield changes ($\Delta y < 50$ bps); convexity correction is needed for larger moves.
- **Credit models assume stable recovery rates**: empirically, recovery rates are negatively correlated with default rates (both drop in recessions), understating tail credit risk.
- **Yield-curve models**: affine term-structure models (Vasicek, CIR) impose specific factor structures that may misfit observed curve shapes; Nelson-Siegel decomposition (level, slope, curvature) is a more flexible empirical alternative widely used by central banks.

## Related Concepts

- [[time-value-of-money|Time Value of Money]] — Bond pricing is a direct TVM application; YTM = IRR of cash flows
- [[npv|Net Present Value]] — Bond price = PV of coupon annuity + PV of par; same discounting logic as NPV
- [[irr|Internal Rate of Return]] — Yield to maturity is the IRR of the bond's cash flow stream
- [[portfolio-theory|Portfolio Theory]] — Bond-equity allocation; duration-aware multi-asset optimization
- [[stochastic-calculus|Stochastic Calculus]] — Short-rate models (Vasicek, CIR, HJM) for interest rate derivative pricing use SDE framework
- [[garch|GARCH Models]] — Yield volatility modeling; heteroskedasticity in yield changes motivates GARCH for rate risk
- [[cointegration|Cointegration]] — Short and long rates are cointegrated; spread stationarity underpins pairs strategies on yield curve
- [[corporate-finance|Corporate Finance]] — Cost of debt $r_D$ (YTM of corporate bonds) is a WACC input; capital structure affects credit spreads
- [[options-pricing|Options Pricing]] — Interest rate options (caps, floors, swaptions) priced via short-rate models; callable bonds embed options
- [[macroeconomics|Macroeconomics]] — Yield curve shape reflects monetary policy expectations; inverted curve predicts recession
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/financial-engineering|Financial Engineering MOC]]

## Source Materials

- [[wiki/sources/courses/fina-investments|FINA3103 Investments]]
- [[wiki/sources/courses/fina-financial-management|FINA2303 Financial Management]]
- [[wiki/sources/courses/hkust-financial-mathematics|MATH4424/4514 Financial Mathematics]]
- [[wiki/sources/courses/engineering-economics|EEMT5510 Engineering Economics and Cost Management]]
