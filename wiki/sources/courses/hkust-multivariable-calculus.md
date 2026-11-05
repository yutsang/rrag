---
title: "HKUST Multivariable Calculus"
full_name: "HKUST Multivariable Calculus (MATH2011/2023)"
type: source
tags: [courses, math, undergraduate, calculus, multivariable, math2011, math2023, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH2011"
confidence: medium
---

## 概述

MATH2011 多變量微積分為香港科技大學理工科二年級學生提供向量微積分的完整訓練，以 Stewart《多變量微積分》或 Marsden & Tromba《向量微積分》為教材，先修要求為 MATH1013 微積分 II。課程系統涵蓋多變量函數的偏微分與方向導數、Hessian 矩陣與多變量優化、重積分（含 Jacobian 換元）、向量場的散度與旋度，以及 Green 定理、Stokes 定理與散度定理（Gauss 定理）這三大向量積分定理。MATH2023 榮譽版在相同框架下加入更嚴格的 $\epsilon$-$\delta$ 分析與微分形式初步。學生完成課程後能夠計算高維空間的面積分與體積分、求解帶約束的極值問題（Lagrange 乘數法），並理解梯度向量場的保守性與位勢函數。這些工具是機器學習梯度下降法的幾何基礎、流體力學與電磁學的數學語言，亦直接連結運籌學中非線性規劃的 KKT 最優性條件。

## Course Structure

| Course | Content | Audience |
|---|---|---|
| MATH2011 | Multivariable calculus (standard) | Science/Engineering |
| MATH2023 | Multivariable calculus (advanced/honors) | High-achievers |

## Key Topics

### Vector-Valued Functions
- Parametric curves in $\mathbb{R}^2$ and $\mathbb{R}^3$: position, velocity, acceleration
- Arc length, curvature, unit tangent/normal/binormal vectors (Frenet-Serret)
- Space curves: helices, lemniscates

### Partial Derivatives
- Limits and continuity in $\mathbb{R}^n$; partial derivatives definition
- Higher-order partial derivatives; Clairaut's theorem (symmetry of mixed partials)
- Chain rule for multivariable functions: tree diagram method
- Directional derivatives and gradient $\nabla f$; gradient points in direction of steepest ascent
- Tangent planes and linear approximation

### Optimization in Multiple Variables
- Critical points: $\nabla f = 0$; second-derivative test via Hessian matrix
- **Lagrange multipliers**: constrained optimization $\nabla f = \lambda \nabla g$; multiple constraints
- Global extrema on closed bounded regions

### Multiple Integrals
- **Double integrals**: Fubini's theorem; iterated integrals; polar coordinates
- Applications: area, volume, mass, center of mass, moments of inertia
- **Triple integrals**: cylindrical and spherical coordinates; Jacobian of transformation
- Change of variables: $\iint_R f \,dA = \iint_S f(g(u,v),h(u,v)) |J| \,du\,dv$

### Vector Calculus
- **Vector fields**: gradient, divergence $\nabla \cdot \mathbf{F}$, curl $\nabla \times \mathbf{F}$
- **Line integrals**: work $\int_C \mathbf{F} \cdot d\mathbf{r}$; scalar line integrals for arc length/mass
- **Green's theorem**: $\oint_C P\,dx + Q\,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$
- **Surface integrals**: flux $\iint_S \mathbf{F} \cdot d\mathbf{S}$; parametric surfaces
- **Stokes' theorem**: $\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$
- **Divergence theorem** (Gauss): $\oiint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V (\nabla \cdot \mathbf{F}) \,dV$
- Conservative fields: $\mathbf{F} = \nabla \phi$; path independence; potential functions

## Connections to OR and Engineering

- **Gradient descent**: the negative gradient $-\nabla f$ is the steepest descent direction — foundational for all gradient-based [[optimization]] methods including SGD, Adam
- **Lagrange multipliers** generalize to KKT conditions in constrained [[optimization]]
- **Hessian matrix** determines convexity/concavity; positive definite Hessian → local minimum
- **Jacobian** appears in sensitivity analysis of systems and in normalizing flows (ML)
- Divergence theorem is used in fluid dynamics and finite element analysis

## Related Concepts

- [[optimization]]
- [[linear-algebra]]
- [[differential-equations]]
- [[probability-theory]]

## Source Materials

- MATH2011 Course Materials
