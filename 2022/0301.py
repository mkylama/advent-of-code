with open('input/03.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

prios = ' abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

compartments = [[x[:(len(x)//2)], x[(len(x)//2):]] for x in _input]
print('0301:', sum([prios.index([i for i in c1 if i in c2][0]) for (c1, c2) in compartments]))

groups = [_input[i:i + 3] for i in range(0, len(_input), 3)]
print('0302:', sum([prios.index([i for i in r1 if i in r2 and i in r3][0]) for (r1, r2, r3) in groups]))
