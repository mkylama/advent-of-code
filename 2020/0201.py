with open('input/02.txt', 'r') as file:
    _input = [x.strip().split(' ') for x in file.readlines()]

def is_valid_1(line):
	limits = [int(x) for x in line[0].split('-')]
	letter = line[1][0:1]
	count = line[2].count(letter)
	if count >= limits[0] and count <= limits[1]:
		return True

def is_valid_2(line):
	positions = [int(x) - 1 for x in line[0].split('-')]
	letter = line[1][0:1]
	if line[2][positions[0]] != line[2][positions[1]] and (line[2][positions[0]] == letter or line[2][positions[1]] == letter):
		return True
	return False

valid_1 = 0
valid_2 = 0

for line in _input:
	if is_valid_1(line):
		valid_1 += 1
	
	if is_valid_2(line):
		valid_2 += 1

print("0201: {}".format(valid_1))
print("0202: {}".format(valid_2))
