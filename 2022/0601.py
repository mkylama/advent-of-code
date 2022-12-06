with open('input/06.txt', 'r') as file:
    _input = list(file.read().strip())

def process(msg, dist):
    return [i for i in range(dist, len(msg)) if len(set(msg[i-dist:i])) == dist][0]

print('0601:', process(_input, 4))
print('0602:', process(_input, 14))