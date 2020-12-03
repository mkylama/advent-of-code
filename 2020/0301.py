with open('input/03.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

def slope(step_x, step_y):
	trees = 0
	pos_x = 0
	pos_y = 0

	while pos_y < len(_input):
		if _input[pos_y][pos_x % len(_input[pos_y])] == '#':
			trees += 1
		pos_x += step_x
		pos_y += step_y

	return trees

print("0301: {}".format(slope(3, 1)))
print("0302: {}".format(slope(1, 1) * slope(3, 1) * slope(5, 1) * slope(7, 1) * slope(1, 2)))
