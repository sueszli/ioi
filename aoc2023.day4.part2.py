from collections import deque


INPUT = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


# parse into read-only data structure
CARDS = {}
for line in INPUT.splitlines():
    if len(line) <= 0:
        continue
    card = {}
    card["id"] = int(line.split(": ")[0].split(" ")[-1].strip())
    card["winning_nums"] = [int(elem) for elem in line.split(": ")[1].split(" | ")[0].split(" ") if len(elem) > 0]
    card["card_nums"] = [int(elem) for elem in line.split(": ")[1].split(" | ")[1].split(" ") if len(elem) > 0]
    card["match_count"] = len([elem for elem in card["card_nums"] if elem in card["winning_nums"]])
    card["unlocked_card_ids"] = [(card["id"] + i + 1) for i in range(card["match_count"])]
    CARDS[card["id"]] = card


# calculate total num of reads (this will take a while)
total_reads: int = 0
q: deque[int] = deque()

q.extend(range(1, len(CARDS) + 1))
while len(q) > 0:
    total_reads += 1

    id = q.popleft()
    unlocked = CARDS[id]["unlocked_card_ids"]
    q.extend(unlocked)
    print("queue length:", len(q))

print("total_reads:", total_reads)
