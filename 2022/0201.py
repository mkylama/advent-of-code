with open('input/02.txt', 'r') as file:
    _input = [[ord(x[0])-64, ord(x[2])-87] for x in file.readlines()]

#                   shape score + outcome score
print('0201:', sum([s2          + (s2-s1+1)%3*3 for (s1, s2) in _input]))
print('0202:', sum([(s1+oc)%3+1 + oc*3-3        for (s1, oc) in _input]))