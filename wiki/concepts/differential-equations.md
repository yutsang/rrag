---
title: "Differential Equations"
full_name: "Differential Equations (ODEs and PDEs)"
type: concept
tags: [mathematics, differential-equations, dynamical-systems]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/hkust-odes-pdes"
confidence: high
---

## 概述

微分方程描述量的變化率與量本身之間的關係，是建模連續時間動態系統的通用數學語言，在工程控制、物理學、生態學、金融及運籌學中無處不在。常微分方程（ODE）按求解方法劃分為可分離方程（$dy/dt = g(t)h(y)$）、一階線性方程（積分因子法）、二階線性常係數方程（特徵方程法：根的實/複/重複性決定通解形式）和方程組（矩陣指數 $e^{At}$ 以特徵分解表達，直接連結[[wiki/concepts/linear-algebra|線性代數]]）；穩定性分析以平衡點附近的線性化雅可比矩陣特徵值符號判定局部穩定性（負實部→穩定，正實部→不穩定），這是控制理論和動態系統的基礎語言。偏微分方程（PDE）的三大典型代表——熱方程（$u_t = \alpha u_{xx}$，拋物型，描述擴散）、波方程（$u_{tt} = c^2 u_{xx}$，雙曲型，描述傳播）、Laplace/Poisson方程（$\nabla^2 u = f$，橢圓型，描述穩態）——覆蓋了大多數物理和工程問題，並通過傅里葉級數和分離變量法求解。在運籌學和金融的交叉點，Black-Scholes PDE（$\partial V/\partial t + \frac{1}{2}\sigma^2 S^2 \partial^2 V/\partial S^2 + rS \partial V/\partial S - rV = 0$）將期權定價歸結為拋物型 PDE 的邊界值問題；Hamilton-Jacobi-Bellman（HJB）方程是連續時間最優控制和隨機動態規劃的核心，直接連結 Bellman 最優性原理與[[wiki/concepts/algorithms-and-data-structures|動態規劃]]；庫存控制的連續時間模型（$\dot{x}(t) = u(t) - d(t)$，庫存水位的狀態方程）是 ODE 在供應鏈優化中的直接應用。數值求解方法（Euler 法、Runge-Kutta RK4、剛性方程的隱式方法）和穩定性理論（數值穩定域、步長選擇）是計算實現的核心問題，掌握這些技術是理解隨機微分方程（SDE）和隨機控制的必要前提。

## What It Is

A **differential equation** is an equation involving an unknown function and its derivatives. It models systems where the rate of change depends on the current state.

**ODE (Ordinary)**: involves derivatives with respect to a single variable (usually time $t$).
**PDE (Partial)**: involves partial derivatives with respect to multiple variables (e.g., space and time).

**Order**: highest derivative appearing. **Linearity**: linear in the unknown function and its derivatives (no products of derivatives or nonlinear functions of the unknown).

## First-Order ODEs

General form: $\frac{dy}{dt} = f(t, y)$.

**Separable**: $\frac{dy}{dt} = g(t)h(y)$ → $\int \frac{dy}{h(y)} = \int g(t) \, dt$.

**Linear**: $\frac{dy}{dt} + p(t)y = q(t)$. Solved via integrating factor $\mu(t) = e^{\int p(t)dt}$:
$$y(t) = \frac{1}{\mu(t)}\left[\int \mu(t) q(t) \, dt + C\right]$$

**Example — Inventory decay**: $\frac{dI}{dt} = -\lambda I$ gives $I(t) = I_0 e^{-\lambda t}$ (exponential depletion).

**Equilibria and stability**: $y^*$ with $f(t, y^*) = 0$ is stable if $\partial f/\partial y < 0$ at $y^*$ (perturbations decay).

## Second-Order Linear ODEs

Form: $ay'' + by' + cy = g(t)$.

