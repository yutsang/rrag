---
title: "Behavioral Economics"
full_name: "Behavioral Economics"
type: concept
tags: [economics, behavioral-economics, decision-making, prospect-theory, cognitive-bias]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/engineering-economics.md"
confidence: high
---

## 概述

行為經濟學系統性地記錄人類決策偏離理性期望效用最大化的規律，是古典微觀經濟學「理性人」假設的實證修正。其核心理論體系由三根支柱構成：前景理論（Kahneman & Tversky, 1979）以參考點依賴的 S 形價值函數 $v(x)$ 取代效用函數，揭示損失厭惡係數 $\lambda \approx 2.25$ 及對小概率的過度加權；雙曲折現 $U = u_0 + \beta \sum_t \delta^t u_t$（$\beta < 1$）描述的時間不一致偏好，解釋了偏好逆轉現象並挑戰以固定 MARR 折現的工程經濟規範模型；框架效應（亞洲疾病問題）與 Ellsberg 悖論的模糊厭惡，則說明决策結果依賴問題呈現方式，違反描述不變性公理。這些偏差在運籌學應用中產生具體後果：NPV 為正的項目可能因框架效應被否決，IRR 的百分比形式迎合 System 1 直覺而被過度倚重，而成本估算的系統性低估（努力扭曲與過度樂觀）是項目成本超支的行為根源。在金融時間序列領域，損失厭惡與投資者過度反應是 [[garch|GARCH]] 槓桿效應（負衝擊增大未來波動）的心理層面解釋；在收益管理中，Kahneman-Knetsch-Thaler（1986）的公平感知理論限制了動態定價的可行幅度，使純數學最優解在實務中面臨顧客抵制。EEMT5510 L11 以聖彼得堡悖論、Ellsberg 悖論及最後通牒博弈為脈絡，連結行為偏差到工程項目談判與資本預算決策的現實情境。

## Core Mechanism

**Behavioral economics** studies how psychological, cognitive, and emotional factors influence economic decisions. It emerged as a critique of the **normative model** (rational utility maximization) by documenting systematic deviations — not random errors, but predictable patterns of "irrational" behavior.

### Normative vs. Descriptive Decision Theory

| Aspect | Normative (Classical) | Descriptive (Behavioral) |
|--------|----------------------|--------------------------|
| Assumption | Rational, utility-maximizing agents | Bounded rationality, heuristics |
| Risk handling | Expected utility theory | Prospect theory |
| Time preference | Exponential discounting | Hyperbolic discounting |
| Information processing | Complete, unbiased | Subject to framing, anchoring |
| Relevance | How people *should* decide | How people *actually* decide |

## Bounded Rationality

Herbert Simon introduced **bounded rationality**: cognitive limitations, incomplete information, and time constraints prevent people from finding optimal solutions. Instead, people **satisfice** — they seek solutions that are "good enough" rather than optimal.

### Probability Matching (L11)

Given a coin with $P(H) = 0.6$ and $P(T) = 0.4$, the rational prediction strategy is to predict H every time (accuracy 60%). Experimentally, humans and animals tend to **probability-match**: predict H about 60% of the time (accuracy $0.6^2 + 0.4^2 = 0.52$). One evolutionary rationalization: in a group of agents competing for payoffs that depend on uniqueness, randomization reduces competition — individual suboptimality can be group-optimal.

Daniel Kahneman extended this with the **dual-process theory**:
- **System 1**: Fast, automatic, intuitive. Prone to biases.
- **System 2**: Slow, deliberate, analytical. Requires effort.

Most everyday decisions use System 1, which explains the pervasiveness of cognitive biases.

## Risk Aversion and Expected Utility

### The St. Petersburg Paradox

A coin is flipped until heads appears. The payoff is $2^n$ where $n$ is the number of flips. The **expected value** is infinite:

$$E[X] = \sum_{n=1}^{\infty} \frac{1}{2^n} \cdot 2^n = \sum_{n=1}^{\infty} 1 = \infty$$

Yet people will only pay a modest amount to play. Daniel Bernoulli resolved this by proposing that people maximize **expected utility**, not expected value, with a **concave utility function** (diminishing marginal utility of wealth):

