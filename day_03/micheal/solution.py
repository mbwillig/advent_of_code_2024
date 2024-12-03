import os
import re

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    txt = read_input_text()
    pat = r"mul\((\d{1,3}),(\d{1,3})\)"
    print(sum([int(a) * int(b) for a,b in re.findall(pat,txt)]))

def part_b():
    txt = read_input_text()
    pats = [r"mul\((\d{1,3}),(\d{1,3})\)",
            r"(do\(\))",
            r"(don't\(\))"]
    results = sorted([res for pat in pats for res in re.finditer(pat,txt)], key = lambda x: x.start())

    ans = 0
    multiplier = 1
    for result in results:
        match result.groups():
            case (a,b):
                ans += int(a) * int(b) * multiplier
            case (r'do()',):
                multiplier = 1
            case (r"don't()",):
                multiplier = 0

    print(ans)
