---
layout: post
title: "[Learing] Standord NLP 01"
---

# Meaning of a word

$$
signifier(symbol) = signified(meaning) = denotational semantics
$$

- 字典中一般用上意词、同义词来表达词的含义：没法计算词语的相似性；
- One-Hot encoding：统一无法计算词语的相似性；

Solution: learn to encode similarity in the vectors themselves

Distributional semantics: A word's meaning is given by the words that frequently appear close-by (**context**).

Word Vectors：
目标：经常出现在相似语境中的词的向量是相似的。

Word2Vec: 一个词向量计算框架

Position t, Center word c, Context words o:

Use similarity of word vectors to calculate the probability of word c in context o. Adjust the word vector to maximize this probability.

Data likelihood:
$$
Likelihood = L(\theta) = \prod_{t = 1}^{T}\prod_{-m <= j <= m}^{n} P(w_{t+j}|w_t;\theta)
$$

Objective function:
$$
J(\theta) = - log
$$

# Word Vectors



# Models
YONO: You Only Need One Model for Open-domain Question Answering