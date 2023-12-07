import math

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

all_words = {}  # key: start index, value: word
gear_ratio_sum = 0

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

        # get start of words
        starts_indices = set()
        for x, y in digit_neighbours:
            curr = y
            while is_digit(x, curr):
                curr -= 1
            starts_indices.add((x, curr + 1))

        # read words
        words = {}
        for x, y in starts_indices:
            word = ""
            curr = y
            while is_digit(x, curr):
                word += lines[x][curr]
                curr += 1
            words[(x, y)] = word

        # update global stores
        all_words.update(words)
        if len(words) == 2 and char == "*":
            nums = [int(word) for word in list(words.values())]
            gear_ratio_sum += math.prod(nums)


print(f"total sum: {sum([int(word) for word in list(all_words.values())])}")
print(f"gear ratio sum: {gear_ratio_sum}")
