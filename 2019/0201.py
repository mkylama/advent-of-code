with open('input/02.txt', 'r') as file:
    _input = file.read().strip().split(',')

_input = list(map(int, _input))


def gravity(i, a, b):
    i = i.copy()
    i[1] = a
    i[2] = b

    pos = 0

    while i[pos] != 99:
        if i[pos] == 1:
            i[i[pos+3]] = i[i[pos+1]] + i[i[pos+2]]
        elif i[pos] == 2:
            i[i[pos+3]] = i[i[pos+1]] * i[i[pos+2]]
        pos = pos + 4

    return (i[0])

print('0201: {}'.format(gravity(_input, 12, 2)))

found = False

for noun in range(0, 99):
    if found:
        break;
    for verb in range(0, 99):
        if gravity(_input, noun, verb) == 19690720:
            print('0202: {}'.format(100 * noun + verb))
            found = True
            break