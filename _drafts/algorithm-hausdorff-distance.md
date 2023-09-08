---
layout: post
title: "[algorithm] Hausdorff Distance"
---
# Introduction

Hausdorff Distance is a measure of the degree of mismatch between two sets of points that takes into account the order of the points in the sets. It is defined as the maximum of the distances from a point in one set to the closest point in the other set.

## Definition

Let $A$ and $B$ be subsets of a metric space $(M, d)$. The directed Hausdorff distance from $A$ to $B$ is defined by

$$
d_{H}(A, B)=\max 
    \left( 
        \sup _{a \in A} ( 
            \inf _{b \in B} d(a, b)
        ),
        \sup _{b \in B} (
            \inf _{a \in A} d(a, b)
        )
    \right)
$$

where 
- $d(a, b)$ is the distance between points $a$ and $b$.
- sup is the supremum, or least upper bound, of a set.
- inf is the infimum, or greatest lower bound, of a set.
- $\inf _{b \in B} d(a, b)$ is the distance from point $a$ to its nearest neighbor in $B$.
- $\sup _{a \in A} \inf _{b \in B} d(a, b)$ is the distance from the nearest neighbor in $A$ to its nearest neighbor in $B$.

## Implementation

```python
import numpy as np

def hausdorff_distance(A, B):
    """
    Compute the Hausdorff Distance between A and B
    """
    D_mat = np.sqrt(np.sum((A[:, None, :] - B[None, :, :]) ** 2, axis=-1))
    return np.max(np.array([np.max(np.min(D_mat, axis=0)), np.max(np.min(D_mat, axis=1))]))
```

## Distance with Big O

The Hausdorff distance can be used to compare two GPS traces. The coordinate of GPS coordinates is usually in Latitude, Longitude, and Altitude (LLA). To compute the Hausdorff distance, we need to use the Big O algorithm to compute the distance between two points in LLA.

```python
import numpy as np

def lla2ecef(lat, lon, alt):
    """
    Convert LLA to ECEF
    """
    a = 6378137.0
    b = 6356752.314245
    f = (a - b) / a
    e_sq = f * (2 - f)
    lamb = np.deg2rad(lat)
    phi = np.deg2rad(lon)
    s = np.sin(lamb)
    N = a / np.sqrt(1 - e_sq * s * s)

    sin_lambda = np.sin(lamb)
    cos_lambda = np.cos(lamb)
    sin_phi = np.sin(phi)
    cos_phi = np.cos(phi)

    x = (alt + N) * cos_lambda * cos_phi
    y = (alt + N) * cos_lambda * sin_phi
    z = (alt + (1 - e_sq) * N) * sin_lambda

    return x, y, z
```