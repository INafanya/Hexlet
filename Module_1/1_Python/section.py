def is_degenerated(line):
    return line[0][0] == line[1][0] and line[0][1] == line[1][1]


def is_vertical(line):
    return line[0][0] == line[1][0] and line[0][1] != line[1][1]


def is_horizontal(line):
    return line[0][0] != line[1][0] and line[0][1] == line[1][1]


def is_inclined(line):
    return line[0][0] != line[1][0] and line[0][1] != line[1][1]



line1 = (0, 10), (100, 130)
line2 = (42, 1), (42, 2)
line3 = (100, 50), (200, 50)
line4 = (42, 2), (42, 2)

print(is_vertical(line1))