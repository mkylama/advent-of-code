import re

with open('input/04.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]
    _input.append('');


def validate_data_1(fields):
    for key in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if not key in fields:
            return False
    return True


regex = {
    'byr': "^(19[2-9][0-9]|200[0-2])$",
    'iyr': "^(201[0-9]|2020)$",
    'eyr': "^(202[0-9]|2030)$",
    'hgt': "^(1([5-8][0-9]|9[0-3])cm|(59|6[0-9]|7[0-6])in)$",
    'hcl': "^#[0-9a-f]{6}$",
    'ecl': "^(amb|blu|brn|gry|grn|hzl|oth)$",
    'pid': "^[0-9]{9}$",
    'cid': ".*",
}


def validate_data_2(fields):
    for key, value in fields.items():
        if not bool(re.match(regex[key], value)):
            return False

    return True


valid_1 = 0
valid_2 = 0

passport = {}

for line in _input:
    if len(line) > 0:
        fields = line.split(' ')
        for field in fields:
            key, value = field.split(':')
            passport[key] = value
    else:
        if validate_data_1(passport):
            valid_1 += 1
            if validate_data_2(passport):
                valid_2 += 1
        passport.clear()

print("0401: {}".format(valid_1))
print("0402: {}".format(valid_2))
