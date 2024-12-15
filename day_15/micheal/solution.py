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
    field, instructions = read_input_text().split("\n\n")
    field = {i + 1j * j: symb
             for i, row in enumerate(field.split("\n"))
             for j, symb in enumerate(row)
             if symb != "."}

    def trymove(loc, dir):
        symb = field.get(loc)
        if symb is None:
            return True
        elif symb == "#":
            return False
        elif symb == "O":
            canmove = trymove(loc+dir, dir)
            if canmove:
                del field[loc]
                field[loc+dir] = symb
            return canmove

    symb2instruct = {
       ">" : 1j,
        "^" : -1,
        "<" : -1j,
        "v" : 1
    }
    loc = [k for k,v in field.items() if v == "@"][0]
    for instruction in instructions:
        if dir := symb2instruct.get(instruction):
            if trymove(loc+dir, dir):
                del field[loc]
                loc+=dir
                field[loc] = "@"

    score = sum([x.real * 100 + x.imag for x, symb in field.items() if symb == "O"])
    print(score)



part_a()
def part_b():
    field, instructions = read_input_text().split("\n\n")
    field = field.replace("#", "##").replace(".", "..").replace("@", "@.").replace("O", "[]")

    field = {i + 1j * j: symb
             for i, row in enumerate(field.split("\n"))
             for j, symb in enumerate(row)
             if symb != "."}

    symb2instruct = {
       ">" : 1j,
        "^" : -1,
        "<" : -1j,
        "v" : 1
    }
    loc = [k for k,v in field.items() if v == "@"][0]

    def get_movable_MoveSet(loc, dir):
        print(loc, field[loc])
        frontline = {loc,}
        behind = set()
        while frontline:
            next_frontline = set()
            frontline = {x for x in frontline if x in field}
            for loc in frontline:
                if field.get(loc+dir) == "#":
                    print("obstruction", loc+dir)
                    return set()
                elif dir.imag and field.get(loc+dir) in list("[]"): #if we move left right we do nor care about the wide boxes
                    next_frontline.add(loc+dir)
                elif field.get(loc+dir) == "[" :
                    next_frontline |= {loc+dir, loc+dir+1j}
                elif field.get(loc+dir) == "]":
                    next_frontline |= {loc + dir, loc + dir - 1j}
            behind |= frontline
            frontline = next_frontline
        return behind

    symb2instruct = {
       ">" : 1j,
        "^" : -1,
        "<" : -1j,
        "v" : 1
    }
    selfloc = [k for k,v in field.items() if v == "@"][0]
    for instruction in instructions:
        if dir := symb2instruct.get(instruction):
            if movable := get_movable_MoveSet(selfloc, dir):
                selfloc += dir
                movelist = list(movable)
                movesymbs = [field[x] for x in movelist]
                for loc in movelist:
                    del field[loc]
                for loc,symb in zip(movelist,movesymbs):
                    field[loc+dir] = symb

    score = sum([x.real * 100 + x.imag for x, symb in field.items() if symb == "["])
    print(score)

def printfield(field):
    for i in range(50):
        print("".join((field.get(i+j*1j, ".")for j in range(100))))
part_b()


