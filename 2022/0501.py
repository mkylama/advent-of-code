with open('input/05.txt', 'r') as file:
    _input1, _input2 = file.read().rstrip().split('\n\n')


def rearrange(stacks, moves, reverse=False):
    for move in moves:
        c, f, t = [int(x) for x in move.split(' ')[1::2]]
        stacks[t-1] += stacks[f-1][-c:][::1 if reverse else -1]
        stacks[f-1] = stacks[f-1][:-c]
    return ''.join([x[-1] for x in stacks])


stacks = [''.join(x).strip() for x in zip(*[list(x[1::4]) for x in _input1.split('\n')][:-1][::-1])]
moves = _input2.split('\n')

print('0501:', rearrange(stacks[:], moves))
print('0502:', rearrange(stacks[:], moves, reverse=True))
