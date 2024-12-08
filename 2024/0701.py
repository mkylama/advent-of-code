with open('input/07.txt', 'r') as file:
    i = [[int(y) for y in x.replace(':','').split()] for x in file.read().strip().split('\n')]

def calibrate(base, nums, concat=False):
    if len(nums) == 1:
        return [base + nums[0]] + [base * nums[0]] + ([int(str(base) + str(nums[0]))] if concat else [])
    else:
        return calibrate(base + nums[0], nums[1:], concat) \
            + calibrate(base * nums[0], nums[1:], concat) \
            + (calibrate(int(str(base) + str(nums[0])), nums[1:], concat) if concat else [])

print('0701:', sum([row[0] for row in i if row[0] in calibrate(row[1], row[2:])]))
print('0702:', sum([row[0] for row in i if row[0] in calibrate(row[1], row[2:], True)]))
