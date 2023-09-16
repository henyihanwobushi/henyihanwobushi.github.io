---
layout: post
title: "[Algorithm] Hausdorff Distance"
date: 2023-09-16 16:59 +0800
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

Hausdorff distance with a custom distance function:

```python
import numpy as np

def hausdorff_distance(A, B, distance_func):
    """
    Compute the Hausdorff Distance between A and B
    """
    D_mat = np.array([[distance_func(a, b) for b in B] for a in A])
    return np.max(np.array([np.max(np.min(D_mat, axis=0)), np.max(np.min(D_mat, axis=1))]))
```


## Distance with Big O

The Hausdorff distance can be used to compare two GPS traces. The coordinate of GPS coordinates is usually in Latitude, Longitude.

The distance between two points on the earth's surface is calculated using the Haversine formula. The Haversine formula is an equation important in navigation, giving great-circle distances between two points on a sphere from their longitudes and latitudes.

The Haversine formula is:

$$
d=2 r \arcsin \left(\sqrt{\sin ^{2}\left(\frac{\varphi_{2}-\varphi_{1}}{2}\right)+\cos \left(\varphi_{1}\right) \cos \left(\varphi_{2}\right) \sin ^{2}\left(\frac{\lambda_{2}-\lambda_{1}}{2}\right)}\right)
$$

where:
- $d$ is the distance between the two points (along a great circle of the sphere; see spherical distance),
- $r$ is the radius of the sphere,
- $\varphi_{1}, \varphi_{2}:$ latitude of point 1 and latitude of point 2, in radians,
- $\lambda_{1}, \lambda_{2}:$ longitude of point 1 and longitude of point 2, in radians.

The Haversine formula is numerically ill-conditioned for small distances. When the points are close together, the formula is inaccurate due to catastrophic cancellation. The error is relative to the square of the distance between the points (i.e. quadratic error). The error is zero when the points are antipodal (on opposite sides of the sphere).

Python implementation:

```python
import numpy as np

def haversine_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(np.radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = np.sin(dlat / 2) ** 2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon / 2) ** 2
    c = 2 * np.arcsin(np.sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r
```

Then we can calculate the Hausdorff distance between two GPS traces:

```python
# ...
hausdorff_distance(A, B, lambda a, b: haversine_distance(*a, *b))
```