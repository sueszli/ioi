INPUT = """
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483
"""

# see: https://github.com/hyper-neutrino/advent-of-code/blob/main/2023/day07p2.py


def jcombinations(card):
    if card == "":
        return [""]
    return [x + y for x in ("23456789TQKA" if card[0] == "J" else card[0]) for y in jcombinations(card[1:])]


def get_rank(card):
    def innerrank(card):
        counts = [card.count(char) for char in card]
        if 5 in counts:
            return 6
        if 4 in counts:
            return 5
        if 3 in counts:
            if 2 in counts:
                return 4
            return 3
        if counts.count(2) == 4:
            return 2
        if 2 in counts:
            return 1
        return 0

    # get the highest score of all possible combinations
    score = max(map(innerrank, jcombinations(card)))

    # map card to ascii with joker as '.' (lowest value)
    ascii_map = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}
    newcard = [ascii_map.get(char, char) for char in card]

    return (score, newcard)  # sort by score first, then by card


plays = list(map(str.split, INPUT.strip().splitlines()))
plays = [(card, int(bid)) for card, bid in plays]

plays.sort(key=lambda play: get_rank(play[0]))

ans = 0
for rank, (card, bid) in enumerate(plays, 1):
    ans += rank * bid
print(ans)
