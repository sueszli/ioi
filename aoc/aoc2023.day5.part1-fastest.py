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

# see: https://www.youtube.com/watch?v=NmxHw_bHhGM

seeds = list(map(int, INPUT.strip().splitlines()[0].split(":")[1].split()))
blocks = list(map(str.strip, INPUT.split("\n\n")))[1:]

for block in blocks:
    # get ranges of this block
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))

    # take each seed through all ranges
    new_seeds = []
    for seed in seeds:
        for dst, src, step in ranges:
            if src <= seed < src + step:
                new_seeds.append(seed - src + dst)  # match -> apply map
                break
        else:
            new_seeds.append(seed)  # no match -> identity

    # update seeds after this block
    seeds = new_seeds

print(min(seeds))
