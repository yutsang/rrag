---
title: "Facility Location"
full_name: "Facility Location Problem (FLP)"
type: concept
tags: [optimization, operations-research, supply-chain, facility-location, integer-programming]
created: "2026-04-14"
updated: "2026-04-14"
source: "https://doi.org/10.1287/opre.2019.1920"
confidence: high
---

## 概述

設施選址問題（Facility Location Problem, FLP）是在候選地點集合中決定開設哪些設施（倉庫、工廠、醫院、服務站），並將各顧客分配至開設設施，以最小化固定開設成本與變動服務成本之和的整數規劃問題。無容量限制版本（UFL）的標準公式為 min Σ fj yj + Σij cij xij，約束每位顧客恰由一設施服務，且只能分配至已開設的設施；LP 鬆弛具有半整數最優解，最佳近似比為 1.488（Shmoys-Tardos-Aardal 局部搜索算法）。有容量限制版本（CFLP）更貼近實際但更難，在 P ≠ NP 假設下不存在常數近似比。特殊變體包括：p-median（選恰好 p 個設施最小化加權距離）、p-center（最小化最大響應時間，用於緊急服務選址）及樞紐選址（Hub Location，結合網絡流的航空/快遞樞紐設計）。求解方法包括拉格朗日鬆弛（對分配約束對偶化，子問題按設施分解）、Benders 分解（將開設決策與分配決策分離）及貪婪啟發式。在供應鏈研究中，設施選址是五大績效驅動因素之首，與庫存集中化的風險池化效應、運輸網絡設計及兩階段隨機規劃密切交織。

## What It Is

**Facility location** asks: given potential locations for facilities (warehouses, factories, hospitals, fire stations) and a set of customers with known demands, decide which facilities to open and how to assign customers to facilities to minimize total cost.

This is a **strategic** supply chain decision with long time horizons — contrasted with tactical (inventory policy) and operational (daily routing) decisions.

## Core Models

### Uncapacitated Facility Location (UFL)

$$\min \sum_{j \in J} f_j y_j + \sum_{i \in I} \sum_{j \in J} c_{ij} x_{ij}$$

$$\text{s.t.} \quad \sum_{j \in J} x_{ij} = 1 \; \forall i, \quad x_{ij} \leq y_j \; \forall i,j, \quad y_j \in \{0,1\}, \; x_{ij} \geq 0$$

- $y_j \in \{0,1\}$: open facility $j$ or not
- $x_{ij}$: fraction of customer $i$'s demand served from facility $j$
- $f_j$: fixed cost of opening facility $j$
- $c_{ij}$: cost of serving customer $i$ from facility $j$ (often = $d_{ij} \cdot D_i$, distance × demand)

LP relaxation of UFL has half-integral solutions. **Best known approximation**: 1.488 (Shmoys-Tardos-Aardal with local search).

### Capacitated Facility Location (CFLP)

Add capacity constraints: $\sum_i x_{ij} D_i \leq C_j y_j$. More realistic but harder. No constant-factor approximation unless P=NP.

### p-Median Problem

Choose exactly $p$ facilities from $J$ to minimize total weighted distance. No fixed costs — just pick the best $p$ locations.

**Weber problem** (continuous): locate a single facility in the plane to minimize total weighted distance. Solved by Weiszfeld algorithm.

### p-Center Problem (Minimax Location)

Minimize the maximum distance from any customer to its nearest facility. Used for emergency service placement (ambulances, fire stations) where worst-case response time matters.

### Hub Location

Hub-and-spoke networks: choose hub locations and route all demand through hubs. Combines facility location with [[network-flows]]. Applied in airline networks, parcel delivery.

## Solution Approaches

### Exact Methods

**LP relaxation + B&B**: solve LP relaxation; branch on fractional $y_j$. Modern MIP solvers handle CFLP with hundreds of facilities.

**Lagrangian relaxation**: dualize the assignment constraints $\sum_j x_{ij} = 1$ with multipliers $\lambda_i$. The Lagrangian subproblem decomposes by facility: each facility problem is solvable in $O(I)$. Subgradient method updates $\lambda$. Provides a tight lower bound, often near-optimal.

**Benders decomposition**: separate facility open/close (master) from customer assignment (subproblem). The dual of the assignment LP provides Benders cuts. Effective when $|J|$ is small relative to $|I|$.

### Heuristics

**Add/drop/swap**: start with all open, drop facilities with most cost savings; or start empty and add greedily. Local search: try swapping one open facility for one closed.

**Greedy**: sequentially open the facility with highest demand coverage per cost. Approximation ratio = $1 - (1-1/p)^p \approx 1 - 1/e \approx 63\%$ coverage.

## Multi-Period and Stochastic Extensions

**Dynamic facility location**: facility opening/closing decisions over multiple periods with reconfiguration costs. Relevant for evolving demand patterns (China's demographic shifts).

**Stochastic facility location**: demand or costs are uncertain. Robust optimization (worst-case over uncertainty set) or stochastic programming (expected cost over scenarios).

**Two-stage stochastic**: locate facilities (first stage), then observe demand and assign customers (second stage). Connects to [[newsvendor-problem]] structure.

## Industry Applications

| Application | Model Variant |
|---|---|
| Amazon warehouse placement | CFLP with delivery time constraints |
| Retail chain (Starbucks, 7-Eleven) | p-median with cannibalization |
| Hospital/emergency services | p-center (minimize max response time) |
| Manufacturing plant location | CFLP with transport network |
| Cloud data center placement | Hub location with latency constraints |
| Hong Kong post office network | p-median |

## Supply Chain Context (IEDA3460)

Chopra & Meindl identify **facility location** as one of five supply chain performance drivers (with inventory, transportation, information, sourcing). Key decisions:
- **Number of warehouses**: more warehouses reduce outbound transport costs, increase inventory costs (risk pooling effect diluted)
- **Location relative to demand**: offshore production vs. near-shore trade-offs
- **Consolidation vs. distribution**: one central DC vs. regional DCs

## Related Concepts

- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — facility location as a key supply chain design driver
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — risk pooling benefits of facility consolidation
- [[wiki/concepts/capacity-planning|Capacity Planning]] — capacity sizing at each facility
- [[wiki/concepts/queueing-theory|Queueing Theory]] — service facility sizing given arrival rates
- [[wiki/mocs/operations-research|Operations Research MOC]] — integer programming and combinatorial optimization context
- [[integer-programming]] — UFL/CFLP are canonical IP problems
- [[network-flows]] — transportation subproblem in Benders decomposition
- [[vehicle-routing-problem]] — Location-Routing Problems combine both

## Source Materials

- raw/courses/IEDA/IEDA3460/syllabus_2022.pdf
- raw/courses/IEDA/IEDA4200/2021 Fall/IEDA4200_Syllabus2021.pdf
