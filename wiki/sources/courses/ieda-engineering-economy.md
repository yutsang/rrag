---
title: "Engineering Economy"
full_name: "IEDA3230 Engineering Economy"
type: source
tags: [courses, ieda, undergraduate, engineering-economics, finance, ieda3230, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/IEDA/IEDA3230"
confidence: medium
---

## 概述

IEDA 3230「工程經濟學」是香港科技大學 IEDA 學系三年級本科生的必修課，由陳英珠教授（Spring 2021）主講，是工業工程課程中連結工程設計與商業決策的核心橋樑科目。課程以資金時間價值（六大現值/終值/年值換算因子）為出發點，系統介紹工程投資決策的主要方法：淨現值（NPV）、內部報酬率（IRR）、等效年值（AW）及效益成本比（BCR），並涵蓋直線法、雙倍餘額遞減法、年數總和法及 MACRS 等折舊方法的稅後現金流分析。課程進一步探討通貨膨脹（名義利率與實際利率的 Fisher 方程）、風險（敏感性分析、情境分析）及決策樹分析，並以「挑戰者對抗現有設備」的替換分析（最低等效年成本）作為實務應用。資本預算的線性規劃建模將本課與 IEDA 3010（運籌學 I）連結，而折舊稅盾與 NPV 分析則為 IEDA 4330 等財務相關課程提供工程經濟基礎，是攻讀工程管理、財務工程或運籌學的學生必備的量化決策工具。

## Course Overview

**Instructor**: Ying-Ju Chen (Spring 2021)
IEDA3230 provides IE students with financial analysis tools for engineering investment decisions. It covers similar ground to EEMT5510 (Engineering Economics for Managers) but at a more technical level with greater emphasis on decision-tree analysis and real options.

## Key Topics

### Time Value of Money
- Single payment: PV, FV, compound interest
- Uniform series: present worth factor, capital recovery factor, uniform series compound amount
- Gradient series: arithmetic and geometric gradients
- Nominal vs. effective interest rates; continuous compounding

### Investment Evaluation Methods
- **Net Present Value (NPV)**: sum of discounted cash flows; see [[npv]]
- **Internal Rate of Return (IRR)**: discount rate making NPV = 0; see [[irr]]
- **Payback period**: simple and discounted; liquidity-focused
- **Benefit-Cost Ratio (BCR)**: for public sector projects
- Mutually exclusive alternatives: incremental analysis, study period

### Depreciation and Taxes
- Straight-line, declining balance, sum-of-years-digits
- MACRS (Modified Accelerated Cost Recovery System)
- After-tax cash flow analysis: tax shield from depreciation
- See [[depreciation]]

### Inflation and Risk
- Real vs. nominal interest rates; Fisher equation: $(1+i) = (1+i')(1+f)$ where $f$ is inflation
- Risk: breakeven analysis, sensitivity analysis, scenario analysis
- **Decision trees**: expected value criterion for risky decisions; real options framing

### Replacement Analysis
- Economic life: minimize equivalent annual cost (EAC)
- Challenger vs. defender; sunk cost irrelevance
- One-shot vs. repeated replacements

### Capital Budgeting with Limited Resources
- LP formulation for capital budgeting under budget constraints
- Connects to [[linear-programming]] and integer programming

## Related Concepts

- [[npv]]
- [[irr]]
- [[depreciation]]
- [[time-value-of-money]]
- [[linear-programming]]
- [[corporate-finance]]