$$U(W) = \ln(W) \quad \text{(Bernoulli's utility function)}$$

With log utility the expected utility of the St. Petersburg game is:

$$E[u(X)] = \sum_{n=1}^{\infty} \frac{1}{2^n} \ln(2^n) = \ln 2 \sum_{n=1}^{\infty} \frac{n}{2^n} = 2 \ln 2 = \ln 4$$

so the certainty equivalent is just \$4 — much closer to observed willingness-to-pay. A concave utility function implies **risk aversion**: the utility of the expected value exceeds the expected utility of the gamble.

### Risk Premium and Certainty Equivalent

- **Certainty equivalent (CE)**: The guaranteed amount that provides the same utility as the gamble.
- **Risk premium**: $E[X] - CE$ — the amount a risk-averse individual will forgo to avoid uncertainty.

## Prospect Theory

Developed by **Kahneman and Tversky (1979)**, prospect theory is the cornerstone of behavioral economics. It differs from expected utility theory in three fundamental ways:

### 1. Reference Dependence

People evaluate outcomes as **gains or losses relative to a reference point**, not as final wealth states. The reference point is typically the status quo, but can be influenced by expectations, aspirations, or framing.

### 2. The Value Function

The value function $v(x)$ replaces the utility function and has a distinctive S-shape:

- **Concave for gains**: Diminishing sensitivity to increasing gains ($v''(x) < 0$ for $x > 0$).
- **Convex for losses**: Diminishing sensitivity to increasing losses ($v''(x) > 0$ for $x < 0$).
- **Steeper for losses**: The function is steeper in the loss domain, capturing **loss aversion** — losses loom roughly twice as large as equivalent gains ($\lambda \approx 2.25$ in Kahneman & Tversky's estimates).

Behavioral implication: People are **risk-averse for gains** (prefer a sure \$500 over a 50% chance of \$1,000) but **risk-seeking for losses** (prefer a 50% chance of losing \$1,000 over a sure loss of \$500).

### 3. Probability Weighting

People do not weight outcomes by objective probabilities. Instead, they use a **probability weighting function** $\pi(p)$ that:
- **Overweights small probabilities**: Explains lottery ticket purchases and insurance buying.
- **Underweights moderate and high probabilities**: Contributes to risk-seeking in the gain domain for low-probability high-payoff gambles.

## Framing Effects

How a problem is **framed** — the words, context, and reference point used to present options — can reverse preferences, violating the rational choice axiom of **description invariance**.

### The Asian Disease Problem (Tversky & Kahneman, 1981)

A disease threatens 600 lives. Two programs are offered:

**Gain frame**:
- Program A: 200 people will be saved. (72% choose this)
- Program B: 1/3 probability all 600 saved, 2/3 probability none saved. (28%)

**Loss frame**:
- Program C: 400 people will die. (22% choose this)
- Program D: 1/3 probability nobody dies, 2/3 probability 600 die. (78%)

Programs A and C are identical, as are B and D. Yet the majority preference reverses between frames. In the gain frame, people are risk-averse (choose the sure thing); in the loss frame, they are risk-seeking (choose the gamble). This is exactly what prospect theory predicts.

### Implications for Engineering Economy

Project proposals can be framed as gains (value created) or losses (costs avoided). The framing can influence acceptance even when the [[npv|NPV]] is identical. Decision-makers should be aware of framing effects and evaluate projects using consistent, quantitative methods.

## Ambiguity Aversion

### Ellsberg's Paradox (1961)

An urn contains 30 red balls and 60 balls that are either black or yellow (unknown ratio).

- **Gamble A**: Win \$100 if red. (Most prefer this)
- **Gamble B**: Win \$100 if black.

This implies $P(\text{red}) > P(\text{black})$, i.e., $1/3 > P(\text{black})$.

- **Gamble C**: Win \$100 if red or yellow.
- **Gamble D**: Win \$100 if black or yellow. (Most prefer this)

This implies $P(\text{black or yellow}) > P(\text{red or yellow})$, which means $P(\text{black}) > 1/3$ — contradicting the first preference.

The resolution: People are **ambiguity-averse** — they prefer known probabilities over unknown ones, even when the expected values are the same. This cannot be explained by expected utility theory with any probability assignment.

## Time Inconsistency

### Hyperbolic Discounting

Standard economic models assume **exponential discounting**: future utility is discounted at a constant rate. This implies **time-consistent** preferences — if you prefer A over B today, you will still prefer A over B tomorrow.

In reality, people exhibit **present-biased preferences** described by **hyperbolic (or quasi-hyperbolic) discounting**:

$$U = u_0 + \beta \sum_{t=1}^{T} \delta^t u_t$$

where $\beta < 1$ captures the extra discounting of all future periods relative to the present. This creates a **present bias**: people disproportionately overweight immediate rewards.

### Preference Reversal (L11)

When offered "\$100 in 30 days vs. \$110 in 31 days", most people wait for the extra dollar. But "\$100 today vs. \$110 tomorrow" often triggers a switch to the immediate \$100. Under exponential discounting, either both pairs should favor the delayed option or both should favor the sooner — the **reversal** is the signature of non-exponential preferences. The consequence for [[time-value-of-money|TVM]] analyses: using a flat nominal MARR to aggregate intertemporal preferences will systematically mis-predict real consumer choices on long-horizon projects (retirement savings, home purchases, energy-efficiency investments).

### Consequences

- **Procrastination**: Tasks with immediate costs and delayed benefits (e.g., studying, exercising) are postponed.
- **Impulsive consumption**: Rewards with immediate benefits and delayed costs (e.g., overspending) are chosen.
- **Preference reversal**: At a distance, people prefer the larger-later reward; as the smaller-sooner reward becomes imminent, they switch.

### Self-Awareness

- **Sophisticated**: Aware of their present bias. May use commitment devices (automatic savings, deadlines).
- **Naive**: Unaware. Repeatedly plan to start "tomorrow" but never do.

## Effort Distortion and Procrastination

People distort their perception of effort costs:
- **Immediate effort** feels disproportionately costly (leading to procrastination).
- **Future effort** feels easy (leading to overcommitment).

This explains why projects regularly underestimate required effort and why cost overruns are systematic rather than random.

## Regret Theory

People anticipate the **regret** they would feel if a chosen alternative turns out worse than an unchosen one. Anticipated regret can cause:
- **Status quo bias**: Staying with the current option to avoid regret from a bad switch.
- **Omission bias**: Preferring inaction (errors of omission feel less regretful than errors of commission).
- **Diversification**: Spreading investments to minimize maximum possible regret.

In engineering economy, regret analysis provides an alternative decision framework: choose the alternative that minimizes the maximum regret across possible scenarios.

### Lottery Ticket Experiment (L11)

Students given a lottery ticket were offered a chance to exchange it for another ticket plus a small monetary incentive — fewer than 50% agreed. But when given pens and offered the same trade, over 90% agreed. The difference is anticipated regret: "if I swap and my original would have won, I'd be devastated; if I don't swap, I'd never know I missed out." Inaction shields the decision-maker from counterfactual information.

## Fairness

People care about fairness, not just self-interest:

### Distributive Justice
Outcomes should be allocated equitably. People reject unfair divisions even at personal cost.

### Procedural Justice
The process by which decisions are made matters. Fair procedures increase acceptance of outcomes.

### The Ultimatum Game

Player 1 proposes a split of \$10. Player 2 accepts or rejects (rejection means both get nothing). Rational prediction: Player 1 offers \$0.01; Player 2 accepts (something > nothing). Actual behavior: offers below 20-30% are frequently rejected. People punish unfairness at personal cost.

This has direct implications for engineering project negotiations, cost-sharing arrangements, and stakeholder management.

## Related Concepts

- [[npv|NPV]] — Normative evaluation method; behavioral factors explain why NPV-positive projects are sometimes rejected
- [[irr|IRR]] — The intuitive percentage may be preferred due to cognitive ease (System 1)
- [[time-value-of-money|TVM]] — Rational exponential discounting vs. behavioral hyperbolic discounting
- [[cvp-analysis|CVP Analysis]] — Breakeven framing can influence risk perception
- [[financial-ratios|Financial Ratios]] — Performance metrics subject to anchoring and framing biases
- [[revenue-management|Revenue Management]] — Reference-dependent pricing, charm prices, and fairness concerns (Kahneman-Knetsch-Thaler 1986) constrain dynamic pricing more than the textbook optimum would suggest
- [[consumer-behavior|Consumer Behavior]] — Prospect theory, mental accounting, and anchoring are the micro-foundations that marketing's purchase decision models describe empirically
- [[ab-testing|A/B Testing]] — Behavioral nudges are the most common experimental treatments; effect sizes often reflect framing rather than real preference shifts
- [[garch|GARCH Models]] — Leverage effect and asymmetric volatility are the time-series shadow of loss aversion and investor overreaction
- [[wiki/mocs/operations-research|Operations Research MOC]] — Part of the OR PhD reading spine (Behavioral Operations)

## Source Materials

- L11 - Behavioral Economics
- [[wiki/sources/courses/engineering-economics.md|EEMT5510 Engineering Economics and Cost Management]]
