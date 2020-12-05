import re

def bpass_to_binary(bpass):
    bpass = re.sub("[FL]", '0', bpass)
    bpass = re.sub("[BR]", '1', bpass)
    return bpass


with open('input/05.txt', 'r') as file:
    _input = [bpass_to_binary(x.strip()) for x in file.readlines()]


def get_seat_id(bpass):
    row = int(''.join(bpass[:7]), 2)
    col = int(''.join(bpass[-3:]), 2)

    return row * 8 + col


seat_ids = [get_seat_id(x) for x in _input]


def find_missing_seat(seat_ids):
    seat_ids.sort()
    for i in range(0, len(seat_ids) - 1):
        if seat_ids[i] + 2 == seat_ids[i + 1]:
            return seat_ids[i]+1


print("0501: {}".format(max(seat_ids)))
print("0502: {}".format(find_missing_seat(seat_ids)))
