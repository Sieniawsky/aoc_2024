def contains_target(lines, x, y, directions):
    search_area = [["M", "S"], ["S", "M"]]
    for search in search_area:
        found = 0
        for i in range(2):
            new_x = x + directions[i][0]
            new_y = y + directions[i][1]
            if 0 <= new_x < len(lines) and 0 <= new_y < len(lines[new_x]):
                if lines[new_x][new_y] == search[i]:
                    found += 1
        if found == 2:
            return True
    return False

def main():
    f = open("data/day_4_1.txt", "r")

    lines = list(map(lambda x: x.strip(), f.readlines()))
    found = 0
    for x in range(len(lines)):
        for y in range(len(lines[x])):
            if lines[x][y] == "A":
                target_found_ne = contains_target(lines, x, y, [(1, 1), (-1, -1)])
                target_found_se = contains_target(lines, x, y, [(1, -1), (-1, 1)])
                if target_found_ne and target_found_se:
                    found += 1
    print(found)    

if __name__ == "__main__":
    main()