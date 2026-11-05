---
title: "Operations Research II"
full_name: "IEDA3250 Operations Research II — Stochastic Models"
type: source
tags: [courses, ieda, undergraduate, operations-research, probability, ieda3250, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3250"
confidence: medium
---

## 概述

IEDA 3250「運籌學 II——隨機模型」是 IEDA 3010（確定性 OR）的隨機對應課程，前置要求為 IEDA 2520（概率論）及 IEDA 3010，是香港科技大學 IEDA 學系三年級本科生的核心必修課。課程系統介紹應用概率與隨機過程的四大支柱：離散時間馬可夫鏈（轉移概率矩陣、Chapman-Kolmogorov 方程、穩態分佈、平均首次通過時間、庫存 (s, S) 策略分析）、泊松過程（指數間隔時間、合併與分拆、非齊次泊松過程）、連續時間馬可夫鏈（生成矩陣 Q、全局平衡方程、生滅過程）及排隊理論（M/M/1、M/M/c Erlang-C 公式、M/G/1 Pollaczek-Khinchine 公式、Little's Law L = λW、Jackson 網絡乘積型解）。課程亦涵蓋更新理論（更新報酬定理、最優替換策略），為庫存管理、服務系統設計及設備可靠性提供嚴格的隨機建模工具。本課是 OR 博士研究中隨機控制、馬可夫決策過程及強化學習等研究方向的本科級必備基礎。

## Course Overview

IEDA3250 is the stochastic counterpart to IEDA3010, covering probabilistic OR models. Prerequisites include IEDA2520 (Probability for Engineers) and IEDA3010 (OR I).

## Key Topics

### Discrete-Time Markov Chains
- Markov property, transition probability matrix
- Chapman-Kolmogorov equations, $n$-step transitions
- State classification: transient, recurrent, absorbing
- Stationary (steady-state) distributions; balance equations
- Mean first passage times
- Application: inventory (s, S) policy analysis, Markov decision processes (intro)

### Poisson Process
- Definition: independent and stationary increments, exponential inter-arrivals
- Properties: merging, splitting, decomposition
- Non-homogeneous Poisson process
- Applications: arrival modeling for queues and inventory

### Continuous-Time Markov Chains
- Holding times, transition rates, generator matrix $Q$
- Global balance equations for steady state
- Birth-death processes (M/M/c queue as special case)

### Queueing Theory
- M/M/1: traffic intensity $\rho$, steady-state probabilities, $L$, $L_q$, $W$, $W_q$
- M/M/c: multi-server queue, Erlang-C formula, call center staffing
- M/G/1: Pollaczek-Khinchine formula, effect of service time variability
- Finite buffer queues (M/M/1/K), finite population (M/M/c//N)
- Little's Law $L = \lambda W$ (see [[littles-law]])
- Jackson networks: product-form networks, PASTA

### Renewal Theory
- Renewal process, renewal function, elementary renewal theorem
- Renewal reward theorem: long-run average rate
- Applications: optimal replacement policies

## Connections

Directly extends [[queueing-theory]] and [[stochastic-processes]] concept pages. Provides the theoretical foundation for [[capacity-planning]] and [[revenue-management]] stochastic models.

## Related Concepts

- [[stochastic-processes]]
- [[queueing-theory]]
- [[littles-law]]
- [[probability-theory]]
- [[newsvendor-problem]]
- [[capacity-planning]]
