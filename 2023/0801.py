import re

with open('input/08.txt') as file:
   _input = [x.strip() for x in file.readlines()]

instructions = _input[0]
nodes = {y[0]: {'L': y[1], 'R': y[2]} for y in [re.findall(r'[\w\d]+', x) for x in _input[2:]]}

step = 1
pos = 'AAA'

while True:
    pos = nodes[pos][instructions[(step - 1) % len(instructions)]]
    if pos == 'ZZZ':
        break
    step += 1

print('0801:', step)

def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def lcm_list(l):
    while len(l) > 1:
        x, y = l.pop(), l.pop() 
        l.append((x * y) // gcd(x, y))
    return l[0]

poss = [x for x in nodes.keys() if x[2] == 'A']
loops = []

for cur in poss:
    step = 1
    pos = cur
    while True:
        pos = nodes[pos][instructions[(step - 1) % len(instructions)]]
        if pos[2] == 'Z':
            loops.append(step)
            break
        step += 1

print(loops)

print('0802:', lcm_list(loops))
