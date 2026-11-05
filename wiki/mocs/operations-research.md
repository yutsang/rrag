---
title: "Operations Research"
full_name: "Operations Research (OR)"
type: overview
tags: [moc, or, operations-research, phd]
created: "2026-04-11"
updated: "2026-04-14"
source: ""
confidence: high
---

## 概述

此 MOC 為作業研究（Operations Research, OR）領域的導覽地圖，整合現有概念頁面並規劃學術論文閱讀路徑。服務於 HKUST 課程基礎與未來兼讀 OR 博士班的文獻累積。每條閱讀路徑先列概念基礎，再接相關論文。隨新論文收錄持續擴充。

## Purpose

This is the master navigation page for Operations Research content in the wiki. It serves two audiences:

1. **Now** — a map over coursework-derived concept pages (queueing, inventory, revenue management, multi-criteria decision, time series) grouped by classical OR sub-area.
2. **Next** — a reading spine for advanced OR research. As academic papers enter `wiki/sources/papers/`, they attach here under the most relevant sub-section, forming a literature trail.

Papers are added via `workflows/ingest-paper.md`. When a sub-section accumulates 3+ papers, split it into its own dedicated MOC under `wiki/mocs/or-<subarea>.md`.

## Reading Paths

### 1. Queueing and Stochastic Service Systems

