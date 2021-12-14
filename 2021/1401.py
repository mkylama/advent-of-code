with open('input/14.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

def increment(dictionary, key, value):
    if key in dictionary:
        dictionary[key] += value
    else:
        dictionary[key] = value

def insert(pairs):
    new_pairs = {}
    for pair in pairs:
        for new_pair in [pair[0] + rules[pair], rules[pair] + pair[1]]:
            increment(new_pairs, new_pair, pairs[pair])
    return new_pairs

def answer(pairs):
    elements = {template[0]: 1}
    for pair in pairs:
        increment(elements, pair[1], pairs[pair])
    return max(elements.values()) - min(elements.values())

template = _input[0]
rules = dict([x.split(' -> ') for x in _input[2:]])

pairs = {template[i:i+2]: template.count(template[i:i+2]) for i in range(len(template)-1)}

for step in range(40):
    pairs = insert(pairs)
    if step == 9:
        print('1401:', answer(pairs))

print('1402:', answer(pairs))