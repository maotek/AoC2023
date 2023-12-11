import numpy as np

with open('day11/day11.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]

x, y = len(data[0]), len(data)

# Part 1
matrix = np.array(list(map(list, data)))
cols = np.where(np.all(matrix == '.', axis=0))[0]
rows = np.where(np.all(matrix == '.', axis=1))[0]

for i in range(len(rows)):
    matrix = np.insert(matrix, rows[i] + i + 1, '.' * x, axis=0)
for i in range(len(cols)):
    matrix = np.insert(matrix, cols[i] + i + 1, '.' * y, axis=1)

y_coords, x_coords = np.where(matrix == '#')
coords = list(zip(x_coords, y_coords))


sm = 0

for a_x, a_y in coords:
    for b_x, b_y in coords:
        if a_x == b_x and a_y == b_y:
            continue
        res = (abs(b_y - a_y) + abs(b_x - a_x))
        sm += res
print(sm/2)


# Part 2
sm = 0
matrix = np.array(list(map(list, data)))
cols = np.where(np.all(matrix == '.', axis=0))[0]
rows = np.where(np.all(matrix == '.', axis=1))[0]
y_coords, x_coords = np.where(matrix == '#')
coords = list(zip(x_coords, y_coords))

mult = 1000000
for a_x, a_y in coords:
    for b_x, b_y in coords:
        if a_x == b_x and a_y == b_y:
            continue
        a = 0
        for i in rows:
            if a_y < i < b_y or b_y < i < a_y:
                a += 1
        b = 0
        for i in cols:
            if a_x < i < b_x or b_x < i < a_x:
                b += 1
        sm += (abs(b_y - a_y) - a + (a * mult) +
               abs(b_x - a_x) - b + (b * mult))
print(sm/2)
