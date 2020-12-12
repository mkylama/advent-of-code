import itertools

with open('input/09.txt', 'r') as file:
    _input = [int(x.strip()) for x in file.readlines()]


def find_attack_point():
    for i in range(25, len(_input)):
        c = [sum(x) for x in list(itertools.combinations(set(_input[i-25:i]), 2))]
        if _input[i] not in c:
            return(_input[i])


def find_weakness(attack_point):
	for i in range(0, len(_input)):
		total = 0
		for j in range(i, len(_input)):
			total += _input[j]
			if total > attack_point:
				break
			elif total == attack_point:
				return min(_input[i:j]) + max(_input[i:j])


attack_point = find_attack_point()
encryption_weakness = find_weakness(attack_point)

print("0901: {}".format(attack_point))
print("0902: {}".format(encryption_weakness))
