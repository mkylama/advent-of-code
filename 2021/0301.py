with open('input/03.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]


def most_common_bit(binary_list, index):
    bit = 0

    for binary in binary_list:
        bit += 1 if binary[index] == '1' else -1

    bit = '0' if bit < 0 else '1'

    return bit


# ------
# Part 1
# ------
bits = [most_common_bit(_input, b) for b in range(0, len(_input[0]))]

gamma = int(''.join(bits), 2)
epsilon = pow(2, len(bits)) - gamma - 1

print('0301:', gamma * epsilon)


# ------
# Part 2
# ------
oxygen_list = _input.copy()
co2_list = _input.copy()

for b in range(0, len(_input[0])):
    if len(oxygen_list) > 1:
        oxygen_bit = most_common_bit(oxygen_list, b)
        oxygen_list = [i for i in oxygen_list if i[b] == oxygen_bit]
    if len(co2_list) > 1:
        co2_bit = most_common_bit(co2_list, b)
        co2_list = [i for i in co2_list if i[b] != co2_bit]

oxygen = int(oxygen_list[0], 2)
co2 = int(co2_list[0], 2)

print('0302:', oxygen * co2)