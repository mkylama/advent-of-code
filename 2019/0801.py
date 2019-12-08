with open('input/08.txt', 'r') as file:
    _input = file.read().strip()

width = 25
height = 6

layer_count = int(len(_input) / (width * height))

layers = []

for l in range(0, layer_count):
	sub = _input[l*width*height:((l+1)*width*height)]
	layers.append({
		'0': sub.count('0'),
		'1': sub.count('1'),
		'2': sub.count('2')
	})

min_zero = min(layers, key=lambda x:x['0'])

print('0801: {}'.format(min_zero['1']*min_zero['2']))

render = ['2'] * width * height

for d in range(0, len(_input)):
	target = d % (width * height)
	if render[target] is '2':
		render[target] = _input[d]

print('\n0802:\n')

for r in range(0, height):
	sub = ''.join(render)[r*width:(r+1)*width]
	print(sub.replace('0',' '))