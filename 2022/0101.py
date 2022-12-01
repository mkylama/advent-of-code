with open('input/01.txt', 'r') as file:
    _input = [[int(y) for y in x.split('\n')] for x in file.read().strip().split('\n\n')]

print('0101:', max([sum(x) for x in _input]))
print('0102:', sum(sorted([sum(x) for x in _input])[-3:]))
