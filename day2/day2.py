import re

with open('day2/day2.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

red, green, blue = 12, 13, 14

# Part 1
sm = 0
for i in data:
    a = i.split(": ")
    id = int(a[0].split(" ")[1])
    r = map(int, re.findall(r'(\d+)\s+red', a[1]))
    g = map(int, re.findall(r'(\d+)\s+green', a[1]))
    b = map(int, re.findall(r'(\d+)\s+blue', a[1]))
    if all([n <= red for n in r]) and all([n <= green for n in g]) and all([n <= blue for n in b]):
        sm += id
print(sm)


# Part 2
sm = 0
for i in data:
    a = i.split(": ")
    id = int(a[0].split(" ")[1])
    r = max(map(int, re.findall(r'(\d+)\s+red', a[1])))
    g = max(map(int, re.findall(r'(\d+)\s+green', a[1])))
    b = max(map(int, re.findall(r'(\d+)\s+blue', a[1])))
    sm += r * g * b
print(sm)
