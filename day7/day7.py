from collections import Counter
from functools import cmp_to_key
with open('day7/day7.txt', 'r') as f:
    data = [x.strip().split() for x in f.readlines()]

# Part 1
card = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']


def compare(a, b):
    rank_a = get_rank(dict(Counter(a[0])))
    rank_b = get_rank(dict(Counter(b[0])))
    if rank_a < rank_b:
        return 1
    elif rank_b < rank_a:
        return -1
    else:
        for i in range(5):
            if card.index(a[0][i]) < card.index(b[0][i]):
                return 1
            elif card.index(a[0][i]) > card.index(b[0][i]):
                return -1


def get_rank(dct: dict) -> int:
    x = dct.values()
    if set(x) == {5}:
        return 0
    elif set(x) == {4, 1}:
        return 1
    elif set(x) == {3, 2}:
        return 2
    elif set(x) == {3, 1}:
        return 3
    elif Counter(x)[2] == 2:
        return 4
    elif Counter(x)[2] == 1:
        return 5
    else:
        return 6


sm = 0
for i, j in enumerate(map(lambda x: x[1], sorted(data, key=cmp_to_key(compare)))):
    sm += (i + 1) * int(j)
print(sm)


# Part 2
card = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']


def to_max_rank(card):
    if 'J' not in card:
        return card
    if card == 'JJJJJ':
        return 'AAAAA'
    c_no_j = Counter(card.replace('J', ""))
    highest_count = sorted(
        filter(lambda x: x[1] == c_no_j.most_common()[0][1], c_no_j.most_common()), key=cmp_to_key(lambda x, y: card.index(x[0]) - card.index(y[0])))

    return card.replace('J', highest_count[0][0])


def compare(a, b):
    rank_a = get_rank(dict(Counter(to_max_rank(a[0]))))
    rank_b = get_rank(dict(Counter(to_max_rank(b[0]))))
    if rank_a < rank_b:
        return 1
    elif rank_b < rank_a:
        return -1
    else:
        for i in range(5):
            if card.index(a[0][i]) < card.index(b[0][i]):
                return 1
            elif card.index(a[0][i]) > card.index(b[0][i]):
                return -1


sm = 0
for i, j in enumerate(map(lambda x: x[1], sorted(data, key=cmp_to_key(compare)))):
    sm += (i + 1) * int(j)
print(sm)