**Homogeneous** ($g = 0$): characteristic equation $ar^2 + br + c = 0$.
- Two real roots $r_1 \neq r_2$: $y_h = C_1 e^{r_1 t} + C_2 e^{r_2 t}$
- Repeated root: $y_h = (C_1 + C_2 t)e^{rt}$
- Complex roots $r = \alpha \pm i\beta$: $y_h = e^{\alpha t}(C_1 \cos\beta t + C_2 \sin\beta t)$

**Particular solution** by undetermined coefficients (polynomial, exponential, sinusoidal forcing) or variation of parameters.

## Systems of ODEs

$\mathbf{x}' = A\mathbf{x}$ where $\mathbf{x} \in \mathbb{R}^n$. Solution via eigendecomposition of $A$:
$$\mathbf{x}(t) = \sum_i c_i e^{\lambda_i t} \mathbf{v}_i$$

where $(\lambda_i, \mathbf{v}_i)$ are eigenvalue-eigenvector pairs.

**Phase plane analysis** (2D): classify equilibria by eigenvalues of Jacobian:
- Both negative real: stable node (sink)
- Both positive real: unstable node (source)
- Opposite signs: saddle point (unstable)
- Pure imaginary: center (periodic orbits)
- Complex with negative real part: stable spiral

## Laplace Transforms

Transform ODEs to algebraic equations. $\mathcal{L}\{f(t)\} = F(s) = \int_0^\infty e^{-st} f(t) dt$.

Key pairs: $\mathcal{L}\{e^{at}\} = 1/(s-a)$, $\mathcal{L}\{t^n\} = n!/s^{n+1}$, $\mathcal{L}\{f'\} = sF(s) - f(0)$.

**Procedure**: take Laplace transform → algebraic equation in $F(s)$ → solve for $F(s)$ → inverse transform. Convolution theorem handles forcing terms.

## Partial Differential Equations

**Heat equation**: $\frac{\partial u}{\partial t} = k \frac{\partial^2 u}{\partial x^2}$. Models diffusion — temperature, probability density, option prices.

**Wave equation**: $\frac{\partial^2 u}{\partial t^2} = c^2 \frac{\partial^2 u}{\partial x^2}$. Models vibrations, acoustics.

**Laplace equation**: $\nabla^2 u = 0$. Steady-state heat, potential fields.

**Solution methods**: separation of variables, Fourier series, transform methods, numerical methods (finite differences, finite elements).

## Numerical Methods for ODEs

When analytical solutions don't exist:

**Euler's method**: $y_{n+1} = y_n + h f(t_n, y_n)$. First-order accurate, $O(h)$ error per step.

**Runge-Kutta (RK4)**: fourth-order accurate, $O(h^4)$ error. The standard workhorse.

**Stiff equations**: systems where different components evolve on very different timescales. Explicit methods require tiny $h$ → use implicit methods (backward Euler, Crank-Nicolson).

## Connections to OR and Finance

**Black-Scholes PDE** (see [[stochastic-calculus]]): $\frac{\partial C}{\partial t} + rS\frac{\partial C}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 C}{\partial S^2} - rC = 0$. Solved by finite differences or analytically.

**Hamilton-Jacobi-Bellman equation** (stochastic control):
$$-\frac{\partial V}{\partial t} = \max_u \left\{r(x, u) + \frac{\partial V}{\partial x}f(x,u) + \frac{1}{2}\sigma^2 \frac{\partial^2 V}{\partial x^2}\right\}$$
A PDE whose solution gives the optimal policy for continuous-time stochastic control problems.

**Epidemic models** (SIR): $\dot{S} = -\beta SI$, $\dot{I} = \beta SI - \gamma I$, $\dot{R} = \gamma I$. Used in pandemic supply chain disruption analysis.

**Inventory in continuous time**: $\dot{I}(t) = q(t) - d(t)$ where $q$ = replenishment rate, $d$ = demand rate. Optimal control formulation.

## Related Concepts

- [[stochastic-calculus]]
- [[stochastic-processes]]
- [[optimization]]
- [[linear-algebra]]
- [[probability-theory]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
