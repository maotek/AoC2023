import re
import math
from functools import reduce

with open('day8/day8.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]
seq = data[0]
lines = data[2:]

maps = {}

for i in lines:
    x = re.match(r'(\w+) = \((\w+), (\w+)\)', i)
    maps[x.group(1)] = [x.group(2), x.group(3)]


# Part 1
idx = 0
dest = 'AAA'
moves = 0
while dest != 'ZZZ':
    moves += 1
    dest = maps[dest][0] if seq[idx] == 'L' else maps[dest][1]
    idx = (idx + 1) % len(seq)

print(moves)


# Part 2
dests = list(filter(lambda x: x.endswith('A'), maps.keys()))

vars = []
for i in dests:
    idx = 0
    dest = i
    moves = 0
    while not dest.endswith('Z'):
        moves += 1
        dest = maps[dest][0] if seq[idx] == 'L' else maps[dest][1]
        idx = (idx + 1) % len(seq)
    vars.append(moves)


def reducer(a, b):
    gcd = math.gcd(a, b)
    return b*int(a / gcd)


print(reduce(reducer, vars))
