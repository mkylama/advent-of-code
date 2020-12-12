with open('input/12.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


headings = ['S', 'W', 'N', 'E']
dir_values = {'R': 1, 'L': -1}


def move_coord(coords, heading, value):
    i = headings.index(heading)
    coords[abs(i % 2 - 1)] += value * int((i // 2 - .5) * 2)


def rotate_ship(current, direction, angle):
    return headings[(headings.index(current) + angle // 90 * dir_values[direction]) % 4]


def rotate_waypoint(waypoint, direction, angle): 
    for i in range(0, angle // 90):
        waypoint.reverse()
        waypoint[bool(dir_values[direction] + 1)] *= -1


def move_ship(location, waypoint, multiplier):
    for i in [0, 1]:
        location[i] += waypoint[i] * multiplier


def navigate():
    location = [0, 0]

    heading = 'E'

    for inst in _input:
        a = inst[:1]
        v = int(inst[1:])

        if a in headings:
            move_coord(location, a, v)
        elif a in dir_values:
            heading = rotate_ship(heading, a, v)
        elif a == 'F':
            move_coord(location, heading, v)

    return abs(location[0]) + abs(location[1])


def navigate_with_waypoint():
    location = [0, 0]
    waypoint = [10, 1]

    for inst in _input:
        a = inst[:1]
        v = int(inst[1:])

        if a in headings:
            move_coord(waypoint, a, v)
        elif a in dir_values:
            heading = rotate_waypoint(waypoint, a, v)
        elif a == 'F':
            move_ship(location, waypoint, v)

    return abs(location[0]) + abs(location[1])


print("1201: {}".format(navigate()))
print("1202: {}".format(navigate_with_waypoint()))
