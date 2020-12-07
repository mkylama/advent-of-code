with open('input/07.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

rules = {}

for rule in _input:
	parts = rule.split('contain')
	key = ' '.join(parts[0].strip().split(' ')[:-1])
	values = parts[1].strip().split(', ')
	rules[key] = {' '.join(x.split(' ')[1:-1]):int(x.split(' ')[0]) for x in values if not 'no other bags' in x}


def contains_shiny_gold(bag):
	if 'shiny gold' in rules[bag]:
		return True
	for inner_bag in rules[bag]:
		if contains_shiny_gold(inner_bag):
			return True

	return False


def bagception(bag):
	count = 0
	for inner_bag, amount in rules[bag].items():
		count += amount * (1 + bagception(inner_bag))
	return count


print("0701: {}".format(sum(contains_shiny_gold(bag) for bag in rules)))
print("0702: {}".format(bagception('shiny gold')))
