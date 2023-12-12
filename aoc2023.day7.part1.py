INPUT = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

from functools import cmp_to_key

cards, bids = zip(*list(map(str.split, INPUT.strip().splitlines())))


def compare(str1: str, str2: str) -> int:
    o1 = {c: str1.count(c) for c in str1}
    o2 = {c: str2.count(c) for c in str2}
    if len(o1) != len(o2):
        return len(o2) - len(o1)

    max1 = max(o1.values())
    max2 = max(o2.values())
    if max1 != max2:
        return max1 - max2

    rank = "AKQJT98765432"
    for c1, c2 in list(zip(str1, str2)):
        if c1 != c2:
            return rank.index(c2) - rank.index(c1)

    return 0


sorted_cards = sorted(cards, key=cmp_to_key(compare))
total = 0
for i, card in enumerate(sorted_cards):
    bid = int(bids[cards.index(card)])
    total += bid * (i + 1)
print(total)
