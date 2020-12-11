with open('input/11.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

width = len(_input[0])
height = len(_input)

_input = ''.join(_input)

directions = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]


def adjacent_occupied(layout, chair, only_first):
    x = chair % width
    y = chair // width

    occupied = 0

    for dx, dy in directions:
        ax = x + dx
        ay = y + dy
        while ax >= 0 and ax < width and ay >= 0 and ay < height:
            if layout[ax + ay * width] == 'L':
                break
            elif layout[ax + ay * width] == '#':
                occupied += 1
                break
            elif only_first:
                break
            ax += dx
            ay += dy

    return occupied


def occupy_seats(layout, emptylimit, only_first):
    while(True):
        new_layout = layout
        for chair in range(0, len(layout)):

            if layout[chair] != '.':
                occupied = adjacent_occupied(layout, chair, only_first)
                if layout[chair] == 'L' and occupied == 0:
                    new_layout = new_layout[:chair] + '#' + new_layout[chair+1:]
                elif layout[chair] == '#' and occupied >= emptylimit:
                    new_layout = new_layout[:chair] + 'L' + new_layout[chair+1:]



        if new_layout == layout:
            return new_layout.count('#')

        layout = new_layout


print("1101: {}".format(occupy_seats(_input, 4, True)))
print("1102: {}".format(occupy_seats(_input, 5, False)))