with open('input/05.txt', 'r') as file:
    _input = file.read().strip().split(',')

_input = list(map(int, _input))


def param(v):
    s = str(v)
    return int(s[-2:]), s[-3:-2] is not '0', s[-4:-3] is not '0', s[-5:-4] is not '0'

def gravity(i, a, b):
    i = i.copy()

    pos = 0

    while i[pos] != 99:

        op, b1, b2, b3 = param(i[pos])

        if b1:
            p1 = i[pos+1]
        else:
            p1 = i[i[pos+1]]

        if b2:
            p2 = i[pos+2]
        else:
            p2 = i[i[pos+2]]

        if b3:
            p3 = i[pos+3]
        else:
            p3 = i[i[pos+3]]

        print(i[pos], op, b1, p1, b2, p2, b3, p3)

        if op == 1:
            i[b3] = b2 + b3
        elif op == 2:
            i[b3] = b2 * b3
        elif op == 3:
            i[b1] = 1
            pos += - 2
        elif op == 4:
            print('output: {}'.format(i[pos]+1))
            pos += 2
        pos += 4

    return (i[0])

print('0501: {}'.format(gravity(_input, 12, 2)))

# found = False

# for noun in range(0, 99):
#     if found:
#         break;
#     for verb in range(0, 99):
#         if gravity(_input, noun, verb) == 19690720:
#             print('0202: {}'.format(100 * noun + verb))
#             found = True
#             break