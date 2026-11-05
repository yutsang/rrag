---
title: "HKUST Stochastic Modeling"
full_name: "HKUST Stochastic Modeling (MATH4432/IEDA3250 overlap)"
type: source
tags: [courses, math, undergraduate, stochastic-processes, markov-chains, queueing, math4432, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH4432"
confidence: medium
---

## 概述

MATH4432 隨機過程為數學系四年級學生提供馬可夫鏈、泊松過程、鞅論及更新理論的嚴格數學處理，先修要求為 MATH2411 概率論及 MATH2111 線性代數。本課程以 Ross《隨機過程導論》或 Durrett《概率：理論與範例》為參考教材，相較於工業工程系 IEDA3250 的應用導向，更注重測度論基礎、極限定理的嚴格證明及收斂性分析。學生完成課程後能夠分析離散時間與連續時間馬可夫鏈的穩態分佈與混合時間、推導 M/M/1 及 M/M/c 排隊模型的精確解、運用鞅的可選停止定理解決賭徒破產等問題，以及理解更新獎勵過程在庫存與替換策略中的長期均值分析。布朗運動一節引入 Itô 積分的直覺，為 MATH4424 金融數學及隨機最優控制課程搭建橋梁；鞅與風險中性定價的聯繫亦使本課程成為量化金融研究的重要基礎。

## Course Overview

MATH4432 provides a more mathematically rigorous treatment of stochastic processes than IEDA3250, with greater emphasis on martingales, optional stopping, and the connection to measure theory.

## Key Topics

### Discrete-Time Markov Chains (Rigorous)
- Transition matrices; Chapman-Kolmogorov equations
- Communication classes; irreducibility; aperiodicity
- Recurrence and transience: criteria via first-passage times; classification of random walks
- Stationary distributions: existence and uniqueness for irreducible aperiodic chains
- **Convergence theorem**: $\pi^{(n)} \to \pi$ (mixing time, spectral gap)
- Time-reversibility; detailed balance equations
- Absorption: absorbing states, fundamental matrix $N = (I-Q)^{-1}$, expected absorption time

### Poisson Process (Rigorous)
- Characterizations: independent increments, stationary increments, exponential inter-arrival
- Superposition, thinning, conditioning (order statistics property)
- Compound Poisson processes; Poisson random measures
- Non-homogeneous Poisson processes

### Continuous-Time Markov Chains
- Generator matrix $Q$; Kolmogorov forward/backward equations
- Embedded jump chain; holding times
- Stationary distributions; balance equations
- Birth-death chains: M/M/1, M/M/$c$ queues with full derivations

### Martingales
- Definition: $E[X_{n+1} | \mathcal{F}_n] = X_n$
- Optional stopping theorem: conditions and applications
- Doob's martingale convergence theorem
- Applications: gambler's ruin, stopping times, Wald's identity

### Renewal Theory
- Renewal processes; elementary renewal theorem: $m(t)/t \to 1/\mu$
- Key renewal theorem; residual and age distributions
- Renewal reward processes
- Applications: long-run average cost in inventory/replacement models

### Brownian Motion (Introduction)
- Definition via independent increments and Gaussian distributions
- Continuity but non-differentiability; quadratic variation
- Reflection principle; first-passage distribution
- Connection to random walk scaling limit
- Introduction to Itô integral — see [[stochastic-calculus]]

## Connection to Finance

- Geometric Brownian motion as stock price model: $dS = \mu S\,dt + \sigma S\,dW$ — see [[stochastic-calculus]] and [[options-pricing]]
- Martingales and risk-neutral pricing: absence of arbitrage ↔ existence of equivalent martingale measure
- Markov chains in credit rating migration models — see [[fixed-income]]

## Related Concepts

- [[stochastic-processes]]
- [[stochastic-calculus]]
- [[queueing-theory]]
- [[options-pricing]]

## Source Materials

- MATH4432 Course Materials
