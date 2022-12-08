with open('input/08.txt', 'r') as file:
    _input = [[int(y) for y in x.strip()] for x in file.readlines()]

from pprint import pprint as pp

width = len(_input[0])
height = len(_input)

visible = 0

for y in range(0, height):
    for x in range(0, width):
        if x in [0, width-1] or \
            y in [0, height-1] or \
            _input[y][x] > max(_input[y][:x]) or \
            _input[y][x] > max(_input[y][x+1:]) or \
            _input[y][x] > max([c[x] for c in _input[:y]]) or \
            _input[y][x] > max([c[x] for c in _input[y+1:]]):
                visible += 1

print('0801:', visible)


def get_view(height, trees):
    visible = 0
    for tree in trees:
        visible += 1
        if height <= tree:
            break
    return visible


def prod(numbers):
    result = 1
    for number in numbers:
        if number > 0:
            result *= number
    return result


scores = []

for y in range(0,height):
    for x in range(0, width):
        views = [
            get_view(_input[y][x], _input[y][:x][::-1]),
            get_view(_input[y][x], _input[y][x+1:]),
            get_view(_input[y][x], [c[x] for c in _input[:y]][::-1]),
            get_view(_input[y][x], [c[x] for c in _input[y+1:]])
        ]
        scores.append(prod(views))

print('0802:', max(scores))
