with open('input/06.txt', 'r') as file:
    _input = list(file.read().strip())

def process(message, distinct):
    for i in range(distinct,len(_input)):
        if len(set(_input[i-distinct:i])) == distinct:
            return i

print('0601', process(_input, 4))
print('0602', process(_input, 14))
