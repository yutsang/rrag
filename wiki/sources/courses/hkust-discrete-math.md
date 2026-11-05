---
title: "HKUST Discrete Mathematics"
full_name: "HKUST Discrete Mathematics (MATH2343/COMP2711)"
type: source
tags: [courses, math, undergraduate, discrete-math, combinatorics, graph-theory, math2343, comp2711, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH2343"
confidence: medium
---

## 概述

MATH2343 離散數學及 COMP2711 電腦科學數學工具為電腦科學與工業工程二年級學生提供組合數學、圖論及數理邏輯的系統訓練，是理工科課程中銜接數學與計算機科學的橋接課程。數學版 MATH2343 以 Rosen《離散數學及其應用》為標準教材，側重嚴格的數學證明方法（直接證明、反證法、數學歸納法）；CS 版 COMP2711 則更強調演算法正確性分析與計算複雜度。先修要求僅為高中數學，使其成為理工科一、二年級學生的入門離散課程。課程使學生掌握命題邏輯與謂詞邏輯的推理規則、集合論與關係代數、排列組合的計數技術（容斥原理、生成函數、遞推關係）、圖論基礎（連通性、樹、歐拉迴路、二部圖配對）及初等數論（模運算、RSA 密碼系統）。這些工具是演算法設計與分析（圖演算法、動態規劃的組合結構）、密碼學、網路流優化及整數規劃問題建模的數學基礎，對理解計算複雜性與 NP 難問題的理論框架亦不可或缺。

## Course Structure

MATH2343 and COMP2711 cover overlapping material from different angles — the Math version emphasizes proof rigor, while the CS version emphasizes algorithmic applications.

## Key Topics

### Logic and Proofs
- Propositional logic: truth tables, logical equivalences, CNF/DNF
- Predicate logic: quantifiers, nested quantifiers, inference rules
- Proof techniques: direct, contrapositive, contradiction, mathematical induction (weak, strong, well-ordering)

### Set Theory and Relations
- Set operations: union, intersection, complement, power set, Cartesian product
- Relations: properties (reflexive, symmetric, transitive); equivalence relations; partial orders
- Functions: injections, surjections, bijections; composition; inverse

### Combinatorics
- **Counting**: addition and multiplication principles; permutations $P(n,r) = \frac{n!}{(n-r)!}$; combinations $\binom{n}{r}$
- **Binomial theorem**: $(x+y)^n = \sum_{k=0}^n \binom{n}{k} x^k y^{n-k}$
- **Inclusion-exclusion**: $|A \cup B \cup C| = |A| + |B| + |C| - |A\cap B| - \cdots + |A\cap B\cap C|$
- Pigeonhole principle; recurrence relations; generating functions
- **Catalan numbers**, Stirling numbers (combinatorial structures)

### Graph Theory
- **Definitions**: graphs, digraphs, multigraphs; degree, adjacency, incidence matrices
- **Paths and connectivity**: walks, trails, paths; connected components; cut vertices, bridges
- **Trees**: characterizations; spanning trees; minimum spanning tree (Kruskal, Prim)
- **Eulerian and Hamiltonian**: Euler circuits (Königsberg); Hamilton paths (NP-complete)
- **Planar graphs**: Euler's formula $V - E + F = 2$; Kuratowski's theorem; graph coloring
- **Bipartite graphs**: König's theorem; matching theory (Hall's marriage theorem)
- **Directed graphs**: DAGs; topological sort; strongly connected components (Tarjan/Kosaraju)

### Number Theory (selected)
- Divisibility; GCD, LCM; Euclidean algorithm
- Modular arithmetic; Fermat's little theorem; Chinese remainder theorem
- Primality; RSA cryptosystem sketch — see [[cryptography]]

### Algorithms Connections
- Big-O notation defined rigorously here (mathematical framework for [[algorithms-and-data-structures]])
- Graph algorithms (BFS, DFS, Dijkstra) have correctness proofs via graph theory
- NP-completeness: reductions; Cook's theorem (SAT is NP-complete)

## OR Relevance

- **Network flows** are applied graph theory — max-flow/min-cut, network simplex: see [[network-flows]]
- **Integer programming** models on graphs: vertex cover, independent set, set cover — see [[integer-programming]]
- **Matching theory** applies to assignment problems: bipartite matching = Hungarian algorithm
- **Combinatorial optimization**: TSP, VRP, facility location are all graph/combinatorics problems

## Related Concepts

- [[algorithms-and-data-structures]]
- [[network-flows]]
- [[integer-programming]]
- [[cryptography]]

## Source Materials

- MATH2343 Course Materials
