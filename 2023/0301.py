import re

with open('input/03.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

part_numbers = []
gears = {}

for line in range(len(_input)):
    numbers = re.findall(r'\d+', _input[line])
    start_index = 0
    for number in numbers:
        is_part = False
        start = _input[line].index(number, start_index)
        end = len(number) + start + 1
        start_index = end
        number = int(number)
        for y in range(line - 1, line + 2):
            if y >= 0 and y < len(_input):
                for x in range(start - 1, end):
                    if x >= 0 and x < len(_input[line]):
                        symbol = re.findall(r'[^\d\.]', _input[y][x])
                        if symbol:
                            is_part = True
                        if _input[y][x] == '*':
                            gear = f'{x},{y}'
                            if gear in gears:
                                gears[gear].append(number)
                            else:
                                gears[gear] = [number]
        if is_part:
            part_numbers.append(number)

print('0301:', sum(part_numbers))
print('0302:', sum([g[0]*g[1] for g in gears.values() if len(g) == 2]))
