import re
import operator
from functools import reduce
with open('day3/day3.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

x = len(data[0])
y = len(data)


# Part 1
def check(a, b):
    c = list(filter(lambda d: 0 <= d[0] < x and 0 <= d[1] < y, [
             (a - 1, b - 1), (a - 1, b), (a - 1, b + 1), (a, b - 1), (a, b + 1), (a + 1, b - 1), (a + 1, b), (a + 1, b + 1)]))
    for i, j in c:
        if not data[i][j].isdigit() and data[i][j] != '.':
            return True
    return False


sm = 0
for i in range(len(data)):
    matches = re.finditer(r'\d+', data[i])
    for j in matches:
        if (check(i, j.start()) or check(i, j.end() - 1)):
            sm += int(j.group())
print(sm)


# Part 2
def check2(a, b):
    c = list(filter(lambda d: 0 <= d < y, [a - 1, a, a + 1]))
    adjacents = []
    for row in c:
        matches = re.finditer(r'\d+', data[row])
        for i in matches:
            if any([x in list(range(*i.span())) for x in [b-1, b, b+1]]):
                adjacents.append(i.group())
    if len(adjacents) == 2:
        return reduce(operator.mul, map(int, adjacents))
    return 0


sm = 0
for i in range(len(data)):
    matches = re.finditer(r'\*', data[i])
    for j in matches:
        sm += check2(i, j.start())
print(sm)
