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
solution = []

for line in FLOOR_PLAN:
    regex_matches = list(re.finditer(r"[^/\\|+-]+", line))
    regex_matches = [{"start": rm.start(), "end": rm.end(), "text": rm.group()} for rm in regex_matches]
    if not regex_matches:
        continue

    print(f"{line}")
    new_queue = []

    for room in queue:
        # find regex_matches that are in the room
        rm_in_room = lambda rm, room: max(room["rms"][-1]["start"], rm["start"]) < min(room["rms"][-1]["end"], rm["end"])
        rms = [rm for rm in regex_matches if rm_in_room(rm, room)]
        regex_matches = [rm for rm in regex_matches if not rm_in_room(rm, room)]

        # add regex_matches to room, keep in queue
        if rms:
            room["rms"].extend(rms)
            new_queue.append(room)
            
        # find room name and chairs, remove from queue, add to solution
        else:
            text = "".join([rm["text"] for rm in room["rms"]])
            name = re.search(r"\((?:[A-Za-z]+\s?)+\)", text)
            assert name
            room["name"] = name[0][1:-1]
            room["chairs"] = {f: text.count(f) for f in CHAIR_TYPES}
            solution.append(room)            
            print("\t" * 6 + f"completed '{room['name']}' with {room["chairs"]}")

    queue = new_queue
    
    for rm in regex_matches:
        queue.append({"name": None, "chairs": {}, "rms": [rm]})
        print("\t" * 5 + f"\tcreated new room ({rm["start"]}-{rm["end"]})")


print("\n\n")
assert len(queue) == 0, f"queue should be empty, but contains {len(queue)} rooms"
solution.extend(queue)
for s in solution:
    print(s["name"], s["chairs"], len(s["rms"]))
