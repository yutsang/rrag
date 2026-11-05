---
title: "Quality Engineering"
full_name: "IEDA3270 Quality Engineering"
type: source
tags: [courses, ieda, undergraduate, quality, statistics, ieda3270, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3270"
confidence: medium
---

## 概述

IEDA 3270「品質工程」是香港科技大學 IEDA 學系三年級本科生的必修課，以 IEDA 2520 及 IEDA 2540 的概率統計知識為前置基礎。課程將統計方法應用於製造與服務流程的品質監控與持續改善，涵蓋統計製程管制（SPC）：X̄-chart、R-chart、S-chart 等計量型管制圖及 p-chart、c-chart 等計數型管制圖、失控信號規則（Western Electric rules）、CUSUM 與 EWMA 圖；製程能力分析（Cp、Cpk、Cpm 指標及六標準差 3.4 DPMO 目標）；驗收抽樣（OC 曲線、生產者與消費者風險、AQL、MIL-STD-105E）；以及試驗設計（DOE）：全因子 2k 設計、部分因子設計（分辨度、混淆）、響應曲面法及 Taguchi 參數設計。課程使用的主要教材通常為 Montgomery 的《Introduction to Statistical Quality Control》，為六標準差（DMAIC）方法論提供完整的定量基礎，並廣泛應用於電子製造、醫療設備及服務業品質管理等場景，是工業工程師進入業界或深造研究的核心統計應用技能。

## Course Overview

IEDA3270 bridges probability/statistics theory (from IEDA2520/2540) with practical quality management in manufacturing and service contexts. The course emphasizes statistical thinking for process improvement.

## Key Topics

### Statistical Foundations for Quality
- Descriptive statistics: histograms, box plots, Pareto charts
- Probability distributions relevant to quality: Normal, Binomial, Poisson, Exponential
- Hypothesis testing for quality decisions: z-test, t-test, F-test, chi-square
- Confidence intervals for process parameters

### Statistical Process Control (SPC)
- Common cause vs. special cause variation; Shewhart's rational subgrouping
- Control charts for variables: $\bar{X}$-chart, $R$-chart, $S$-chart, individual-moving range (I-MR)
- Control charts for attributes: $p$-chart, $np$-chart, $c$-chart, $u$-chart
- Control chart design: subgroup size, sampling frequency, control limits
- Out-of-control signals: Western Electric rules (beyond UCL/LCL, runs, trends)
- CUSUM and EWMA charts for detecting small shifts

### Process Capability Analysis
- Specification limits (USL, LSL) vs. control limits
- Capability indices: $C_p$, $C_{pk}$, $C_{pm}$
- Process performance vs. capability
- Six Sigma quality target: 3.4 DPMO, $C_{pk} = 2.0$

### Acceptance Sampling
- Single and double sampling plans $(n, c)$
- Operating characteristic (OC) curves
- Producer's risk ($\alpha$) and consumer's risk ($\beta$)
- AQL and LTPD; MIL-STD-105E / ISO 2859

### Design of Experiments (DOE)
- One-factor experiments: ANOVA (one-way, two-way)
- Full factorial designs: $2^k$ designs, main effects and interactions
- Fractional factorial designs: $2^{k-p}$, design resolution, aliasing
- Response surface methodology: central composite designs, steepest ascent
- Taguchi methods: signal-to-noise ratio, parameter design, tolerance design

## Related Concepts

- [[statistical-quality-control]]
- [[hypothesis-testing]]
- [[capacity-planning]]
- [[ab-testing]]
- [[probability-theory]]
