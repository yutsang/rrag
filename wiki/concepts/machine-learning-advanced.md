---
title: "Machine Learning (Advanced)"
full_name: "Advanced Machine Learning Methods"
type: concept
tags: [machine-learning, deep-learning, statistical-learning]
created: "2026-04-14"
updated: "2026-04-14"
source: "wiki/sources/courses/comp-machine-learning"
confidence: high
---

## 概述

進階機器學習在迴歸、分類基礎上引入統計學習理論的嚴格框架：VC 維度量化假設類複雜度，泛化誤差界將訓練誤差與 VC 維度的函數連結，而偏差-方差分解則揭示模型複雜度與樣本量之間的根本性張力。支援向量機（SVM）透過最大間隔超平面實現結構風險最小化，其對偶形式與核技巧使其可在無窮維特徵空間（RBF 核）中進行高效計算，且全局最優解有保障（凸二次規劃）。神經網絡的通用逼近定理確保單隱層 MLP 可逼近任意連續函數，但這是存在性而非構造性結果；深度架構（CNN 利用空間局部性、LSTM/Transformer 處理序列依賴）在影像、語言和時序預測任務上大幅超越淺層模型。集成方法中，Bagging 降低方差（Random Forest）而 Boosting 降低偏差（AdaBoost、Gradient Boosting）；XGBoost 和 LightGBM 通過正則化目標函數、列取樣和直方圖近似，在結構化表格數據競賽中持續佔據主導地位。在運籌學的橋接應用中，「先預測後優化」（predict-then-optimize）範式正在演進為端對端可微優化，將決策損失直接反向傳播至預測模型；強化學習與馬可夫決策過程（MDP）的連結使 ML 成為隨機動態規劃的計算替代方案。

## Statistical Learning Theory

**The learning problem**: given training data $\{(x_i, y_i)\}_{i=1}^n$ drawn iid from distribution $\mathcal{D}$, find hypothesis $h \in \mathcal{H}$ minimizing **expected risk** $R(h) = E_{(x,y) \sim \mathcal{D}}[L(h(x), y)]$.

We can only minimize **empirical risk** $\hat{R}(h) = \frac{1}{n}\sum L(h(x_i), y_i)$.

**Generalization bound** (VC theory): with probability $1-\delta$:
$$R(h) \leq \hat{R}(h) + O\left(\sqrt{\frac{d_{VC} + \ln(1/\delta)}{n}}\right)$$

where $d_{VC}$ is the VC dimension — a measure of hypothesis class complexity.

**Bias-variance decomposition** (squared loss):
$$E[\text{error}] = \text{Bias}^2 + \text{Variance} + \text{Noise}$$
- High bias: model too simple (underfitting)
- High variance: model too complex (overfitting)
- Regularization trades higher bias for lower variance

## Support Vector Machines (SVM)

**Hard-margin SVM**: find hyperplane $w^T x + b = 0$ separating two classes with maximum margin $2/\|w\|$.

$$\min_{w,b} \frac{1}{2}\|w\|^2 \quad \text{s.t.} \quad y_i(w^T x_i + b) \geq 1 \; \forall i$$

**Dual formulation**: $\max_\alpha \sum_i \alpha_i - \frac{1}{2}\sum_{i,j} \alpha_i \alpha_j y_i y_j x_i^T x_j$ s.t. $\alpha_i \geq 0$, $\sum_i \alpha_i y_i = 0$. Decision depends only on **support vectors** (points on margin).

**Soft-margin SVM**: add slack variables for misclassification, controlled by $C$. Large $C$ → narrow margin but few errors; small $C$ → wide margin but more tolerance.

**Kernel trick**: replace $x_i^T x_j$ with $K(x_i, x_j) = \phi(x_i)^T\phi(x_j)$. Never compute $\phi$ explicitly — just evaluate $K$.
- RBF/Gaussian: $K(x, z) = \exp(-\|x-z\|^2 / 2\sigma^2)$ — infinite-dimensional feature space
- Polynomial: $K(x, z) = (x^T z + c)^d$
- String kernel: for sequences in NLP

