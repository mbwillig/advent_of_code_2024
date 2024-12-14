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

def getSlope(x):
    return x.real/x.imag

def bin_search_solve(a, b, sol):
    """binary search throug press A amounts (for which we calculate press B amounts to attain X value)
    to get the proportions for which the slope is OK. THen check whether the stepsizes work out"""
    assert (a.real / a.imag) != (b.real / b.imag)

    lowslope, highslope = list(sorted([("A", a), ("B", b)], key=lambda x: getSlope(x[1])))

    solslope = getSlope(sol)
    n_low_min, n_low_max = 0, sol.real // lowslope[1].real
    while n_low_min <= n_low_max:
        n_low = (n_low_min + n_low_max) // 2
        n_high = (sol.real - (lowslope[1].real * n_low)) / (highslope[1].real)
        slope = getSlope(n_low * lowslope[1] + n_high * highslope[1])
        if slope > solslope:
            n_low_min = n_low + 1
        elif slope < solslope:
            n_low_max = n_low - 1
        elif slope == solslope:
            if n_high.is_integer():
                return (n_low * {"A": 3, "B": 1}[lowslope[0]] +
                        n_high * {"A": 3, "B": 1}[highslope[0]])
            else:
                return 0
    return 0

def part_a():

    def parsechunk(txtchunk):
        nums = (  [re.findall(r"\d+", line)
                   for line in txtchunk.split("\n")])
        a,b,sol = [int(x) + int(y) * 1j
                   for x,y in nums]

        return a,b,sol

    ans = 0
    for chunk in read_input_text().split("\n\n"):
        a,b,sol = parsechunk(chunk)
        ans += bin_search_solve(a,b,sol)
    print(ans)

def part_b():

    def parsechunk(txtchunk):
        nums = (  [re.findall(r"\d+", line)
                   for line in txtchunk.split("\n")])
        a,b,sol = [int(x) + int(y) * 1j
                   for x,y in nums]
        sol += 10000000000000 + 10000000000000j
        return a,b,sol


    ans = 0
    for chunk in read_input_text().split("\n\n"):
        a,b,sol = parsechunk(chunk)
        ans += bin_search_solve(a,b,sol)
    print(ans)

part_b()