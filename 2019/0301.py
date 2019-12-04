with open('input/03.txt', 'r') as file:
    _input = file.read().strip().split('\n')

_input = [i.split(',') for i in _input]

coords = {}

def iter(inp, i, c):
    x = 0
    y = 0

    step = 0

    for m in inp[i]:
        d = m[:1]
        for n in range(int(m[1:])):
            step += 1
            if d == 'R':
                x += 1
            elif d == 'L':
                x -= 1
            elif d == 'U':
                y += 1
            elif d == 'D':
                y -= 1

            if '{},{}'.format(x, y) in c:
                if i not in c['{},{}'.format(x, y)]:
                    c['{},{}'.format(x, y)][i] = step
            else:
                c['{},{}'.format(x, y)] = {i: step}

iter(_input, 0, coords)
iter(_input, 1, coords)

dist = None
steps = None

for p in coords:
    if 0 in coords[p] and 1 in coords[p]:
        # 0301
        c = list(map(int, p.split(',')))
        if dist is None or abs(c[0]) + abs(c[1]) < dist:
            dist = abs(c[0]) + abs(c[1])
        # 0302
        if steps is None or coords[p][0] + coords[p][1] < steps:
            steps = coords[p][0] + coords[p][1]

print('0301: {}'.format(dist))
print('0302: {}'.format(steps))