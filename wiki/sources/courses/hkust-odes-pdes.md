---
title: "HKUST ODEs and PDEs"
full_name: "HKUST Ordinary and Partial Differential Equations (MATH2351/3343)"
type: source
tags: [courses, math, undergraduate, differential-equations, odes, pdes, math2351, math3343, level-2]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/MATH/MATH2351"
confidence: medium
---

## 概述

MATH2351 常微分方程與 MATH3343 偏微分方程構成香港科技大學工程數學的核心課程序列，分別面向二年級和三年級的工程及數學學生，先修要求為 MATH1013 及 MATH2011 多變量微積分。MATH2351 以 Boyce & DiPrima《常微分方程初值問題》或 Zill《微分方程》為標準教材，系統介紹一階 ODE 的解析解法（分離變數、積分因子）、二階線性 ODE（特徵方程、未定係數法、參數變換法）、Laplace 變換及線性系統的相平面分析；MATH3343 則涵蓋熱方程、波動方程及 Laplace 方程的分離變數法、Fourier 級數展開與 Fourier 變換。學生完成課程後能夠建立動態系統的 ODE 模型（庫存動態、傳染病 SIR 模型、RLC 電路）、利用 Laplace 變換求解具有不連續驅動力的初值問題，以及應用有限差分或 Fourier 方法數值求解 PDE。在金融工程中，Black-Scholes 定價方程正是一個抛物型 PDE，而 Hamilton-Jacobi-Bellman 方程則將最優控制問題歸結為非線性 PDE，使本課程成為量化金融與隨機最優控制的必要數學基礎。

## Course Structure

| Course | Content |
|---|---|
| MATH2351 | Ordinary Differential Equations |
| MATH3343 | Partial Differential Equations |

## Key Topics

### MATH2351: Ordinary Differential Equations

**First-Order ODEs**:
- Separable equations: $\frac{dy}{dx} = f(x)g(y)$
- Linear first-order: $y' + P(x)y = Q(x)$; integrating factor $\mu = e^{\int P \,dx}$
- Exact equations: $M\,dx + N\,dy = 0$ when $\frac{\partial M}{\partial y} = \frac{\partial N}{\partial x}$
- Bernoulli, Ricatti equations; existence and uniqueness (Picard-Lindelöf)

**Second-Order Linear ODEs**:
- Homogeneous with constant coefficients: characteristic equation; overdamped, critically damped, underdamped cases
- Method of undetermined coefficients; variation of parameters
- Euler-Cauchy equation: $x^2y'' + axy' + by = 0$
- Applications: spring-mass systems, RLC circuits, resonance

**Systems of ODEs**:
- Matrix form $\mathbf{x}' = A\mathbf{x}$; eigenvalue methods
- Phase portraits: stable/unstable nodes, saddle points, centers, spirals
- Nonlinear systems: linearization about equilibria

**Laplace Transforms**:
- Definition and properties; inverse Laplace transform
- Solving IVPs with discontinuous forcing: unit step (Heaviside), impulse (Dirac delta)
- Convolution theorem: $\mathcal{L}\{f*g\} = \mathcal{L}\{f\}\mathcal{L}\{g\}$

**Series Solutions**:
- Power series method; Frobenius method near regular singular points
- Bessel functions, Legendre polynomials

### MATH3343: Partial Differential Equations

**Classification**:
- Second-order linear PDEs: elliptic (Laplace), parabolic (heat), hyperbolic (wave)
- Canonical forms; characteristics

**Heat Equation** $u_t = k u_{xx}$:
- Separation of variables; Fourier series solution
- Initial-boundary value problems on finite domains
- Fundamental solution (Gaussian kernel): $u(x,t) = \frac{1}{\sqrt{4\pi kt}} e^{-x^2/(4kt)}$

**Wave Equation** $u_{tt} = c^2 u_{xx}$:
- D'Alembert's solution for infinite strings
- Standing waves on finite strings; normal modes

**Laplace/Poisson Equation** $\nabla^2 u = 0$:
- Harmonic functions; maximum principle
- Dirichlet and Neumann boundary conditions
- Separation of variables in polar coordinates; Fourier series methods

**Fourier Analysis**:
- Fourier series: orthogonality, convergence (Dirichlet conditions), Gibbs phenomenon
- Fourier transform: convolution theorem, Parseval's identity
- Discrete Fourier transform intro; FFT connection

## Applications in Finance and OR

- **Black-Scholes PDE**: $\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0$ — a parabolic PDE solvable by Fourier transform or finite-difference methods; see [[options-pricing]] and [[stochastic-calculus]]
- **Hamilton-Jacobi-Bellman equation**: a nonlinear PDE governing optimal control problems — see [[optimization]]
- Compartmental models (SIR epidemics, inventory dynamics) use ODE systems

## Related Concepts

- [[differential-equations]]
- [[stochastic-calculus]]
- [[optimization]]
- [[options-pricing]]

## Source Materials

- MATH2351 Course Materials
