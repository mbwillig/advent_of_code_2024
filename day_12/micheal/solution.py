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

def makeGroups(field):
    groups = []
    ungrouped = set(field.keys())
    while ungrouped:
        start = ungrouped.pop()
        new = {start}
        symb = field[start]
        grp = set()
        while new:
            nextnew = {dir +loc
                       for loc in new
                       for dir in [-1,1,1j,-1j]
                       if field.get(loc+dir, "") == symb}
            grp |=new
            nextnew -= grp #no repeats
            new = nextnew

        ungrouped -= grp
        groups.append(grp)
    return groups

def part_a():



    def scoregrp_per(grp):
        per = sum([loc + dir not in grp
                   for loc in grp
                   for dir in [1,-1,1j,-1j]])
        return per * len(grp)


    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    print(sum((scoregrp_per(x) for x in makeGroups(field))))

part_a()

def part_b():

    def scoregrp_sides(grp):
        """number of sides should equal number of coreners
           one location can have multiple or no coreners.
           Each outer corner requires two non occupied neighbours at 90 degree offset
           Each innter corner requires diag neighbours sharing only one direct neighbour"""

        def getCornersForLoc(loc, grp):
            clockwise = {1: -1j,
                         -1j: -1,
                         -1: 1j,
                         1j: 1}

            outer_corners = sum([(not (grp & {loc + dir1, loc + dir2}))
                        for dir1, dir2 in clockwise.items()])

            inner_corners = sum((loc+diag in grp) and len(grp & {loc + adj for adj in [diag.real, diag.imag * 1j]}) == 1
                              for diag in (1+1j, 1+-1j,-1 + 1j, -1-1j)) * 0.5 #each corner seen from two diags
            return inner_corners + outer_corners


        sides = sum((getCornersForLoc(loc, grp) for loc in grp))
        return sides * len(grp)

    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    print(sum((scoregrp_sides(x) for x in makeGroups(field))))

part_b() #440553 too low #821070 too high