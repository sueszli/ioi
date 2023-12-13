INPUT = """
LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)
"""

fstline = INPUT.strip().splitlines()[0]
lines = [(m[0], m[1].split(", ")) for m in [l.removesuffix(")").split(" = (") for l in INPUT.strip().splitlines()[2:]]]
lookup = lambda x: list(filter(lambda line: line[0] == x, lines))[0][1]

curr = "AAA"
cmds = fstline
steps = 0

while len(cmds) > 0:
    if cmds[0] == "R":
        curr = lookup(curr)[1]
    else:
        curr = lookup(curr)[0]

    cmds = cmds[1:]
    if len(cmds) == 0 and curr != "ZZZ":
        cmds = fstline

    steps += 1
    print(curr)

print(steps)
