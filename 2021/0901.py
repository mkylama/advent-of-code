with open('input/09.txt', 'r') as file:
    _input = [[int(x) for x in list(y.strip())] for y in file.readlines()]

def is_low_point(x, y):
    if x > 0 and _input[y][x-1] <= _input[y][x]:
        return False
    if x < len(_input[y]) - 1 and _input[y][x+1] <= _input[y][x]:
        return False
    if y > 0 and _input[y-1][x] <= _input[y][x]:
        return False
    if y < len(_input) - 1 and _input[y+1][x] <= _input[y][x]:
        return False
        
    return True

print('0901:', sum([sum([_input[y][x] + 1 for x in range(len(_input[y])) if is_low_point(x, y)]) for y in range(len(_input))]))

def crawler(x, y):
    if _input[y][x] == 9:
        return []

    coords = [str(x) + ':' + str(y)]

    if x > 0 and _input[y][x-1] > _input[y][x]:
        coords.extend(crawler(x-1, y))
    if x < len(_input[y]) - 1 and _input[y][x+1] > _input[y][x]:
        coords.extend(crawler(x+1, y))
    if y > 0 and _input[y-1][x] > _input[y][x]:
        coords.extend(crawler(x, y-1))
    if y < len(_input) - 1 and _input[y+1][x] > _input[y][x]:
        coords.extend(crawler(x, y+1))

    return list(dict.fromkeys(coords))

basins = sorted(sum([[len(crawler(x, y)) for x in range(len(_input[y])) if is_low_point(x, y)] for y in range(len(_input))], []))

print('0902:', basins[-1] * basins[-2] * basins[-3])