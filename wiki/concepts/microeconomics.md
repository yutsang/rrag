---
title: "Microeconomics"
full_name: "Microeconomics"
type: concept
tags: [economics, microeconomics, decision-making]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/econ-microeconomics"
confidence: high
---

## 概述

微觀經濟學（Microeconomics）研究個體決策主體——消費者與廠商——的最優化行為，以及市場機制如何通過價格信號協調分散決策達成均衡。需求理論以效用最大化為基礎，推導出需求函數與 Slutsky 方程（將價格效應分解為替代效應與收入效應）；廠商理論從成本最小化與利潤最大化導出供給函數與最優規模（$P = MC$ 的邊際定價原則）。市場結構分析（完全競爭、獨占、寡占、獨占性競爭）刻畫了不同競爭強度下價格加成的形成機制，Lerner 指數 $L = (P - MC)/P = 1/|\varepsilon|$ 揭示了市場力量與需求彈性之間的精確反比關係。在運籌學的接口上，微觀經濟學提供了三個核心輸入：需求彈性是 [[revenue-management|收益管理]] 最優動態定價模型的需求曲線參數；外部性理論（Pigouvian 稅）與公共財理論（搭便車問題）是供應鏈協調合約（數量折扣、回購契約）設計所依賴的市場失靈框架；賽局理論（Cournot、Bertrand、Stackelberg）在寡占分析中的應用，是 [[game-theory|博弈論]] 機制設計與拍賣設計研究的直接前驅。供應鏈的雙重加成（double marginalization）問題本質上是垂直市場結構中的壟斷問題，其矯正方案（協調合約）直接借鑒了 Pigouvian 思路。[[behavioral-economics|行為經濟學]] 提供的參考點依賴與損失厭惡理論，則是對傳統微觀效用最大化假設的修正，尤其在消費者行為模型（[[consumer-behavior|Consumer Behavior]]）與動態定價的顧客公平感知分析中不可或缺。

## What It Is

**Microeconomics** studies the behavior of individual agents (consumers, firms) and how markets aggregate these decisions into prices and quantities.

## Supply and Demand

**Demand curve**: $Q^d = f(P)$ — quantity demanded as a function of price. Downward sloping (law of demand). Shifts with income, prices of substitutes/complements, tastes, expectations.

**Supply curve**: $Q^s = g(P)$ — quantity supplied. Upward sloping. Shifts with input costs, technology, number of producers.

**Market equilibrium**: $Q^d = Q^s$. Price $P^*$ and quantity $Q^*$ clear the market. Surplus/shortage mechanisms restore equilibrium.

## Elasticity

**Price elasticity of demand**: $\varepsilon = \frac{\partial Q/Q}{\partial P/P} = \frac{\partial \ln Q}{\partial \ln P}$

- $|\varepsilon| > 1$: elastic (luxury goods, many substitutes) — price increase reduces total revenue
- $|\varepsilon| < 1$: inelastic (necessities, few substitutes, addictive goods) — price increase raises total revenue
- $|\varepsilon| = 1$: unit elastic — revenue maximizing price

**Income elasticity**: $\varepsilon_I = \partial \ln Q / \partial \ln I$. Positive for normal goods; negative for inferior goods (instant noodles).

**Cross-price elasticity**: measures substitutability (positive) or complementarity (negative).

**OR relevance**: price elasticity is the key input for [[revenue-management]] and pricing optimization.

## Consumer Theory

**Utility maximization**: consumer chooses bundle $(x_1, x_2)$ to $\max U(x_1, x_2)$ s.t. $p_1 x_1 + p_2 x_2 = I$.

**Indifference curves**: $U(x_1, x_2) = \bar{u}$; MRS = $-\partial U/\partial x_1 / (\partial U / \partial x_2) = p_1/p_2$ at optimum.

**Demand functions**: $x_i^*(p_1, p_2, I)$ — derived from utility maximization. Slutsky equation decomposes price effects into substitution + income effects.

## Producer Theory

**Production function** $f(K, L)$: output from capital $K$ and labor $L$. Returns to scale: increasing (IRS), constant (CRS), decreasing (DRS).

**Cost minimization**: choose inputs to produce $q$ at minimum cost. Results in cost function $C(q)$.

**Profit maximization**: $\max_{q} \; p \cdot q - C(q)$. FOC: $p = C'(q) = MC$ (price = marginal cost).

