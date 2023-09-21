---
layout: post
title: "[Algorithm] Hash"
---

Hash is a algorithm to map data of arbitrary size to data of fixed size. Data hashes are usually used to verify the integrity of data. Different hash values indicate that the input data is different, but the same hash value does not necessarily mean that the input data is the same. Different data may have the same hash value, which is called **hash collision**.

## Hash Algorithms

| Algorithm | Description | Hash Size | Collision Probability |
| --------- | ----------- | --------- | --------------------- |
| MD5       |             | 128 bits  | 1/2^128               |
| SHA-1     |             | 160 bits  | 1/2^160               |
| SHA-256   |             | 256 bits  | 1/2^256               |
| SHA-512   |             | 512 bits  | 1/2^512               |

