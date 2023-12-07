import re

with open('input/06.txt') as file:
   _input = [x.strip() for x in file.readlines()]

times = re.findall(r'\d+', _input[0])
distances = re.findall(r'\d+', _input[1])

def multiply(nums, base=1):
    for num in nums:
        base *= num
    return base

def count_ways(time, distance):
    ways = 0
    for w in range(1, time):
        if w * (time - w) > distance:
            ways += 1
    return ways

print('0601:', multiply([count_ways(int(times[i]), int(distances[i])) for i in range(len(times))]))
print('0602:', count_ways(int(''.join(times)), int(''.join(distances))))
