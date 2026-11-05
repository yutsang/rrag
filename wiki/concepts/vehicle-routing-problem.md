---
title: "Vehicle Routing Problem"
full_name: "Vehicle Routing Problem (VRP)"
type: concept
tags: [optimization, operations-research, combinatorial-optimization, logistics]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/ieda-routing-fleet-management"
confidence: high
---

## 概述

車輛路線問題（Vehicle Routing Problem, VRP）是在容量約束下規劃一組車輛從倉庫出發、服務所有客戶並返回的最低成本路線集合，是旅行商問題（TSP）對多車輛的直接推廣，也是組合優化中研究最廣泛的 NP 難問題之一。VRP 的核心難度在於需同時決定路線劃分（哪些客戶由哪輛車服務）和路線排序（同一車輛的訪問順序），兩者相互耦合。精確求解的主流方法是分支定價法（Branch-and-Price）：以列生成動態生成可行路線，定價子問題為資源約束最短路徑（RCSP），可最優求解規模達千名客戶的 CVRP 實例。啟發式方面，Clarke-Wright 節省演算法是經典構造法，大鄰域搜尋（Large Neighborhood Search, LNS）是當前實際效果最佳的局部搜尋框架，而 2-opt、Or-opt 及模擬退火等局部搜尋方法則是改進解的標準工具。VRP 衍生變體豐富，包括帶時間窗（VRPTW）、多倉庫（MDVRP）、隨機需求（Stochastic VRP）及動態請求（Dynamic VRP，如網約車調度）等，是運籌學博士研究在隨機規劃、近似動態規劃及魯棒優化方向的重要應用場景。

## What It Is

The **Vehicle Routing Problem (VRP)** asks: given a depot, a set of $n$ customers with known demands, and a fleet of vehicles with capacity $Q$, find routes for all vehicles that:
- Start and end at the depot
- Visit each customer exactly once
- Satisfy vehicle capacity constraints
- Minimize total travel distance (or cost, or time)

VRP generalizes the **Traveling Salesman Problem (TSP)** to multiple vehicles.

## Traveling Salesman Problem (TSP)

TSP is the special case with a single vehicle (infinite capacity). Find a Hamiltonian cycle through all $n$ nodes of minimum total weight.

**Complexity**: NP-hard. Exact solution via branch-and-bound/cutting planes (Concorde solver handles instances with tens of thousands of cities). For $n = 20$, brute force requires $(20-1)!/2 \approx 6 \times 10^{16}$ tours.

**Approximation**: Christofides algorithm achieves a 3/2-approximation guarantee using MST + minimum-weight perfect matching on odd-degree vertices. Best known polynomial-time ratio.

**Integer programming formulation** (Miller-Tucker-Zemlin):
$$\min \sum_{i,j} c_{ij} x_{ij} \quad \text{s.t.} \quad \sum_j x_{ij} = 1, \sum_i x_{ij} = 1, \; \text{subtour elimination}$$

## VRP Variants

| Variant | Additional Constraint |
|---|---|
| **CVRP** (Capacitated) | Vehicle capacity $Q$, customer demands $d_i$ |
| **VRPTW** (Time Windows) | Customer $i$ must be served in $[a_i, b_i]$ |
| **VRPB** (Backhauls) | Mix of delivery and pickup customers |
| **MDVRP** (Multi-Depot) | Multiple depots, vehicles return to origin depot |
| **PDVRP** (Pickup-Delivery) | Paired pickup and delivery requests |
| **Dynamic VRP** | New requests arrive during execution (ride-hailing) |
| **Stochastic VRP** | Demands or travel times are random |

## Exact Algorithms

**Branch-and-bound**: enumerate solutions, prune with LP lower bounds. Practical for $n \leq 50$.

**Branch-and-price** (column generation): the dominant exact method for large VRP. Each column is a feasible route; pricing problem is a resource-constrained shortest path (RCSP). State-of-the-art solvers handle $n \leq 1000$ optimally.

**Benders decomposition**: separate routing (master) from capacity allocation (subproblem).

## Heuristic Algorithms

### Construction Heuristics
**Clarke-Wright Savings Algorithm**: start with depot-customer-depot routes for each customer; merge routes if the "saving" $s_{ij} = c_{i0} + c_{0j} - c_{ij}$ (cost saved by serving $i$ and $j$ together) is positive and capacity allows. O(n² log n), produces good initial solutions.

**Nearest neighbor**: build route by always visiting the nearest unvisited customer. Fast but poor quality.

**Sweep algorithm**: order customers by polar angle around depot; fill vehicles sequentially.

### Local Search and Metaheuristics
**2-opt**: swap two edges in a route if it reduces distance. Core local search for TSP.
**Or-opt**: move sequences of 1, 2, or 3 customers to other positions.
**3-opt**: more powerful but expensive.

**Simulated annealing (SA)**: accept worse solutions with probability $e^{-\Delta/T}$, where temperature $T$ decreases over time. Escapes local optima; temperature schedule is critical.

**Tabu search**: maintain a list of forbidden (tabu) moves to escape local optima; aspiration criterion can override tabu.

**Genetic algorithms / evolutionary**: population of solutions, crossover (order crossover OX, partially mapped crossover PMX) and mutation operators.

**Large Neighborhood Search (LNS)**: destroy part of a solution (remove random customers), repair with constructive heuristic. State-of-the-art for practical VRP.

## Modern Applications

- **Last-mile delivery** (Amazon, JD.com): dynamic VRP with time windows, hundreds of stops per vehicle
- **Ride-hailing** (Didi, Uber): online matching + routing under real-time demand
- **Food delivery** (Meituan): VRPTW with short time windows, stochastic travel times
- **School bus routing**: VRPTW variant, safety constraints
- **Medical supply chains**: MDVRP with cold chain constraints

## OR PhD Leverage Points

VRP is a rich research area:
- **Stochastic VRP**: chance-constrained models, robust optimization, approximate dynamic programming
- **VRP with profits** (selective VRP): choose which customers to serve — connects to [[revenue-management]]
- **Humanitarian logistics**: VRP under uncertainty for disaster response
- **Green VRP**: minimize emissions, electric vehicle range constraints

## Related Concepts

- [[network-flows]]
- [[integer-programming]]
- [[linear-programming]]
- [[supply-chain-management]]
- [[logistics-and-transportation]]
- [[newsvendor-problem]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
