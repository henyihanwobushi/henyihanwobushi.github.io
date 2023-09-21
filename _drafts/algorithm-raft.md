---
layout: post
title: "[Algorithm] Raft"
---

Raft is a algorithm that solves the problem of distributed consensus. It is designed to be easy to understand. It's equivalent to Paxos in fault-tolerance and performance.

## Problem

The problem of distributed consensus is that how to make a group of servers agree on a value. The problem is important because it is a fundamental part of the infrastructure of many systems, including databases, search engines, and configuration management systems.

## Solution

Raft decomposes the consensus problem into three relatively independent subproblems:

- Leader election
- Log replication

### Leader election

When the existing leader fails or when the algorithm initializes, a new leader needs to be elected.



# Reference
- [In Search of an Understandable Consensus Algorithm](https://raft.github.io/raft.pdf)
- The Raft Consensus Algorithm ([https://raft.github.io/](https://raft.github.io/))
- Implementing Raft ([https://eli.thegreenplace.net/2020/implementing-raft-part-0-introduction/](https://eli.thegreenplace.net/2020/implementing-raft-part-0-introduction/))