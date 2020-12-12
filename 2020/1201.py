with open('input/12.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


directions = ['S', 'W', 'N', 'E']
lr_values = {'R': 1, 'L': -1}


def move_coord(coords, direction, value):
    i = directions.index(direction)
    coords[abs(i % 2 - 1)] += value * int((i // 2 - .5) * 2)


def rotate_ship(current, left_or_right, angle):
    ci = directions.index(current)
    ci = (ci + angle // 90 * lr_values[left_or_right]) % 4
    return directions[ci]


def rotate_waypoint(waypoint, left_or_right, angle): 
    for i in range(0, angle // 90):
        waypoint.reverse()
        waypoint[bool(lr_values[left_or_right] + 1)] *= -1


def move_ship(location, waypoint, multiplier):
    for i in [0, 1]:
        location[i] += waypoint[i] * multiplier


def navigate():
    location = [0, 0]

    direction = 'E'

    for inst in _input:
        a = inst[:1]
        v = int(inst[1:])

        if a in directions:
            move_coord(location, a, v)
        elif a in lr_values:
            direction = rotate_ship(direction, a, v)
        elif a == 'F':
            move_coord(location, direction, v)

    return abs(location[0]) + abs(location[1])


def navigate_with_waypoint():
    location = [0, 0]
    waypoint = [10, 1]

    for inst in _input:
        a = inst[:1]
        v = int(inst[1:])

        if a in directions:
            move_coord(waypoint, a, v)
        elif a in lr_values:
            direction = rotate_waypoint(waypoint, a, v)
        elif a == 'F':
            move_ship(location, waypoint, v)

    return abs(location[0]) + abs(location[1])


print("1201: {}".format(navigate()))
print("1202: {}".format(navigate_with_waypoint()))