Foundations:
- [[wiki/concepts/littles-law|Little's Law]] — $L = \lambda W$, the universal relation between WIP, arrival rate, and lead time.
- [[wiki/concepts/queueing-theory|Queueing Theory]] — M/M/1, M/M/c, pooling effects, psychology of waiting.
- [[wiki/concepts/capacity-planning|Capacity Planning]] — bottleneck analysis, throughput, utilization.
- [[wiki/concepts/stochastic-processes|Stochastic Processes]] — DTMC, Poisson process, CTMC, renewal theory, Jackson networks.

Applied context: `[[wiki/sources/courses/service-ops|EEMT5520 Service Operations Management]]` — Cathay Pacific, Pizza Hut pooling, Arome bakery cases. Also `[[wiki/sources/courses/ieda-stochastic-models|IEDA3250]]`.

Papers: *(none yet)*

### 2. Inventory Theory and Supply Chain

Foundations:
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — single-period inventory, critical ratio $F^{-1}(C_u/(C_u+C_o))$.
- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — bullwhip effect, planning horizons, SAP APO.
- [[wiki/concepts/scor-model|SCOR Model]] — Plan, Source, Make, Deliver, Return.
- [[wiki/concepts/logistics-and-transportation|Logistics and Transportation]] — network design, last-mile, intermodal, 3PL.

Applied context: `[[wiki/sources/courses/enterprise-systems|EEMT5360]]`, `[[wiki/sources/courses/service-ops|EEMT5520]]`, `[[wiki/sources/courses/ieda-supply-management|IEDA4100]]`, `[[wiki/sources/courses/ieda-data-driven-scm|IEDA4410]]`.

Papers: *(none yet)*

### 3. Revenue Management and Dynamic Pricing

Foundations:
- [[wiki/concepts/revenue-management|Revenue Management]] — dynamic pricing, overbooking, yield management, fare classes.
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — seat-protection decisions as single-period inventory.
- [[wiki/concepts/game-theory|Game Theory]] — mechanism design, auctions, contract theory relevant to pricing.

Applied context: `[[wiki/sources/courses/service-ops|EEMT5520]]` — airline fare-class allocation, hotel demand control. Also `[[wiki/sources/courses/ieda-demand-management|IEDA4420]]`.

Papers: *(none yet)*

### 4. Multi-Criteria Decision Analysis

Foundations:
- [[wiki/concepts/ahp|AHP]] — analytic hierarchy process, pairwise comparisons, eigenvector weights, consistency ratio.
- [[Data Envelopment Analysis (DEA)|DEA]] — data envelopment analysis, non-parametric efficiency measurement, CCR and BCC models.
- [[wiki/concepts/balanced-scorecard|Balanced Scorecard]] — four-perspective strategy mapping.

Applied context: `[[wiki/sources/courses/integrated-business|EEMT5560]]` — Saint Honore efficiency, Bloom & Grow AHP, Chinese Pharmaceuticals forecasting.

Papers: *(none yet)*

### 5. Financial Time Series and Econometrics

Foundations:
- [[wiki/concepts/arma-models|ARMA Models]] — Box-Jenkins methodology, stationarity, ACF/PACF identification.
- [[wiki/concepts/garch|GARCH]] — volatility clustering, conditional heteroskedasticity, EGARCH asymmetry.
- [[wiki/concepts/cointegration|Co-integration]] — common stochastic trends, Engle-Granger, Johansen, VECM.
- [[wiki/concepts/linear-regression|Linear Regression]] — OLS, multicollinearity, residual diagnostics.

Applied context: `[[wiki/sources/courses/financial-time-series|MSBD5006]]`.

Papers: *(none yet)*

### 6. Statistical Learning for OR

Foundations:
- [[wiki/concepts/hypothesis-testing|Hypothesis Testing]] — z/t-tests, ANOVA, power analysis, p-value interpretation.
- [[wiki/concepts/ab-testing|A/B Testing]] — hypothesis testing, sample size, Type I/II errors, lift measurement.
- [[wiki/concepts/logistic-regression|Logistic Regression]] — binary classification, odds ratios, ROC curves.
- [[wiki/concepts/decision-trees|Decision Trees]] — CART, Random Forest, XGBoost.
- [[wiki/concepts/clustering|Clustering]] — k-means, hierarchical, DBSCAN, elbow method.
- [[wiki/concepts/pca|PCA]] — dimensionality reduction via eigendecomposition.
- [[wiki/concepts/machine-learning-advanced|Machine Learning (Advanced)]] — SVM, neural networks, backprop, CNNs, VC theory.
- [[wiki/concepts/benfords-law|Benford's Law]] — first-digit distribution, anomaly detection.

Applied context: `[[wiki/sources/courses/applied-statistics|EEMT5500]]` — Moneyball, Framingham, Netflix. Also `[[wiki/sources/courses/comp-machine-learning|COMP4211]]`, `[[wiki/sources/courses/comp-data-mining|COMP4331]]`.

Papers: *(none yet)*

### 7. Behavioral Operations

Foundations:
- [[wiki/concepts/behavioral-economics|Behavioral Economics]] — prospect theory, anchoring, nudges.
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — the pull-to-center bias (empirically deviates from rational optimum).
- [[wiki/concepts/consumer-behavior|Consumer Behavior]] — decision process, compensatory vs non-compensatory models.
- [[wiki/concepts/game-theory|Game Theory]] — strategic interaction, Nash equilibrium, principal-agent problems.

Papers: *(none yet)*

### 8. Financial Engineering and Capital Budgeting

Foundations:
- [[wiki/concepts/time-value-of-money|Time Value of Money]] — PV, FV, annuities, effective rates.
- [[wiki/concepts/npv|Net Present Value (NPV)]] — capital budgeting decision rule.
- [[wiki/concepts/irr|Internal Rate of Return (IRR)]] — incremental ERR, reinvestment assumption.
- [[wiki/concepts/depreciation|Depreciation]] — MACRS, tax shield, ATCF.
- [[wiki/concepts/cvp-analysis|CVP Analysis]] — break-even, operating leverage, quadratic profit models.
- [[wiki/concepts/portfolio-theory|Portfolio Theory]] — Markowitz mean-variance, CAPM, Sharpe ratio, Black-Litterman.
- [[wiki/concepts/options-pricing|Options Pricing]] — put-call parity, Black-Scholes, Greeks, binomial trees, real options.
- [[wiki/concepts/fixed-income|Fixed Income]] — bond pricing, duration, yield curve, credit risk models.
- [[wiki/concepts/stochastic-calculus|Stochastic Calculus]] — Brownian motion, Itô's lemma, GBM, Black-Scholes derivation.
- [[wiki/concepts/corporate-finance|Corporate Finance]] — MM theorems, WACC, agency costs, capital structure.

Applied context: `[[wiki/sources/courses/engineering-economics|EEMT5510]]`, `[[wiki/sources/courses/accounting|SBMT5010]]`, `[[wiki/sources/courses/fina-investments|FINA3103]]`, `[[wiki/sources/courses/ieda-financial-derivatives-advanced|IEDA4331]]`.

Papers: *(none yet)*

### 9. Mathematical Programming (LP / IP / NLP)

Foundations:
- [[wiki/concepts/linear-programming|Linear Programming]] — simplex method, duality theory, sensitivity analysis, shadow prices.
- [[wiki/concepts/integer-programming|Integer Programming]] — branch-and-bound, cutting planes, branch-and-price, modeling patterns.
- [[wiki/concepts/optimization|Optimization]] — unconstrained/constrained, KKT conditions, convex optimization, gradient descent.

Applied context: `[[wiki/sources/courses/ieda-operations-research-i|IEDA3010]]`.

Papers: *(none yet)*

### 10. Network Flows and Combinatorial Optimization

Foundations:
- [[wiki/concepts/network-flows|Network Flows]] — shortest path, max-flow/min-cut, min-cost flow, MST, network simplex.
- [[wiki/concepts/vehicle-routing-problem|Vehicle Routing Problem]] — TSP, VRP variants, Clarke-Wright savings, metaheuristics.
- [[wiki/concepts/facility-location|Facility Location]] — UFL/CFLP, p-median/p-center, Benders decomposition, Lagrangian relaxation.
- [[wiki/concepts/integer-programming|Integer Programming]] — modeling combinatorial problems as MIPs.

Applied context: `[[wiki/sources/courses/ieda-routing-fleet-management|IEDA3410]]`, `[[wiki/sources/courses/ieda-transportation-systems|IEDA3901]]`.

Papers: *(none yet)*

### 11. Simulation and Monte Carlo Methods

Foundations:
- [[wiki/concepts/simulation|Simulation]] — Monte Carlo, discrete-event simulation, variance reduction, output analysis.
- [[wiki/concepts/stochastic-processes|Stochastic Processes]] — underlying probability models for simulation.

Applied context: `[[wiki/sources/courses/ieda-system-simulation|IEDA4130]]`.

Papers: *(none yet)*

### 12. Game Theory and Mechanism Design

Foundations:
- [[wiki/concepts/game-theory|Game Theory]] — Nash equilibrium, prisoner's dilemma, extensive-form games, auctions, mechanism design.
- [[wiki/concepts/microeconomics|Microeconomics]] — principal-agent, adverse selection, moral hazard, incentive compatibility.

Applied context: `[[wiki/sources/courses/econ-microeconomics|ECON2113]]`.

Papers: *(none yet)*

## Sub-Areas Not Yet Covered

The following classical OR sub-areas have no concept pages yet. They will be seeded as the user ingests papers that require them:

- **Stochastic Programming and Robust Optimization** — two-stage, L-shaped, distributional robustness, scenario generation
- **Dynamic Programming and Approximate DP** — Bellman equation, value/policy iteration, ADP, reinforcement learning for OR
- **Markov Decision Processes** — MDP formulations, POMDPs, average-reward MDPs
- **Scheduling** — job shop, project scheduling (RCPSP), machine scheduling
- **Statistical Quality Control** — see [[wiki/concepts/statistical-quality-control|Statistical Quality Control]] (page exists; not yet wired into a reading path)

When a paper that introduces one of these topics is ingested, the ingesting agent should:
1. Create a stub concept page under `wiki/concepts/`
2. Populate it with the foundational definitions from that paper
3. Move the sub-area from this list to a new reading path section above

## OR-Adjacent Leverage Points from Coursework

During the 2026-04-11 HW/case integration pass, subagents surfaced specific coursework artifacts that are **directly transferable to OR research directions**. These are not papers — they are worked datasets, simulations, or student projects from the existing courses that map cleanly to an OR sub-area and could seed a first-year thesis topic or a reproducible baseline.

| Artifact | Course | Most natural OR sub-area | Leverage |
|---|---|---|---|
| **2016 Moutai HFT project** — ARFIMA + ACD on tick data | [[wiki/sources/courses/financial-time-series\|MSBD5006]] | Financial time series / optimal execution | Bridges directly to Hawkes-process limit-order-book literature; reproducible baseline for an optimal-execution paper |
| **2010 VIX–MOVE–TED spread cointegration** | [[wiki/sources/courses/financial-time-series\|MSBD5006]] | Risk-sensitive MDPs, regime-switching | Cross-asset volatility contagion is a classical setup for risk-sensitive control |
| **2009 CLP vs HK Electric VECM pairs trade** | [[wiki/sources/courses/financial-time-series\|MSBD5006]] | Optimal stopping, statistical arbitrage | VECM residual → optimal-stopping formulation is a clean research exercise |
| **2019 GJR-GARCH Asian options** | [[wiki/sources/courses/financial-time-series\|MSBD5006]] | Simulation / variance reduction | Classical OR application (Monte Carlo, importance sampling, control variates) |
| **EEMT5520 Cathay Pacific Cargo Terminal** — full WACC/NPV model | [[wiki/sources/courses/service-ops\|EEMT5520]] | Capacity planning under demand uncertainty | Single-shot capacity decision with multi-scenario NPV — extendable to real-options framing |
| **EEMT5560 MBS Game** — simulated firm with 70/30 unfilled-demand spillover | [[wiki/sources/courses/integrated-business\|EEMT5560]] | Dynamic inventory / capacity, simulation optimization | The 70/30 rule makes stockouts not merely lost sales but competitor revenue — a distinctive inventory/MDP formulation |
| **EEMT5500 insurance fraud classifier** | [[wiki/sources/courses/applied-statistics\|EEMT5500]] | Statistical learning for OR | Reproducible 7-model bake-off with real dataset and anomaly diagnostics |

These are the **highest-signal leverage points** the coursework provides for a future PhD reading list. Use them as the "prior knowledge" when assessing whether a newly ingested paper is close to or far from existing mastery.

## Recommended First-Year Reading (PhD)

*(to be populated by the user; this section is for advisors' suggested reading lists and survey papers)*

## External References

- **INFORMS** — umbrella society for OR in North America. Key journals: *Operations Research*, *Management Science*, *MSOM*, *M&SOM*, *POM*, *Interfaces*.
- **SIAM** — applied math society. *SIAM Journal on Optimization* is a core outlet.
- **arXiv math.OC** — optimization and control preprints. <https://arxiv.org/list/math.OC/recent>
- **OR-Tools** — Google's open-source solver suite.
- **Gurobi / CPLEX** — commercial LP/MIP solvers with academic licenses.

## Maintenance Notes

This MOC is the spine of the OR research pipeline. Update it whenever:
- A new paper is ingested — add to the relevant sub-section's "Papers:" list.
- A sub-section reaches 3+ papers — consider splitting into its own dedicated MOC.
- A "Sub-Area Not Yet Covered" topic gets its first paper — promote it to a full reading path.
- A new concept page is created under `wiki/concepts/` that belongs in an OR sub-area.
