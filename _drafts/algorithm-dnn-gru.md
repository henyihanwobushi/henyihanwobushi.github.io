---
layout: post
title: "[Algorithm] DNN-GRU"
---

# Introduction

This is a note for the paper [Deep Neural Networks with Gated Recurrent Units for Noise Robust Speech Recognition](https://arxiv.org/pdf/1511.06978.pdf).

# Gated Recurrent Unit

The GRU is a gating mechanism in RNN. It is similar to LSTM, but has fewer parameters than LSTM.

## LSTM

The LSTM has three gates: input gate, forget gate, and output gate. The input gate controls the amount of new information to be added to the memory cell. The forget gate controls the amount of information to be forgotten from the memory cell. The output gate controls the amount of information to be output from the memory cell.