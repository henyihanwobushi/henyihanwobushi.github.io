import math
import random

class HyperLogLog(object):
    def __init__(self, b=16, M=None):
        self.b = b
        self.m = 1 << b
        self.M = M if M else [0] * self.m
        self.alpha = self.get_alpha()

    def get_alpha(self):
        if self.m == 16:
            return 0.673
        elif self.m == 32:
            return 0.697
        elif self.m == 64:
            return 0.709
        else:
            return 0.7213 / (1 + 1.079 / self.m)

    def add(self, x):
        '''Adds an element to the HyperLogLog.'''
        x = hash(x)
        a, b = self.split(x)
        j = self.get_j(b)
        w = self.get_w(b)
        self.M[j] = max(self.M[j], w)

    def split(self, x):
        '''Returns the first x bits, and the rest of the bits.'''
        a = x >> (64 - self.b)
        b = x & ((1 << (64 - self.b)) - 1)
        return a, b

    def get_j(self, b):
        '''Returns the leftmost b bits of x.'''
        return b ^ ((1 << (self.b - 1)) - 1)

    def get_w(self, b):
        '''Returns the position of the first 1 bit from the right.'''
        return self.get_rho(b) + 1

    def get_rho(self, x):
        '''Returns the position of the first 1 bit from the right.'''
        rho = 1
        while x & 1 == 0:
            rho += 1
            x >>= 1
        return rho

    def count(self):
        '''Returns the estimated cardinality.'''
        E = self.alpha * self.m * self.m / sum(math.pow(2, -x) for x in self.M)
        if E <= 5.0 / 2.0 * self.m:
            V = self.M.count(0)
            if V != 0:
                E = self.linear_counting(V)
        elif E > 1.0 / 30.0 * math.pow(2, 64):
            E = -math.pow(2, 64) * math.log(1 - E / math.pow(2, 64))
        return E

    def linear_counting(self, V):
        return self.m * math.log(self.m / V)

    def merge(self, other):
        assert self.b == other.b
        for i in range(self.m):
            self.M[i] = max(self.M[i], other.M[i])

    def __add__(self, other):
        assert self.b == other.b
        hll = HyperLogLog(self.b)
        hll.merge(self)
        hll.merge(other)
        return hll
    
    def serialize(self):
        return self.M

    

    def dump(self):
        print(self.M)

    def __iadd__(self, other):
        assert self.b == other.b
        self.merge(other)
        return self
    
    def __eq__(self, other):
        assert self.b == other.b
        return self.M == other.M

    def __str__(self):
        return str(self.count)

    def __repr__(self):
        return str(self.count)

if __name__ == '__main__':
    hll = HyperLogLog(16)
    for i in range(1000):
        hll.add(random.randint(0, 1000))
    
    print(hll.count())

    hll2 = HyperLogLog(16)
    for i in range(100):
        hll2.add(random.randint(0, 1000))
    
    print(hll2.count())

    hll += hll2
    print(hll.count())