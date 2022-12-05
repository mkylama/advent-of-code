def create_stacks(rows, size):
    stacks = [[] for x in range(size)]

    for containers in reversed(rows):
        for idx, container in enumerate(containers):
            if container != ' ':
                stacks[idx].append(container)

    return stacks


def rearrange(stacks, moves, reverse=False):
    for move in moves:
        (c, f, t) = [int(x) for x in move.split(' ')[1::2]]
        stacks[t-1].extend(stacks[f-1][-c:] if reverse else reversed(stacks[f-1][-c:]))
        stacks[f-1] = stacks[f-1][:-c]

    return ''.join([x[-1] for x in stacks])


with open('input/05.txt', 'r') as file:
    _input1, _input2 = file.read().split('\n\n')

rows = [x[1::4] for x in _input1.split('\n')]
stack_count = len(rows.pop())
moves = _input2.strip().split('\n')

stacks = create_stacks(rows, stack_count)

print('0501:', rearrange([x[:] for x in stacks], moves))
print('0502:', rearrange([x[:] for x in stacks], moves, reverse=True))
