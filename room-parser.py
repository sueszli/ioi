# see: https://stackoverflow.com/questions/71826437/parsing-ascii-floor-plan-image-in-python
# - Read the floor plan below and print the number of chairs per room.
# - Sort alphabetically by room name.

# ```
# total:
# W: 3, P: 2, S: 0, C: 0
# living room:
# W: 3, P: 0, S: 0, C: 0
# office:
# W: 0, P: 2, S: 0, C: 0
# ```


FLOOR_PLAN = """
+-----------+------------------------------------+
|           |                                    |
| (closet)  |                                    |
|         P |                            S       |
|         P |         (sleeping room)            |
|         P |                                    |
|           |                                    |
+-----------+    W                               |
|           |                                    |
|        W  |                                    |
|           |                                    |
|           +--------------+---------------------+
|                          |                     |
|                          |                W W  |
|                          |    (office)         |
|                          |                     |
+--------------+           |                     |
|              |           |                     |
| (toilet)     |           |             P       |
|   C          |           |                     |
|              |           |                     |
+--------------+           +---------------------+
|              |           |                     |
|              |           |                     |
|              |           |                     |
| (bathroom)   |           |      (kitchen)      |
|              |           |                     |
|              |           |      W   W          |
|              |           |      W   W          |
|       P      +           |                     |
|             /            +---------------------+
|            /                                   |
|           /                                    |
|          /                          W    W   W |
+---------+                                      |
|                                                |
| S                                   W    W   W |
|                (living room)                   |
| S                                              |
|                                                |
|                                                |
|                                                |
|                                                |
+--------------------------+---------------------+
                           |                     |
                           |                  P  |
                           |  (balcony)          |
                           |                 P   |
                           |                     |
                           +---------------------+
""".strip().splitlines()

import re

CHAIR_TYPES = "CPSW"
queue = []
ans = []

for line in FLOOR_PLAN:
    regex_matches = list(re.finditer(r"[^/\\|+-]+", line))
    regex_matches = [{"start": rm.start(), "end": rm.end(), "text": rm.group()} for rm in regex_matches]
    if not regex_matches:
        continue

    print(f"{line}")

    for room in queue:
        # find room to assign regex match to
        found = False
        for rm in regex_matches:
            last_rm = room["rms"][-1]
            has_overlap = max(last_rm["start"], rm["start"]) < min(last_rm["end"], rm["end"])
            if has_overlap:
                room["rms"].append(rm)
                regex_matches.remove(rm)
                found = True
                break

        # else set room as complete
        if not found:
            text = "".join([rm["text"] for rm in room["rms"]])
            name = re.search(r"\((?:[A-Za-z]+\s?)+\)", text)
            assert name
            room["name"] = name[0][1:-1]
            room["furn_count"] = {f: text.count(f) for f in CHAIR_TYPES}
            ans.append(room)            
            room["complete"] = True
            print("\t" * 6 + f"completed '{room['name']}' with {room["furn_count"]}")

    # remove completed rooms from queue
    queue = [r for r in queue if r["complete"] == False]

    # create new rooms in queue with remaining regex matches
    for rm in regex_matches:
        queue.append({"name": None, "furn_count": {}, "rms": [rm], "complete": False})
        print("\t" * 5 + f"\tcreated new room ({rm["start"]}-{rm["end"]})")


print("\n\n")
assert len(queue) == 0, f"queue should be empty, but contains {len(queue)} rooms"
ans.extend(queue)
for a in ans:
    print(a["name"], a["furn_count"], len(a["rms"]))
