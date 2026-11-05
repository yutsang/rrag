---
title: "NLP Basics"
full_name: "Natural Language Processing Basics (Text Analytics)"
type: concept
tags: [nlp, text-analytics, machine-learning, sentiment-analysis, bag-of-words]
created: "2026-04-09"
updated: "2026-04-14"
source: "wiki/sources/courses/applied-statistics"
confidence: high
---

## 概述

自然語言處理（NLP）基礎涵蓋文本預處理（小寫化、標點移除、停用詞過濾、Porter 詞幹提取）、詞袋模型（Bag-of-Words）以及情感分析等核心技術，其目標是將非結構化文字轉換為機器學習模型可處理的數值特徵矩陣（Document-Term Matrix）。詞袋模型的關鍵弱點在於它忽略詞序與語義：「dog bites man」與「man bites dog」具有相同的 BoW 表示，而否定詞（「not good」）無法被正確處理；稀疏性移除（removeSparseTerms）是降維的實用工具，可將詞彙表從數千項壓縮至數百項。EEMT5500 課程以 1,181 條 Apple 推文情感分類為案例，展示從 3,289 個原始詞彙精簡至 309 個保留詞彙的完整管道，並透過 Amazon Mechanical Turk 大規模眾包標注說明實際 NLP 訓練資料的獲取方式。分類結果顯示：單一分裂的 CART 樹（以「freak」為切點）已能超越多數類別基準，而隨機森林（88.73%）略優於交叉驗證最優 CART（88.45%），但兩者均有60-77%的假陰性率，反映類別不平衡（85/15）帶來的系統性偏差。TF-IDF、Word2Vec、BERT 等現代 NLP 方法分別解決了詞頻加權、語義相似性和上下文表示等 BoW 的核心侷限；在運籌學中，NLP 廣泛用於客戶反饋挖掘、供應鏈風險情報抓取及市場情緒監控，是結構化決策支援系統的重要數據來源。

## Core Mechanism

**Natural Language Processing (NLP)** is the field of computer science and AI concerned with enabling computers to understand, interpret, and generate human language. **Alan Turing** (1950) first proposed that a machine could be called intelligent if it could conduct a real-time conversation indistinguishable from a human's — still known today as the Turing test. Early chatterbots like **ELIZA** (1960s) used rule-based grammar; modern systems lean on statistical and machine learning techniques trained on large corpora. The EEMT5500 course focuses on the foundational technique of converting unstructured text into structured numerical features for machine learning.

### The 2013 AP Twitter Hack: Why It Matters

EEMT5500 opens the lecture with a compelling cautionary tale: in April 2013, a hacked Associated Press Twitter account posted "Breaking: Two Explosions in the White House and Barack Obama is injured." Within seconds the S&P 500 and DJIA dropped roughly 1%, and the White House rapidly clarified. Twitter processes **~500 million tweets per day**, far beyond human review capacity. The business case for text analytics is that managing brand perception, detecting offensive posts, and spotting market-moving news require automation.

### The Fundamental Challenge

Text data is **unstructured** — it has no inherent numerical representation, often contains poor spelling, non-traditional grammar, and is multilingual. Before any statistical model can be applied, text must be transformed into a structured format (typically a matrix of numbers). Ambiguity ("I put my bag in the car. It is large and blue" — is "it" the bag or the car?), homonyms (band = musical group or ring; right = correct or opposite of left), metaphors, and sarcasm all complicate the task. The **Bag-of-Words (BoW)** model is the simplest and most widely used approach, sacrificing nuance for tractability.

## Text Preprocessing Pipeline

The preprocessing pipeline converts raw text into clean, normalized tokens. Each step reduces noise and dimensionality while preserving meaningful signal.

### Step 1: Lowercasing

Convert all text to lowercase to ensure "Apple", "apple", and "APPLE" are treated as the same word.

```r
corpus = tm_map(corpus, content_transformer(tolower))
```

### Step 2: Punctuation Removal

