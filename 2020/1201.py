with open('input/12.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


directions = ['N', 'E', 'S', 'W']
lr_values = {'R': 1, 'L': -1}


def rotate_ship(current, left_or_right, angle):
    ci = directions.index(current)
    ci = int((ci + angle / 90 * lr_values[left_or_right]) % 4)
    return directions[ci]


def move_ship(location, direction, value):
    if direction == 'N':
        location[1] += value
    elif direction == 'E':
        location[0] += value
    elif direction == 'S':
        location[1] -= value
    elif direction == 'W':
        location[0] -= value


def navigate():
    location = [0, 0]

    direction = 'E'

    for inst in _input:
        a = inst[:1]
        v = int(inst[1:])

        if a in directions:
            move_ship(location, a, v)
        elif a in lr_values:
            direction = rotate_ship(direction, a, v)
        elif a == 'F':
            move_ship(location, direction, v)

    return abs(location[0]) + abs(location[1])


def rotate_waypoint(waypoint, left_or_right, angle): 
    for i in range(0, int(angle / 90)):
        waypoint.reverse()
        if left_or_right == 'L':
            waypoint[0] *= -1
        else:
            waypoint[1] *= -1


def move_waypoint(location, direction, value):
    if direction == 'N':
        location[1] += value
    elif direction == 'E':
        location[0] += value
    elif direction == 'S':
        location[1] -= value
    elif direction == 'W':
        location[0] -= value


def move_ship_toward_waypoint(location, waypoint, multiplier):
    location[0] += waypoint[0] * multiplier
    location[1] += waypoint[1] * multiplier


def navigate_with_waypoint():
    location = [0, 0]
    waypoint = [10, 1]

    for inst in _input:
        a = inst[:1]
        v = int(inst[1:])

        if a in directions:
            move_waypoint(waypoint, a, v)
        elif a in lr_values:
            direction = rotate_waypoint(waypoint, a, v)
        elif a == 'F':
            move_ship_toward_waypoint(location, waypoint, v)

    return abs(location[0]) + abs(location[1])


print("1201: {}".format(navigate()))
print("1202: {}".format(navigate_with_waypoint()))
