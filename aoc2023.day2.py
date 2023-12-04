from functools import reduce

INPUT = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

MAX_VALS = {"red": 12, "green": 13, "blue": 14}

id_sum = 0
power_sum = 0

lines = [line for line in INPUT.split("\n") if line]
for game in lines:
    min_vals = {"red": 0, "green": 0, "blue": 0}
    valid = True

    rolls = game.rstrip().split(": ")[1].split("; ")
    for roll in rolls:
        for vcpair in [i.split(" ") for i in roll.split(", ")]:
            val, color = vcpair

            # update min_vals
            min_vals[color] = max(min_vals[color], int(val))

            # check validity
            if int(val) > MAX_VALS[color]:
                valid = False

    power = reduce(lambda x, y: x * y, min_vals.values())
    power_sum += power

    if valid:
        game_id = int(game.split(": ")[0].split(" ")[1])
        id_sum += game_id


print(f"Sum of powers: {power_sum}")
print(f"Sum of valid game IDs: {id_sum}")
