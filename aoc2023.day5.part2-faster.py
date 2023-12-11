import sys

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


def gen_get_location():
    maps = {}
    blocks = list(map(str.strip, INPUT.split("\n\n")))
    for b in blocks:
        name = b.split(":")[0].strip()

        data = b.split(":")[1].strip().splitlines()
        data = [elem.split(" ") for elem in data]
        intdata: list[list[int]] = [[int(elem) for elem in row] for row in data]

        assert name not in maps
        if name == "seeds":
            continue
        mapper = lambda data: (lambda x: (lambda row: row[0] + (x - row[1]) if row else x)(next(iter([row for row in data if x >= row[1] and x < (row[1] + row[2])]), None)))
        maps[name] = mapper(intdata)

    f1 = maps["seed-to-soil map"]
    f2 = maps["soil-to-fertilizer map"]
    f3 = maps["fertilizer-to-water map"]
    f4 = maps["water-to-light map"]
    f5 = maps["light-to-temperature map"]
    f6 = maps["temperature-to-humidity map"]
    f7 = maps["humidity-to-location map"]
    return lambda seed: f7(f6(f5(f4(f3(f2(f1(seed)))))))


def remove_overlaps(ranges: list[range]) -> list[range]:
    sorted_ranges = sorted(ranges, key=lambda r: r.start)

    non_overlapping_ranges = []
    curr = sorted_ranges[0]
    for r in sorted_ranges[1:]:
        if curr.stop >= r.start:
            curr = range(curr.start, max(curr.stop, r.stop))
        else:
            non_overlapping_ranges.append(curr)
            curr = r
    non_overlapping_ranges.append(curr)

    return non_overlapping_ranges


if __name__ == "__main__":
    seeds = list(map(int, list(filter(lambda x: x, INPUT.splitlines()))[0].split(":")[1].strip().split(" ")))
    seed_ranges: list[range] = remove_overlaps([range(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)])  # optimization: remove range overlaps
    get_location = gen_get_location()

    minlocation: int = sys.maxsize
    for i, seed_range in enumerate(seed_ranges):
        for j, seed in enumerate(seed_range):
            minlocation = min(minlocation, get_location(seed))
            print(f"seed pair {(i)/(len(seed_ranges) -1) * 100:.2f}%: {(j)/(len(seed_range) -1) * 100:.2f}%")
    print("solution:", minlocation)
