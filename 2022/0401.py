with open('input/04.txt', 'r') as file:
    _input = [[int(y) for y in ','.join(x.split('-')).split(',')] for x in file.readlines()]

print('0401:', len(['x' for (r1l, r1r, r2l, r2r) in _input if (r1l >= r2l and r1r <= r2r) or (r1l <= r2l and r1r >= r2r)]))
print('0402:', len(['x' for (r1l, r1r, r2l, r2r) in _input if set(range(r1l,r1r+1)).intersection(range(r2l,r2r+1))]))
