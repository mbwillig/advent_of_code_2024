import os
from functools import cache

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

def solve(steps):
    @cache
    def getstones(stone, blinks2go):
        if blinks2go == 0:
            return 1
        elif stone == 0:
            return getstones(1, blinks2go - 1)
        elif not (len(str(stone)) % 2):
            n = len(str(stone))
            return (getstones(int(str(stone)[:n // 2]), blinks2go - 1)
                    +
                    getstones(int(str(stone)[n // 2:]), blinks2go - 1))
        else:
            return getstones(stone * 2024, blinks2go - 1)

    print(sum([getstones(int(stone), 75) for stone in read_input_text().split()]))

def part_a():
    solve(25)

def part_b():
    solve(75)



part_b()