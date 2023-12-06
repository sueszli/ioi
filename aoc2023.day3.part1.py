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


word_start_indices = set()

for iline, line in enumerate(lines):
    for ichar, char in enumerate(line):
        if char == "." or char.isdigit():
            continue

        in_bounds = lambda x, y: x > -1 and x < len(lines) and y > -1 and y < len(line)
        is_digit = lambda x, y: lines[x][y].isdigit()

        neighbours = [
            (iline - 1, ichar - 1),
            (iline - 1, ichar),
            (iline - 1, ichar + 1),
            (iline, ichar - 1),
            (iline, ichar),
            (iline, ichar + 1),
            (iline + 1, ichar - 1),
            (iline + 1, ichar),
            (iline + 1, ichar + 1),
        ]
        digit_neighbours = [(x, y) for x, y in neighbours if in_bounds(x, y) and is_digit(x, y)]

        print(char, "--->", digit_neighbours)

        # indices.update(new_indices)
