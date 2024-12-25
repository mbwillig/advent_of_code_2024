import os
import numpy as np
from itertools import batched
from collections import defaultdict

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

def mix(a,b):
    return a ^ b

def prune(x):
    return x % 16777216

def increment_secret_number(x, times = 1):
    for _ in range(times):
        x = prune(mix( x * 64, x))
        x = prune(mix(x // 32, x))
        x = prune(mix(x * 2048, x))
    return x

def part_a():
    ans = 0
    for inp in read_input_lines():
        ans += increment_secret_number(int(inp), 2000)

    print(ans)


def part_b():
    secrets = [[int(x) for x in read_input_lines()]]
    for step in range(2000):
        secrets.append([increment_secret_number(x) for x in secrets[-1]])

    prices = np.array(secrets) % 10
    n_timestamps, n_traders = prices.shape
    changes = prices[1:] - prices[:-1]

    def countPatScores():
        scores = defaultdict(int)
        for traderix in range(n_traders):
            visited = set()
            for price, changeset in zip(prices[4:,traderix], # price on index 4 is the first obtainable
                                         (tuple(changes[i:i+4, traderix]) for i in range(n_timestamps - 4))
                                         ):
                if changeset in visited:
                    continue
                scores[changeset] += price
                visited.add(changeset)
        return scores


    print(max(countPatScores().values()))


part_b()
