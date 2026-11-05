---
title: "Data Envelopment Analysis"
full_name: "Data Envelopment Analysis (DEA)"
type: concept
tags: [operations-research, efficiency, benchmarking, linear-programming, dea]
created: "2026-04-10"
updated: "2026-04-12"
source: "wiki/sources/courses/integrated-business"
confidence: high
---

## 概述

資料包絡分析（DEA）是一種基於線性規劃的非參數效率評估方法，用於比較一組決策單元（DMU）的相對效率。它無需預設投入與產出之間的函數關係，透過建構效率前沿面來識別最佳實務單位，並為低效率單位提供改善目標和標竿參考。DEA 廣泛應用於銀行分行績效評估、醫院效率比較及連鎖零售店營運分析等場景。

## Core Mechanism

**Data Envelopment Analysis (DEA)** is a non-parametric method that uses linear programming to evaluate the relative efficiency of a set of **Decision Making Units (DMUs)** -- entities that consume multiple inputs to produce multiple outputs. Unlike regression or parametric methods, DEA does not require assuming a functional relationship between inputs and outputs. Instead, it constructs an **efficient frontier** from the best-performing units and measures all others relative to that frontier.

### Efficiency Definition

The fundamental efficiency concept in DEA is:

```
Efficiency = Weighted sum of outputs / Weighted sum of inputs
```

For a DMU with *s* outputs (y₁, y₂, ..., yₛ) and *m* inputs (x₁, x₂, ..., xₘ):

```
Efficiency = (u₁y₁ + u₂y₂ + ... + uₛyₛ) / (v₁x₁ + v₂x₂ + ... + vₘxₘ)
```

Where *u* and *v* are the output and input weights, respectively. The key insight is that DEA **allows each DMU to choose its own most favorable weights** -- if a unit is still inefficient even with its best possible weights, it is genuinely underperforming.

### CCR Model (Charnes-Cooper-Rhodes)

The original DEA model, proposed by Charnes, Cooper, and Rhodes in 1978, assumes **constant returns to scale (CRS)**. The fractional programming formulation for evaluating DMU $j_0$ is:

$$\text{Max } E_0 = \frac{\sum_{r=1}^{s} u_r y_{r j_0}}{\sum_{i=1}^{m} v_i x_{i j_0}}$$

$$\text{s.t. } \frac{\sum_{r=1}^{s} u_r y_{rj}}{\sum_{i=1}^{m} v_i x_{ij}} \le 1 \quad \forall j = 1, \ldots, n$$

$$u_r, v_i \ge \varepsilon > 0$$

This fractional program is converted to a standard linear program (the **Charnes-Cooper transformation**) by fixing the denominator to 1:

$$\text{Max } E_0 = \sum_{r=1}^{s} u_r y_{r j_0}$$

$$\text{s.t. } \sum_{i=1}^{m} v_i x_{i j_0} = 1$$

$$\sum_{r=1}^{s} u_r y_{rj} - \sum_{i=1}^{m} v_i x_{ij} \le 0 \quad \forall j$$

$$u_r, v_i \ge \varepsilon$$

A DMU is **efficient** if and only if its optimal objective value equals 1.0. An efficiency score less than 1.0 indicates the unit could produce the same outputs with fewer inputs (or produce more outputs with the same inputs). Note that the LP must be solved **once per DMU** ($n$ LPs for $n$ units), because each DMU is allowed to pick its own most favorable weights.

### BCC Model (Banker-Charnes-Cooper)

The BCC model (1984) relaxes the CRS assumption to allow **variable returns to scale (VRS)**. It adds a free variable *u₀* to the LP formulation, which captures the returns-to-scale characteristic:

- $u_0 > 0$: Decreasing returns to scale
- $u_0 = 0$: Constant returns to scale
- $u_0 < 0$: Increasing returns to scale

