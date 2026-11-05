---
title: "HKUST Advanced Analysis"
full_name: "HKUST Advanced Analysis (MATH3033/4033)"
type: source
tags: [courses, math, undergraduate, real-analysis, measure-theory, functional-analysis, math3033, math4033, level-3]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH3033"
confidence: medium
---

## 概述

MATH3033 實分析與 MATH4033 度量論構成香港科技大學數學系三、四年級的高階分析序列，是數學專業課程中邏輯嚴謹性要求最高的核心課程，先修要求為 MATH2011 多變量微積分及 MATH2111 線性代數。MATH3033 以 Rudin《數學分析原理》（Baby Rudin）或 Bartle & Sherbert《實分析導論》為教材，系統建立度量空間的拓撲基礎、函數列的一致收斂理論及 Riemann-Stieltjes 積分；MATH4033 則進入 Lebesgue 測度與積分理論，涵蓋 $\sigma$-代數、單調收斂定理、Fatou 引理、控制收斂定理及 $L^p$ 空間的完備性（Riesz-Fischer 定理）。學生完成課程後具備嚴格分析不等式與收斂性的能力，並理解 Radon-Nikodym 定理（密度函數的測度論表達）這一連結概率論與分析學的核心結果。這些工具是機器學習理論（VC 維、Rademacher 複雜度的一致收斂界）、梯度下降收斂性分析及金融數學中鞅理論與 Girsanov 測度變換的數學支柱，對有志從事理論性研究的學生尤為重要。

## Course Structure

| Course | Content |
|---|---|
| MATH3033 | Real Analysis (metric spaces, sequences, integration) |
| MATH4033 | Measure Theory and Integration |

## Key Topics

### MATH3033: Real Analysis

**Metric Spaces**:
- Definition; open/closed sets; convergence; Cauchy sequences; completeness
- Compact sets: sequential compactness, Heine-Borel theorem in $\mathbb{R}^n$
- Continuous functions on compact sets: uniform continuity, extreme value theorem
- Contraction mapping theorem (Banach fixed-point): $d(Tx, Ty) \leq k\,d(x,y)$, $k < 1$

**Sequences and Series of Functions**:
- Pointwise vs. uniform convergence
- Uniform convergence preserves continuity, integrability, differentiability (under conditions)
- Power series: radius of convergence; term-by-term differentiation and integration
- Stone-Weierstrass theorem: polynomials dense in $C[a,b]$

**Riemann Integration (rigorous)**:
- Upper and lower Riemann sums; Darboux criterion
- Riemann-Stieltjes integral: generalization for measure-theoretic bridge

**Multivariable Analysis**:
- Differentiability in $\mathbb{R}^n$; total derivative as linear map (Jacobian)
- Inverse and implicit function theorems
- Manifolds (intro): smooth curves and surfaces in $\mathbb{R}^3$

### MATH4033: Measure Theory

**Lebesgue Measure**:
- Outer measure; measurable sets; $\sigma$-algebras; Borel sets
- Lebesgue measure on $\mathbb{R}^n$: translation invariance, completeness
- Non-measurable sets (Vitali); measure zero sets

**Lebesgue Integration**:
- Measurable functions; simple functions; Lebesgue integral definition
- Monotone convergence theorem; Fatou's lemma; Dominated convergence theorem (DCT)
- Comparison with Riemann: $f$ Riemann integrable ↔ $f$ a.e. continuous
- $L^p$ spaces: Hölder's and Minkowski's inequalities; completeness (Riesz-Fischer)

**Product Measures and Fubini**:
- Product $\sigma$-algebra; product measure
- Fubini-Tonelli theorem: iterated integrals = double integral under integrability

**Radon-Nikodym Theorem**:
- Absolute continuity of measures: $\nu \ll \mu$
- Radon-Nikodym derivative (density): $d\nu = f\,d\mu$
- Applications: conditional expectations in probability; change of measure in finance

## Connections to ML and Finance

- **Statistical learning theory**: VC dimension, Rademacher complexity, uniform convergence bounds rely on measure theory
- **Optimization convergence**: gradient descent convergence proofs use metric space completeness and DCT
- **Martingale theory**: conditional expectation defined via Radon-Nikodym; Girsanov's theorem (change of measure) is a Radon-Nikodym derivative — see [[stochastic-calculus]]
- **Probability theory foundations**: Kolmogorov's axioms formalized in measure-theoretic framework — see [[probability-theory]]

## Related Concepts

- [[probability-theory]]
- [[stochastic-calculus]]
- [[optimization]]

## Source Materials

- MATH3033 Course Materials
