with open('input/09.txt', 'r') as file:
    _input = [x.strip().split(' ') for x in file.readlines()]


def move_head(h, d):
    for i in range(2):
        h[i] += {'R': [1, 0], 'L': [-1, 0], 'U': [0, 1], 'D': [0, -1]}[d][i]


def move_tail(h, t):
    if abs(h[0]-t[0]) > 1 or abs(h[1]-t[1]) > 1:
        for i in range(2):
            t[i] += round((h[i]-t[i])/1.9)


def simulate(knots=2):
    visits = set()
    coords = [[0, 0] for x in range(0, knots)]

    for motion in _input:
        for i in range(int(motion[1])):
            move_head(coords[0], motion[0])
            for tail in range(len(coords)-1):
                move_tail(coords[tail], coords[tail+1])
            visits.add(','.join([str(x) for x in coords[-1]]))

    return len(visits)


print('0901:', simulate())
print('0902:', simulate(10))
