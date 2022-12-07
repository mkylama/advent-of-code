with open('input/07.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


def push_value(tree, path, key, value):
    cwp = tree
    for d in path:
        cwp = cwp[d]
    cwp[key] = int(value) if value.isnumeric() else {}


def build_tree(lines):
    tree = {'/':{}}
    cwd = []
    for line in lines:
        p = line.split(' ')
        if p[0] == '$':
            if p[1] == 'cd':
                if p[2] == '..':
                    cwd.pop()
                else:
                    cwd.append(p[2])
            elif p[1] == 'ls':
                pass
        else:
            push_value(tree, cwd, p[1], p[0])
    return tree


def get_dir_sizes(d, sizes=[]):
    size = 0
    for f in d:
        if type(d[f]) == dict:
            d_size, sizes = get_dir_sizes(d[f], sizes)
            sizes.append(d_size)
            size += d_size
        else:
            size += d[f]
    return size, sizes


tree = build_tree(_input)
root_size, sizes = get_dir_sizes(tree)

print('0701:', sum([size for size in sizes if size <= 100000]))

needed_space = 30000000 - 70000000 + root_size
for size in sorted(sizes):
    if size >= needed_space:
        print('0702:', size)
        break
