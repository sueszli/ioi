INPUT = """
Time:      7  15   30
Distance:  9  40  200
"""

# my boat:
# - starting speed: 0mm/ms
# - each second holding the button = +1mm/ms

times = list(map(int, INPUT.strip().splitlines()[0].split(":")[1].split()))
distances = list(map(int, INPUT.strip().splitlines()[1].split(":")[1].split()))
assert len(times) == len(distances)
races = list(zip(times, distances))

for race in races:
    time = race[0]
    dist = race[1]
    print(time, dist)
