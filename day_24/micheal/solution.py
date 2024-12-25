import os
from copy import copy
from random import randrange
CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def run(connections, sig_outputs):
    connections = copy(connections)
    sig_outputs = copy(sig_outputs)
    op2func = {
        "XOR" : lambda x,y: (x+y) == 1,
        "AND": lambda x, y: x and y,
        "OR": lambda x, y: x or y
    }
    while connections:
        solvable = [(k, (a,b,op)) for (k, (a,b,op)) in connections.items() if a in sig_outputs and b in sig_outputs]
        if not solvable:
            return [2] * 46
        for (k, (a,b,op)) in solvable:
            del connections[k]
            sig_outputs[k] = op2func[op](sig_outputs[a], sig_outputs[b])

    bits = ([int(sig_outputs[x]) for x in
           sorted([x for x in sig_outputs.keys() if "z" in x])])

    return bits

def part_a():
    values, connections = read_input_text().split("\n\n")

    sig_outputs = {k:int(v) for k,v in [x.split(": ") for x in values.split("\n")]}
    connections = {k: (a,b,op) for a, op, b, _, k in [x.split() for x in connections.split("\n")] }



    print(sum(x * (2**i) for i,x in enumerate(run(connections, sig_outputs)))) #20145091047033 too low

def part_b():
    """
    each z{d} should be structured like xor(xor(x{d}, y{d}), isoverflow

    concrete: z is always made by XOR (with exception of z45). THis is not true for
    z06, z11, z35 these should each be swapped with an output that does use xor
    also since z != 0 the xor should not directly refer to an x or y but indirecty refer to x and y of the output z
    3 xors exist that are not connected """




    values, connections = read_input_text().split("\n\n")
    sig_outputs = {k:int(v) for k,v in [x.split(": ") for x in values.split("\n")]}
    connections = {k: (a,b,op) for a, op, b, _, k in [x.split() for x in connections.split("\n")] }

    toBits = lambda  x:  [int(x) for x in format (x ,  'b' )][::-1]

    bits_x = ([int(sig_outputs[x]) for x in sorted([x for x in sig_outputs.keys() if "x" in x])])
    bits_y = ([int(sig_outputs[x]) for x in sorted([x for x in sig_outputs.keys() if "y" in x])])
    int_x = sum(x * (2 ** i) for i, x in enumerate(bits_x))
    int_y = sum(x * (2 ** i) for i, x in enumerate(bits_y))
    int_z = int_x+int_y
    bits_z = toBits(int_z)

    z_no_xor = [k for k, v in connections.items() if "z" in k
                                                  and v[-1] != "XOR"
                                                  and k != 'z45']

    xor_connections_excl_z_excl_ref_xy = [k for k, v in connections.items()
                                          if "z" not in k
                                          and v[-1] == "XOR"
                                          and not (set('xy') & set(v[0][0] + v[1][0]))]

    z_value_for_xor = [
        y[1:] for k in xor_connections_excl_z_excl_ref_xy
              for x in connections[k][:-1]
              for y in connections[x][:-1] if y[0] in "yx"
    ][::2] # all xors refer with one step indirection to the correct digit of z

    for node, z_digit in zip(xor_connections_excl_z_excl_ref_xy,z_value_for_xor):
        connections["z" + z_digit], connections[node] =  connections[node], connections["z" + z_digit]

    def additionalTests(connections):

        def additionaltest(a,b):
            c = toBits(a+b)
            c += [0] * (46 - len(c))
            a = toBits(a)
            a += [0] * (45-len(a))
            b = toBits(b)
            b += [0] * (45-len(b))
            sig_outputs = {}
            for i, bit in enumerate(a):
                sig_outputs["x" + str(i).zfill(2)] = bit
            for i, bit in enumerate(b):
                sig_outputs["y" + str(i).zfill(2)] = bit

            ans = run(connections,sig_outputs)
            assert 2 not in ans
            return ans == c

        for case in range(1000):
            a,b = randrange(0, (2**45) -1),randrange(0, (2**45) -1)
            if not additionaltest(a,b):
                return False
        return True


    # one switch remains
    nodes = list(connections.keys())
    for i, fromnode in enumerate(nodes):
        for tonode in nodes[i+1:]:
            connections2 = copy(connections)
            connections2[fromnode], connections2[tonode] = connections2[tonode], connections2[fromnode]
            ans = run(connections2,sig_outputs)

            if ans == bits_z:
                if additionalTests(connections2):
                    print(",".join(sorted(z_no_xor + [fromnode,tonode] + xor_connections_excl_z_excl_ref_xy)))
                    # have to remove z45 from the string since



part_b()
#fhc,ggt,hqk,mwh,qhj,z06,z11,z35 not the right ans

