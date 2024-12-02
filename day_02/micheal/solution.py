import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
import operator
from copy import deepcopy
from collections import Counter, ChainMap, defaultdict, deque
from itertools import cycle
from functools import reduce

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    lines = [[int(y) for y in x.split()]for x in read_input_lines() ]

    oneSign = lambda x: len({np.sign(a-b) for a,b in zip(x[:-1], x[1:])}) == 1
    smallSteps = lambda x: all((4 > abs(a-b) > 0 for a,b in zip(x[:-1], x[1:])))

    print(sum((oneSign(x) and smallSteps(x) for x in lines)))

def part_b():

    def get_variants(levels):
        yield levels
        for ix in range(len(levels)):
            yield [v for i,v in enumerate(levels) if i != ix]

    lines = [[int(y) for y in x.split()]for x in read_input_lines() ]

    oneSign = lambda x: len({np.sign(a-b) for a,b in zip(x[:-1], x[1:])}) == 1
    smallSteps = lambda x: all((4 > abs(a-b) > 0 for a,b in zip(x[:-1], x[1:])))
    isOk = lambda x: oneSign(x) and smallSteps(x)

    print(sum((any((isOk(var) for var in get_variants(x))) for x in lines)))

part_a()
part_b()