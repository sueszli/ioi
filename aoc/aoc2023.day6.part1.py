import math

INPUT = """
Time:        40     92     97     90
Distance:   215   1064   1505   1100
"""

# goal: beating maxdist
# each second holding the button = +1mm/ms

times = list(map(int, INPUT.strip().splitlines()[0].split(":")[1].split()))
distances = list(map(int, INPUT.strip().splitlines()[1].split(":")[1].split()))
assert len(times) == len(distances)
races = list(zip(times, distances))

ans = []
for race in races:
    time = race[0]
    maxdist = race[1]

    is_solution = lambda x: (time - x) * x > maxdist  # time holding button beats maxdist
    solutions = [x for x in range(0, time) if is_solution(x)]

    ans.append(len(solutions))

print("solution:", math.prod(ans))