**Cost curves**: $MC$, $AC$ (average cost), $AVC$, $AFC$. $MC$ intersects $AC$ at its minimum (efficient scale).

## Market Structures

### Perfect Competition
Many small firms, homogeneous product, free entry. $P = MC = \min AC$ in long-run equilibrium. Zero economic profit in long run — price competition eliminates rents.

### Monopoly
Single seller, downward-sloping demand curve. Monopolist sets $MR = MC$. Markup: $P - MC = P/|\varepsilon|$ (Lerner index). Creates deadweight loss. Source of market power: economies of scale, patents, network effects.

### Oligopoly
Few large firms, strategic interaction → [[game-theory]]. Cournot (quantity competition), Bertrand (price competition), Stackelberg (sequential). Actual behavior often between competitive and monopoly outcomes.

### Monopolistic Competition
Many firms, differentiated products (restaurants, clothing). $P > MC$ in short run; free entry drives economic profit to zero in long run. Product variety but some deadweight loss.

## Externalities and Market Failure

**Negative externality**: production/consumption imposes costs on third parties (pollution). Social cost > private cost → overproduction at market equilibrium.

**Positive externality**: education, vaccination → underproduction.

**Pigouvian tax/subsidy**: correct externality by making private cost = social cost.

**Coase theorem**: if property rights are well-defined and transactions costs are low, private bargaining achieves efficient outcome regardless of who holds the rights.

**Public goods**: non-excludable + non-rival → free-rider problem → underprovision by markets.

## Applications to OR

- **Demand modeling**: econometric demand functions for pricing and forecasting
- **Revenue management**: optimal pricing requires understanding demand elasticity and consumer segmentation
- **Mechanism design** (reverse micro): design market rules to achieve desired outcomes — see [[game-theory]]
- **Supply chain coordination**: double marginalization is a market failure within a supply chain — contracts fix it
- **Auction design**: Vickrey auctions, spectrum auctions derived from micro theory

## Assumptions and Limitations

- **Rational utility maximization**: standard micro assumes consistent, transitive preferences and perfect information. [[behavioral-economics|Behavioral economics]] documents systematic violations — loss aversion, framing effects, hyperbolic discounting — that require descriptive models to supplement or replace the normative framework.
- **Partial equilibrium vs. general equilibrium**: supply-demand analysis holds "other things equal." In practice, a price change in one market ripples through input and output markets simultaneously; Walrasian general equilibrium or computable general equilibrium (CGE) models are needed for policy analysis.
- **Static models**: most micro models are comparative statics. Dynamic effects (entry deterrence, learning-by-doing, network externalities) require game-theoretic or dynamic programming extensions.
- **Externalities and public goods**: markets fail when social and private costs diverge. Pigouvian corrections assume the regulator can observe and price externalities perfectly — often not feasible, motivating second-best mechanism design.

## Related Concepts

- [[game-theory|Game Theory]] — Strategic interaction in oligopoly; mechanism design; auction theory
- [[revenue-management|Revenue Management]] — Optimal pricing requires demand elasticity estimates and consumer segmentation from micro theory
- [[behavioral-economics|Behavioral Economics]] — Systematic deviations from rational-agent micro model; prospect theory, anchoring, present bias
- [[consumer-behavior|Consumer Behavior]] — Applied consumer theory; purchase decision process, B2B vs B2C segmentation
- [[porters-five-forces|Porter's Five Forces]] — Industry structure analysis grounded in market structure theory (barriers to entry, substitute goods)
- [[macroeconomics|Macroeconomics]] — Macro aggregates from micro foundations (representative agent, New Keynesian DSGE)
- [[cvp-analysis|CVP Analysis]] — CVP profit maximization under linear demand is applied producer theory
- [[newsvendor-problem|Newsvendor Problem]] — Optimal order quantity derived from marginal analysis: order up to where marginal cost equals marginal expected revenue
- [[wiki/mocs/operations-research|Operations Research MOC]]

## Source Materials

- [[wiki/sources/courses/econ-microeconomics|ECON2113 Microeconomic Theory]]
- [[wiki/sources/courses/econ-introductory-economics|ECON2103 Introductory Economics]]
- [[wiki/sources/courses/fina-financial-markets|FINA1303 Introduction to Financial Markets]]
