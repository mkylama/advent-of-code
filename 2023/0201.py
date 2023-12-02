with open('input/02.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

limits = {'red': 12, 'green': 13, 'blue': 14}

part1 = 0
part2 = 0

for game in _input:
    possible = True
    minimums = {'red': 1, 'green': 1, 'blue': 1}

    name, sets = game.split(': ')

    for _set in sets.split('; '):
        for cubes in _set.split(', '):
            amount, color = cubes.split(' ')
            if int(amount) > limits[color]:
                possible = False
            if int(amount) > minimums[color]:
                minimums[color] = int(amount)
                
    if possible:
        part1 += int(name.split(' ')[-1])
    part2 += minimums['red'] * minimums['green'] * minimums['blue']

print('0201:', part1)
print('0202:', part2)
