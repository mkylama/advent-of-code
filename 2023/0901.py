with open('input/09.txt') as file:
   _input = [[int(y) for y in x.strip().split(' ')] for x in file.readlines()]

def predict(numbers, future=True):
    seqs = [numbers.copy()]
    while sum(seqs[-1]) != 0:
        seqs.append([seqs[-1][n + 1] - seqs[-1][n] for n in range(len(seqs[-1]) - 1)])
    for seq in reversed(range(len(seqs) - 1)):
        if future:
            seqs[seq] = seqs[seq] + [seqs[seq][-1] + seqs[seq + 1][-1]]
        else:
            seqs[seq] = [seqs[seq][0] - seqs[seq + 1][0]] + seqs[seq]
    return seqs[0][-1] if future else seqs[0][0]

print('0901:', sum([predict(x) for x in _input]))
print('0901:', sum([predict(x, False) for x in _input]))
