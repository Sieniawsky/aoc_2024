def scan(lines, x, y):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    search_area = ["M", "A", "S"]
    found = 0
    for direction in directions:
        for search in search_area:
            adjustment_x = (abs(direction[0]) + search_area.index(search)) * direction[0]
            adjustment_y = (abs(direction[1]) + search_area.index(search)) * direction[1]
            new_x = x + adjustment_x
            new_y = y + adjustment_y
            if 0 <= new_x < len(lines) and 0 <= new_y < len(lines[new_x]):
                if lines[new_x][new_y] == search:
                    if search == "S":
                        found += 1
                else:
                    break
    return found

if __name__ == "__main__":
    f = open("data/day_4_1.txt", "r")

    lines = list(map(lambda x: x.strip(), f.readlines()))
    found = 0
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == "X":
                found += scan(lines, x, y)
    print(found)

# 0: [1, 2, 3, 4, 5]
# 1: [6, 7, 8, 9, 10]
# 2: [11, 12, 13, 14, 15]
# 3: [16, 17, 18, 19, 20]
# 4: [21, 22, 23, 24, 25]


# 0,0
# 1,0, 0,1
# 2,0, 1,1, 0,2
# 3,0, 2,1, 1,2, 0,3
# 4,0, 3,1, 2,2, 1,3, 0,4
# 4,1, 3,2, 2,3, 1,4
# 4,2, 3,3, 2,4
# 4,3, 3,4
# 4,4

# 0,4
# 1,4, 0,3
# 2,4, 1,3, 0,2
# 3,4, 2,3, 1,2, 0,1
# 4,4, 3,3, 2,2, 1,1, 0,0
# 4,3, 3,2, 2,1, 1,0
# 4,2, 3,1, 2,0
# 4,1, 3,0
# 4,0
