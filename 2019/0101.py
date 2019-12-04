import math

with open('input/01.txt', 'r') as file:
    _input = file.read().strip().split('\n')

def fuel1(f):
    return math.floor(int(i) / 3) - 2

total = 0

for i in _input:
    total = total + fuel1(int(i))

print('0101: {}'.format(total))

def fuel2(f):
    fc = math.floor(f / 3) - 2
    if fc < 0:
        fc = 0
    if fc > 0:
        fc = fc + fuel2(fc)
    return fc

total = 0

for i in _input:
    total = total + fuel2(int(i))

print('0102: {}'.format(total))