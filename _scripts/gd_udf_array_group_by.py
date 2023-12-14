# encoding: utf-8
from odps.udf import annotate
import math
from collections import defaultdict
from functools import reduce


@annotate("array<array<string>>->map<string,array<string>>")
class gd_udf_array_group_by(object):
    def evaluate(self, a1):
        ''' group by first element of element array'''
        if a1 is None:
            return None

        result = {}

        for e in a1:
            if e is None:
                continue
            result.setdefault(e[0], [])
            result[e[0]].append(e)
        return result


if __name__ == '__main__':
    print(gd_udf_array_group_by().evaluate([['a', 'b'], ['a', 'c'], ['a', 'd'], ['b', 'c'], ['b', 'd'], ['c', 'd']]))
