with open('input/11.txt', 'r') as file:
    _input = [[y.strip().split(' ') for y in x.strip().split('\n')] for x in file.read().split('\n\n')]


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x


def lcm_list(l):
    while len(l) > 1:
        x, y = l.pop(), l.pop() 
        l.append((x * y) // gcd(x, y))
    return l[0]


def process(rounds, divider=1):
    monkeys = [
        {
            'id': int(data[0][1].replace(':','')),
            'items': [int(x.replace(',','')) for x in data[1][2:]],
            'operation': ' '.join(data[2][1:]).replace('new = ', ''),
            'divisible': int(data[3][3]),
            'true': int(data[4][5]),
            'false': int(data[5][5]),
            'inspects': 0
        } for data in _input]
    cm = lcm_list([m['divisible'] for m in monkeys])
    
    for i in range(rounds):
        for monkey in monkeys:
            while monkey['items']:
                monkey['inspects'] += 1
                old = monkey['items'].pop(0)
                new = eval(monkey['operation']) // divider
                monkeys[monkey['true' if new % monkey['divisible'] == 0 else 'false']]['items'].append(new % cm)

    inspects = sorted([m['inspects'] for m in monkeys])
    return inspects[-1] * inspects[-2]


print('1101:', process(20, 3))
print('1102:', process(10000))
