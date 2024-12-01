with open('input/01t.txt', 'r') as file:
    _input = [[int(y) for y in x.split('   ')] for x in file.read().strip().split('\n')]

left, right = zip(*_input)

print('0101:', sum([abs(x[0] - x[1]) for x in zip(sorted(left), sorted(right))]))
print('0102:', sum([x * right.count(x) for x in left]))
