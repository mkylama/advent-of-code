with open('input/13.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

instructions = [[int(y) if y.isnumeric() else y for y in x.replace('fold along ', '').split('=')] for x in _input[_input.index('')+1:]]
_input = [[int(y) for y in x.split(',')] for x in _input[0:_input.index('')]]

def fold(dots, axis, line):
    ai = 1 if axis == 'y' else 0
    for d in dots:
        if d[ai] > line:
            d[ai] = abs(d[ai] - 2 * line)

for i in range(len(instructions)):
    fold(_input, instructions[i][0], instructions[i][1])
    if i == 0:
        print('1301:', len([list(x) for x in set(tuple(x) for x in _input)]))

grid = [[' ' for x in range(max([y[0] for y in _input]) + 1)] for y in range(max([x[1] for x in _input]) + 1)]

for dot in _input:
    grid[dot[1]][dot[0]] = '#'

print('1302:')
for line in grid:
    print(''.join(line))