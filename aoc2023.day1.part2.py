INPUT = """
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def replace_first_mapping_occurrence(line):
    # get index of all keys
    index = {}
    for key in MAPPING.keys():
        i = line.find(key)
        if i != -1:
            index[key] = i

    # get pair with lowest value
    min_pair = min(index.items(), key=lambda x: x[1])

    # replace first key with value, but only the first occurrence
    output = line.replace(min_pair[0], str(MAPPING[min_pair[0]]), 1)
    return output


lines = [line for line in INPUT.split("\n") if line]
updated_lines = []

for line in lines:
    while any(key in line for key in MAPPING.keys()):
        line = replace_first_mapping_occurrence(line)
    updated_lines.append(line)

print(f"lines: {lines}")
print(f"updated_lines: {updated_lines}")

num_lines = ["".join(filter(str.isdigit, line)) for line in updated_lines]
edge_num_lines = [int(num[0] + num[-1]) for num in num_lines]
total_sum = sum(edge_num_lines)

print(f"solution: {total_sum}")
