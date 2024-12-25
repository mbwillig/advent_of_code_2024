import os
import heapq
from random import random
from collections import defaultdict
from functools import cache

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

"""
Which state matters aftr press?
for robot being moved: loc


"""

class Human:
    def goto_symb_and_press(self,x,y):
        self.key2loc = defaultdict(int)
        return 1

class Robot:

    def __init__(self, submover, keymap):
        self.submover = submover
        self.loc2key = keymap #loc 2 symb
        self.key2loc = {v:k for k,v in keymap.items()} # symbol to location on controller

    def press_sybols_starting_from_A(self,symbols):
        loc = 0
        dist = 0
        for symbol in symbols:
            dist += self.goto_symb_and_press(loc, symbol)
            loc = self.key2loc[symbol]
        return dist


    def goto_symb_and_press(self, startloc, symb):
        gotoloc = self.key2loc[symb]
        return self.get_min_cost_from_loc_a_to_loc_b_and_press(startloc, gotoloc)

    @cache
    def get_min_cost_from_loc_a_to_loc_b_and_press(self,loc_a, loc_b):
        # dijkstra using keymap + cost_per_move

        states = [(0,random(),loc_a,0, False)] #cost, random, location, submover loc, ispressed
        heapq.heapify(states)
        state2score = {}

        while True:
            next_dist, _, next_loc, submov_loc,ispressed = heapq.heappop(states)
            if (next_loc == loc_b) & ispressed:
                return next_dist #return score, we are done
            if (next_loc, submov_loc) not in state2score:
                state2score[ (next_loc, submov_loc)] = next_dist
                if next_loc == loc_b:
                    heapq.heappush(states,
                                   (next_dist +
                                   self.submover.goto_symb_and_press(submov_loc, "A"),
                                   random(),
                                   next_loc,
                                   0,
                                   True)) # we move submover to loc 0 (activate) and push

                else:
                    for dir in [1,-1,-1j, 1j]:
                        if next_loc in self.loc2key:
                            heapq.heappush(states,
                                           (next_dist +
                                           self.submover.goto_symb_and_press(submov_loc, dir),
                                           random(),
                                           next_loc+dir,
                                           self.submover.key2loc[dir],
                                           False))  # we move submover to loc 0 (activate) and

def part_a():
    arrowpad = {0: "A", 1: 1j, -1j: -1, -1j + 1: 1, 1 - 2j: -1j}

    numpad = {-3 - 2j: "7", -3 - 1j: "8", -3: "9",
              -2 - 2j: "4", -2 - 1j: "5", -2: "6",
              -1 - 2j: "1", -1 - 1j: "2", -1: "3",
                                -1j: "0",  0: "A"
              }
    robot0 = Robot(Human(),arrowpad)
    robot1 = Robot(robot0,arrowpad)
    robot2 = Robot(robot1,numpad)

    ans = 0
    for line in read_input_lines():
        ans += int(line[:-1]) * robot2.press_sybols_starting_from_A(line)
    print(ans)

part_a()

def part_b():
    arrowpad = {0: "A", 1: 1j, -1j: -1, -1j + 1: 1, 1 - 2j: -1j}

    numpad = {-3 - 2j: "7", -3 - 1j: "8", -3: "9",
              -2 - 2j: "4", -2 - 1j: "5", -2: "6",
              -1 - 2j: "1", -1 - 1j: "2", -1: "3",
              -1j: "0", 0: "A"
              }

    bot = Human()
    for _ in range(25):
        bot = Robot(bot,arrowpad)
    bot = Robot(bot,numpad)

    ans = 0
    for line in read_input_lines():
        ans += int(line[:-1]) * bot.press_sybols_starting_from_A(line)
    print(ans)

part_b()