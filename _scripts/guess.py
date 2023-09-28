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


def cooling_rate_from_half_life_period(half_life_period):
    return math.log(2) / half_life_period


def player_consist(actions=28):
    action = random.choice(["R", "P", "S"])
    return [action] * actions


def player_random(actions=28):
    return [random.choice(["R", "P", "S"]) for _ in range(actions)]


def player_optimal(actions=28):
    action = random.choice(["R", "P", "S"])
    return [random.choice(["R", "P", "S"]) if random.random() < 0.1 else action for _ in range(actions)]


def player_change(change_last=10, actions=28):
    choices = ["R", "P", "S"]
    action1 = random.choice(choices)
    choices.remove(action1)
    action2 = random.choice(choices)
    return [action1] * (actions - change_last) + [action2] * change_last


if __name__ == "__main__":
    def opt(cr=0.24):
        errors = 0
        e1 = play(history_actions=player_change(),
                  base_hotness=1, cooling_rate=cr)
        # e2 = play(history_actions=player_consist(),
        #           base_hotness=1, cooling_rate=cr)
        e2 = 0
        e3 = play(history_actions=player_optimal(),
                  base_hotness=1, cooling_rate=cr)
        # e4 = play(history_actions=player_random(),
        #           base_hotness=1, cooling_rate=cr)
        e4 = 0
        errors += e1 + e2 + e3 + e4
        return errors
    half_life_periods = range(1, 10)
    erros = [opt(cr=cooling_rate_from_half_life_period(hl))
             for hl in half_life_periods]
    print("| Half-life period | Errors |")
    print("| --- | --- |")
    for h, e in zip(half_life_periods, erros):
        print(f'| {h} | {e} |')
    print("e", opt(cr=1))
