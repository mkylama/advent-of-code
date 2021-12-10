with open('input/10.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}

points = {')': [3, 1], ']': [57, 2], '}': [1197, 3], '>': [25137, 4]}

part1 = 0
part2 = []


def autocomplete(expected):
    total = 0
    while expected:
        total = total * 5 + points[expected.pop()][1]
    return total


for chunk in _input:
    expected = []
    for char in chunk:
        if char in pairs.keys():
            expected.append(pairs[char])
        elif char == expected[-1]:
            expected.pop()
        else:
            part1 += points[char][0]
            expected = []
            break
    if expected:
        part2.append(autocomplete(expected))


print('1001:', part1)
print('1002:', sorted(part2)[len(part2) // 2])