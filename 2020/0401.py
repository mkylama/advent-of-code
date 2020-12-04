import re

with open('input/04.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]
    _input.append('');


def validate_data_1(fields):
    if len(fields) < 7 or (len(fields) == 7 and 'cid' in fields):
        return False
    return True


def validate_data_2(fields):
    if not (bool(re.match("^\d{4}$", fields['byr'])) and int(fields['byr']) >= 1920 and int(fields['byr']) <= 2002):
        return False

    if not (bool(re.match("^\d{4}$", fields['iyr'])) and int(fields['iyr']) >= 2010 and int(fields['iyr']) <= 2020):
        return False

    if not (bool(re.match("^\d{4}$", fields['eyr'])) and int(fields['eyr']) >= 2020 and int(fields['eyr']) <= 2030):
        return False

    if not (bool(re.match("^\d+(in|cm)$", fields['hgt'])) and (fields['hgt'][-2:] == 'in' and int(fields['hgt'][:-2]) >= 59 and int(fields['hgt'][:-2]) <= 76) or (fields['hgt'][-2:] == 'cm' and int(fields['hgt'][:-2]) >= 150 and int(fields['hgt'][:-2]) <= 193)):
        return False

    if not bool(re.match("^#[\da-f]{6}$", fields['hcl'])):
        return False

    if not bool(re.match("^(amb|blu|brn|gry|grn|hzl|oth)$", fields['ecl'])):
        return False

    if not bool(re.match("^\d{9}$", fields['pid'])):
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
        valid = validate_data_1(passport)
        if valid:
            valid_1 += 1
            if valid and validate_data_2(passport):
                valid_2 += 1
        passport.clear()

print("0401: {}".format(valid_1))
print("0402: {}".format(valid_2))
