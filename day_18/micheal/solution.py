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


def part_a(time = 1024):
    size = 71
    field = {i + (j * 1j) for i in range(size) for j in range(size)}
    for line in (read_input_lines()[:time]):
        j,i = line.split(",")
        field -= {int(i) + 1j * int(j)}

    visited = {0,}
    current = {0,}
    for step in range(1,999999999):
        adj = ({l + d for l in current for d in [1,-1,1j,-1j]} & field) - visited
        visited |= adj
        current = adj
        if ((size-1)+(size-1)*1j) in current:
            return step
        assert current
print(part_a())

def part_b():
    search_space_low = 0
    search_space_high = len(read_input_lines())
    while search_space_high  > search_space_low:
        middle = (search_space_high + search_space_low)//2
        try:
            part_a(middle)
        except AssertionError:
            search_space_high = middle
            continue
        search_space_low = middle+1
    print(read_input_lines()[search_space_high-1])

part_b()


