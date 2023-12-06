from calendar import c
from curses.ascii import isdigit


INPUT = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

lines = [line for line in INPUT.split("\n") if line]

output = []

for iline, line in enumerate(lines):
    for ichar, char in enumerate(line):
        top = iline - 1
        mid = iline
        bottom = iline + 1
        is_valid_vert = lambda x: x > -1 and x < len(lines)

        left = ichar - 1
        center = ichar
        right = ichar + 1
        is_valid_hor = lambda x: x > -1 and x < len(line)

        neighbour_indices = [
            [
                (top, left) if is_valid_vert(top) and is_valid_hor(left) else None,
                (top, center) if is_valid_vert(top) and is_valid_hor(center) else None,
                (top, right) if is_valid_vert(top) and is_valid_hor(right) else None,
            ],
            [
                (mid, left) if is_valid_vert(mid) and is_valid_hor(left) else None,
                (mid, center) if is_valid_vert(mid) and is_valid_hor(center) else None,  # self
                (mid, right) if is_valid_vert(mid) and is_valid_hor(right) else None,
            ],
            [
                (bottom, left) if is_valid_vert(bottom) and is_valid_hor(left) else None,
                (bottom, center) if is_valid_vert(bottom) and is_valid_hor(center) else None,
                (bottom, right) if is_valid_vert(bottom) and is_valid_hor(right) else None,
            ],
        ]
        flat_neighbour_indices = [elem for row in neighbour_indices for elem in row]

        # self must be symbol
        if isdigit(char) or char == ".":
            continue

        # neighbour must be number

        # get smallest number in neighbours

        print(char, "-->", flat_neighbour_indices)
