with open('input/02.txt', 'r') as file:
    _input = [x.strip().split(' ') for x in file.readlines()]

def is_valid_1(limits, letter, pwd):
    count = pwd.count(letter)
    if count >= limits[0] and count <= limits[1]:
        return True
    return False

def is_valid_2(pos, letter, pwd):
    if pwd[pos[0]-1] != pwd[pos[1]-1] and (pwd[pos[0]-1] == letter or pwd[pos[1]-1] == letter):
        return True
    return False

valid_1 = 0
valid_2 = 0

for line in _input:
    numbers = [int(x) for x in line[0].split('-')]
    letter = line[1][0:1]

    if is_valid_1(numbers, letter, line[2]):
        valid_1 += 1
    
    if is_valid_2(numbers, letter, line[2]):
        valid_2 += 1

print("0201: {}".format(valid_1))
print("0202: {}".format(valid_2))
