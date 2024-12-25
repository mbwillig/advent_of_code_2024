import os
import sys
import pandas as pd
import numpy as np
import math

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()

class OpcodeInterpreter():

    def __init__(self,a,b,c, instructions, part_b = False):
        self.a, self.b, self.c = a,b,c
        self.ix = 0
        self.result = []
        self.instructions = instructions
        self.part_b = part_b

    def combo(self, x):
        if x < 4:
            return x
        return {4: self.a, 5: self.b, 6: self.c}[x]

    def resolveOpcode(self, opcode, operant):

        match opcode:
            case 0:
                self.a = math.floor(self.a/(2**self.combo(operant)))
            case 1:
                self.b = self.b ^ operant
            case 2:
                self.b = self.combo(operant) % 8
            case 3:
                if self.a:
                    self.ix = operant - 2
            case 4:
                self.b = self.b ^ self.c
            case 5:
                self.result.append(self.combo(operant) %8)
                if self.part_b:
                    n = len(self.result) - 1
                    assert n < len(self.instructions)
                    assert self.result[n] == self.instructions[n]
            case 6:
                self.b = math.floor(self.a / (2 ** self.combo(operant)))
            case 7:
                self.c = math.floor(self.a / (2 ** self.combo(operant)))

    def step(self):
        opcode, operant =self.instructions[self.ix:self.ix+2]
        self.resolveOpcode(opcode, operant)
        self.ix += 2

    def run(self):
        while self.ix < len(self.instructions):
            self.step()
        if self.part_b:
            assert self.result == self.instructions


def part_a():
    oci = OpcodeInterpreter(44374556,0,0, [2,4,1,5,7,5,1,6,0,3,4,1,5,5,3,0])
    oci.run() # we append
    print(",".join([str(x) for x in oci.result]))

part_a()
def part_b():

    instructions = [2,4, # b = a%8
                    1,5, # b %= 5
                    7,5, # c = a / (2**b)
                    1,6, # b %= 6
                    0,3, # a//=8
                    4,1, # b ^= c
                    5,5, # yield b%8
                    3,0] # loop

    def solvenext(ix=0, digit = 0 ):
        if digit == len(instructions):
            return ix/8

        best = float("inf")
        for ix in range(ix, ix+8):
            oci = OpcodeInterpreter(ix, 0, 0, instructions)
            oci.run()  # we append
            assert oci.result[::-1][:digit] == instructions[::-1][:digit], (oci.result[::-1][:digit], instructions[::-1][:digit])
            if oci.result[-(digit+1)] == instructions[-(digit+1)]:
                ans = solvenext(ix * 8, digit+1)
                best = min(ans, best)

        return best

    print(solvenext())


part_b()

