with open('input/01.txt', 'r') as file:
    _input = [int(x) for x in file.readlines()]

incs = 0

for a in range(1, len(_input)):
    incs += _input[a] > _input[a-1]

print('0101:', incs)

incs = 0

for a in range(3, len(_input)):
    incs += sum(_input[a-2:a+1]) > sum(_input[a-3:a])

print('0102:', incs)