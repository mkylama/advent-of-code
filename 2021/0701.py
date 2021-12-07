with open('input/07.txt', 'r') as file:
    _input = [int(x) for x in file.readline().split(',')]

_input.sort()

print('0701:', sum([abs(x - _input[int(len(_input)/2)]) for x in _input]))

def fuel(distance):
    return distance * (distance + 1) / 2

print('0702:', int(sum([fuel(abs(x - round(sum(_input) / len(_input)))) for x in _input])))