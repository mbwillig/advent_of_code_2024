import os
import heapq

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)
from random import random

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)
             if symb != "#"}

    rot1 = lambda x: x.real * 1j + x.imag
    rot2 = lambda x: (- x.real) * 1j + (-x.imag)
    start = [k for k,v in field.items() if v == "S"][0]
    end = [k for k, v in field.items() if v == "E"][0]

    state2score = {}
    action_stack =  [( 0, random(),(start, 1j))]
    heapq.heapify(action_stack)

    while True:
        next_dist, _, next_loc = heapq.heappop(action_stack)
        if next_loc[0] == end:
            print(next_dist)
            return
        if next_loc not in state2score:
            state2score[next_loc] = next_dist
            if (next_pos := next_loc[0] + next_loc[1]) in field:
                heapq.heappush(action_stack,(next_dist + 1,random(), (next_pos, next_loc[1])))
            for newdir in [rot1(next_loc[1]),rot2(next_loc[1])]:
                heapq.heappush(action_stack,(next_dist + 1000, random(), (next_loc[0], newdir)))

part_a()

def part_b():
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)
             if symb != "#"}

    rot1 = lambda x: x.real * 1j + x.imag
    rot2 = lambda x: (- x.real) * 1j + (-x.imag)
    start = [k for k,v in field.items() if v == "S"][0]
    end = [k for k, v in field.items() if v == "E"][0]

    state2score_path = {}
    action_stack =  [( 0, random(),(start, 1j), None)]
    heapq.heapify(action_stack)

    while action_stack:
        next_dist, _, next_loc, source = heapq.heappop(action_stack)

        if next_loc in state2score_path and state2score_path[next_loc][0] == next_dist:#multiple routes
            state2score_path[next_loc][1].add(source)
        elif next_loc not in state2score_path:
            state2score_path[next_loc] = (next_dist, {source,})
            if (next_pos := next_loc[0] + next_loc[1]) in field:
                heapq.heappush(action_stack,(next_dist + 1,
                                                   random(),
                                                   (next_pos, next_loc[1]),
                                                   next_loc))
            for newdir in [rot1(next_loc[1]),rot2(next_loc[1])]:
                heapq.heappush(action_stack,(next_dist + 1000,
                                                   random(),
                                                   (next_loc[0], newdir),
                                                   next_loc))
    best_state = sorted([(end,dir) for dir in [1j, -1j, 1, -1]], key = lambda x: state2score_path[x][0])[0]
    print(best_state,state2score_path[best_state])
    visited = set()
    visiting = {best_state,}
    while visiting:
        visited |= visiting
        visiting = {state for vis in visiting for state in state2score_path[vis][1] if state is not None}

    print(len({x[0] for x in visited}))

part_b()