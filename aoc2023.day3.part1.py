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

num_start_indices = set()

for iline, line in enumerate(lines):
    for ichar, char in enumerate(line):
        if char == "." or char.isdigit():
            continue

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
        print("\tdigit neighbours of", char, ":", digit_neighbours)

        # get start of word
        for x, y in digit_neighbours:
            curr = y
            while is_digit(x, curr):
                curr -= 1
            print("\t\tword for", x, y, "starts at", x, curr + 1)
            num_start_indices.add((x, curr + 1))

# get entire word
nums = []
for x, y in num_start_indices:
    num = ""
    curr = y
    while is_digit(x, curr):
        num += lines[x][curr]
        curr += 1
    nums.append(int(num))

print(nums)
print("sum:", sum(nums))
