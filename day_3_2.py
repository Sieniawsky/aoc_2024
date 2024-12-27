import re

def sum_muls(target):
    matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", target)
    total = 0
    for x in matches:
        total += int(x[0]) * int(x[1])
    return total

if __name__ == "__main__":
    f = open("data/day_3_1.txt", "r")

    sub_text = re.sub(r"(don't\(\)(.|\n)+?do\(\)|don't\(\)(.|$)+)", "", f.read())
    print(sum_muls(sub_text))
