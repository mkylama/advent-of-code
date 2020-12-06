with open('input/06.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]
    _input.append('');


count_1 = 0
count_2 = 0

answers = []

for line in _input:
    if len(line) > 0:
        answers.append(set(line[::1]))
    else:
        count_1 += len(set.union(*answers))
        count_2 += len(set.intersection(*answers))
        answers = []


print("0601: {}".format(count_1))
print("0602: {}".format(count_2))
