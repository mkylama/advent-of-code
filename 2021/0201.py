with open('input/02.txt', 'r') as file:
    _input = [x.split() for x in file.readlines()]

hpos = 0
depth = 0
aim = 0
dwa = 0

for m in _input:
    if m[0] == 'forward':
        hpos += int(m[1])
        dwa += int(m[1]) * aim
    elif m[0] == 'down':
        depth += int(m[1])
        aim += int(m[1])
    elif m[0] == 'up':
        depth -= int(m[1])
        aim -= int(m[1])

print('0201:', hpos * depth)
print('0202:', hpos * dwa)
