with open('input/01.txt', 'r') as file:
    _input = [int(x) for x in file.readlines()]

for a in range(0, len(_input)):
    for b in range(a+1, len(_input)):
        if _input[a] + _input[b] == 2020:
            print("0101: {}".format(_input[a] * _input[b]))
        for c in range(b+1, len(_input)):
            if _input[a] + _input[b] + _input[c] == 2020:
                print("0102: {}".format(_input[a] * _input[b] * _input[c]))
