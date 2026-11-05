---
title: "Fundamentals of Artificial Intelligence"
full_name: "COMP3211 Fundamentals of Artificial Intelligence"
type: source
tags: [courses, comp, undergraduate, artificial-intelligence, search, machine-learning, comp3211, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP3211"
confidence: medium
---

## 概述

COMP3211 人工智能基礎為計算機科學三年級學生提供 AI 的系統性入門，以 Russell & Norvig《人工智能：一種現代方法》（AIMA，第四版）為標準教材，先修要求為 COMP2012 資料結構及 MATH2411/COMP2711 離散數學與概率論基礎。課程遵循 AIMA 的架構，依序涵蓋理性代理的 PEAS 框架、無信息搜索（BFS、DFS、IDA*）與啟發式搜索（A*）、對抗性搜索（minimax 與 alpha-beta 剪枝）、知識表示（命題邏輯、一階邏輯）、貝葉斯網絡的概率推理，以及決策樹、朴素貝葉斯和神經網絡的機器學習入門。學生完成課程後能夠設計並分析搜索算法、建構貝葉斯信念網絡進行診斷推理、實作基本分類器，並理解 AI 系統設計中的探索-利用（exploration-exploitation）權衡。COMP3211 是後續 COMP4211 機器學習、COMP4901 深度學習及自然語言處理課程的核心先修科目，其搜索與規劃技術亦直接關聯運籌學中的啟發式算法與組合優化求解器設計。

## Course Overview

**Textbook**: Russell & Norvig, *Artificial Intelligence: A Modern Approach* (AIMA)
**Lecture Topics**: Introduction, Agents, Search, Games, Machine Learning, Knowledge Representation & Reasoning, Uncertainty

Classical AI curriculum following the AIMA structure. Covers both search-based and knowledge-based AI, plus a machine learning module.

## Key Topics

### 1. Introduction and Intelligent Agents
- Definitions of AI: thinking/acting humanly vs. rationally
- **Rational agent**: perceives environment via sensors; acts via actuators to maximize performance measure
- **PEAS framework**: Performance, Environment, Actuators, Sensors
- Environment types: fully vs. partially observable; deterministic vs. stochastic; episodic vs. sequential; static vs. dynamic; discrete vs. continuous; single vs. multi-agent

### 2. Search Algorithms
**Uninformed Search**:
- Problem formulation: state space, initial state, goal test, actions, transition model, path cost
- BFS: complete, optimal (unit cost); time/space $O(b^d)$
- DFS: not complete (infinite spaces), not optimal; space $O(bm)$
- Iterative deepening DFS (IDDFS): combines BFS completeness with DFS space efficiency
- Uniform Cost Search (Dijkstra): optimal for general costs

**Informed (Heuristic) Search**:
- Greedy best-first search: $f(n) = h(n)$; not optimal
- **A* search**: $f(n) = g(n) + h(n)$; optimal and complete if $h$ is admissible (never overestimates)
- Consistent heuristic: monotone; ensures A* expands nodes in non-decreasing f order
- Heuristic design: relaxed problems (8-puzzle: misplaced tiles, Manhattan distance)
- See [[algorithms-and-data-structures]]

### 3. Games and Adversarial Search
- Two-player zero-sum games; minimax algorithm: MAX maximizes, MIN minimizes
- **Alpha-beta pruning**: eliminates branches that cannot affect result; reduces effective depth
- Expectiminimax for stochastic games (backgammon)
- Evaluation functions for non-terminal states: material advantage in chess
- Monte Carlo Tree Search (MCTS): used in AlphaGo
- See [[game-theory]]

### 4. Machine Learning
- Supervised learning: classification, regression; training/test/validation split
- **Decision trees**: ID3 algorithm; information gain; Quinlan's C4.5; pruning — see [[decision-trees]]
- **Naïve Bayes**: probabilistic classifier; conditional independence assumption
- **Neural networks**: perceptron; backpropagation; multi-layer (intro to deep learning) — see [[machine-learning-advanced]]
- Unsupervised learning: k-means clustering; hierarchical clustering — see [[clustering]]
- Overfitting: bias-variance tradeoff; cross-validation; regularization

### 5. Knowledge Representation and Reasoning
- Propositional logic: resolution; DPLL algorithm for satisfiability
- First-order logic (FOL): quantifiers; predicates; unification; forward/backward chaining
- **Knowledge graphs**: entities, relations, triples; ontologies (OWL, RDF)
- Planning: STRIPS representation; state-space search for plans

### 6. Uncertainty and Probabilistic Reasoning
- Probability basics; Bayes' rule applied to AI diagnosis
- **Bayesian networks**: directed acyclic graphs; conditional independence; d-separation
- Inference in Bayes nets: variable elimination; sampling methods (MCMC, rejection sampling)
- Hidden Markov Models (HMMs): filtering, prediction, smoothing (Viterbi algorithm)
- See [[probability-theory]]

## Related Concepts

- [[algorithms-and-data-structures]]
- [[machine-learning-advanced]]
- [[decision-trees]]
- [[game-theory]]
- [[nlp-basics]]

## Source Materials

- COMP3211 Course Materials
