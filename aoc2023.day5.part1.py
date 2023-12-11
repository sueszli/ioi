from typing import Callable

INPUT = """
seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def gen_mapper(data: list[list[int]]) -> Callable[[int], int]:
    def func(x: int):
        matched_range = [True if (x >= row[1] and x < (row[1] + row[2])) else False for row in data]
        if not any(matched_range):
            return x

        assert matched_range.count(True) == 1
        idx = matched_range.index(True)
        row = data[idx]

        return row[0] + (x - row[1])

    return func


maps = {}
blocks = list(map(str.strip, INPUT.split("\n\n")))
for b in blocks:
    name = b.split(":")[0].strip()

    data = b.split(":")[1].strip().splitlines()
    data = [elem.split(" ") for elem in data]
    intdata: list[list[int]] = [[int(elem) for elem in row] for row in data]

    assert name not in maps
    if name == "seeds":
        flatintdata = [elem for row in intdata for elem in row]
        maps[name] = flatintdata
    else:
        maps[name] = gen_mapper(intdata)


seeds = maps["seeds"]
locations = []
for seed in seeds:
    soil = maps["seed-to-soil map"](seed)
    fertilizer = maps["soil-to-fertilizer map"](soil)
    water = maps["fertilizer-to-water map"](fertilizer)
    light = maps["water-to-light map"](water)
    temperature = maps["light-to-temperature map"](light)
    humidity = maps["temperature-to-humidity map"](temperature)
    location = maps["humidity-to-location map"](humidity)

    locations.append(location)
    print(f"seed ({seed}) -> location ({location})")

print(min(locations))
