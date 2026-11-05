---
title: "Search Engines"
full_name: "COMP4321 Search Engines for Web and Enterprise Data"
type: source
tags: [courses, comp, undergraduate, information-retrieval, search-engines, nlp, comp4321, level-4]
created: "2026-04-14"
updated: "2026-04-14"
source: "raw/courses/COMP/COMP4321"
confidence: medium
---

## 概述

COMP4321 網絡與企業數據搜索引擎為計算機科學四年級學生系統介紹信息檢索（IR）的核心理論與工程實踐，先修要求為 COMP3311 資料庫系統及 COMP3711 演算法，對自然語言處理有興趣的學生尤為適合。課程參考 Manning、Raghavan & Schütze《信息檢索導論》（IIR）及 Blair & Maron（1985）等經典實證研究，涵蓋網路爬蟲架構（robots.txt、URL 去重）、倒排索引的構建與壓縮（BSBI、SPIMI、$\gamma$ 編碼）、布林模型與向量空間模型（TF-IDF、BM25）、PageRank 與 HITS 連結分析排名演算法，以及查詢擴展（Rocchio 相關反饋）與拼寫校正（噪聲通道模型）。現代語義搜索部分介紹 Word2Vec 詞嵌入、LSA 奇異值分解及 DPR 密集段落檢索等深度學習方法。課程配合大型實驗項目，要求學生以 Java 或 Python 從零開發一個完整的搜索引擎原型，直接培養索引工程、相關性排名調優及 IR 評估指標（MAP、NDCG）的實踐能力。搜索引擎技術是推薦系統、企業知識庫管理及 RAG（檢索增強生成）系統的底層基礎設施。

## Key Topics

### Information Retrieval Fundamentals
- Information retrieval (IR) vs. database retrieval: structured vs. unstructured data; relevance
- Evaluation metrics: precision, recall, F1, MAP (mean average precision), NDCG (normalized discounted cumulative gain)
- **Blair & Maron (1985)** — classic empirical study showing full-text search recall far below user expectations
- Cranfield paradigm: test collections (queries + relevance judgments) for IR evaluation

### Web Crawling
- Crawler architecture: URL frontier; politeness (robots.txt, crawl delay); DNS caching
- BFS vs. focused crawling; duplicate detection (SimHash, URL normalization)
- Dynamic content: JavaScript rendering; Selenium/Puppeteer for SPAs
- Crawl scheduling: prioritizing fresh content; estimating page change frequency

### Indexing
- **Inverted index**: vocabulary (dictionary) → postings lists (doc IDs + positions)
- Index construction: BSBI (blocked sort-based) and SPIMI for large corpora
- **Compression**: $\delta$-coding, $\gamma$-coding for postings; Elias-Fano representation
- Index updates: add/delete documents; lazy deletion with re-indexing
- Skip pointers in postings lists for AND query optimization

### Retrieval Models
- **Boolean model**: exact match; no ranking; poor user experience
- **Vector Space Model (TF-IDF)**: documents and queries as vectors; cosine similarity
  - TF: $tf(t,d) = \log(1 + f_{t,d})$; IDF: $idf(t) = \log(N/df_t)$; combined weight
  - Cosine similarity: $\cos(\mathbf{q}, \mathbf{d}) = \frac{\mathbf{q} \cdot \mathbf{d}}{|\mathbf{q}||\mathbf{d}|}$
- **BM25** (Okapi BM25): probabilistic model; tunable parameters $k_1$, $b$; widely used in practice
- **Language models**: query likelihood; Jelinek-Mercer smoothing; Dirichlet smoothing

### Web Ranking
- **PageRank**: random surfer model; $PR(u) = \frac{1-d}{N} + d\sum_{v \to u} \frac{PR(v)}{L(v)}$; power iteration
- **HITS** (Kleinberg): hub and authority scores; query-dependent; vs. PageRank query-independent
- Anchor text; click-through data; freshness signals
- Learning to Rank: pointwise, pairwise (RankSVM), listwise (LambdaMART); LETOR datasets

### Query Processing
- Query parsing: tokenization, stemming (Porter), lemmatization, stopword removal
- Query expansion: relevance feedback (Rocchio algorithm); pseudo-relevance feedback; query suggestion
- Phrase queries: positional index; biword index trade-off
- Spelling correction: edit distance; noisy channel model (P(q|w) × P(w))

### Semantic Search (Modern)
- Latent Semantic Analysis (LSA): SVD of term-document matrix; latent topics
- Word embeddings: Word2Vec (skip-gram, CBOW); GloVe; semantic similarity in embedding space
- Dense retrieval: bi-encoder models (DPR — Dense Passage Retrieval); FAISS for ANN search
- Cross-encoder reranking: BERT-based relevance scoring; two-stage pipeline
- See [[nlp-basics]]

## Related Concepts

- [[nlp-basics]]
- [[recommendation-systems]]
- [[machine-learning-advanced]]
- [[algorithms-and-data-structures]]

## Source Materials

- COMP4321 Course Materials
