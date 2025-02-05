INPUT = """
three2twone
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""

lines = [line for line in INPUT.split("\n") if line]

sum = 0
for line in lines:
    line = (
        line.rstrip()
        .replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "th3ee")
        .replace("four", "fo4r")
        .replace("five", "fi5e")
        .replace("six", "s6x")
        .replace("seven", "se7en")
        .replace("eight", "ei8ht")
        .replace("nine", "ni9e")
    )
    digits = [int(i) for i in line if i.isdigit()]
    sum += (10 * digits[0]) + digits[-1]

print(f"solution: {sum}")
