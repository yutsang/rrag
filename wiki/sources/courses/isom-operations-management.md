---
title: "Operations Management"
full_name: "ISOM2700 Operations Management"
type: source
tags: [courses, isom, undergraduate, operations-management, supply-chain, quality, isom2700, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/ISOM/ISOM2700"
confidence: medium
---

## 概述

ISOM2700 運營管理為工商管理學院二年級學生提供生產與服務運營管理的系統知識，以 Cachon & Terwiesch《運營管理》（Operations Management，McGraw-Hill）或 Slack《運營管理》為標準參考教材，先修要求為 ISOM1500/2500 統計學及 ISOM1700 工商管理概論，是供應鏈管理、收益管理及商業分析高年級課程的核心基礎。課程以個案教學為主，透過零售（庫存管理）、航空（超訂模型）及醫療服務（排隊分析）等真實案例將理論與實踐連結，涵蓋流程分析（Little's Law、瓶頸識別）、預測方法（指數平滑、追蹤信號）、質量管理（六西格瑪 DMAIC、統計過程控制）、能力規劃（引前/滯後/平均策略）、庫存控制（EOQ 模型、報童模型的臨界比率最優解）及收益管理（EMSR 容量分配、超訂決策）。學生完成課程後能夠計算流程效率指標（產能利用率、週期時間）、建立安全庫存模型（基於服務水平的需求不確定性分析）、設計控制圖進行質量監測，以及理解收益管理中的邊際分析邏輯，為從事製造業、零售及服務業的運營改善與數據驅動決策奠定堅實基礎。

## Key Topics

### Introduction to Operations Management
- Operations function: transformation process (inputs → outputs)
- Service vs. manufacturing operations; service characteristics (IHIP)
- Competitive priorities: cost, quality, speed, flexibility
- See [[supply-chain-management]]

### Process Analysis
- Process flow diagrams; flow rate, inventory, flow time (Little's Law)
- Throughput time; cycle time; bottleneck identification
- Process improvement: eliminate waste; reduce variability
- **Little's Law**: $I = R \times T$ — inventory = throughput rate × flow time — see [[littles-law]]

### Quality Management
- Dimensions of quality: performance, reliability, conformance, durability, serviceability
- TQM principles: customer focus, continuous improvement, employee involvement
- Statistical Process Control (SPC): control charts ($\bar{X}$-chart, R-chart, p-chart) — see [[statistical-quality-control]]
- Six Sigma DMAIC methodology; process capability $C_p$, $C_{pk}$

### Capacity Planning
- Capacity measures: design, effective, actual capacity; utilization and efficiency
- Capacity cushion; capacity expansion strategies: lead, lag, average
- Break-even analysis for capacity decisions — see [[cvp-analysis]]
- Project management: CPM/PERT for capacity expansion projects

### Forecasting
- Time series decomposition: trend, seasonality, cycles, random variation
- Methods: naïve, simple moving average, weighted moving average, exponential smoothing
- Forecast error metrics: MAD, MSE, MAPE; tracking signal
- Causal forecasting: regression-based demand models

### Inventory Management
- Costs: holding, ordering, shortage costs
- EOQ model: $Q^* = \sqrt{\frac{2DS}{H}}$; reorder point $R = d \cdot L$
- Safety stock: variability in demand and lead time; service level
- Newsvendor model for perishable/single-period goods — see [[newsvendor-problem]]
- ABC analysis; cycle counting

### Revenue Management
- Perishable capacity: airlines, hotels, restaurants
- Capacity allocation; overbooking models
- Price discrimination; fare classes; EMSR — see [[revenue-management]]

## Related Concepts

- [[supply-chain-management]]
- [[littles-law]]
- [[newsvendor-problem]]
- [[revenue-management]]
- [[statistical-quality-control]]
- [[queueing-theory]]

## Source Materials

- ISOM2700 Course Materials
