---
layout: post
title: "[algorithm] Hausdorff Distance"
---
# Introduction

Hausdorff Distance is a measure of the degree of mismatch between two sets of points that takes into account the order of the points in the sets. It is defined as the maximum of the distances from a point in one set to the closest point in the other set.

## Definition

Let $A$ and $B$ be subsets of a metric space $(M, d)$. The directed Hausdorff distance from $A$ to $B$ is defined by

$$
d_{H}(A, B)=\max \left(\sup _{a \in A} \inf _{b \in B} d(a, b), \sup _{b \in B} \inf _{a \in A} d(a, b)\right)
$$