Remove all punctuation marks. "don't" becomes "dont", "state-of-the-art" becomes "stateoftheart". This simplifies tokenization but can lose meaning in some cases.

```r
corpus = tm_map(corpus, removePunctuation)
```

### Step 3: Stop Word Removal

Remove common words that carry little semantic meaning: "the", "is", "at", "which", "on", etc. The `tm` package in R provides a standard English stop word list.

```r
corpus = tm_map(corpus, removeWords, stopwords("english"))
```

### Step 4: Stemming

Reduce words to their root form using the **Porter Stemmer** (Martin Porter, 1980). This collapses inflected forms:
- "running", "runs", "ran" -> "run"
- "connection", "connected", "connecting" -> "connect"
- "organization", "organize", "organized" -> "organ"

```r
corpus = tm_map(corpus, stemDocument)
```

The Porter Stemmer uses a series of rule-based suffix-stripping steps. It occasionally produces non-intuitive stems (e.g., "organization" -> "organ") but is effective at reducing dimensionality. The R package `SnowballC` provides the implementation.

## Bag-of-Words Model

The **Bag-of-Words (BoW)** model represents each document as a vector of word frequencies, ignoring word order and grammar. The result is a **Document-Term Matrix (DTM)** where:
- Each row is a document
- Each column is a unique term
- Each cell contains the frequency (or binary presence) of that term in that document

### Sparsity and Dimensionality Reduction

In the Apple tweet case:
- **Initial DTM**: 1,181 documents x 3,289 unique terms
- Most cells are zero (extremely sparse matrix)
- **After sparsity removal** (threshold 0.995): 1,181 documents x **309 terms**

The `removeSparseTerms()` function removes terms that appear in fewer than (1 - threshold) proportion of documents. At threshold 0.995, a term must appear in at least 0.5% of documents (about 6 out of 1,181) to be retained.

```r
dtm = DocumentTermMatrix(corpus)
sparse = removeSparseTerms(dtm, 0.995)
```

### Limitations of Bag-of-Words

- **Ignores word order**: "dog bites man" and "man bites dog" have identical BoW representations
- **No semantics**: Cannot capture meaning, sarcasm, or context
- **High dimensionality**: Even after sparsity removal, hundreds of features remain
- **No negation handling**: "not good" is represented as two separate positive features ("not" and "good")

Modern NLP has largely moved to embedding-based approaches (Word2Vec, BERT, GPT) that address these limitations, but BoW remains an effective baseline for many classification tasks.

## Case Study: Apple Tweet Sentiment Analysis (Lecture 6)

### Data Collection and Labeling

Tweets mentioning Apple products were collected and labeled for sentiment (positive/negative) using **Amazon Mechanical Turk (AMT)** — a crowdsourcing platform where human workers classify content at scale. This is a common approach for creating labeled training data for NLP tasks.

The target variable was **"Harsh"** — whether a tweet expressed negative/harsh sentiment toward Apple (TRUE/FALSE).

### Data Split

- **Training set**: 826 tweets (699 FALSE, 127 TRUE — ~15% positive rate)
- **Test set**: 355 tweets (300 FALSE, 55 TRUE)

The class imbalance (85/15 split) is typical of real-world sentiment data — most tweets are neutral or positive.

### Model Comparison

| Model | Accuracy | False Positive Rate | False Negative Rate | Notes |
|-------|----------|--------------------|--------------------|-------|
| Baseline (majority class) | 84.51% | 0% | 100% | Always predicts FALSE |
| CART (cp=0.2) | 87.89% | 0.33% | 76.64% | Single split on "freak" |
| CART (cp=0.001) | 87.61% | 2.67% | 65.45% | Uses "freak", "hate", "wtf", "like", "look" |
| CART (cp=0.034, CV) | **88.45%** | 1.00% | 69.09% | Cross-validated optimal |
| Random Forest | **88.73%** | 2.33% | 60.00% | Best accuracy, least interpretable |

### Key Observations

1. **Even the simplest CART model** (single split on "freak") beats the baseline by 3+ percentage points, demonstrating that even crude text features carry predictive signal

