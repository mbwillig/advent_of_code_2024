import os

CURRENT_DIRECTORY = os.path.dirname(__file__)
os.chdir(CURRENT_DIRECTORY)

def read_input_text():
    with open('input.txt', 'r') as fh:
        return fh.read().strip()


def part_a():
    arr = [[i//2, int(v), None] if not i%2 else [None, int(v), []] for i,v in enumerate(read_input_text())]

    i = 1
    ii = len(arr) -1
    while i<ii:
        tofillSink = arr[i][1]
        toFillSource = arr[ii][1]
        willSync = min(tofillSink,toFillSource)
        arr[i][2].append((arr[ii][0], willSync))

        arr[i][1] -= willSync
        arr[ii][1] -= willSync

        if not arr[ii][1]:
            ii-=2
        if not arr[i][1]:
            i+=2

    score = 0
    ix = 0
    for item in arr:
        if item[2] is None:
            item = [item]
        else:
            item = item[2]

        for subitem in item:
            next_ix = ix + subitem[1]
            avrgix = (ix + (next_ix-1))/2
            score += subitem[0] * subitem[1] * avrgix
            ix = next_ix

    print(score)



part_a()



def part_b():
    arr = [[i // 2, int(v), None] if not i % 2 else [None, int(v), []] for i, v in enumerate(read_input_text())]
    def findSpace(n,ix):
        for i in range(1,ix,2):
            if arr[i][1] >= n:
                return i

    def printScore(arr):
        ans = 0
        ix = 0
        for x in arr:
            if x[0] is not None:
                ans+=x[0] * ((ix + (ix + x[1]) -1)/2) * x[1]
                ix += x[1]
            else:
                for subarr in x[2]:
                    ans +=  subarr[0] *(((ix + (ix +  subarr[1]) -1)) / 2)  * subarr[1]
                    ix +=  subarr[1]
                ix += x[1]
        print(ans)



    for i,item in list(enumerate(arr))[::-2]:
        to_ix = findSpace(item[1], i)
        if to_ix:
            arr[to_ix][2].append([item[0], item[1]])
            arr[to_ix][1] -= item[1]
            arr[i][0] = 0

    printScore(arr)


part_b()