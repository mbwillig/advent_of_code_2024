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
    cols = zip(*[[int(y) for y in x.split()] for x in read_input_lines()])
    cols = [sorted(x) for x in cols]
    print(sum([abs(a-b) for a,b in zip(*cols)]))

def part_b():
    left,right = zip(*[[int(y) for y in x.split()] for x in read_input_lines()])
    counts_right = Counter(right)
    print(sum([x * counts_right.get(x, 0) for x in left]))

part_a()
part_b()