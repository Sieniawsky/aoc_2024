import re

if __name__ == "__main__":
    f = open("data/day_3_1.txt", "r")
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", f.read())

    total = 0
    for x in matches:
        total += int(x[0]) * int(x[1])
    print(total)
