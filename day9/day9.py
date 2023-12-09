with open('day9/day9.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]
data = [list(map(int, i.split())) for i in data]


def difs(lst):
    res = []
    for i in range(1, len(lst)):
        res.append(lst[i] - lst[i-1])
    return res


sm = 0
for i in data:
    lists = [i, difs(i)]
    while not all([x == 0 for x in lists[-1]]):
        lists.append(difs(lists[-1]))

    num = 0
    print(lists)
    for j in range(len(lists)-1, -1, -1):
        num = lists[j][-1] + num
    sm += num
print(sm)


sm = 0
for i in data:
    lists = [i, difs(i)]
    while not all([x == 0 for x in lists[-1]]):
        lists.append(difs(lists[-1]))
    num = 0
    for j in range(len(lists)-1, -1, -1):
        num = lists[j][0] - num
    sm += num
print(sm)
