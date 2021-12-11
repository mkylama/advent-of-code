with open('input/11.txt', 'r') as file:
    _input = [[int(y) for y in x.strip()] for x in file.readlines()]

def increment(grid, y, x):
    grid[y][x] += 1
    if grid[y][x] == 10:
        flash(grid, y, x)

def flash(grid, y, x):
    global flashes
    flashes += 1
    for fy in range(-1,2):
        if y+fy in range(10):
            for fx in range(-1,2):
                if x+fx in range(10):
                    increment(grid, y+fy, x+fx)

def add_step(grid):
    for y in range(10):
        for x in range(10):
            increment(grid, y, x)
    for y in range(10):
        for x in range(10):
            if grid[y][x] > 9:
                grid[y][x] = 0

flashes = 0
iterator = 1

while True:
    add_step(_input)
    if iterator == 100:
        print('1101:', flashes)
    elif sum(sum(_input, [])) == 0:
        print('1102:', iterator)
        break
    iterator += 1