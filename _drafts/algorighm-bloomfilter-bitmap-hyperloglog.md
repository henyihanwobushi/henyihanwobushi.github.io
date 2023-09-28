---
layout: post
title: "[algorighm] Bloomfilter, Bitmap, Hyperloglog"
---

## Bitmap

Bitmap is a data structure that uses a bit to represent the existence of an element in a set. It is usually used to determine whether an element is in a set. The bitmap is usually implemented by an array of bits, and the size of the array is determined by the number of elements in the set. For example, if the set is {1, 3, 5, 7, 9}, then the bitmap is an array of 10 bits. The first bit represents whether 0 is in the set, the second bit represents whether 1 is in the set, and so on.

### Bitmap in python

```python

class Bitmap(object):
    def __init__(self, max):
        self.size = int((max + 31 - 1) / 31)
        self.array = [0 for i in range(self.size)]

    def set(self, num):
        if num < 0:
            return
        array_index = int(num / 31)
        bit_index = int(num % 31)
        ele = 1 << bit_index
        self.array[array_index] |= ele

    def clean(self, num):
        if num < 0:
            return
        array_index = int(num / 31)
        bit_index = int(num % 31)
        ele = 1 << bit_index
        self.array[array_index] &= ~ele

    def test(self, num):
        if num < 0:
            return False
        array_index = int(num / 31)
        bit_index = int(num % 31)
        ele = 1 << bit_index
        if self.array[array_index] & ele != 0:
            return True
        return False

```