with open('input/06.txt', 'r') as file:
    _input = [int(x) for x in file.readline().split(',')]

nums = [_input.count(x) for x in range(0, 9)]

for d in range(0, 256):
    nums.append(nums.pop(0))
    nums[6] += nums[8]
    if d == 79:
        print('0601:', sum(nums))
    elif d == 255:
        print('0602:', sum(nums))