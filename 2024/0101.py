with open('input/01.txt', 'r') as file:
    _input = [[int(y) for y in x.split()] for x in file.read().strip().split('\n')]

left, right = zip(*_input)

print('0101:', sum([abs(l - r) for l, r in zip(sorted(left), sorted(right))]))
print('0102:', sum([l * right.count(l) for l in left]))
