with open('input/11.txt') as file:
   _input = [x.strip() for x in file.readlines()]

height = len(_input)
width = len(_input[0])

vrt = []
hor = []
glx = []

# find vertical spaces and galaxies
for y in range(height):
    gs = [x for x in range(width) if _input[y][x] != '.']
    if gs:
        for x in gs:
            glx.append((x,y)) 
    else:
        hor.append(y)

# find horizontal spaces
for x in range(width):
    gs = [y for y in range(height) if _input[y][x] != '.']
    if len(gs) == 0:
        vrt.append(x)

def summer(expansion_multiplier=2):
    exp = 1 * expansion_multiplier - 1 
    dist = 0
    for g1 in range(len(glx) - 1):
        for g2 in range(g1 + 1, len(glx)):
            dist += abs(glx[g1][0] - glx[g2][0]) + abs(glx[g1][1] - glx[g2][1])
            dist += exp * len([v for v in vrt if v in range(*sorted([glx[g1][0], glx[g2][0]]))])
            dist += exp * len([h for h in hor if h in range(*sorted([glx[g1][1], glx[g2][1]]))])
    return dist

print('1101:',summer())
print('1102:',summer(1000000))
