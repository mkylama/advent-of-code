with open('input/10.txt', 'r') as file:
    _input = [x.strip().split(' ') for x in file.readlines()]

x = 1
cycles = 0
strengths = []
crt = ''

for cmd in _input:
    for i in range(len(cmd)):
        crt += '#' if cycles % 40 in [x-1, x, x+1] else ' '
        cycles += 1
        if (cycles + 20) % 40 == 0:
            strengths.append(cycles * x)
        if i == 1:
            x += int(cmd[1])

print('1002:', sum(strengths))
print('1002:')
print('\n'.join([crt[i*40:(i+1)*40] for i in range(len(crt)//40)]))
