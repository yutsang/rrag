---
title: "HKUST Calculus Sequence"
full_name: "HKUST Calculus Sequence (MATH1003/1012/1013/1014/1023/1024)"
type: source
tags: [courses, math, undergraduate, calculus, math1003, math1012, math1013, math1014, math1023, math1024, level-1]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH"
confidence: medium
---

## 概述

香港科技大學微積分序列課程為理工科學生提供極限、微分、積分及級數的系統訓練，是大學理工科課程的最核心數學基礎。MATH1003（微積分及線性代數）為商科及部分工科學生提供入門，而 MATH1012/1013/1014/1023/1024 則構成工程及理科學生的完整微積分序列，從單變量微積分到多變量延伸，涵蓋向量幾何、偏導數及重積分。課程以 Stewart《微積分》或 Apostol《數學分析》（榮譽班）為標準教材，搭配每週習題課鞏固計算技能。學生在課程中掌握函數極限的 $\varepsilon$-$\delta$ 定義、各類微分與積分技巧（分部積分、三角換元、部分分式）、冪級數展開及 Taylor 近似，以及 Lagrange 乘數法等約束最優化工具。這些技術直接支撐後續的運籌學優化課程（KKT 條件、梯度方法）、數值分析及機器學習中的梯度下降演算法，是理工科所有定量課程的共同語言。

## Course Structure

| Course | Content | Audience |
|---|---|---|
| MATH1003 | Single-variable calculus + linear algebra intro | Business, some engineering |
| MATH1012 | Calculus I (limits, differentiation, integration) | Science/Engineering |
| MATH1013 | Calculus II (integration techniques, sequences, series) | Science/Engineering |
| MATH1014 | Calculus III (multivariable intro, partial derivatives) | Science/Engineering |
| MATH1023 | Honors Calculus I | High-achievers (BEng/BSc) |
| MATH1024 | Honors Calculus II | High-achievers |

## Key Topics

### Single-Variable Calculus (MATH1012/1013)
- **Limits**: epsilon-delta definition, L'Hôpital's rule, continuity, intermediate value theorem
- **Differentiation**: product/quotient/chain rules, implicit differentiation, related rates
- **Applications**: optimization (first and second derivative tests), curve sketching, Newton's method
- **Integration**: Riemann sums, fundamental theorem of calculus, substitution, integration by parts
- **Techniques**: partial fractions, trigonometric substitution, improper integrals
- **Sequences and series**: convergence tests (comparison, ratio, root, integral), Taylor/Maclaurin series, radius of convergence

### Multivariable Calculus Intro (MATH1014)
- Vectors in $\mathbb{R}^3$: dot product, cross product, lines and planes
- Partial derivatives, gradient, directional derivatives
- Chain rule for multivariable functions
- Unconstrained optimization: critical points, second-derivative test (Hessian)
- Lagrange multipliers for constrained optimization
- Double and triple integrals, Jacobian, change of variables

## OR Relevance

- Calculus is the prerequisite for [[optimization]] (gradient methods require derivatives)
- Taylor expansion underlies sensitivity analysis in LP
- Lagrange multipliers = KKT conditions in [[linear-programming]] and convex [[optimization]]
- Series convergence is needed for geometric series formulas in [[time-value-of-money]]

## Related Concepts

- [[optimization]]
- [[linear-algebra]]
- [[differential-equations]]
- [[probability-theory]]
