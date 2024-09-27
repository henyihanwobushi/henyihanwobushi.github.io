---
layout: post
title: "[Tool] LLM"
---

# Introduction

Large Language Models (LLMs) are the next generation of NLP models. They are capable of generating text with a high degree of fluency and coherence. LLMs have been shown to out perform human-generated text in many tasks such as machine translation, question answering and summarization.

LLM is a type of neural network that uses deep learning techniques to learn from large amounts of text data. It can generate human-like text, understand context and make predictions based on the input data.

## Tecnologies

LLM is based on NLP (Natural Language Processing) and deep learning tecnhologies, like Wav2Vec, Transformers...

### Word Vectors

Word vectors are a way to represent words in a numerical format. They capture the semantic meaning of a word by representing it in a high-dimensional space, instead of one-hot encoding. The word vectors are learned from large amounts of text data, and they capture the syntactic and semantic relationships between words. The similarity between words can be measured using dot product of word vectors.

#### Word2Vec
The method used to learn word vectors is called Word2Vec. It's build on that, "Word meaning depends on its context".

Word vectors are a vector composition, one for the word as center word, and another as context word.

Word vectors are trained using all the word squences, for each word at position $t$, we got a center word $o$, and $m$ context word $c$, we can calculate the pribability  of o given c as $ P(w_{t+j} | w_t) $, or vice versa, $ P(w_t | w_{t+j}) $.

For all variables to be optimized, $\theta$, we have data likelihood:
$$ Likelihood = L(\theta) = \prod_{t=1}^{T} \prod_{-m\leq j \leq m} p(w_{t+j}|w_t) $$

The objective function is to negative log likelihood:
$$ J(\theta) = - \log \frac{1}{T}log L(\theta) 
= - \frac{1}{T} \sum_{t=1}^{T}\sum_{-m \leq j \leq m,\space j \neq 0} logP(w_{t+j}|w_t;\theta)$$

To minimize the objective function, we use stochastic gradient descent (SGD) to update the parameters $\theta$ iteratively.

We use two vectors per word $w$:
- $v_w$: when $w$ is the center word,
- $u_w$: when $w$ is the context word.
Then, we can calculate the probability of o given c as:
$$ P(o|c) = \frac{exp(u_o^T v_c)}{\sum_{v\in V}exp(u_w^T v_c)} $$

$$
\theta = \begin{bmatrix}v_a.. \\ v_b.. \\ v_z.. \\ u_a.. \\ u_z.. \end{bmatrix}
$$

update equation:
$$
 \theta^{new} = \theta^{old} - \alpha \nabla_{\theta}J(\theta) \\
 \theta_j^{new} = \theta_j^{old} - \alpha \frac{\partial J(\theta)}{\partial \theta_j}
$$

### Predict With Word Vectors

Given a word $w_t$, we have the word vectors $v_w$ and $u_w$, we can calculate the probability with neutral network:

$$ 
h = f(Wx + b) \\ 
s = u^T h 
$$

The Jacobians are:
$$
\frac{\partial}{\partial u}(u^T h) = h^T \\
\frac{\partial}{\partial h}\big(f(z)\big) = diag\big(f'(z)\big) \\
\frac{\partial}{\partial b}(Wx + b) = I \\
\frac{\partial s}{\partial b} = 
\frac{\partial s}{\partial h}
\frac{\partial h}{\partial z}
\frac{\partial z}{\partial h}
=u^Tdiag\big(f'(z)\big)I
$$

The gradient update with SGD, which compiles to a computation graph, and the parameters are updated as:
- forward propagation: calculate the output of each layer;
- back propagation: initialize the oupput gradient to 1, then calculate the gradient of each layer with chain rule;

And this work is completed by the frameworks like PyTorch, TensorFlow.


### Language Model

A language model is a system that assigns a probability distribution to sequences of words. It is used for predicting the next word in a sequence, given the previous words.

$$
P(w_1, w_2, ..., w_n) = \prod_{t=1}^{n} P(w_t|w_1, w_2, ..., w_{t-1})
$$

#### N-gram Model (fixed-window)
An n-gram language model assigns a probability to the next word in a sequence with $n$ words chunks.

There a Markov assumption, which is that the next word in a sequence depends only on the previous $n-1$ words.

$$
P(w | n-gram) = \frac {count(n-gram, w)}{count(n-gram)}
$$

#### Neutral Networks Language Model

- words / one-hot vectors:
  $x^{(1)}$, $x^{(2)}$, ..., $x^{(T)}$
- concatenate all words into a single vector $e$:
  $e = [e^{(1)}, e^{(2)}, e^{(3)}, e^{(4)} ]$
- the hidden layer:
  $h = f(We + b)$
- output distribution:
  $\hat{y} = softmax(Uh + b_2) \in \mathbb{R}^{|V|}$

The problem of fixed-size neutral network is that, it can't process dynamic window size.

### RNN

RNNs are a type of neural network that can process sequential data, such as text or time series.

- input: word one-hot vector:
  $x^{(t)} \in \mathbb{R}^{|V|}$
- word embedding:
  $e^{(t)} = Ex^{(t)}$
- hidden states:
  $h^{(t)} = \sigma \big( W_{h}h^{(t-1)} + W_{e}e^{(t)} + b_1\big) $ with initial hidden state $h^{(0)}$
- output layer:
  $\hat{y} = softmax(Uh^{(t)} + b_2) \in \mathbb{R}^{|V|}$

The key idea is to use a hidden state $h_t$ that represents the probability distribution over all possible previous words in the sequence.

$$
J^{(t)}(\theta) = CE(y^{(t)}, \hat{y}^{(t)}) = -\sum_{w \in V} y^{(t)}_w \log \hat{y}^{(t)}_w = -\log \hat{y}^{(t)}_{x_{t-1}}
$$

The overall loss function on step t is cross-entropy between the predicted probability distribution $\hat{y}^{(t)}$ and the true next word $y^{(t)}$(one-hot for $x^{(t+1)}$)

$$
J(\theta) = \frac{1}{T}\sum_{t=1}^{T}J^{(t)}(\theta)
= -\frac{1}{T}\sum_{t=1}^{T} J^{(t)}(\theta)
= \frac{1}{T}\sum_{t=1}^{T} \log \hat{y}^{(t)}_{x_{t-1}}
$$

#### Model Evaluation

The statndard evaluation of language model is perplexity:

$$
PPL = \prod_{t=1}^{T} \big( \frac{1}{P_{LM}(x^{t+1}|x^t,x^{t-1},...,x^1)} \big)^{(1/T)}\\
= \prod_{t=1}^{T}\bigg( \frac{1}{\hat{y}_{x_{t+1}}^{(t)}} \bigg)^{1/T}\\
= exp \bigg(\frac{1}{T}\sum_{t=1}^{T}-\log \hat{y}_{x_{t+1}}^{(t)}\bigg)\\
=exp\bigg(\frac{1}{T}\sum_{t=1}^{T}J^{(t)}(\theta)\bigg)
$$

The perplexity is the exponential of negative log likelihood, the lower the perplexity is, the better the model.

### Transformers

Transformers are a type of neural network that uses attention mechanisms to learn from large amounts of data. Before Tranformers, NLP models used recurrent neural networks (RNNs) or long short-term memory (LSTM) networks to process text data.

# Applications

LLMs shows ability to:
- 

## Q&A



## General Predict Machine



### RAG