The BCC model typically produces efficiency scores greater than or equal to CCR scores, since the VRS frontier "envelops" the data more tightly.

### Input vs. Output Orientation

DEA models come in two orientations:

- **Input-oriented**: "How much can inputs be proportionally reduced while maintaining current output levels?" -- appropriate when managers have more control over inputs
- **Output-oriented**: "How much can outputs be proportionally increased with current input levels?" -- appropriate when inputs are fixed

Under CRS (CCR model), both orientations yield the same efficiency score. Under VRS (BCC model), they may differ.

## Efficient Frontier and Peer Analysis

The efficient frontier is formed by the convex combination of all efficient DMUs. For any inefficient DMU, DEA identifies:

1. **Efficiency score** -- The proportional reduction in inputs (or increase in outputs) needed to reach the frontier
2. **Reference set (peers)** -- The efficient DMUs that form the relevant benchmark
3. **Target values** -- Specific input/output levels the inefficient DMU should aim for
4. **Slack values** -- Additional input reductions or output increases needed beyond proportional improvement

This peer analysis is particularly valuable for managers because it provides concrete, achievable targets based on actual peer performance rather than theoretical ideals.

## Worked Example: Bank Branch LP

The EEMT5560 Lecture 03 example uses six bank branches with one input (number of staff) and two outputs (personal transactions and business transactions):

| Branch | Staff | Personal Trans | Business Trans |
|--------|-------|----------------|----------------|
| A | 8  | 360   | 160 |
| B | 5  | 125   | 75  |
| C | 10 | 1,000 | 200 |
| D | 11 | 770   | 330 |
| E | 15 | 1,350 | 450 |
| F | 6  | 210   | 270 |

The LP for branch A, before the Charnes-Cooper transformation:

$$\text{Max } E_A = \frac{360 u_1 + 160 u_2}{8 v_1}$$

$$\text{s.t. } \frac{360 u_1 + 160 u_2}{8 v_1} \le 1, \quad \frac{125 u_1 + 75 u_2}{5 v_1} \le 1, \quad \frac{1000 u_1 + 200 u_2}{10 v_1} \le 1, \ldots$$

Rewriting in standard form, the denominator is fixed to 1 and the constraints become linear:

$$\text{Max } E_A = 360 u_1 + 160 u_2$$

$$\text{s.t. } 8 v_1 = 1$$

$$360 u_1 + 160 u_2 - 8 v_1 \le 0 \quad \text{(A)}$$

$$125 u_1 + 75 u_2 - 5 v_1 \le 0 \quad \text{(B)}$$

$$1000 u_1 + 200 u_2 - 10 v_1 \le 0 \quad \text{(C)} \ldots$$

$$u_1, u_2, v_1 \ge \varepsilon$$

This single LP yields branch A's efficiency; the same structure is re-solved with A's input/output values swapped for each of B, C, D, E, F. Typical results show 3-4 branches on the frontier with scores of 1.0 and the rest between 0.6 and 1.0, each with a reference set of efficient peers.

## Saint Honore Case Study

The course applies DEA to evaluate **82 Saint Honore cake shop branches** in Hong Kong using **Frontier Analyst** software. Saint Honore is a legacy Hong Kong bakery founded 1972 with 100+ retail outlets competing against brands like Maxim's, A-1 Bakery, and Arome. The DEA model structure illustrates real-world complexity:

**Controlled inputs** (management can adjust):
- Number of staff (FTE average)
- Number of SKUs sold
- Spoilage rate (% of sales)
- Monthly operating expenses (excluding rent)

**Uncontrolled inputs** (fixed environmental factors):
- Floor area (sq ft)
- Monthly rent

**Outputs**:
- Average daily transaction count
- Monthly sales revenue

Separating controlled from uncontrolled inputs is critical -- efficiency improvement recommendations can only target controllable variables. A branch with high rent and small floor area may appear inefficient, but those factors cannot be changed in the short term. DEA's ability to incorporate both types allows for fairer comparisons.

