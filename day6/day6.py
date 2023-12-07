from functools import *

with open('day6/day6.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

times = list(map(int,  data[0].split()[1:]))
recs = list(map(int,  data[1].split()[1:]))

res = []

for i in range(len(times)):
    time = times[i]
    rec = recs[i]
    wins = 0
    for i in range(time):
        if (time - i) * i > rec:
            wins += 1
    res.append(wins)

print(reduce(lambda x, y: x * y, res))

time = int(''.join(data[0].split()[1:]))
rec = int(''.join(data[1].split()[1:]))
wins = 0
for i in range(time):
    if (time - i) * i > rec:
        wins += 1
print(wins)
