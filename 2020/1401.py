with open('input/14.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


def bitmask(mask, value, ignore):
    b_value = list('{0:b}'.format(value).zfill(36))
    for i in range(36):
        if mask[i] != ignore:
            b_value[i] = mask[i]
    return ''.join(b_value)


def version_1():
    mem = {}
    mask = ''

    for line in _input:
        parts = line.split()
        if parts[0] == 'mask':
            mask = parts[-1]
        else:
            mem[int(parts[0][4:-1])] = int(bitmask(mask, int(parts[2]), 'X'), 2)

    return sum(mem.values())


def version_2():
    mem = {}
    mask = ''

    for line in _input:
        parts = line.split()
        if parts[0] == 'mask':
            mask = parts[-1]
        else:
            masked_address = bitmask(mask, int(parts[0][4:-1]), '0')
            floating = masked_address.count('X')
            for i in range(pow(2, floating)):
                address = masked_address
                for r in '{0:b}'.format(i).zfill(floating):
                    address = address.replace('X', r, 1)
                mem[int(address, 2)] = int(parts[2])

    return sum(mem.values())


print("1401: {}".format(version_1()))
print("1402: {}".format(version_2()))