import re

with open('input/04.txt', 'r') as file:
    _input = file.readlines()
_input = [re.split(':\s+|\s+\|\s+', x) for x in _input]
_input = [[re.split('\s+', p) for p in c] + [1, 0] for c in _input]

card            = 0
winning_numbers = 1
numbers         = 2
card_count      = 3
scratched       = 4

points = []
first_round = True

while sum([c[card_count] for c in _input]):
    for line in _input:
        line[scratched] += line[card_count]
        matches = []
        for number in line[numbers]:
            if number in line[winning_numbers]:
                matches.append(number)
        if matches and first_round:
            points.append(2 ** (len(matches) - 1))
        line_nro = int(line[card][1])
        for x in range(line_nro, line_nro + len(matches)):
            if x < len(_input):
                _input[x][card_count] += line[card_count]
        line[card_count] = 0
    if first_round:
        first_round = False


print('0401:', sum(points))
print('0402:', sum([c[4] for c in _input]))
