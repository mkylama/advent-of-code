from pprint import pprint as pp
import math

with open('input/10.txt', 'r') as file:
    _input = file.read().strip().split('\n')

# asteroids = []
# detected = []

# for y in range(0,len(_input)):
#     for x in range(0,len(_input[0])):
#         if _input[y][x] is '#':
#             asteroids.append([x,y])

# def dist(a, b):
#     return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

# def dist_m(a, b):
#     return abs(b[0]-a[0]) + abs(b[1]-a[1])

# def between(a, b, c):
#     return dist(a, c) + dist(b, c) - dist(a, b) < 0.000001

# for a in asteroids:
#     detects = 0
#     for b in asteroids:
#         if b is not a:
#             visible = True
#             for c in asteroids:
#                 if c is not a and c is not b:
#                     if between(a, b, c):
#                         visible = False
#             if visible:
#                 detects += 1
#     print(detects,a)
#     detected.append(detects)

# print(max(detected))

asteroids = []
detected = []

for y in range(0,len(_input)):
    for x in range(0,len(_input[0])):
        if _input[y][x] is '#':
            asteroids.append([x,y])

for a in asteroids:
    angles = {}
    for b in asteroids:
        if b is not a:
            deg = math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))+180
            if deg == 360.0:
                deg = 0.0
            if deg in angles:
                angles[deg].append(b)
            else:
                angles[deg] = [b]
    detected.append(len(angles))
    if len(angles) == 299:
        print(a)

print('1001: {}'.format(max(detected)))


a = [26, 29]

angles = {}

for b in asteroids:
    if b is not a:
        deg = math.degrees(math.atan2(b[1]-a[1], b[0]-a[0]))+90+360
        if deg >= 360.0:
            deg -= 360.0
        if deg in angles:
            angles[deg].append(b)
        else:
            angles[deg] = [b]

#pp(angles)

x = sorted(list(angles))
for i in range(0, len(x)):
    print (i+1, x[i])