2. **The word "freak"** is the single most predictive feature — tweets containing "freak" are overwhelmingly negative. This makes intuitive sense given Apple's product context

3. **Cross-validation** (10-fold, cp grid from 0.001 to 0.2) identified cp = 0.034 as optimal, producing a 2-split tree using "freak" and "hate"

4. **Random Forest** achieves the highest accuracy (88.73%) and the best false negative rate (60.00%), but sacrifices the interpretability of a single tree. The model uses `nodesize` and `ntree` parameters with default settings

5. **All models have high false negative rates** (60-77%), meaning they miss most truly negative tweets. This is a consequence of the class imbalance — the models favor predicting the majority class

## Practical Applications of Text Analytics

The course highlights several real-world applications:

- **Sentiment analysis**: Monitoring brand perception on social media (over 7,000 research articles published on this topic)
- **Customer feedback classification**: Routing support tickets by topic or urgency
- **Spam detection**: Classifying emails as spam or legitimate
- **Document categorization**: Organizing large document collections by topic
- **Political analysis**: Tracking public opinion through social media text

### Industry Impact

- Hundreds of startups develop sentiment analysis solutions
- Real-time tweet analysis websites monitor public sentiment
- Text analytics handles the massive volume of unstructured data generated online — impossible to process manually

## Data Labeling with Amazon Mechanical Turk

The Apple tweets were labeled via **Amazon Mechanical Turk (AMT)**, a crowdsourcing platform where workers perform small tasks (a "HIT" — human intelligence task) for microtransaction fees (e.g., $0.02 per classified tweet). The EEMT5500 prompt was: *"Judge the sentiment expressed by the following item toward Apple Inc."* with five ordinal options from Strongly Negative (-2) to Strongly Positive (+2). **Five workers labeled each tweet** and the scores were averaged:

- "LOVE U @APPLE" → 1.8
- "@apple @twitter Happy Programmers' Day folks!" → 0.4
- "So disappointed in @Apple Sold me a Macbook Air that WONT run my apps..." → -1.4

AMT is the canonical example of how to bootstrap labeled training data at scale when automation is impossible but the task is too time-consuming for a single annotator. The averaging across 5 workers reduces individual noise, and the binary `Harsh = (Avg <= -1)` target then feeds into supervised learning.

## From BoW to Modern NLP

BoW has significant limitations: ignoring word order, handling negation poorly ("not good" becomes two positive features), and missing semantic similarity ("car" and "automobile" are orthogonal). Modern NLP addresses these via:

- **TF-IDF**: weights terms by inverse document frequency, penalizing common words
- **Word embeddings** (Word2Vec, GloVe): dense vectors where semantically similar words are close
- **Transformers** (BERT, GPT): context-dependent representations that capture long-range dependencies
- **LLMs**: replace the entire BoW → classifier pipeline with a prompt to a general-purpose model

EEMT5500 focuses on BoW as a baseline precisely because it is simple, transparent, and often surprisingly effective for text classification — the Apple tweet example improves over the majority-class baseline by nearly 4 percentage points with a single split on "freak".

## Related Concepts

- [[decision-trees|Decision Trees]] — primary classifier applied to text features in the course
- [[logistic-regression|Logistic Regression]] — commonly used baseline classifier for text classification
- [[clustering|Clustering]] — unsupervised text grouping (topic modeling is a related technique)
- [[recommendation-systems|Recommendation Systems]] — content-based filtering uses text features for item descriptions
- [[linear-regression|Linear Regression]] — regression on text features can predict continuous outcomes (e.g., review scores)
- [[ab-testing|A/B Testing]] — can test different text/messaging variants for effectiveness
- [[pca|PCA]] — Latent Semantic Analysis applies SVD/PCA to document-term matrices
- [[wiki/entities/hkust|HKUST]] — course home institution

## Source Materials

- Lecture 6: Text Analytics (NLP)
- [[wiki/sources/courses/applied-statistics|EEMT5500 Applied Probability, Statistics and Data Analytics]]
