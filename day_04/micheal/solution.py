import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_lines():
    with open('input.txt', 'r') as fh:
        return [x.strip() for x in fh.readlines()]

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    field = {i+1j * j: symb
             for i,row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}
    dirs = {a+1j*b for a in [-1, 0, 1] for b in [-1, 0, 1]} - {0}

    ans = 0
    for startpos in field:
        for dir in dirs:
            ans += "".join([field.get(startpos + dir * x, "") for x in range(4)]) == "XMAS"

    print(ans)



def part_b():
    field = {i + 1j * j: symb
             for i, row in enumerate(read_input_lines())
             for j, symb in enumerate(row)}

    ans = 0
    for startpos in [k for k,v in field.items() if v == "A"]:
        for dir in {(-1 -1j), (1 - 1j) }:
            if {"M", "S"} ^ {field.get(startpos + dir * sign) for sign in [1, -1]}:
                break
        else:
            ans += 1

    print(ans)

part_a()
part_b()