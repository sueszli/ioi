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


indices = set()

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

        # get indices of all digits around this char
        digit_neighbour_indices = [
            [
                (top, left) if is_valid_vert(top) and is_valid_hor(left) and lines[top][left].isdigit() else None,
                (top, center) if is_valid_vert(top) and is_valid_hor(center) and lines[top][center].isdigit() else None,
                (top, right) if is_valid_vert(top) and is_valid_hor(right) and lines[top][right].isdigit() else None,
            ],
            [
                (mid, left) if is_valid_vert(mid) and is_valid_hor(left) and lines[mid][left].isdigit() else None,
                (mid, center) if is_valid_vert(mid) and is_valid_hor(center) and lines[mid][center].isdigit() else None,  # self
                (mid, right) if is_valid_vert(mid) and is_valid_hor(right) and lines[mid][right].isdigit() else None,
            ],
            [
                (bottom, left) if is_valid_vert(bottom) and is_valid_hor(left) and lines[bottom][left].isdigit() else None,
                (bottom, center) if is_valid_vert(bottom) and is_valid_hor(center) and lines[bottom][center].isdigit() else None,
                (bottom, right) if is_valid_vert(bottom) and is_valid_hor(right) and lines[bottom][right].isdigit() else None,
            ],
        ]

        if char == "." or char.isdigit():
            continue
        new_indices = [elem for row in digit_neighbour_indices for elem in row if elem is not None]
        indices.update(new_indices)

# group by row
indices_by_row = {}
for index in indices:
    row = index[0]
    if row not in indices_by_row:
        indices_by_row[row] = []
    indices_by_row[row].append(index[1])

# sort each row
for row in indices_by_row:
    indices_by_row[row] = sorted(indices_by_row[row])

# for each index in each group, find the starting point of word / numbers
print(indices_by_row)
