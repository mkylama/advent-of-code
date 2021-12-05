with open('input/04.txt', 'r') as file:
    _input = [x.strip() for x in file.readlines()]

numbers = [int(x) for x in _input[0].split(',')]

boards = []

for line in range(2, len(_input), 6):
    boards.append([[int(n) for n in x.split(' ') if len(n) > 0] for x in _input[line:line+5]])

def bingo(number, board):
    # mark number
    for row in board:
        for i in range(0, 5):
            if row[i] == number:
                row[i] = -1
    # check if bingo
    for col in range(0,5):
        _sum = 0
        for row in range (0,5):
            if col == 0 and sum(board[row]) == -5:
                return True
            _sum += board[row][col]
        if _sum == -5:
            return True

winners = []

for number in numbers:
    for b in range(0, len(boards)):
        if boards[b]:
            if bingo(number, boards[b]):
                winners.append(sum([sum([c for c in r if c > 0]) for r in boards[b]]) * number)
                boards[b] = []

print('0401:', winners[0])
print('0402:', winners[len(winners)-1])