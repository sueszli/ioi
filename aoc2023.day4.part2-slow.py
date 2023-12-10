INPUT = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

# parse into read-only data structure
CARDS = []
for index, line in enumerate(INPUT.splitlines()):
    if len(line) <= 0:
        continue
    card = {}
    card["id"] = int(line.split(": ")[0].split(" ")[-1].strip())
    card["winning_nums"] = [int(elem) for elem in line.split(": ")[1].split(" | ")[0].split(" ") if len(elem) > 0]
    card["card_nums"] = [int(elem) for elem in line.split(": ")[1].split(" | ")[1].split(" ") if len(elem) > 0]
    card["match_count"] = len([elem for elem in card["card_nums"] if elem in card["winning_nums"]])
    card["unlocked_card_ids"] = [(card["id"] + i + 1) for i in range(card["match_count"])]
    CARDS.append(card)

    print("processed: ", card["id"])


# copy card ids, hop until no copies left
history: list[int] = []
id_queue: list[int] = []
id_queue.extend(range(1, len(CARDS) + 1))

while len(id_queue) > 0:
    id = id_queue.pop(0)
    history.append(id)

    arr_idx = id - 1
    card = CARDS[arr_idx]
    unlocked = card["unlocked_card_ids"]
    id_queue.extend(unlocked)

    print("queue length:", len(id_queue))


# print history
hs = {}
for h in history:
    if h not in hs.keys():
        hs[h] = 0
    hs[h] += 1

for k, v in hs.items():
    print(f"card {k}: {v} times")
print(f"total cards: {sum(hs.values())}")
