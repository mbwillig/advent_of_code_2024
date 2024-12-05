import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    constraints, updates =[[x for x in y.split("\n")] for y in read_input_text().split("\n\n")]
    constraints = [x.split("|") for x in constraints]
    updates = [x.split(",") for x in updates]

    def lineOK(update):
        for c_a,c_b in constraints:
            try:
                ix_a, ix_b = update.index(c_a),update.index(c_b)
                if ix_a>ix_b:
                    return False
            except ValueError:
                pass
        return True

    f_middle = lambda x: x[len(x)//2]
    print(sum([int(f_middle(x)) for x in updates if lineOK(x)]))

def part_b():
    constraints, updates = [[x for x in y.split("\n")] for y in read_input_text().split("\n\n")]
    constraints = [x.split("|") for x in constraints]
    updates = [x.split(",") for x in updates]

    def lineOK(update):
        for c_a, c_b in constraints:
            try:
                ix_a, ix_b = update.index(c_a), update.index(c_b)
                if ix_a > ix_b:
                    return False
            except ValueError:
                pass
        return True

    def reorder(update):
        new_update = []
        to_place = set(update)
        while to_place:
            blocked_by_rules = {x[1] for x in constraints if x[0] in to_place}
            next_item = (to_place - blocked_by_rules).pop()
            new_update.append(next_item)
            to_place -= {next_item}
        return new_update

    f_middle = lambda x: x[len(x) // 2]
    print(sum([int(f_middle(reorder(x))) for x in updates if not lineOK(x)]))

part_b()