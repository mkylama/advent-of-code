with open('input/04.txt', 'r') as file:
    _input = file.read().strip().split('\n')

cc = len(_input[0])
rc = len(_input)

def find_xmas(r, c):
    found = 0
    for d in [[0,1], [1,0], [0,-1], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1]]:
        if 0 <= r + 3 * d[0] < rc and 0 <= c + 3 * d[1] < cc:
            if ''.join([_input[r+x*d[0]][c+x*d[1]] for x in range(4)]) == 'XMAS':
                found += 1
    return found

def find_x_mas(r, c):
    se = ''.join([_input[r+x[0]][c+x[1]] for x in [[-1,-1], [0,0], [1,1]]])
    sw = ''.join([_input[r+x[0]][c+x[1]] for x in [[-1,1], [0,0], [1,-1]]])
    return se in ['MAS', 'SAM'] and sw in ['MAS', 'SAM']

print('0401:', sum([sum([find_xmas(x, y) for x in range(cc) if _input[x][y] == 'X']) for y in range(rc)]))
print('0402:', sum([sum([find_x_mas(x, y) for x in range(1, cc-1) if _input[x][y] == 'A']) for y in range(1, rc-1)]))
