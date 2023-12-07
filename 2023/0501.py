import json

with open('input/05.txt') as file:
   _input = json.load(file)

def mapper(seed, _map, r=False):
    a = 0 if r else 1
    b = 1 if r else 0
    for _range in _input['maps'][_map]:
        if seed in range(_range[a], _range[a] + _range[2]):
            return seed - _range[a] + _range[b]
    return seed

locs = []

for seed in _input['seeds']:
    soil = mapper(seed, 'seed-to-soil')
    fertilizer = mapper(soil, 'soil-to-fertilizer')
    water = mapper(fertilizer, 'fertilizer-to-water')
    light = mapper(water, 'water-to-light')
    temperature = mapper(light, 'light-to-temperature')
    humidity = mapper(temperature, 'temperature-to-humidity')
    location = mapper(humidity, 'humidity-to-location')

    locs.append(location)

print('0501:', min(locs))

ranges = []

for x in range(0, len(_input['seeds']), 2):
    ranges.append(range(_input['seeds'][x], _input['seeds'][x] + _input['seeds'][x+1]))

location = 0
searching = True
while searching:
    location += 1
    humidity = mapper(location, 'humidity-to-location', True)
    temperature = mapper(humidity, 'temperature-to-humidity', True)
    light = mapper(temperature, 'light-to-temperature', True)
    water = mapper(light, 'water-to-light', True)
    fertilizer = mapper(water, 'fertilizer-to-water', True)
    soil = mapper(fertilizer, 'soil-to-fertilizer', True)
    seed = mapper(soil, 'seed-to-soil', True)
    for r in ranges:
        if seed in r:
            searching = False

print('0502:', location)
