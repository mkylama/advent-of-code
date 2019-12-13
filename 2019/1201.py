import re

with open('input/12.txt', 'r') as file:
    moons = file.read().strip().split('\n')

for i in range(len(moons)):
    moons[i] = [list(map(int, re.findall(r'-?\d+', moons[i]))), [0, 0, 0]]

from pprint import pprint as pp
import copy

pos = 0
vel = 1

moons_orig = copy.deepcopy(moons)

def is_zero(d):
    for a in range(len(moons)):
        if moons[a][pos][d] != moons_orig[a][pos][d] or moons[a][vel][d] != moons_orig[a][vel][d]:
            return False
    return True

def lcm(a, b):
    c, d = a, b
    while c:
        c, d = d % c, c
    return a // d * b

loop = 0

patterns = [None, None, None]

while loop < 1000 or patterns[0] is None or patterns[1] is None or patterns[2] is None:
    loop += 1
    # update velocity
    for a in range(len(moons) - 1):
        for b in range(a + 1, len(moons)):
            for d in range(3):
                if moons[a][pos][d] > moons[b][pos][d]:
                    moons[a][vel][d] -= 1
                    moons[b][vel][d] += 1
                elif moons[a][pos][d] < moons[b][pos][d]:
                    moons[a][vel][d] += 1
                    moons[b][vel][d] -= 1
    # update pos
    for a in range(len(moons)):
        for d in range(3):
            moons[a][pos][d] += moons[a][vel][d]

    if loop == 1000:
        total = 0

        for a in range(len(moons)):
            total += (abs(moons[a][pos][0]) + abs(moons[a][pos][1]) + abs(moons[a][pos][2])) * (abs(moons[a][vel][0]) + abs(moons[a][vel][1]) + abs(moons[a][vel][2]))

        print('1201: {}'.format(total))

    for p in range(3):
        if patterns[p] is None:
            if is_zero(p):
                patterns[p] = loop 

print('1202: {}'.format(lcm(patterns[0], lcm(patterns[1], patterns[2]))))
