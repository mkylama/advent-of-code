with open('input/08.txt', 'r') as file:
    _input = [[[''.join(sorted(list(z))) for z in y.split(' ')] for y in x.strip().split(' | ')] for x in file.readlines()]

print('0801:', sum([sum([1 for o in l[1] if len(o) in [2, 3, 4, 7]]) for l in _input]))

def overlap(a, b):
    return len([x for x in a if x in b])

def get_output(line):
    digits = [''] * 10
    
    # 1 4 7 8
    for pattern in line[0]:
        if len(pattern) == 2:
            digits[1] = pattern
        elif len(pattern) == 4:
            digits[4] = pattern
        elif len(pattern) == 3:
            digits[7] = pattern
        elif len(pattern) == 7:
            digits[8] = pattern

    # 2 3 5 6 9 0
    for pattern in line[0]:
        if len(pattern) == 5:
            if overlap(pattern, digits[4]) == 2:
                digits[2] = pattern
            elif overlap(pattern, digits[1]) == 2:
                digits[3] = pattern
            else:
                digits[5] = pattern
        elif len(pattern) == 6:
            if overlap(pattern, digits[1]) == 1:
                digits[6] = pattern
            elif overlap(pattern, digits[4]) == 4:
                digits[9] = pattern
            else:
                digits[0] = pattern

    return int(''.join([str(digits.index(x)) for x in line[1]]))

print('0802:', sum([get_output(x) for x in _input]))