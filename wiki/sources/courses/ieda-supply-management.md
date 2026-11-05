---
title: "IEDA 4100 Supply Management"
full_name: "IELM/IEDA 4100: Integrated Production Systems"
type: source
tags: [courses, ieda, undergraduate, supply-chain, production, inventory, ieda4100, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA4100/ESU_Source/IELM4100_Syllabus.pdf"
confidence: high
author: "Qian Liu"
date_published: "2017-01-01"
---

## 概述

IEDA 4100（原 IELM 4100）「整合生產系統」是香港科技大學 IEDA 學系四年級本科生的核心必修課，由劉倩教授於 2017 年春季主講，採用 Nahmias & Olsen 的《Production and Operations Analysis》（Waveland Press，第 7 版，2015）為教材。課程沿生產計劃的層級結構系統展開，涵蓋需求預測（移動平均、指數平滑、Holt 趨勢法、Holt-Winters 季節法、迴歸預測、MAE/MAPE/MSE 誤差指標）、總體計劃（追趕 vs. 平準策略的線性規劃建模）、庫存控制（確定性 EOQ/EPQ/數量折扣，以及隨機性 (s,Q)、(s,S) 與週期回顧 (R,S) 策略、Type I/II 服務水準）、物料需求計劃（MRP BOM 展開、毛需求/淨需求/計劃訂單）與準時生產（JIT 看板系統、SMED 快速換模、平準化 Heijunka）、作業排程（SPT/EDD/WSPT 單機規則、Johnson 雙機流程型排程）及專案排程（CPM 關鍵路徑計算、PERT Beta 分佈、趕工線性規劃）。評核為作業（10%）、兩次小測（5%）、期中（35%）及期末考試（50%），是 IEDA 3460（需求供應分析）的定量延伸，並與 IEDA 4420（動態定價）共同構成供應鏈管理的完整本科框架。

## Course Overview

**IELM/IEDA 4100 Integrated Production Systems** (Spring 2017, Prof. Qian Liu) studies the fundamental concepts and principles of integrated production systems. Students learn to apply quantitative models to production management across the full planning hierarchy — from long-horizon aggregate plans down to day-to-day scheduling decisions.

**Textbook**: Nahmias & Olsen, *Production and Operations Analysis*, Waveland Press, 7th Ed. (2015).

## Course Outline

| Module | Topic | Duration |
|--------|-------|----------|
| 1 | Forecasting | 1.5 weeks |
| 2 | Aggregate Planning | 2 weeks |
| 3 | Inventory Control | 3.5 weeks |
| 4 | Push and Pull Production: MRP and JIT | 1.5 weeks |
| 5 | Operations Scheduling | 2.5 weeks |
| 6 | Project Scheduling | 1.5 weeks |

## Key Topics

### Forecasting (Module 1)

Production planning begins with demand forecasting. Methods covered:
- **Moving averages**: simple MA smooths noise; weighted MA emphasizes recent observations.
- **Exponential smoothing**: Ft+1 = αDt + (1−α)Ft. The smoothing parameter α controls the speed of adaptation.
- **Holt's method**: extends exponential smoothing to capture trend via a second smoothing equation.
- **Holt-Winters**: further extends to capture seasonality.
- **Regression-based forecasting**: when causal variables (price, promotions) are available.

Forecast error metrics: MAE, MAPE, MSE, tracking signal. See [[wiki/concepts/arma-models|ARMA Models]] for time series foundations.

### Aggregate Planning (Module 2)

**Aggregate planning** determines workforce level, production rate, and inventory level over a medium horizon (3–18 months) to minimize total cost. The LP formulation:

Minimize: Σ_t [c_p · P_t + c_h · I_t + c_w · W_t + c_f · F_t + c_o · O_t]

Subject to: inventory balance (I_t = I_{t-1} + P_t − D_t), workforce balance (W_t = W_{t-1} + H_t − F_t), capacity constraints.

Where P = production, I = inventory, W = workforce, H = hires, F = fires, O = overtime.

**Chase vs. level strategies**: pure chase varies production to match demand (minimal inventory, high hiring/firing costs); pure level keeps production constant (high inventory costs, stable workforce).

### Inventory Control (Module 3)

The largest module, covering deterministic and stochastic inventory models:

**Deterministic models**:
- **EOQ (Economic Order Quantity)**: Q* = √(2DS/H). Balances ordering cost S against holding cost H per unit per year. See [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] for stochastic extension.
- **EOQ with quantity discounts**: evaluate total cost at breakpoints.
- **Production lot sizing (EPQ)**: Q* = √(2DS / H(1 − d/p)) where d/p is the ratio of demand to production rate.

**Stochastic models**:
- **(s, Q) policy**: place order Q when inventory hits reorder point s. Safety stock s_s = z_α · σ_L where z_α is the service-level z-score.
- **(s, S) policy**: order-up-to S when inventory falls below s. Optimal under fixed ordering costs.
- **Periodic review (R, S) policy**: every R periods, order up to S. Requires safety stock to cover R + L periods of demand uncertainty.
- **Service levels**: Type I (cycle service level = probability of no stockout per cycle) vs. Type II (fill rate = fraction of demand satisfied immediately).

### MRP and JIT (Module 4)

**Material Requirements Planning (MRP)** is a push system:
- Explodes the **Bill of Materials (BOM)** to derive dependent demand for components.
- **Gross requirements** minus on-hand and scheduled receipts = **net requirements**.
- **Planned order releases** offset net requirements by lead time.
- MRP-II extends to capacity requirements planning (CRP).

**Just-In-Time (JIT)** is a pull system:
- The **kanban** system: a withdrawal kanban authorizes movement; a production kanban authorizes manufacturing. Inventory is held only between adjacent stages.
- JIT requires stable, level demand schedules (heijunka), small lot sizes, fast setups (SMED), and reliable supplier relationships.
- JIT vs. MRP trade-off: JIT excels for repetitive manufacturing with stable demand; MRP better for complex assemblies with variable demand.

### Operations Scheduling (Module 5)

Single-machine scheduling with n jobs, each with processing time p_j, due date d_j, and weight w_j:
- **SPT rule**: shortest processing time first minimizes mean flow time.
- **EDD rule**: earliest due date first minimizes maximum lateness.
- **Weighted SPT (WSPT)**: sequence by w_j/p_j descending, minimizes weighted completion time.
- **Branch and bound / dynamic programming**: exact algorithms for weighted tardiness.

**Parallel machines** and **flow shop** (Johnson's algorithm for 2-machine flow shop minimizing makespan).

**Job shop scheduling**: most general setting; NP-hard in general. Dispatching rules (SPT, FIFO, CR) used in practice.

### Project Scheduling (Module 6)

**CPM (Critical Path Method)**: compute early start (ES), early finish (EF), late start (LS), late finish (LF) for each activity. The critical path is the longest path; activities on it have zero float.

**PERT (Program Evaluation and Review Technique)**: models activity durations as Beta-distributed random variables; uses mean and variance to estimate project completion distribution.

**Time-cost trade-off (crashing)**: reducing activity durations costs money; LP identifies minimum-cost crashing schedule to meet a deadline.

## Related Concepts

- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] — single-period stochastic inventory
- [[wiki/concepts/supply-chain-management|Supply Chain Management]] — broader supply chain context
- [[wiki/concepts/capacity-planning|Capacity Planning]] — aggregate planning and throughput
- [[wiki/concepts/queueing-theory|Queueing Theory]] — service systems and job shop analysis
- [[wiki/concepts/arma-models|ARMA Models]] — time series forecasting foundations

## Source Materials

- raw/courses/IEDA/IEDA4100/ESU_Source/IELM4100_Syllabus.pdf
