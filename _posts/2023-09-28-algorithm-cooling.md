---
layout: post
title: "[Algorithm] Cooling"
date: 2023-09-28 00:23 +0800
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

The most simple condition is that the opponent will take the same action every time. In this case, we can easily guess the action by counting the number of times the opponent has taken each action, let's call this player S.

|        | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action | R   | R   | R   | R   | R   | R   | R   | R   | R   | R   |
| Guess  | R   | R   | R   | R   | R   | R   | R   | R   | R   | R   |

The second condition is that the opponent will take the same action most of the time, and take other actions occasionally. In this case, we want to keep the guess consist with the action which the opponent has taken most of the time, let's call this player O.

|        | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action | R   | R   | R   | R   | R   | R   | R   | R   | P   | R   |
| Guess  | R   | R   | R   | R   | R   | R   | R   | R   | R   | R   |

The third condition is that the opponent will take the same action most of the time, and from some opint, the opponent will take other actions most of the time. In this case, we want to change the guess to the action which the opponent has changed to, let's call this player C.

|        | 1   | 2   | 3   | 4   | 5   | 6   | 7   | 8   | 9   | 10  |
| ------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Action | R   | R   | R   | R   | R   | S   | S   | S   | S   | S   |
| Guess  | R   | R   | R   | R   | R   | R   | R   | S   | S   | S   |

Let's implement the algorithm in Python:

```python
import random
import math
import collections

def guess(history_actions, base_hotness=1, cooling_rate=1):
    def hotness(time_passed, base_hotness=1, cooling_rate=1):
        return base_hotness * math.exp(-1.0 * time_passed * cooling_rate)
    
    action_hotness = collections.defaultdict(lambda: 0)
    for i, action in enumerate(history_actions):
        action_hotness[action] += hotness(i, base_hotness, cooling_rate)
    
    return max(action_hotness, key=action_hotness.get)

if __name__ == "__main__":
    history_actions = ["R", "R", "R", "R", "R", "S", "S", "S", "S", "S"]
    print(guess(history_actions))
```

We can find that the base hotness doesn't affect the result, but the cooling rate does. The larger the cooling rate is, the more sensitive the guess is to the recent actions. The smaller the cooling rate is, the more sensitive the guess is to the long past actions, and the guess will change more slowly.

## Cooling & Half-life

The half-life of a substance is the time it takes for a quantity to reduce to half its initial value. The term is commonly used in nuclear physics to describe how quickly unstable atoms undergo, or how long stable atoms survive, radioactive decay. The term is also used more generally to characterize any type of exponential or non-exponential decay.

The half-life of a substance is related to the cooling rate of the substance. The larger the cooling rate is, the shorter the half-life is. The smaller the cooling rate is, the longer the half-life is.

We can calculate the half-life period from the cooling rate:

$$
\frac{1}{2} = e^{-kt_{1/2}}
$$

Then we can get:

$$
t_{1/2} = \frac{ln(2)}{k}
$$

And we can get the cooling rate from the half-life period:

$$
k = \frac{ln(2)}{t_{1/2}}
$$

Let's add a function to calculate cooling rate from half-life period:

```python
def cooling_rate_from_half_life_period(half_life_period):
    return math.log(2) / half_life_period
```

And we can test in our Rock-Paper-Scissors guessing algorithm:

```python
if __name__ == "__main__":
    history_actions = ["R", "R", "R", "R", "R", "S", "S", "S", "S", "S"]
    print(guess(history_actions, cooling_rate=cooling_rate_from_half_life_period(3)))
```

More test can be found in [this file](https://gist.github.com/henyihanwobushi/bc526319157c6bc85c49cad5f74f0f9e)

## Reference

- Newton's law of cooling [https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling](https://en.wikipedia.org/wiki/Newton%27s_law_of_cooling)
- Reddit's "hotness" algorithm [https://www.tonysm.com/reddits-hotness-algorithm/](https://www.tonysm.com/reddits-hotness-algorithm/)