from pprint import pprint as pp

with open('input/06.txt', 'r') as file:
    _input = file.read().strip().split('\n')

_input = [i.split(')') for i in _input]
relations = {}

for i in _input:
    if i[0] in relations:
        relations[i[0]].append(i[1])
    else:
        relations[i[0]] = [i[1]]

def orbitor(o,step):
    total = 0
    for r in relations[o]:
        total += step + 1
        if r in relations:
            total += orbitor(r,step+1)
    return total


print('0601: {}'.format(orbitor('COM',0)))


rrelations = {}

for i in _input:
    rrelations[i[1]] = {'parent': i[0]}

current = rrelations['YOU']['parent']

steps = 0

while current in rrelations:
    rrelations[current]['steps'] = steps
    current = rrelations[current]['parent']
    steps += 1

current = rrelations['SAN']['parent']

steps = 0

while current in rrelations:
    if 'steps' in rrelations[current]:
        print('0602: {}'.format(rrelations[current]['steps'] + steps))
        break
    else:
        rrelations[current]['steps'] = steps
        current = rrelations[current]['parent']
        steps += 1