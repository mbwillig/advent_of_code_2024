import os
import re
from collections import defaultdict
import numpy as np
from functools import reduce
from operator import __mul__
CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    w = 101
    h = 103
    quadrants = defaultdict(int)
    steps = 100
    for line in read_input_lines():
        x,y,dx,dy = [int(d) for d in re.findall(r"-?\d+",line)]
        x += dx * steps
        x %= w
        y += dy * steps
        y %= h
        if (x == (w//2)) or (y == (h//2)):
            continue
        quadrants[(np.sign(x-(w//2)),np.sign(y-(h//2)))] += 1
    print(quadrants)
    print(reduce(__mul__, quadrants.values())) #215770422 too low, #448760088 too high

part_a()


def part_b():

    def display(points):
        points = {(x,y) for x,y,_,_ in points}
        for line in range(h):
            print("".join([" " if (line,col) not in points else "#" for col in range(w)]))

    def getOverlap(points):
        return len(points)- len({tuple(p[:2]) for p in points})

    w = 101
    h = 103
    points = [[int(d) for d in re.findall(r"-?\d+", line)] for line in read_input_lines()]
    minscore = len(points)
    for step  in range(10**6):
        for point in points:
            point[0] += point[2]
            point[0] %= w
            point[1] += point[3]
            point[1] %= h
        score = getOverlap(points)
        if not getOverlap(points):
            display(points)
            print(step+1)
        minscore = min(score, minscore)
    print(minscore)

part_b()