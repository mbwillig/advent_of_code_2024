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


def part_a():
    options, lines = read_input_text().split("\n\n")
    options = options.split(", ")
    lines = lines.split("\n")

    @cache
    def is_doable(lineix,pos = 0):
        line = lines[lineix][pos:]
        if not line:
            return True
        for option in options:
            if line.startswith(option):
                ans =  is_doable(lineix,pos+len(option))
                if ans:
                    return ans
        return False

    print(sum((is_doable(i) for i in range(len(lines)))))

part_a()
def part_b():
    options, lines = read_input_text().split("\n\n")
    options = options.split(", ")
    lines = lines.split("\n")

    @cache
    def give_options(lineix, pos=0):
        line = lines[lineix][pos:]
        if not line:
            return 1
        total = 0
        for option in options:
            if line.startswith(option):
                total += give_options(lineix, pos + len(option))

        return total

    print(sum((give_options(i) for i in range(len(lines)))))

part_b()