from functools import reduce
from operator import add

f = open("data/day_1_1.txt", "r")
left = []
right = []
for x in f:
    split = x.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

occurrences = [0] * len(left)
for x in left:
    for y, z in enumerate(right):
        if x == z:
            occurrences[y] += x

sum = reduce(add, occurrences)
print(sum)
