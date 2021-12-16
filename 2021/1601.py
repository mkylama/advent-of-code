with open('input/16.txt', 'r') as file:
    _input = file.readlines()[0].strip()

def hex2bin(char):
    c = ord(char) - 48
    if c > 9:
        c -= 7
    return "{0:b}".format(c).zfill(4)

def packet(binary, packets=-1):
    version_total = 0
    values = []

    while len(binary) > 10 and packets != 0:
        if packets > 0:
            packets -= 1

        version = int(binary[0:3], 2)
        version_total += version

        typeid = int(binary[3:6], 2)

        binary = binary[6:]

        if typeid == 4:
            steps, value = literal(binary)
            values.append(value)
            binary = binary[steps:]
        else:
            steps, operator_values, operator_version_total = operator(binary)
            version_total += operator_version_total
            if typeid == 0:
                values.append(sum(operator_values))
            elif typeid == 1:
                prod = 1
                for r in operator_values:
                    prod *= r
                values.append(prod)
            elif typeid == 2:
                values.append(min(operator_values))
            elif typeid == 3:
                values.append(max(operator_values))
            elif typeid == 5:
                values.append(operator_values[0] > operator_values[1])
            elif typeid == 6:
                values.append(operator_values[0] < operator_values[1])
            elif typeid == 7:
                values.append(operator_values[0] == operator_values[1])
            binary = binary[steps:]
            
    return len(binary), values, version_total

def literal(binary):
    start = 0
    number = ''
    while True:
        number += binary[start + 1: start + 5]
        if binary[start] == '0':
            return start + 5, int(number, 2)
        start += 5

def operator(binary):
    length_type = int(binary[0:1], 2)
    if length_type == 0:
        length = int(binary[1:16], 2)
        left, values, version_total = packet(binary[16:16+length])
        return 1 + 15 + length, values, version_total
    else:
        packets = int(binary[1:12], 2)
        left, values, version_total = packet(binary[12:], packets=packets)
        steps = len(binary) - left
        return len(binary) - left, values, version_total

def decode(message):
    binary = ''.join([hex2bin(x) for x in list(message)])#.rstrip('0')
    left, values, version_total = packet(binary)
    return version_total, int(values[0])

version_total, value = decode(_input)

print('1601:', version_total)
print('1602:', value)
