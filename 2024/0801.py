with open('input/08.txt', 'r') as file:
    i = [list(x) for x in file.read().strip().split('\n')]

cc = len(i[0])
rc = len(i)

def find_antennas(i):
    antennas = {}
    for r in range(rc):
        for c in range(cc):
            char = i[r][c]
            if char != '.':
                if char in antennas:
                    antennas[char].append([c,r])
                else:
                    antennas[char] = [[c,r]]

    return antennas

def find_antinodes(ants, harmonics=False):
    antinodes = []
    for freqs in ants.values():
        if harmonics:
            antinodes.extend(freqs)
        for a in range(len(freqs)-1):
            for b in range(a+1, len(freqs)):
                cd, rd = freqs[a][0]-freqs[b][0], freqs[a][1]-freqs[b][1]

                for conf in [{'node': a, 'm': 1}, {'node': b, 'm': -1}]:
                    curx, cury = freqs[conf['node']][0], freqs[conf['node']][1]
                    while True:
                        curx += cd * conf['m']
                        cury += rd * conf['m']
                        if 0 <= curx < cc and  0 <= cury < rc:
                            antinodes.append([curx, cury])
                        else:
                            break
                        if not harmonics:
                            break

    return [list(t) for t in {tuple(l) for l in antinodes}]

antennas = find_antennas(i)

print('0801:', len(find_antinodes(antennas)))
print('0802:', len(find_antinodes(antennas, True)))
