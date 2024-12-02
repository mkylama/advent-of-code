with open('input/02.txt', 'r') as file:
    _input = [[int(col) for col in row.split()] for row in file.read().strip().split('\n')]

def is_safe(report):
    if report[0] > report[-1]: report.reverse()
    return all([report[index] - report[index-1] in [1, 2, 3] for index in range(1, len(report))])

def is_safe_tolerant(report):
    return any([is_safe(report[:skip] + report[skip+1:]) for skip in [index for index in range(len(report))]])

print('0201:', sum([is_safe(x) for x in _input]))
print('0202:', sum([is_safe_tolerant(x) for x in _input]))
