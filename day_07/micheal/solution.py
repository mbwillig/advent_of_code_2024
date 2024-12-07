import os
import sys
import pandas as pd
import numpy as np
import math
import datetime
from operator import __mul__, __add__
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


def solve_part(ops = [__mul__, __add__]):

    def solve(goal,args, ix, total_so_far):
        if (ix == len(args)):
            return total_so_far == goal
        for op in ops:
            next_total = op(total_so_far,args[ix])
            if next_total <= goal:
                ans = solve(goal,args,ix +1, next_total)
                if ans:
                    return True
        return False

    ans = 0
    for line in read_input_lines():
        goal, args = line.split(":")
        goal = int(goal)
        args = [int(x) for x in args.strip().split()]
        if solve(goal,args,1,args[0]):
            ans+=goal

    print(ans)

solve_part()
solve_part(ops = [__mul__, __add__, lambda x, y: int(str(x) + str(y))])
