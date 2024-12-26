def element_difference(report):
    diffs = []
    for x in range(len(report)):
        if x != len(report) - 1:
            diffs.append(abs(report[x] - report[x + 1]))
    return diffs

if __name__ == "__main__":
    f = open("data/day_2_1.txt", "r")

    reports = []
    for x in f:
        reports.append(list(map(int, x.split())))

    safe = 0

    for report in reports:
        sorted_asc = sorted(report)
        sorted_desc = sorted(report, reverse=True)
        diffs = element_difference(report)

        if (report == sorted_asc or report == sorted_desc) and (min(diffs) >=1 and max(diffs) <= 3):
            safe += 1

    print(safe)
