import os
import numpy as np
from itertools import product

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    locks = []
    keys = []

    for obj in read_input_text().split("\n\n"):
        matrix = np.array([list(x) for x in obj.split("\n")])
        heights = (matrix=="#").sum(axis=0)
        if obj[0] == ".":
            keys.append(heights)
        else:
            locks.append(heights)

    ans = 0
    for key, lock in product(keys,locks):
        ans += ((key+lock) < 8).all()

    print(ans)


part_a()

def part_b():
    pass