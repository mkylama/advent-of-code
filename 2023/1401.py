with open('input/14.txt') as file:
   _input = [x.strip() for x in file.readlines()]

def rotate(pf):
    return [''.join(x) for x in list(zip(*pf[::-1]))]

def tilt(pf):
    return ['#'.join([''.join(sorted(x)) for x in pf[row].split('#')]) for row in range(len(pf))]

def cycle(pf):
    for l in range(4):
        pf = tilt(rotate(pf))
    return pf

def get_load(pf):
    return sum([sum([c+1 for c in range(len(r)) if r[c] == 'O']) for r in pf])

print('1401:', get_load(tilt(rotate(_input))))

previous = []
loop = [None, None]

for i in range(1000000000):
    _input = cycle(_input)
    joined = ''.join(_input)
    if joined in previous:
        loop = [previous.index(joined), i]
        break
    previous.append(joined)

compensation = (1000000000 - loop[1] - 1) % (loop[1] - loop[0])

for i in range(compensation):
    _input = cycle(_input)

print('1402:', get_load(rotate(_input)))
