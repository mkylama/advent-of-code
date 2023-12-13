with open('input/13.txt', 'r') as file:
    _input = [x.split('\n') for x in file.read().strip().split('\n\n')]

def rotate(l):
    return [''.join([l[len(l)-y-1][x] for y in range(len(l))]) for x in range(len(l[0]))]

def mirror(l, smudge=False):
    for i in range(1, len(l)):
        linecount = min(i, len(l) - i)
        if smudge:
            if sum(1 for a, b in zip(''.join(l[i-linecount:i]), ''.join(reversed(l[i:i+linecount]))) if a != b) == 1:
                return i
        else:
            if ''.join(l[i-linecount:i]) == ''.join(reversed(l[i:i+linecount])):
                return i
    return 0

print('1301:', sum([100 * mirror(p) + mirror(rotate(p)) for p in _input]))
print('1302:', sum([100 * mirror(p, True) + mirror(rotate(p), True) for p in _input]))
