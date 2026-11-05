---
title: "Stochastic Processes"
full_name: "Stochastic Processes"
type: concept
tags: [probability, operations-research, stochastic-processes]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/ieda-stochastic-models"
confidence: high
---

## 概述

隨機過程（Stochastic Processes）是研究以時間（或其他指標集）為參數的隨機變量族 {X(t): t∈T} 的數學框架，依狀態空間與時間是否離散分為四類：離散時間馬可夫鏈（DTMC）、連續時間馬可夫鏈（CTMC）、泊松過程及更新過程等。馬可夫性質（Markov Property，無記憶性）是最關鍵的結構假設：下一狀態的轉移概率僅依賴當前狀態，使穩態分析可透過線性方程組 π = πP（DTMC）或 πQ = 0（CTMC）求解。泊松過程是具有獨立平穩增量的唯一計數過程，指數分佈的無記憶性使 M/M/1 等排隊模型的穩態概率得以用幾何分佈 πn = (1−ρ)ρⁿ 的閉合公式表達。連續時間馬可夫鏈透過生成矩陣（Generator Matrix）Q 刻畫轉移速率，全域平衡方程給出穩態分佈，而泊松到達看到時間平均（PASTA 定理）則是排隊分析的重要簡化工具。更新理論（Renewal Theory）的基本更新定理和更新獎勵定理為最優替換策略、預防性維護排程提供長期平均成本的計算框架。在運籌學研究中，隨機過程是排隊網絡分析（Burke 定理、積形式網絡）、（s, S）庫存策略評估、馬可夫決策過程（MDP）及隨機動態規劃的理論基礎。

## What It Is

A **stochastic process** $\{X(t) : t \in T\}$ is a collection of random variables indexed by time. The index set $T$ can be discrete ($T = \{0, 1, 2, \ldots\}$) or continuous ($T = [0, \infty)$). The state space can also be discrete or continuous.

## Discrete-Time Markov Chains (DTMC)

A DTMC satisfies the **Markov property** (memorylessness):
$$P(X_{n+1} = j \mid X_n = i, X_{n-1}, \ldots) = P(X_{n+1} = j \mid X_n = i) = p_{ij}$$

The transition probabilities form the **transition matrix** $P$ where $p_{ij} \geq 0$ and $\sum_j p_{ij} = 1$.

### Steady-State Analysis
If the chain is **irreducible** (every state reachable from every other) and **aperiodic**, a unique **stationary distribution** $\pi$ exists satisfying:
$$\pi = \pi P, \quad \sum_i \pi_i = 1$$

$\pi_i$ is the long-run fraction of time spent in state $i$.

### Classification of States
- **Transient**: chain eventually leaves and never returns with probability 1
- **Recurrent**: chain returns with probability 1; further split into positive recurrent (finite mean return time) and null recurrent
- **Absorbing**: $p_{ii} = 1$; chain never leaves

**Absorption probabilities**: for Markov chains with absorbing states, the probability of being absorbed in state $j$ starting from $i$ satisfies a system of linear equations.

### OR Application: Inventory (s, S) Policy
Model inventory level as a DTMC. States are inventory levels; transitions depend on demand distribution. Steady-state distribution gives long-run average holding and stockout costs.

## Poisson Process

The Poisson process $\{N(t)\}$ counts arrivals over time with:
- **Rate** $\lambda$ (arrivals per unit time)
- **Memoryless inter-arrival times**: $T_i \sim \text{Exp}(\lambda)$, i.e., $P(T > t) = e^{-\lambda t}$
- **Independent increments**: arrivals in disjoint intervals are independent
- **Stationary increments**: $N(t+s) - N(s) \sim \text{Poisson}(\lambda t)$

The Poisson process is the unique counting process with stationary and independent increments and no simultaneous arrivals.

**Merging**: superposition of independent Poisson($\lambda_1$) and Poisson($\lambda_2$) is Poisson($\lambda_1 + \lambda_2$).
**Splitting**: thinning by independent Bernoulli($p$) yields Poisson($p\lambda$).

