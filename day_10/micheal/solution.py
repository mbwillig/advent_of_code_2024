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
    field = {i + 1j * j: int(symb)
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    def getadj(loc):
        for dir in [-1,1,1j,-1j]:
            yield loc+dir

    current_places = {(k,k) for k,v in field.items() if v == 0}
    for height in range(1,10):
        current_places = {(adj, source)
                          for current, source in current_places
                          for adj in getadj(current)
                          if field.get(adj) == height}
    print(len(current_places))

part_a()

def part_b():
    field = {i + 1j * j: int(symb)
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    def getadj(loc):
        for dir in [-1, 1, 1j, -1j]:
            yield loc + dir

    current_places = {k :1 for k, v in field.items() if v == 0}
    for height in range(1, 10):
        next_places = {}
        for loc,ways in current_places.items():
            for adj in (adj for adj in getadj(loc) if field.get(adj) == height):
                next_places[adj] = next_places.get(adj, 0) + ways
        current_places = next_places
    print(sum(current_places.values()))

part_b()