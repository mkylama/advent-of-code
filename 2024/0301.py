import re

with open('input/03.txt', 'r') as file:
    _input = file.read().strip()

print('0301:', sum([int(a)*int(b) for (a, b) in re.findall(r'mul\((\d+),(\d+)\)', _input)]))
print('0302:', sum([int(a)*int(b) for (a, b) in re.findall(r'mul\((\d+),(\d+)\)', re.sub(r'(?s)don\'t\(\).*?(?=do\(\)|$)', '', _input))]))
