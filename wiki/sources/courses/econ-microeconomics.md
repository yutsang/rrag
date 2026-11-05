---
title: "Microeconomics"
full_name: "ECON2113 Microeconomic Theory"
type: source
tags: [courses, econ, undergraduate, microeconomics, consumer-theory, game-theory, econ2113, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/ECON/ECON2113"
confidence: medium
---

## 概述

ECON2113 微觀經濟學理論為經濟系二年級學生提供消費者理論、生產理論及市場競爭的嚴格數學處理，以 Varian《中級微觀經濟學：一個現代方法》（Intermediate Microeconomics: A Modern Approach，Norton 標準教材）為主要教材，先修要求為 ECON2103 及大學一年級微積分，以便處理效用最大化的一階條件與比較靜態分析。課程以拉格朗日最優化方法為核心工具，從消費者效用最大化（Marshallian 需求、Slutsky 方程的替代效應與收入效應分解）到廠商成本最小化（Shephard 引理、條件要素需求），再到一般均衡的 Edgeworth 箱與兩大福利定理，構建嚴格的價格理論體系。博弈論章節涵蓋 Nash 均衡、子博弈完美均衡（逆向歸納）、Cournot 與 Bertrand 寡佔競爭，以及逆向選擇（Akerlof 「檸檬市場」）與道德風險（委託-代理問題）的信息經濟學。學生完成課程後能夠以微積分推導需求與供給函數、分析稅收歸宿與關稅的福利效應、設計激勵相容的合約機制。這些工具與運籌學中的線性規劃對偶理論（影子價格 = 邊際效用）、收益管理中的差異定價及機制設計理論直接相連，對有志從事 OR/IE 研究的學生提供重要的經濟學理論視角。

## Course Overview

**Textbook**: Hal Varian, *Intermediate Microeconomics: A Modern Approach*

Intermediate micro with calculus. Covers consumer and producer theory rigorously using optimization techniques.

## Key Topics

### Consumer Theory
- Preference relations: completeness, transitivity, continuity; utility representation
- Budget constraint; utility maximization: MRS = price ratio at interior solution
- Demand functions: Marshallian (uncompensated) demand; Walras' law
- Slutsky equation: $\frac{\partial x}{\partial p} = \frac{\partial x^h}{\partial p} - x \frac{\partial x}{\partial m}$ (substitution + income effect)
- Expenditure minimization: Hicksian (compensated) demand; duality
- **Revealed preference**: WARP; testing rationality from choice data — see [[behavioral-economics]]

### Producer Theory
- Production functions: returns to scale (IRS, CRS, DRS); isoquants; MRTS
- Cost minimization: conditional factor demands; Shephard's lemma
- Cost curves: short-run vs. long-run; economies of scope; learning by doing
- Profit maximization: $p = MC$ in perfect competition; supply function

### Competitive Markets and Welfare
- Partial equilibrium: producer/consumer surplus; Harberger deadweight loss triangles
- Comparative statics: tax incidence; import/export effects
- General equilibrium: Edgeworth box; Pareto efficiency; first and second welfare theorems

### Market Power
- Monopoly: Lerner index $L = \frac{P-MC}{P} = \frac{1}{|\varepsilon|}$; price discrimination (1st, 2nd, 3rd degree)
- Oligopoly: Cournot quantity competition; Bertrand price competition; Stackelberg leader-follower
- Product differentiation: horizontal (Hotelling line) vs. vertical

### Game Theory (Applied)
- Normal form games; Nash equilibrium; dominant strategies — see [[game-theory]]
- Extensive form games; backward induction; subgame perfect equilibrium
- Repeated games; tacit collusion; Folk theorem
- Adverse selection: Akerlof's lemons market; signaling; screening
- Moral hazard: principal-agent problem; incentive design

### Information Economics
- Asymmetric information: hidden action vs. hidden type
- Mechanism design intro: revelation principle; incentive compatibility; participation constraint

## OR Connections

- Consumer utility maximization is a nonlinear program; firm cost minimization is a linear program when production is linear — see [[optimization]]
- Principal-agent mechanism design connects to [[game-theory]] and [[recommendation-systems]] (incentive alignment)
- Price discrimination with capacity constraints connects to [[revenue-management]]

## Related Concepts

- [[microeconomics]]
- [[game-theory]]
- [[optimization]]
- [[revenue-management]]
- [[behavioral-economics]]

## Source Materials

- ECON2113 Course Materials
