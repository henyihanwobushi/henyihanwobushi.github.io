---
layout: post
title: "[Algorithm] TCN"
---

# Introduction

Temporal Convolutional Networks (TCN) is a type of recurrent neural network (RNN) that is specifically designed to handle time series data. It is a type of RNN that is specifically designed to handle time series data.

# Model

The model is composed of two parts: the encoder and the decoder. The encoder is a stack of convolutional layers and the decoder is a stack of fully connected layers.

The encoder consists of a stack of convolutional layers. Each convolutional layer is composed of a convolutional layer, a batch normalization layer, and a rectified linear unit (ReLU) activation function. The convolutional layers are stacked to increase the complexity of the model.

The decoder consists of a stack of fully connected layers. Each fully connected layer is composed of a fully connected layer, a batch normalization layer, and a ReLU activation function. The fully connected layers are stacked to increase the complexity of the model.

# Dilated Convolutions

The dilated convolutions are used to increase the receptive field of the model.
With 1-D sequence input $x \in \mathbb{R}^{N}$, and a filter $f: \{0, ..., k-1\} \rightarrow \mathbb{R}$, the dilated convolutions are defined as:


## Reference

- [An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](https://arxiv.org/abs/1803.01271)
- [Convolution arithmetic](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)
- [A guide to convolution arithmetic for deep learning](https://arxiv.org/abs/1603.07285)