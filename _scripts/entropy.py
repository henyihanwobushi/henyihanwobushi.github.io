import math


def entropy(p):
    """
    Compute the entropy of a probability distribution.

    Parameters
    p : array of arrays

    Returns
    -------
    H : float
        Entropy.

    """
    N = sum([len(e) for e in p])
    print(N)
    es = [(1.0 * len(e) / N) * math.log(1.0 * len(e) / N) for e in p if len(e) > 0]
    e = -1.0 * sum(es)
    return e


if __name__ == '__main__':
    def generate(n, m=16, random=True):
        if not random:
            return [[1]]*n
        import random
        res = [[] for i in range(m)]
        print(res)
        for e in range(n):
            res[random.randint(0, m - 1)].append(e)
        print(res)
        return res
    print(entropy([[2],[2]]))