## Continuous-Time Markov Chains (CTMC)

In a CTMC, the time spent in state $i$ is Exp($q_i$), and transitions follow probabilities $p_{ij}$. The **generator matrix** (or rate matrix) $Q$ has entries:
- $q_{ij} = q_i p_{ij}$ for $i \neq j$ (transition rates)
- $q_{ii} = -q_i$ (diagonal ensures rows sum to zero)

The **balance equations** for steady-state $\pi$:
$$\pi Q = 0, \quad \sum_i \pi_i = 1$$

**Global balance**: $\pi_i q_i = \sum_{j \neq i} \pi_j q_{ji}$ (rate out of $i$ = rate into $i$).

**CTMC and queueing**: the M/M/1 queue is a CTMC with birth rate $\lambda$ (arrivals) and death rate $\mu$ (service completions). The steady-state probabilities are $\pi_n = (1 - \rho)\rho^n$ where $\rho = \lambda/\mu$.

## Renewal Theory

A renewal process counts the number of renewals (e.g., machine replacements) up to time $t$, where inter-renewal times $X_i$ are iid with mean $\mu$. The **elementary renewal theorem**: $E[N(t)]/t \to 1/\mu$ as $t \to \infty$. The **renewal reward theorem** generalizes this to compute long-run average rewards.

Applications: optimal replacement policies, maintenance scheduling.

## Key Results and Their OR Implications

| Result | Implication |
|---|---|
| Steady-state of M/M/1: $\rho = \lambda/\mu$ must be < 1 | Queue explodes if arrival rate exceeds service rate |
| PASTA (Poisson Arrivals See Time Averages) | Poisson arrivals observe steady-state distribution — simplifies analysis |
| Burke's theorem | Output of M/M/c is Poisson — enables product-form networks |
| Little's Law ($L = \lambda W$) | Connects queue length to waiting time without knowing distribution |

## Markov Decision Processes (MDP)

A **Markov Decision Process** extends a CTMC/DTMC with **actions** and **rewards**: at each state $i$, the decision-maker chooses action $a \in \mathcal{A}(i)$, receives reward $r(i,a)$, and transitions to state $j$ with probability $p_{ij}(a)$. The goal is a policy $\pi: \mathcal{S} \to \mathcal{A}$ that maximizes expected total (discounted or average) reward.

**Bellman equations** (discounted, discount factor $\beta < 1$):
$$V^*(i) = \max_{a \in \mathcal{A}(i)} \left[ r(i,a) + \beta \sum_j p_{ij}(a) V^*(j) \right]$$

Solution methods:
- **Value iteration**: iteratively apply the Bellman operator until convergence. Convergence guaranteed for $\beta < 1$.
- **Policy iteration**: start with a policy, evaluate it (solve a linear system), improve greedily. Converges in finitely many steps.
- **Linear programming formulation**: the MDP value function is the solution to a linear program with one variable per state.

OR applications of MDPs: optimal inventory replenishment ($(s,S)$ policy is MDP-optimal under certain conditions), equipment replacement, dynamic pricing, healthcare treatment scheduling, and as the theoretical foundation of reinforcement learning.

## Limitations and Caveats

1. **Markov assumption**: real systems often have history-dependence (non-Markovian service, batch arrivals). Semi-Markov processes and phase-type distributions extend the framework but complicate analysis.
2. **State space explosion**: DTMC/CTMC models become intractable when the state space is large (e.g., multi-product inventory with continuous levels). Approximate dynamic programming and simulation are the practical remedies.
3. **Stationarity**: Poisson and exponential assumptions imply time-homogeneous rates. Non-stationary arrival rates (rush hours, seasonal demand) require time-dependent analysis or simulation.
4. **Parameter estimation**: transition rates and arrival rates must be estimated from data; estimation error propagates into all steady-state calculations.

## Related Concepts

- [[queueing-theory]]
- [[littles-law]]
- [[newsvendor-problem]]
- [[probability-theory]]
- [[arma-models]]
- [[stochastic-calculus]]
- [[capacity-planning]]
- [[simulation]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
