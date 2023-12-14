with open('input/10.txt') as file:
   _input = [list(x.strip()) for x in file.readlines()]

position = [None, None]
start_d = None
direction = None

ds = {
    'u': {
        'c': [0, -1],
        'v': {'|': 'u', 'F': 'r', '7': 'l'}
    },
    'r': {
        'c': [1,  0],
        'v': {'-': 'r', '7': 'd', 'J': 'u'}
    },
    'd': {
        'c': [0,  1],
        'v': {'|': 'd', 'J': 'l', 'L': 'r'}
    },
    'l': {
        'c': [-1, 0],
        'v': {'-': 'l', 'L': 'u', 'F': 'd'}
    }
}

def get_new_pos(d):
    return [a + b for a, b in zip(ds[d]['c'], position)]

def get_tile(c):
    return _input[c[1]][c[0]]

for y in range(len(_input)):
    for x in range(len(_input[y])):
        if _input[y][x] == 'S':
            position = [x, y]
            break

for d in ds:
    tp = get_new_pos(d)
    if get_tile(tp) in ds[d]['v']:
        direction = d
        start_d = d

visited = {}
visited[f'{position[0]}x{position[1]}'] = {'x': position[0], 'y': position[1]}
steps = 1
while True:
    position = get_new_pos(direction)
    tile = get_tile(position)
    pd = direction
    if tile == 'S':
        break
    else:
        steps += 1
        direction = ds[direction]['v'][tile]
        visited[f'{position[0]}x{position[1]}'] = {'x': position[0], 'y': position[1], 'd': pd+direction}

print('1001:', steps//2)

m = {
    'dd': 'l', 'dr': 'ld', 'dl': '',
    'rr': 'd', 'ru': 'dr', 'rd': '',
    'uu': 'r', 'ul': 'ru', 'ur': '',
    'll': 'u', 'ld': 'ul', 'lu': ''
}

for v in visited:
    if 'd' in visited[v]:
        md = m[visited[v]['d']]
        for d in md:
            position = [visited[v]['x'], visited[v]['y']]
            while True:
                position = get_new_pos(d)
                if f'{position[0]}x{position[1]}' in visited:
                    break
                else:
                    _input[position[1]][position[0]] = 'I'

print('1002:', sum([sum([1 for x in l if x == 'I']) for l in _input]))
