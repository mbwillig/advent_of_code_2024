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
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    pos  = next((k for k, v in field.items() if v == '^'))
    dir2nextdir = {-1: 1j, 1j: 1, 1: -1j, -1j: -1}
    dir = -1
    visited = {pos}

    while (nextPos := (pos + dir)) in field:
        if field[nextPos] == "#":
            dir = dir2nextdir[dir]
        else:
            pos = nextPos
            visited.add(nextPos)

    print(len(visited))


def part_b():
    field = {i + 1j * j : symb
             for i,row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    pos = start = next((k for k, v in field.items() if v == '^'))
    dir2nextdir = {-1: 1j, 1j: 1, 1: -1j, -1j: -1}
    startdir = dir = -1


    def willLoop(pos, field):
        field = field.copy()
        field[pos] = "#"
        pos = start
        dir = startdir
        visited_with_dirs = defaultdict(set, {pos: {dir}})

        while (nextPos := (pos + dir)) in field:

            if field[nextPos] == "#":
                dir = dir2nextdir[dir]
            else:
                # we simulate what would happen if we did place an obstacle here.
                pos = nextPos

            if dir in visited_with_dirs[pos]:
                return True
            visited_with_dirs[pos].add(dir)

        return False


    solutions_tried = {start}
    solutions_found = 0

    while (nextPos := (pos + dir)) in field:
        if field[nextPos] == "#":
            dir = dir2nextdir[dir]
        else:
            # we simulate what would happen if we did place an obstacle here.
            if nextPos not in solutions_tried:
                solutions_tried.add(nextPos)
                solutions_found += willLoop(nextPos, field)

            pos = nextPos

    print(solutions_found)

part_b()