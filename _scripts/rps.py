import random
import math
from collections import defaultdict


def player(times, p_r=1, p_p=1, p_s=1):
    def choose(actions):
        for i in range(times):
            yield random.choice(actions)
    return choose(['r'] * p_r + ['p'] * p_p + ['s'] * p_s)


def guess(actions, init_heat=10, cooling_rate=0.1):
    values = defaultdict(lambda: 0)
    for i in range(len(actions)):
        values[actions[i]] += math.exp(-i * cooling_rate) * init_heat
    return max(values, key=values.get)


def test_guess(init_heat=10, cooling_rate=0.1, rounds=100, prefers=(1, 10, 1)):
    guess_success_count = 0
    for i in range(rounds):
        actions = list(player(11, *prefers))
        g = guess(actions[:-1], 1, 0.1)
        # print(actions[:-1], actions[-1], g)
        if actions[-1] == g:
            guess_success_count += 1

    return 1.0 * guess_success_count / rounds


if __name__ == '__main__':
    for cooling_rate in [0.1, 0.2, 0.5, 1]:
        for init_heat in [1, 2, 5, 10, 20, 50, 100]:
            for rounds in [50, 100, 1000]:
                success_rate = test_guess(init_heat, cooling_rate, rounds)
                print('init_heat: {}, cooling_rate: {}, rounds: {}, success_rate: {}'.format(
                    init_heat, cooling_rate, rounds, success_rate))
    
