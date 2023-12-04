with open('day4/day4.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

# Part 1
sm = 0
for i in data:
    x = i.split(': ')
    cards = x[1].split(" | ")[1].split()
    win = x[1].split(" | ")[0].split()
    l = len([n for n in cards if n in win])
    sm += 2 ** (l - 1) if l != 0 else 0
print(sm)

# Part 2
dct = {n: 1 for n in range(1, len(data)+1)}
for i in range(len(data)):
    x = data[i].split(': ')
    cards = x[1].split(" | ")[1].split()
    win = x[1].split(" | ")[0].split()
    l = len([n for n in cards if n in win])
    for j in range(i+2, i + l + 2):
        dct[j] += dct[i+1]
print(sum(dct.values()))
