from copy import deepcopy

with open('input/08.txt', 'r') as file:
    _input = [x.strip().split(' ') for x in file.readlines()]

for row in _input:
	row[1] = int(row[1])


def program(i):
	instructions = deepcopy(i)
	accumulator = 0
	instruction = 0

	length = len(instructions)

	while True:
		if instruction >= length:
			return accumulator, True
		elif len(instructions[instruction]) > 2:
			return accumulator, False

		instructions[instruction].append(True)

		if instructions[instruction][0] == 'nop':
			instruction += 1
		elif instructions[instruction][0] == 'acc':
			accumulator += instructions[instruction][1]
			instruction += 1
		elif instructions[instruction][0] == 'jmp':
			instruction += instructions[instruction][1]


def execution(i):
	for row in i:
		if row[0] == 'nop':
			row[0] = 'jmp'
		elif row[0] == 'jmp':
			row[0] = 'nop'
		accumulator, executed = program(i)
		if row[0] == 'nop':
			row[0] = 'jmp'
		elif row[0] == 'jmp':
			row[0] = 'nop'
		if executed:
			break
	return accumulator, executed


print("0801: {}".format(program(_input)[0]))
print("0802: {}".format(execution(_input)[0]))
