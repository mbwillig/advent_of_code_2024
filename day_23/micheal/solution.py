import os
from collections import defaultdict
from functools import reduce, cache

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    graph = defaultdict(set)
    for line in read_input_lines():
        a,b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

    ans = set()
    for node in [x for x in graph.keys() if x[0] == 't']:
        for nodeb in graph[node]:
            for nodec in graph[nodeb]:
                if node in graph[nodec]:
                    ans.add(tuple(sorted([node,nodeb,nodec])))

    print(len(ans))

part_a()

def part_b():
    graph = defaultdict(set)
    for line in read_input_lines():
        a, b = line.split("-")
        graph[a].add(b)
        graph[b].add(a)

    all_nodes = set(graph.keys())

    @cache #function calls explode because each group of n can be made in n! orders
    def growgroup(grp):
        candidates = reduce(lambda x, y: x & graph[y],
                            grp,
                            all_nodes) # candidate nodes have a connection to all grp members
        if not candidates: #group is at max size
            return grp

        return max((growgroup(tuple(sorted(list(grp) + [candidate])))
                    for candidate in candidates),
                   key = len) #we take the best path

    print(",".join(sorted(list(growgroup(tuple())))))

part_b()