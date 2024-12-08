import os

from itertools import permutations
from collections import defaultdict

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

    symb2loc = defaultdict(list)
    for k,v in field.items(): symb2loc[v].append(k)
    del symb2loc["."]

    focci = {i2 + (i2-i1) for locs in symb2loc.values() for i1,i2 in permutations(locs, 2)}

    print(sum((x in field for x in focci))) #2013 too high

def part_b():
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    symb2loc = defaultdict(list)
    for k, v in field.items(): symb2loc[v].append(k)
    del symb2loc["."]

    def get_focci(i1,i2):
        ans = set()
        delta = i2-i1
        while i2 in field:
            ans.add(i2)
            i2 += delta
        return ans

    focci = {f for locs in symb2loc.values()
             for i1,i2 in permutations(locs, 2)
             for f in get_focci(i1,i2)}
    print(len(focci))




part_b()