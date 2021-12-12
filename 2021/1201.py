with open('input/12.txt', 'r') as file:
    _input = [x.strip().split('-') for x in file.readlines()]

connections = {}

for c in _input:
    if c[0] != 'end' and c[1] != 'start':
        if c[0] in connections:
            connections[c[0]].append(c[1])
        else:
            connections[c[0]] = [c[1]]
    if c[1] != 'end' and c[0] != 'start':
        if c[1] in connections:
            connections[c[1]].append(c[0])
        else:
            connections[c[1]] = [c[0]]

def crawl(cave, visited, **kwargs):
    if cave == 'end':
        return 1
    success = 0
    v = visited[:]
    if cave.islower():
        v.append(cave)
    for c in connections[cave]:
        if c not in v:
            success += crawl(c, v, **kwargs)
        elif 'revisited' in kwargs and not kwargs['revisited']:
            success += crawl(c, v, revisited=True)
    return success

print('1201:', crawl('start', []))
print('1202:', crawl('start', [], revisited=False))