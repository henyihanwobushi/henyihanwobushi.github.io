---
layout: post
title: "[Algorithm] Cooling"
---

Cooling is removal of heat, usually resulting in a lower temperature and/or phase change.

## Newton's law of cooling

Newton's law of cooling states that the rate of heat loss of a body is directly proportional to the difference in the temperatures between the body and its surroundings as long as the temperature difference is small and the nature of heat transfer mechanism remains the same.

Newton's law of cooling is used for convection with heat transfer coefficient H, surface area A, and surface temperature Ts:

$$
\frac{dQ}{dt} = -H A (T - T_s)
$$

Where:
- $Q$ is the heat loss or gain of the object,
- $t$ is time,
- $T$ is the temperature of the object,
- $T_s$ is the temperature of the surroundings,
- $H$ is the heat transfer coefficient, and
- $A$ is the surface area of the object.

The heat capacity of the object is assumed to be constant over the range of temperatures involved. Then we can simplify the equation to:

$$
\frac{dT}{dt} = k (T_s - T)
$$

Let's define the hotness of an object as the temperature difference between the object and the surroundings: $H = T - T_s$. Then the rate of change of hotness is:

$$
\frac{dH}{dt} = -k H
$$

Then the we can get a function of hotness over time:

$$
H(t) = H_0 e^{-kt}
$$

Where $H_0$ is the initial hotness of the object.

It's easy to see that the hotness of the object will decrease exponentially over time. The larger the $k$ is, the faster the hotness will decrease.

<iframe src="https://www.desmos.com/calculator/jhznirkfzl?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

## Rock-Paper-Scissors

In the game of Rock-Paper-Scissors, we may prefer a certain action over others when we decide to choose a action **randomly**.

We will use Newton's low to guess which action will be taken by the opponent.




## Reference

- Newton's law of cooling [https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling](https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling)
- Reddit's "hotness" algorithm [https://www.tonysm.com/reddits-hotness-algorithm/](https://www.tonysm.com/reddits-hotness-algorithm/)