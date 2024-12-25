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

def get_dists_from_point(loc,field):
    dists = {loc:0}
    current = {loc,}
    for i in range(1,999999):
        if not current:
            return dists
        adj = {loc+delta for loc in current for delta in [1,-1,1j,-1j]
               if (loc+delta in field)
               and ((loc+delta) not in dists)}
        current = adj
        for loc in current:
            dists[loc] = i

def part_a():
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)
             if symb != "#"}

    start = [k for k,v in field.items() if v == "S"][0]
    end = [k for k,v in field.items() if v == "E"][0]

    dists_from_start = get_dists_from_point(start, field)
    dists_from_end = get_dists_from_point(end,field)
    total_dist_no_cheat = dists_from_start[end]

    ans = 0
    for startpos in field:
        for step in [-2,2,-2j,2j]:
            cheatdist = dists_from_start[startpos] + dists_from_end.get(startpos+step,9999999999) + 2
            if (total_dist_no_cheat - cheatdist) > 99:
                ans += 1

    print(ans)


part_a()

def part_b():
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)
             if symb != "#"}

    start = [k for k, v in field.items() if v == "S"][0]
    end = [k for k, v in field.items() if v == "E"][0]

    dists_from_start = get_dists_from_point(start, field)
    dists_from_end = get_dists_from_point(end, field)
    total_dist_no_cheat = dists_from_start[end]

    ans = 0
    for startpos,startdist in dists_from_start.items():
        for endpos,enddist in dists_from_end.items():
            delta = startpos - endpos
            cheatdist = abs(delta.real) + abs(delta.imag)
            saved_time = total_dist_no_cheat - (startdist + enddist + cheatdist)
            if (cheatdist <21) & (saved_time >=100):
                ans+=1

    print(ans)

part_b()