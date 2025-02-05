INPUT = """
Time:        40     92     97     90
Distance:   215   1064   1505   1100
"""

line = lambda x: int("".join(INPUT.strip().splitlines()[x].split(":")[1].split()))
time = line(0)
maxdist = line(1)
print("solution:", len([x for x in range(0, time) if (time - x) * x > maxdist]))
