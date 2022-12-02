with open('input/02.txt', 'r') as file:
    _input = [[ord(x[0])-64, ord(x[2])-87] for x in file.readlines()]

print('0201:', sum([round[1] + (round[1]-round[0]+4)%3*3 for round in _input]))
print('0202:', sum([(round[0]+round[1])%3+1 + round[1]*3-3 for round in _input]))