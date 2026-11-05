---
title: "Routing and Fleet Management"
full_name: "IEDA3410 Routing and Fleet Management"
type: source
tags: [courses, ieda, undergraduate, operations-research, network-flows, ieda3410, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3410"
confidence: high
---

## 概述

IEDA 3410「路徑規劃與車隊管理」是香港科技大學 IEDA 學系三年級本科生的必修課，由齊向通教授於 2021 年秋季主講。課程採用 Ahuja、Magnanti 及 Orlin 合著的《Network Flows: Theory, Algorithms, and Applications》（Prentice Hall，1993）為主要教材，以 Hillier & Lieberman《Introduction to Operations Research》第 14 章作補充。課程以網絡流理論為核心，涵蓋圖論基礎（有向無向圖、路徑、連通性）、最短路徑算法（Dijkstra、Bellman-Ford、Floyd-Warshall）、最大流問題（Ford-Fulkerson、Edmonds-Karp、最大流最小割定理）、最小費用流（網絡單純形法、全單模矩陣保證整數解）、最小生成樹（Kruskal、Prim），以及組合優化的核心難題：旅行商問題（TSP 的整數規劃建模、NP 難性、分支定界、2-opt/3-opt 局部搜索、Christofides 3/2 近似算法）與車輛路線問題（CVRP、Clarke-Wright 節省算法、帶時間窗 VRPTW、模擬退火與禁忌搜索元啟發式）。這些算法直接應用於快遞配送、城市公交規劃及供應鏈最後一哩優化，亦是 OR 博士研究中組合優化與網絡設計的重要本科基礎。

## Course Overview

**Professor**: Xiangtong Qi (Fall 2021)
**Textbook**: R.K. Ahuja, T.L. Magnanti, J.B. Orlin — *Network Flows: Theory, Algorithms, and Applications*, Prentice Hall, 1993.
**Reference**: F.S. Hillier and G.J. Lieberman, *Introduction to Operations Research*, 10th ed. (Chapter 14)

## Learning Outcomes

- Formulate and solve shortest path problems
- Formulate and solve TSP/VRP problems
- Formulate and solve max flow problems
- Formulate and solve min-cost network flow problems
- Formulate and solve spanning tree problems
- Apply these skills to complex real-world logistics problems

## Key Topics

### Graph Theory Foundations
- Directed and undirected graphs; paths, cycles, connectivity
- Trees, spanning trees; graph data structures (adjacency list/matrix)

### Shortest Path Algorithms
- Dijkstra's algorithm (non-negative weights): greedy, O((V+E) log V)
- Bellman-Ford (negative weights): DP relaxation, O(VE), detects negative cycles
- Floyd-Warshall (all-pairs): O(V³) DP
- Label-setting vs. label-correcting algorithms

### Maximum Flow
- Residual graph, augmenting paths
- Ford-Fulkerson: augment along any path
- Edmonds-Karp: BFS augmentation, O(VE²)
- **Max-flow min-cut theorem**: maximum flow = minimum cut capacity

### Minimum Cost Flow
- General formulation: supply nodes, demand nodes, arc capacities and costs
- Network simplex method: basis = spanning tree, pivoting
- Relationship to LP: MCF is an LP with totally unimodular constraint matrix → integer optimal solutions
- Special cases: shortest path, max flow, transportation, assignment

### Minimum Spanning Trees
- Kruskal's algorithm: sort edges, add if no cycle (union-find) — O(E log E)
- Prim's algorithm: grow tree from source — O((V+E) log V)
- Application: network design, Christofides TSP approximation

### Traveling Salesman Problem (TSP)
- Formulation: binary arc variables + subtour elimination constraints
- NP-hardness; exact solution: branch-and-bound with cutting planes
- Nearest neighbor heuristic; 2-opt, 3-opt local search
- Christofides 3/2-approximation algorithm

### Vehicle Routing Problem (VRP)
- CVRP formulation; Clarke-Wright savings algorithm
- Time-window VRP (VRPTW)
- Metaheuristics: simulated annealing, tabu search

## Related Concepts

- [[network-flows]]
- [[vehicle-routing-problem]]
- [[integer-programming]]
- [[linear-programming]]
- [[supply-chain-management]]
- [[logistics-and-transportation]]
