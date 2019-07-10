from collections import defaultdict


def card(s):
    value_dict = {**{str(d): d for d in range(2, 10)}, **{'A': 14, 'T': 10, 'J': 11, 'Q': 12, 'K': 13}}
    return {'val': value_dict[s[0]], 'suit': s[1]}


def counts(cards):
    count_dict = defaultdict(int)
    for c in cards:
        count_dict[c['val']] += 1
    return count_dict


def highest(cards):
    sc = sorted([c['val'] for c in cards])
    return sc[-1]


def flush(cards):
    if len(set([c['suit'] for c in cards])) == 1:
        return highest(cards)


def straight(cards):
    sc = sorted([c['val'] for c in cards])
    if all([sc[i] == sc[0] + i for i in range(1, len(sc))]):
        return highest(cards)


def one_pair(cards):
    cd = counts(cards)
    for k in reversed(sorted(cd.keys())):
        if cd[k] == 2:
            return k


def two_pair(cards):
    cd = counts(cards)
    if list(cd.values()).count(2) == 2:
        return one_pair(cards)


def three_of_a_kind(cards):
    cd = counts(cards)
    for k in reversed(sorted(cd.keys())):
        if cd[k] == 3:
            return k


def four_of_a_kind(cards):
    cd = counts(cards)
    for k in reversed(sorted(cd.keys())):
        if cd[k] == 4:
            return k


def full_house(cards):
    cdv = counts(cards).values()
    if 2 in cdv and 3 in cdv:
        return highest(cards)


def straight_flush(cards):
    if straight(cards) and flush(cards):
        return highest(cards)


def royal_flush(cards):
    if straight_flush(cards) == 14:
        return 14


def hand_value(cards):
    ranked_hands = [highest, one_pair, two_pair, three_of_a_kind, straight, flush, full_house, four_of_a_kind,
                    straight_flush, royal_flush]
    for i, f in reversed(list(enumerate(ranked_hands))):
        val = f(cards)
        if val:
            return i, val


def compare_hands(s):
    cards = [card(c) for c in s.split(' ')]
    ht = hand_value(cards[0:5])
    h1 = 100 * ht[0] + ht[1]
    ht = hand_value(cards[5:10])
    h2 = 100 * ht[0] + ht[1]
    return h1 > h2


with open('p054_poker.txt') as f:
    total = 0
    for line in f:
        if compare_hands(line):
            total += 1
