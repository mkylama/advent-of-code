from heapq import heappop, heappush

with open('input/15.txt', 'r') as file:
    _input = [[int(x) for x in y.strip()] for y in file.readlines()]

def find_edges(grid):
    height = len(grid)
    width = len(grid[0])

    edges = []

    for y in range(width):
        for x in range(height):
            neighbors = [i for i in [(y-1,x), (y+1,x), (y,x-1), (y,x+1)] if i[0] >= 0 and i[0] < height and i[1] >= 0 and i[1] < width]
            for neighbor in neighbors:
                edges.append(((y, x), neighbor, grid[neighbor[0]][neighbor[1]]))
    return edges

def analyse(grid):
    edges = find_edges(grid)
    source = (0, 0)
    target = edges[-1][0]

    graph = {}
    for node_source, node_target, risk_level in edges:
        if node_source not in graph:
            graph[node_source] = [(risk_level, node_target)]
        else:
            graph[node_source].append((risk_level, node_target))

    queue = [(0, source)]
    seen = set()
    while queue:
        (risk_total, node1) = heappop(queue)
        if node1 not in seen:
            seen.add(node1)
            if node1 == target:
                return risk_total
            for risk_level, node2 in graph.get(node1, ()):
                if node2 in seen:
                    continue
                next = risk_total + risk_level
                heappush(queue, (next, node2))

    return -1

def increment(grid, value):
    return [[1 + (x + value - 1) % 9 for x in y] for y in grid]

def concat(first, second, axis):
    new_grid = []
    if axis == 'x':
        for y in range(len(first)):
            new_grid.append(first[y])
            new_grid[y].extend(second[y])
    elif axis == 'y':
        new_grid = first[:]
        for y in second:
            new_grid.append(y)
    return new_grid

print('1501:', analyse(_input))

tile = [y[:] for y in _input]
tilerow = [y[:] for y in _input]
for x in range(1, 5):
    tilerow = concat(tilerow, increment(tile, x), 'x')
tilegrid = [y[:] for y in tilerow]
for x in range(1, 5):
    tilegrid = concat(tilegrid, increment(tilerow, x), 'y')

print('1502:', analyse(tilegrid))