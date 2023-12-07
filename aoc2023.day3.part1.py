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

is_digit = lambda x, y: x > -1 and x < len(lines) and y > -1 and y < len(lines[x]) and lines[x][y].isdigit()

word_dict = {}  # key: start index, value: word

for iline, line in enumerate(lines):
    for ichar, char in enumerate(line):
        if char == "." or char.isdigit():
            continue

        # get all neighbouring digits
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
        digit_neighbours = [(x, y) for x, y in neighbours if is_digit(x, y)]

        print("processing", char)

        # get start of words
        starts_indices = set()
        for x, y in digit_neighbours:
            curr = y
            while is_digit(x, curr):
                curr -= 1
            print("\t\tword for", x, y, "starts at", x, curr + 1)
            starts_indices.add((x, curr + 1))

        # read words
        words = []
        for x, y in starts_indices:
            word = ""
            curr = y
            while is_digit(x, curr):
                word += lines[x][curr]
                curr += 1

            words.append(word)
            word_dict[(x, y)] = word

total = sum([int(word) for word in list(word_dict.values())])
print(f"total: {total}")
