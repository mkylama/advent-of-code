with open('input/01.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

def digits(s, w):
    i = [(s.find(x), x) for x in w if x in s]
    ri = [(s.rfind(x), x) for x in w if x in s]
    return int(str(w.index(min(i)[1]) % 9 + 1) + str(w.index(max(ri)[1]) % 9 + 1))

print('0101:', sum([digits(x, ['1', '2', '3', '4', '5', '6', '7', '8', '9']) for x in _input]))
print('0102:', sum([digits(x, ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', '1', '2', '3', '4', '5', '6', '7', '8', '9']) for x in _input]))