SVMs are convex QPs — globally optimal solution guaranteed. See [[linear-programming]] dual.

## Neural Networks

**Perceptron**: $\hat{y} = \text{sign}(w^T x + b)$. Single layer, linear separator.

**Multi-layer perceptron (MLP)**: stacked layers with nonlinear activations.
$$h^{(l)} = \sigma(W^{(l)} h^{(l-1)} + b^{(l)})$$

**Activation functions**:
- Sigmoid $\sigma(z) = 1/(1+e^{-z})$: saturates, gradient vanishes
- ReLU $\max(0, z)$: fast, no saturation; "dying ReLU" problem
- Leaky ReLU, ELU, GELU: fix dying ReLU
- Softmax (output layer for multiclass): $\text{softmax}(z)_i = e^{z_i}/\sum_j e^{z_j}$

**Universal approximation theorem**: MLP with single hidden layer can approximate any continuous function on compact domain to arbitrary precision (given enough neurons). Existence result, not constructive.

**Backpropagation**: compute gradients of loss w.r.t. all parameters via chain rule. Efficient by caching forward-pass activations and working backward.

### Deep Learning Architectures

**CNNs (Convolutional Neural Networks)**: exploit spatial locality via convolution filters. Parameter sharing reduces model size vs. fully connected. Pooling provides translation invariance. Standard for images (ResNet, VGG, EfficientNet).

**RNNs/LSTMs**: process sequential data. LSTM gates (input, forget, output) solve vanishing gradient. Used for time series, NLP before Transformers.

**Transformers**: self-attention mechanism — each token attends to all others. $\text{Attn}(Q,K,V) = \text{softmax}(QK^T/\sqrt{d_k})V$. Scales to very long sequences via multi-head attention. Foundation of BERT, GPT, LLaMA.

**Graph Neural Networks (GNNs)**: extend deep learning to graph-structured data. Message passing: aggregate neighbor features. Applications: supply chain network prediction, molecule property prediction, logistics.

## Ensemble Methods

**Bagging** (Bootstrap AGGregating): train $T$ models on bootstrap samples; average predictions. Reduces variance. **Random Forest** = bagging + random feature subsets at each split.

**Boosting**: train models sequentially, each correcting previous errors.
- **AdaBoost**: upweight misclassified examples; combine weak classifiers via weighted voting
- **Gradient Boosting**: fit each tree to pseudo-residuals of previous ensemble. **XGBoost**, **LightGBM**: optimized implementations with regularization, parallel tree building. Dominant in tabular data competitions (Kaggle).

## Model Assessment

**Cross-validation** ($k$-fold): partition data into $k$ folds; train on $k-1$, evaluate on 1; rotate. Robust estimate of generalization error.

**Hyperparameter tuning**:
- Grid search: exhaustive over discrete grid
- Random search: random draws — more efficient for high-dimensional spaces
- Bayesian optimization: model the validation loss function (Gaussian process) and acquire next point by maximizing expected improvement

**Calibration**: probability estimates from classifiers may not be calibrated. Platt scaling (logistic regression on scores) or isotonic regression corrects this.

## Connections to OR

- **Prescriptive analytics**: ML predicts demand/outcomes → optimization selects best action
- **Predict-then-optimize** vs. **end-to-end learning**: fitting models to minimize downstream decision loss rather than prediction loss
- **Reinforcement learning**: learning optimal sequential decisions via interaction with environment — closely related to stochastic DP and MDPs
- **Feature importance**: random forest importance, SHAP values explain which features drive predictions — useful for OR model building

## Related Concepts

- [[linear-regression]]
- [[logistic-regression]]
- [[decision-trees]]
- [[clustering]]
- [[pca]]
- [[nlp-basics]]
- [[optimization]]
- [[linear-algebra]]
- [[recommendation-systems]]
- [[wiki/mocs/operations-research|Operations Research MOC]]
- [[wiki/mocs/cs-data-science|CS and Data Science MOC]]
