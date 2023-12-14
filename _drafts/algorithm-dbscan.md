---
layout: post
title: "[Algorithm] DBScan"
---

DBScan is a density-based clustering algorithm. It can find clusters of any shape, and it can also identify outliers. DBScan works by identifying points that are in crowded regions of the space, where many data points are close together, and points that are in sparse regions of the space, where data points are farther apart. [[1]](https://en.wikipedia.org/wiki/DBSCAN)


## Procedure

1. Randomly select a point $p$.
2. Retrieve all points density-reachable from $p$ w.r.t. $\epsilon$ and $MinPts$.
3. If $p$ is a core point, a cluster is formed.
4. If $p$ is a border point, no points are density-reachable from $p$, then visit the next point.
5. Repeat the process until all of the data points have been processed.
6. Points that have not been visited are noise.

Pseudo code:

```
DBSCAN(D, eps, MinPts)
   C = 0
   for each unvisited point P in dataset D
      mark P as visited
      NeighborPts = regionQuery(P, eps)
      if sizeof(NeighborPts) < MinPts
         mark P as NOISE
      else
         C = next cluster
         expandCluster(P, NeighborPts, C, eps, MinPts)
```

## AutoDBSCAN

AutoDBSCAN is an improvement of DBSCAN. It is a density-based clustering algorithm that automatically determines the value of $\epsilon$ and $MinPts$. [[2]](https://en.wikipedia.org/wiki/DBSCAN#AutoDBSCAN)

Pseudo code:

```
AutoDBSCAN(D, MinPts)
   C = 0
   for each unvisited point P in dataset D
      mark P as visited
      NeighborPts = regionQuery(P, eps)
      if sizeof(NeighborPts) < MinPts
         mark P as NOISE
      else
         C = next cluster
         expandCluster(P, NeighborPts, C, eps, MinPts)
```




# Reference

- [1] DBSCAN [https://en.wikipedia.org/wiki/DBSCAN](https://en.wikipedia.org/wiki/DBSCAN)