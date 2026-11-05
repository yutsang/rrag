---
title: "IEDA 4130 System Simulation"
full_name: "IEDA 4130: System Simulation"
type: source
tags: [courses, ieda, undergraduate, simulation, monte-carlo, stochastic, ieda4130, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4130/2022S/IEDA4130_syllabus_2022.pdf"
confidence: high
author: "Shuoguang Yang"
date_published: "2022-01-01"
---

## 概述

IEDA 4130「系統模擬」是香港科技大學 IEDA 學系四年級本科生的選修課，由楊碩光教授於 2022 年春季主講，前置要求為基礎概率與數理統計，採用 Sheldon Ross 的《Simulation》（Academic Press，2012）為參考教材，以 Python Jupyter Notebook 作為全程實作工具。課程圍繞三大模塊展開：隨機變數生成（反函數 CDF 法、接受-拒絕抽樣、逆映射法、泊松過程模擬）、變異數縮減技術（控制變量法最優係數 b* = Cov(Y,C)/Var(C)、對偶變量法、條件蒙地卡羅法，以及模擬輸出的信賴區間分析）及離散事件模擬（未來事件列 FEL 事件驅動範式、M/M/1 與 M/G/1 排隊系統模擬、複合泊松保險破產概率估計）。蒙地卡羅積分的標準誤差 σ/√n 與維度無關的特性，使模擬成為高維問題的首選方法，課程以此為基礎介紹金融衍生品定價（路徑依賴期權的 Monte Carlo 定價）及供應鏈庫存風險評估等前沿應用。作業要求學生在 Python 中實現、驗證並分析模擬方法，評分重視功能正確性（50%）、效率（20%）、文件說明（15%）及書面分析（15%），為 IEDA 3250（隨機模型）的分析解不存在時提供數值補充，亦是 OR 研究中模擬優化的重要工具基礎。

## Course Overview

**IEDA 4130 System Simulation** (Spring 2022, Prof. Shuoguang Yang) builds a bridge between mathematical models and real phenomena by teaching how to design, implement, and analyze computer simulations. As processor speeds improve, simulation enables studying phenomena that are intractable analytically — from queueing systems to financial models.

**Prerequisites**: Basic probability and mathematical statistics.  
**Reference**: Ross, S. (2012). *Simulation*, Academic Press.  
**Programming**: Python (Jupyter Notebook).

## Course Structure

The course is organized into three parts plus a probability review.

| Part | Topics |
|------|--------|
| 0 | Probability review |
| 1 | Generating random variables |
| 2 | Efficiency improvement (variance reduction) |
| 3 | Simulating processes |

## Key Topics

### Part 0: Probability Review

Refresher on probability distributions, expectations, moments, and convergence — essential foundations for interpreting simulation output. Key distributions in simulation: Uniform (basis for all generation), Exponential (inter-arrival times), Normal (central limit theorem), Poisson (arrival counts).

### Part 1: Generating Random Variables

All simulation ultimately relies on generating pseudo-random numbers uniform on [0,1] and transforming them into the desired distribution.

**Continuous distributions**:
- **Inverse CDF method**: if U ~ Uniform[0,1], then X = F⁻¹(U) has CDF F. Simple and exact when F⁻¹ is available analytically (exponential: X = −(1/λ)ln U).
- **Acceptance-rejection sampling**: generate (X, Y) pairs and accept X when Y ≤ f(X)/cg(X) for envelope function cg. Efficiency = 1/c.

**Discrete distributions**: direct inversion using cumulative probability table. For Poisson: exploit relationship to exponential inter-event times.

**Monte Carlo integration**: estimate ∫f(x)dx ≈ (1/n)Σf(X_i) for X_i ~ Uniform. The standard error is σ/√n — accuracy improves as 1/√n regardless of dimension, making Monte Carlo the method of choice in high dimensions.

### Part 2: Variance Reduction Techniques

Naive Monte Carlo has standard error σ/√n. Variance reduction methods achieve the same accuracy with fewer samples:

**Control variates**: if C is a control variable with known mean μ_C correlated with the estimator Y, use Ỹ = Y − b(C − μ_C). The optimal b* = Cov(Y,C)/Var(C) minimizes variance. Variance reduction factor: 1 − ρ²(Y,C) where ρ is the correlation.

**Antithetic variates**: use paired samples (U, 1−U) instead of independent U₁, U₂. If f is monotone in U, the antithetic pairs are negatively correlated, reducing variance. Var(Ỹ_antithetic) = [Var(Y) + Cov(Y₁,Y₂)]/2 < Var(Y)/2 when Cov < 0.

**Conditional Monte Carlo**: replace E[Y] = E[E[Y|Z]] with the conditional expectation E[Y|Z=z] evaluated analytically. By the law of total variance, Var(E[Y|Z]) ≤ Var(Y).

**Statistical analysis of output**: sample mean and sample variance, confidence intervals, run length determination.

### Part 3: Simulating Processes

**Poisson processes**: inter-arrival times are i.i.d. Exp(λ). Simulation: generate N(t) as the number of Exp(λ) inter-arrivals summing to ≤ t.

**Discrete-event simulation (DES)**: the event-driven paradigm. Maintain a **future event list (FEL)** sorted by event time. At each step: remove earliest event, update state, schedule new events, advance simulated clock. Avoids simulating idle periods.

**Queueing systems**: simulate M/M/1, M/G/1, and network queues. Track server utilization, mean queue length, mean waiting time. Verify against analytical results (Little's Law: L = λW; M/M/1: W = 1/(μ−λ)). See [[wiki/concepts/queueing-theory|Queueing Theory]].

**Insurance model**: simulate aggregate claims process (compound Poisson) to estimate ruin probability — an application of simulation to risk theory.

## Connection to Broader Methods

Simulation fills the gap when analytical methods fail:
- Queueing networks with non-exponential service times have no closed-form solutions — simulation is the only recourse.
- Financial derivatives pricing: Monte Carlo simulation (see IEDA 4331, Black-Scholes) is standard for path-dependent options where closed forms don't exist.
- Supply chain risk: simulate stochastic demand and supply disruptions to estimate fill rates and costs beyond what the [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] captures analytically.

## Related Concepts

- [[wiki/concepts/queueing-theory|Queueing Theory]] — analytical models that simulation can verify and extend
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — stochastic inventory; simulation handles complex demand distributions
- [[wiki/concepts/arma-models|ARMA Models]] — time series processes amenable to simulation

## Source Materials

- raw/courses/IEDA/IEDA4130/2022S/IEDA4130_syllabus_2022.pdf
