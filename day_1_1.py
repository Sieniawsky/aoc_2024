f = open("data/day_1_1.txt", "r")
left = []
right = []
for x in f:
    split = x.split()
    left.append(int(split[0]))
    right.append(int(split[1]))

left = sorted(left)
right = sorted(right)
sum = 0

for x in range(len(left)):
    sum += abs(left[x] - right[x])

print(sum)
