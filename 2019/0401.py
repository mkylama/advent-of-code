import re


with open('input/04.txt', 'r') as file:
    _input = file.read().strip().split('-')

limits = list(map(int, _input))


def ascending(pwd):
    if re.search(r'^1*2*3*4*5*6*7*8*9*$', pwd):
        return True
    return False


def valid1(pwd):
    if re.search(r'(\d)\1', pwd):
        return True
    return False


def valid2(pwd):
    repeats = [match.group() for match in re.compile(r'(\d)\1+').finditer(pwd)]
    for r in repeats:
        if len(r) == 2:
            return True
    return False


total1 = 0
total2 = 0

for i in range(limits[0], limits[1]+1):
    s = str(i)
    if ascending(s):
        if valid1(s):
            total1 += 1
        if valid2(s):
            total2 += 1

print('0401: {}'.format(total1))
print('0402: {}'.format(total2))