---
title: "Statistical Quality Control"
full_name: "Statistical Quality Control (SQC)"
type: concept
tags: [quality, statistics, operations, manufacturing]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/ieda-quality-engineering"
confidence: high
---

## 概述

統計品質管制（Statistical Quality Control, SQC）應用統計方法區分製程中的普通原因變異（Common Cause Variation，固有隨機波動）與特殊原因變異（Special Cause Variation，可查明的異常），並透過管制圖、製程能力分析及接受抽樣三大工具實現製程監控與改善。管制圖源自 Shewhart（1924）的 3σ 法則：在製程受控時，99.73% 的採樣點應落於管制上下限（UCL/LCL）之內，即 μ ± 3σ/√n；EWMA 和 CUSUM 圖則對均值的小幅持續偏移更加靈敏。製程能力指數 Cp = (USL−LSL)/6σ 衡量規格寬度與製程散佈之比，Cpk = min[(USL−μ), (μ−LSL)]/3σ 同時考量製程偏心，六標準差品質要求 Cpk ≥ 2.0，對應每百萬機會 3.4 個缺陷（DPMO）。接受抽樣以操作特性曲線（OC Curve）描述不同批次不良率下的接受機率，平衡生產者風險（α，拒絕良批）與消費者風險（β，接受劣批）。實驗設計（DOE）包括全因子設計、分數因子設計及田口方法，用於識別影響品質的關鍵因子並優化製程參數。SQC 是六標準差 DMAIC 方法論的定量骨幹，與假設檢定、線性迴歸及 A/B 測試緊密相連，在製造業、醫療照護、服務流程及軟體開發品質管理中廣泛應用。

## What It Is

**Statistical Quality Control (SQC)** uses statistical methods to monitor, control, and improve process quality. It distinguishes between:
- **Common cause variation**: inherent random fluctuation (stable process)
- **Special cause variation**: assignable, unusual causes (process out of control)

The goal: detect special causes quickly while not over-reacting to common cause noise.

## Control Charts (Statistical Process Control)

A **control chart** plots a quality characteristic over time with:
- **Center line (CL)**: process mean $\mu$
- **Upper control limit (UCL)** = $\mu + 3\sigma/\sqrt{n}$
- **Lower control limit (LCL)** = $\mu - 3\sigma/\sqrt{n}$

The $3\sigma$ rule: if the process is in control, 99.73% of points fall within limits (false alarm rate = 0.27%).

### Variable Control Charts (for measurements)

**$\bar{X}$-chart** (mean chart): monitors the process mean. Plot sample means $\bar{X}_i$ for subgroups of size $n$.

**$R$-chart** (range chart): monitors process variability. Plot sample range $R_i = X_{\max} - X_{\min}$ within each subgroup.

**$S$-chart**: uses sample standard deviation instead of range — preferred for $n > 10$.

**EWMA (Exponentially Weighted Moving Average) chart**: $Z_t = \lambda \bar{X}_t + (1-\lambda) Z_{t-1}$. More sensitive to small persistent shifts than Shewhart $\bar{X}$-chart.

**CUSUM (Cumulative Sum) chart**: optimal for detecting small, sustained process shifts. Tracks cumulative deviations from target.

### Attribute Control Charts (for counts/proportions)

**$p$-chart**: proportion defective. $UCL = \bar{p} + 3\sqrt{\bar{p}(1-\bar{p})/n}$.

**$np$-chart**: number of defectives (fixed sample size $n$).

**$c$-chart**: count of defects per unit (Poisson model). $UCL = \bar{c} + 3\sqrt{\bar{c}}$.

**$u$-chart**: defects per unit (variable sample size).

### Out-of-Control Signals (Western Electric Rules)
Beyond simple UCL/LCL violation:
- 2 of 3 points beyond $2\sigma$ on same side
- 4 of 5 points beyond $1\sigma$ on same side
- 8 consecutive points on same side of CL (process shift)
- 6 consecutive points trending up or down (drift)

## Process Capability

Process capability indices measure whether a process can consistently meet specifications:

| Index | Formula | Meaning |
|---|---|---|
| $C_p$ | $(USL - LSL) / 6\sigma$ | Spread of specs vs. process spread |
| $C_{pk}$ | $\min[(USL-\mu), (\mu-LSL)] / 3\sigma$ | Worst-case capability (accounts for centering) |
| $C_{pm}$ | Cpm adjusts for distance from target | Target-oriented |

**Six Sigma quality**: $C_{pk} = 2.0$ (process spread is $\pm 6\sigma$ within specs). In practice, allows for $1.5\sigma$ shift → 3.4 defects per million opportunities (DPMO).