### Example Improvement Target

A concrete Frontier Analyst report for branch H25 (efficiency score 80.35%, with C76 and Y13 as peers) showed:

| Variable | Actual | Target | Potential Improvement |
|----------|--------|--------|----------------------|
| Area (sq ft) | 893  | 656.55   | -26.48% |
| Expense      | 196,000 | 149,297 | -23.83% |
| Hours        | 98   | 73.26    | -25.25% |
| Rent         | 87,000 | 87,000 | 0.00% (uncontrolled) |
| SKU          | 236  | 165.84   | -29.73% |
| Sales        | 611,000 | 611,000 | 0.00% |
| Spoilage     | 0.05 | 0.03     | -39.27% |
| Staff        | 6.80 | 5.46     | -19.65% |
| Transaction  | 660  | 750      | +13.57% |

The report tells the manager *exactly* how much each controllable input must be trimmed to reach the efficient frontier, and identifies which outputs can be increased -- a major advantage over aggregate KPI rankings.

### Efficiency-Profitability Matrix

After DEA, the course plots branches on a 2x2 matrix crossing efficiency (from DEA) with profitability (% of sales). The four quadrants are:

| | Low Efficiency | High Efficiency |
|---|---|---|
| **High Profitability** | Under-performing potential stars (sleepers) -- process fixes can unlock hidden value | **Benchmark stores (stars)** -- the gold standard |
| **Low Profitability** | Problem stores (??) -- structural issues; need investigation | Candidates for divestment -- efficient but not profitable; wrong location or format |

The EEMT5560 Saint Honore dataset shows a correlation of only $r = 0.7546$ between the two single-ratio rankings (sales per staff vs. profit margin) Raymond Chan had previously used, and a lower Pearson $r = 0.62$ between DEA efficiency and profit margin -- demonstrating that DEA reveals insights that single-ratio KPI dashboards miss. The case explicitly opens with Raymond's frustration that store managers were complaining about annual-bonus decisions made on rankings that were themselves internally inconsistent. DEA settled the argument by giving each store a single composite efficiency score derived from its *own* optimal weights, silencing the "you measured the wrong thing" objection. The case uses Banxia Frontier Analyst's free 12-DMU trial version for classroom reproduction.

### Segmenting Branches on the Matrix

Saint Honore's 82 branches are plotted on the 2x2 efficiency-profitability matrix using medians as cut lines. Interpretation rules taught in class:

- **Stars** (high eff, high profit) -- Protect and replicate. Use as DEA peers for benchmarking.
- **Sleepers** (low eff, high profit) -- Favorable location masks operational slack; process fixes unlock hidden value without the risk of touching revenue.
- **Problem stores** (low eff, low profit) -- Investigate root cause. Distinguish between fixable process issues and structural location/format problems before committing capital.
- **Divestment candidates** (high eff, low profit) -- The hardest call. Operationally tight but unprofitable means the format or location is wrong; efficiency gains cannot rescue a bad site. Closure or repositioning, not process improvement, is the answer.

The 2x2 plus DEA peer analysis together give Raymond a three-step action playbook: (1) identify the quadrant, (2) pull the DEA peer list to see which stores to emulate, (3) read the improvement-target table to see exactly which controllable inputs to cut. This is the course's canonical example of how DEA outputs become managerial actions rather than just numbers.

## Practical Considerations

### Choosing Inputs and Outputs

- **Rule of thumb**: The number of DMUs should be at least 3 times the sum of inputs and outputs ($n \geq 3(m + s)$) to ensure meaningful discrimination
- Inputs should represent resources consumed; outputs should represent results produced
- Avoid highly correlated inputs/outputs as they reduce discriminating power
- Include both financial and non-financial measures for comprehensive evaluation

### Interpreting Results

