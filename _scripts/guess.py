import random
import math
import collections


def guess(history_actions, base_hotness=1, cooling_rate=1):
    def hotness(time_passed, base_hotness=1, cooling_rate=1):
        return base_hotness * math.exp(-1.0 * time_passed * cooling_rate)

    action_hotness = collections.defaultdict(lambda: 0)
    for i, action in enumerate(history_actions):
        action_hotness[action] += hotness(len(history_actions) - i,
                                          base_hotness, cooling_rate)

    return max(action_hotness, key=action_hotness.get)


def play(history_actions, base_hotness=1, cooling_rate=1):
    guesses = [guess(history_actions[:i+1], base_hotness, cooling_rate)
               for i in range(len(history_actions) - 1)]

    print(history_actions)
    print([" "] + guesses)
    return len([1 for a, b in zip(history_actions[1:], guesses) if a != b])


if __name__ == "__main__":
    def opt(cr=0.24):
        errors = 0
        e1 = play(history_actions=[
            "R", "R", "R", "R", "R", "S", "S", "S", "S", "S"], base_hotness=1, cooling_rate=cr)
        e2 = play(history_actions=[
            "R", "R", "R", "R", "R", "S", "R", "R", "R", "R"], base_hotness=1, cooling_rate=cr)
        e3 = play(history_actions=[
            "R", "R", "R", "R", "R", "S", "S", "R", "R", "R"], base_hotness=1, cooling_rate=cr)
        e4 = play(history_actions=[
            "R", "R", "R", "R", "R", "S", "S", "S", "S", "S"], base_hotness=1, cooling_rate=cr)
        errors += e1 + e2 + e3 + e4
        return errors
    erros = [opt(cr=cr/100) for cr in range(1, 200)]
    print(erros)

    print("e", opt(cr=1))
