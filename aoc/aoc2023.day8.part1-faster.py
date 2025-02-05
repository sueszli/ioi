INPUT = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

cmds = INPUT.strip().splitlines()[0]

parsedlines = [(m[0], m[1].split(", ")) for m in [l.removesuffix(")").split(" = (") for l in INPUT.strip().splitlines()[2:]]]
dic = {line[0]: line[1] for line in parsedlines}

curr = "AAA"
steps = 0

while curr != "ZZZ":
    steps += 1
    curr = dic[curr][0 if cmds[0] == "L" else 1]
    cmds = cmds[1:] + cmds[0]

print("ans:", steps)
