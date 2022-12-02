with open('input/02.txt', 'r') as file:
    _input = [[ord(x[0])-64, ord(x[2])-87] for x in file.readlines()]

#                   shape score + outcome score
print('0201:', sum([p2          + (p2-p1+1)%3*3 for (p1, p2) in _input]))
print('0202:', sum([(p1+oc)%3+1 + oc*3-3        for (p1, oc) in _input]))