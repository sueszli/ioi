INPUT = """
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

lines = [line for line in INPUT.split("\n") if line]
num_lines = ["".join(filter(str.isdigit, line)) for line in lines]
edge_num_lines = [int(num[0] + num[-1]) for num in num_lines]
total_sum = sum(edge_num_lines)

print(f"solution: {total_sum}")
