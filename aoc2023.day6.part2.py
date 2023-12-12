import math

INPUT = """
Time:        40     92     97     90
Distance:   215   1064   1505   1100
"""

time = int("".join(INPUT.strip().splitlines()[0].split(":")[1].split()))
maxdist = int("".join(INPUT.strip().splitlines()[1].split(":")[1].split()))
ans = len([x for x in range(0, time) if (time - x) * x > maxdist])
print("solution:", ans)