**Benchmarks**: $C_{pk} \geq 1.33$ (4-sigma) is minimum for capable process; $\geq 1.67$ for critical processes.

## Acceptance Sampling

Decide whether to accept or reject a lot based on a sample — used when 100% inspection is too expensive.

**Sampling plan** $(n, c)$: draw sample of size $n$; accept lot if defectives $\leq c$.

**Operating Characteristic (OC) curve**: $P(\text{accept} \mid p)$ as function of lot proportion defective $p$.

- **AQL (Acceptable Quality Level)**: $p$ at which high probability of acceptance ($1-\alpha$)
- **LTPD (Lot Tolerance Percent Defective)**: $p$ at which low probability of acceptance ($\beta$)
- **Producer's risk** $\alpha$: reject a good lot (Type I error)
- **Consumer's risk** $\beta$: accept a bad lot (Type II error)

**MIL-STD-1916**, **ISO 2859**: standardized sampling plans used in defense and manufacturing.

## Design of Experiments (DOE)

Use designed experiments to identify which factors affect quality:

**Full factorial**: test all combinations of $k$ factors at $l$ levels. $l^k$ runs. Identifies main effects and interactions.

**Fractional factorial** ($2^{k-p}$ design): test a fraction of combinations. Confounds some higher-order interactions (acceptable if these are negligible).

**Response surface methodology**: find optimal settings for continuous factors using first- and second-order polynomial models. Central composite designs.

**Taguchi methods**: robust design — minimize sensitivity of output to uncontrollable noise factors by choosing controllable factor levels.

## Six Sigma (DMAIC)

Six Sigma as a management methodology for quality improvement:
1. **Define**: project scope, customer requirements, CTQ (critical to quality) metrics
2. **Measure**: current process performance, measurement system analysis (MSA/Gage R&R)
3. **Analyze**: root cause analysis (fishbone diagram, 5 Whys), hypothesis testing to confirm causes
4. **Improve**: DOE to find optimal settings, pilot solution
5. **Control**: control charts, control plan, standard operating procedures

## Limitations and Common Pitfalls

1. **3σ limits assume normality**: the $\bar{X}$-chart's false alarm rate of 0.27% is exact only for normally distributed data. Skewed or heavy-tailed processes (e.g., cycle times, defect counts) may require transformed charts or non-parametric alternatives.
2. **Phase I vs. Phase II distinction**: control limits must be established from in-control retrospective data (Phase I) before being used for prospective monitoring (Phase II). Using the same data for both inflates false alarm rates.
3. **Autocorrelation**: traditional control charts assume i.i.d. observations. Autocorrelated processes (chemical processes, high-frequency manufacturing) produce many false alarms; ARIMA-residual charts or EWMA with adjusted parameters are needed.
4. **$C_p$ vs. $C_{pk}$ confusion**: $C_p$ ignores process centering — a high $C_p$ with a poorly centered process still produces many defects. Always report both; $C_{pk}$ is the operational capability measure.
5. **Acceptance sampling is not a substitute for process control**: sampling inspects the past; control charts prevent future defects. Deming argued that incoming inspection is economically wasteful once supplier processes are capable.
6. **DOE requires careful planning**: variance reduction and confounding structure must be decided before running experiments. Post-hoc analysis of unplanned data cannot recover the statistical properties of a designed experiment.

## OR Research Connections

SQC connects to several OR research streams:

- **Optimal stopping / sequential testing**: control chart design is a sequential hypothesis testing problem. CUSUM charts are optimal (Wald's SPRT) for detecting a specified shift magnitude with minimum expected sample size.
- **Markov chain models of process control**: the run-length distribution of a Shewhart chart follows a geometric distribution; more complex charts (EWMA, CUSUM) require DTMC analysis to compute ARL (Average Run Length) — the expected number of samples before a signal.
- **Economic design of control charts**: jointly optimize sample size $n$, sampling interval $h$, and control limits $k$ to minimize total expected cost (sampling cost + false alarm cost + quality loss). Duncan's model (1956) is the classical formulation; extensions include Taguchi loss functions and Bayesian updating of shift probabilities.
- **Inspection and sampling theory**: acceptance sampling connects to reliability theory and Bayesian quality inference; sequential sampling plans extend to multi-stage inspection with early stopping.

## Related Concepts

- [[capacity-planning]]
- [[ab-testing]]
- [[hypothesis-testing]]
- [[probability-theory]]
- [[linear-regression]]
- [[stochastic-processes]]
- [[simulation]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
