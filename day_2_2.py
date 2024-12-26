def element_difference(report):
    diffs = []
    for x in range(len(report)):
        if x != len(report) - 1:
            diffs.append(abs(report[x] - report[x + 1]))
    return diffs

def follows_rules(report):
    sorted_asc = sorted(report)
    sorted_desc = sorted(report, reverse=True)
    diffs = element_difference(report)

    return (report == sorted_asc or report == sorted_desc) and (min(diffs) >=1 and max(diffs) <= 3)

def sublist(report, index):
    return report[:index] + report[index + 1:]

def is_safe(report):
    if follows_rules(report):
        return True
    else:
        for x in range(len(report)):
            subset = sublist(report, x)
            if follows_rules(subset):
                return True
        return False

if __name__ == "__main__":
    f = open("data/day_2_1.txt", "r")

    reports = []
    for x in f:
        reports.append(list(map(int, x.split())))

    safe = 0

    for report in reports:
        if is_safe(report):
            safe += 1

    print(safe)
