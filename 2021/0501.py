import re

with open('input/05.txt', 'r') as file:
    _input = [dict(zip(['x1', 'y1', 'x2', 'y2'], [int(c) for c in re.split(',| -> ', x)])) for x in file.readlines()]

overlaps = {}

def get_range(a, b, keep_direction=False):
    r = list(range(min([a, b]), max([a, b]) + 1))
    if keep_direction and a > b:
        r.reverse()
    return r

for i in _input:
    if i['x1'] == i['x2'] or i['y1'] == i['y2']:
        for x in get_range(i['x1'], i['x2']):
            for y in get_range(i['y1'], i['y2']):
                key = str(x)+':'+str(y)
                if key not in overlaps:
                    overlaps[key] = 1
                else:
                    overlaps[key] += 1

print('0501:', len(overlaps) - list(overlaps.values()).count(1))

for i in _input:
    if abs(i['x1'] - i['x2']) == abs(i['y1'] - i['y2']):
        x = get_range(i['x1'], i['x2'], keep_direction=True)
        y = get_range(i['y1'], i['y2'], keep_direction=True)
        for i in range(0, len(x)):
            key = str(x[i])+':'+str(y[i])
            if key not in overlaps:
                overlaps[key] = 1
            else:
                overlaps[key] += 1

print('0502:', len(overlaps) - list(overlaps.values()).count(1))