- An efficiency score of 1.0 means the DMU is on the frontier -- but it does not necessarily mean it is operating optimally in an absolute sense
- DEA measures **relative** efficiency -- results depend entirely on the set of DMUs included
- Adding or removing DMUs can change the frontier and alter all scores
- Outliers can significantly distort the frontier; data quality is crucial

### Software Tools

- **Frontier Analyst** (used in the EEMT5560 course)
- DEA-Solver, MaxDEA, DEAP
- R packages (Benchmarking, rDEA)
- Python libraries (pyDEA)

## Strengths and Limitations

**Strengths**:
- No need to specify a production function or assume weights a priori
- Handles multiple inputs and outputs simultaneously in different units of measurement
- Provides actionable improvement targets and peer benchmarks
- Works with both financial and operational metrics

**Limitations**:
- Measures only relative efficiency -- all DMUs could be absolutely inefficient
- Sensitive to outliers and data errors (a single erroneous data point can distort the entire frontier)
- Assumes data is deterministic -- does not account for statistical noise
- Results are sample-dependent and may change with different DMU sets
- Can produce many "efficient" units when the number of variables is large relative to sample size

## DEA vs. Regression

A key EEMT5560 discussion question: why use DEA instead of regression to model output as a function of inputs?

| Dimension | Regression | DEA |
|-----------|-----------|-----|
| Approach | Central tendency (line of best fit) | Frontier (line of best practice) |
| Interpretation | Average performance | Best achievable performance |
| Weights | Fixed across all units | Each DMU picks its own best weights |
| Inefficiency | Residuals (can be positive or negative) | Distance from frontier (one-sided) |
| Managerial output | Predicted value | Target values + peer reference set |
| Multiple inputs/outputs | Requires separate models | Unified in single LP |
| Functional form | Parametric (linear, log, etc.) | Non-parametric |

For managerial benchmarking DEA is typically preferred because it identifies the actual best performers and provides concrete peer-based targets, whereas regression lumps every DMU against a statistical average.

## Related Concepts

- [[ahp|Analytic Hierarchy Process]] -- Complementary MCDM tool taught alongside DEA in EEMT5560; AHP weights criteria subjectively from expert judgment while DEA derives weights objectively from LP optimization. Weight-restricted DEA combines the two by importing AHP priorities as bounds on DEA weights.
- [[scor-model|SCOR Model]] -- Supply chain performance framework whose five attributes (Reliability, Responsiveness, Agility, Cost, Asset Management) can serve as DEA inputs/outputs for benchmarking supply chain units.
- [[balanced-scorecard|Balanced Scorecard]] -- Multi-perspective performance framework; DEA can operationalize BSC by using perspective-level metrics as DEA inputs and outputs.
- [[financial-ratios|Financial Ratios]] -- Traditional single-ratio efficiency measures that DEA extends to multi-dimensional analysis.
- [[linear-regression|Linear Regression]] -- Alternative parametric benchmarking approach; contrasts with DEA's non-parametric frontier method.
- [[porters-five-forces|Porter's Five Forces]] -- DEA identifies high-performing peers to benchmark against within an industry defined by Porter's structure.
- [[capacity-planning|Capacity Planning]] -- DEA reveals which units under-utilize capacity and how much slack exists.
- [[queueing-theory|Queueing Theory]] -- For service units, queue-length and utilisation from M/M/c models supply DEA inputs and outputs; efficient branches operate on the frontier of the $\rho$ vs waiting-time surface.
- [[littles-law|Little's Law]] -- Provides comparable throughput ($\lambda$) and flow-time ($W$) measurements that make service DMUs directly benchmarkable in DEA.
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Multi-Criteria Decision Analysis)

## Source Materials

- EEMT5560 Lecture 03: DEA
- EEMT5560 Lecture 04: Saint Honore DEA Case
- Saint Honore Case Study (ST115)
- [[wiki/sources/courses/integrated-business|EEMT5560 Integrated Business Solutions]]
