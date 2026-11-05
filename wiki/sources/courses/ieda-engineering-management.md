---
title: "IEDA 2200: Engineering Management"
full_name: "IEDA 2200 Engineering Management (formerly IELM 2200)"
type: source
tags: [courses, ieda, undergraduate, operations-management, engineering-management, ieda2200, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA2200"
confidence: high
author: "Qiu, X."
date_published: "2016-01-01"
---

## 概述

IEDA 2200「工程管理」（前身為 IELM 2200）是香港科技大學 IEDA 學系二年級本科生的核心必修課，以邱璇博士春季 2016 年開設為準，前置要求為 IEDA 2010。課程採用 Stevenson & Chuong 的《Operations Management》（第 2 版，McGraw Hill）為教材，系統介紹科學管理生產與服務的定量方法，涵蓋項目管理（CPM/PERT 關鍵路徑、趕工）、品質管理（TQM、六標準差 DMAIC、統計製程管制 SPC 管制圖）、預測（移動平均、指數平滑）、庫存管理（EOQ、安全庫存、ABC 分析）、物料需求計劃（MRP BOM 展開）、即時生產（JIT 看板系統）及供應鏈管理（牛鞭效應、供應商管理庫存 VMI）。課程評核包括作業（20%）、課堂參與（10%）、期中（30%）及期末考試（40%），並強調各方法在製造業、零售及物流實務中的應用，為後續的 IEDA 4100（整合生產系統）及 IEDA 3460（需求供應分析）提供操作管理的理論基礎。

## Course Overview

**IEDA 2200: Engineering Management** (previously IELM 2200) provides a broad grounding in the scientific management of business operations. Taught by Dr. Xuan QIU (Spring 2016), the course follows Stevenson & Chuong's *Operations Management* (2nd ed., McGraw Hill). It is a required course for IEDA undergraduates and serves as the primary operations management foundation course.

- **Prerequisite**: IEDA 2010 or equivalent
- **Reference**: William J. Stevenson and Sum Chee Chuong (2013), *Operations Management*, 2nd Edition, McGraw Hill Education (Asia)

## Course Outline

| Topic | Key Concepts |
|---|---|
| 1. Introduction | Scientific management overview; operations strategy |
| 2. Project Management | CPM, PERT, network diagrams, critical path, crashing |
| 3. Product and Service Design | Design for manufacturability, QFD, concurrent engineering |
| 4. Process Selection and Facility Layout | Flow shop vs. job shop; line balancing; cellular manufacturing |
| 5. Location Planning | Weighted factor method, center-of-gravity, transportation model |
| 6. Quality Management | TQM, Six Sigma, control charts (X-bar, R, p), acceptance sampling |
| 7. Forecasting | Moving average, exponential smoothing, trend analysis, MAD, MSE |
| 8. Inventory Management | EOQ, reorder point, safety stock, ABC analysis |
| 9. Aggregate Planning | Chase vs. level strategies, master scheduling |
| 10. MRP and JIT | Bill of materials, MRP explosion, kanban, lean principles |
| 11. Supply Chain Management | Bullwhip effect, vendor-managed inventory, coordination |

## Key Topic Summaries

### Project Management
Uses **Critical Path Method (CPM)** and **Program Evaluation and Review Technique (PERT)** to schedule activities. The critical path is the longest sequence of dependent tasks; any delay on it delays the whole project. Crashing reduces duration by adding resources at extra cost.

### Quality Management
**Total Quality Management (TQM)** emphasizes continuous improvement and customer focus. Statistical process control (SPC) uses control charts to distinguish common cause variation from special cause variation. Six Sigma targets 3.4 defects per million opportunities (DPMO) through DMAIC cycles. Connects to [[wiki/concepts/ab-testing|A/B Testing]] as a structured experiment for process improvement.

### Forecasting
Time series methods (moving averages, exponential smoothing) and causal methods (regression-based). Accuracy measured by MAD (mean absolute deviation) and MSE (mean squared error). Connects to [[wiki/concepts/arma-models|ARMA Models]] for more sophisticated time series analysis.

### Inventory Management
**Economic Order Quantity (EOQ)** balances ordering cost against holding cost. Safety stock buffers against demand and lead-time variability. **ABC analysis** prioritizes inventory items by value. Connects to [[wiki/concepts/newsvendor-problem|Newsvendor Problem]] for single-period stochastic demand.

### MRP and JIT
**Material Requirements Planning (MRP)** uses the master production schedule, bill of materials (BOM), and inventory records to plan component orders. **Just-In-Time (JIT)** / lean manufacturing pulls production based on actual demand (kanban), eliminates waste (muda), and reduces inventory buffers. JIT is a prerequisite to understanding modern [[wiki/concepts/supply-chain-management|Supply Chain Management]].

### Supply Chain Management
Covers end-to-end coordination, the **bullwhip effect** (demand amplification up the chain), vendor-managed inventory (VMI), and coordination contracts. See [[wiki/concepts/supply-chain-management|Supply Chain Management]] and [[wiki/concepts/scor-model|SCOR Model]].

## Practical Takeaways

- **Control charts** give real-time visibility into process stability — essential for any manufacturing or service operation.
- **EOQ and safety stock** formulas are simple but powerful; the real skill is estimating cost parameters accurately.
- **MRP vs. JIT** is a fundamental trade-off: MRP pushes based on forecasts; JIT pulls based on actual demand. Modern systems (ERP) attempt to combine both.
- **CPM/PERT** scales from construction projects to software releases — the network logic is universal.

## Related Concepts

- [[wiki/concepts/supply-chain-management|Supply Chain Management]]
- [[wiki/concepts/scor-model|SCOR Model]]
- [[wiki/concepts/newsvendor-problem|Newsvendor Problem]]
- [[wiki/concepts/capacity-planning|Capacity Planning]]
- [[wiki/concepts/arma-models|ARMA Models]]
- [[wiki/concepts/ab-testing|A/B Testing]]
- [[wiki/concepts/queueing-theory|Queueing Theory]]
- [[wiki/concepts/linear-regression|Linear Regression]]

## Source Materials

- raw/courses/IEDA/IEDA2200/ESU_Source/Syllabus.pdf
- raw/courses/IEDA/IEDA2200/ESU_Source/Notes/Spring 2017/
