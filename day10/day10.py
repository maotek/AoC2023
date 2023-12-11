with open('day10/day10.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]
x = len(data[0])
y = len(data)
s_x, y_x = -1, -1
for a, b in enumerate(data):
    if 'S' in b:
        s_y = a
        s_x = b.index('S')
        break


def next_pos(cur_x, cur_y, prev_x, prev_y):
    diff_x, diff_y = cur_x - prev_x, cur_y - prev_y
    next_x, next_y = cur_x, cur_y
    symbol = data[cur_y][cur_x]
    if symbol == '|':
        next_y = cur_y + diff_y
    elif symbol == '-':
        next_x = cur_x + diff_x
    elif symbol == 'L':
        next_x, next_y = cur_x + diff_y, cur_y + diff_x
    elif symbol == 'J':
        next_x, next_y = cur_x - diff_y, cur_y - diff_x
    elif symbol == '7':
        next_x, next_y = cur_x + diff_y, cur_y + diff_x
    elif symbol == 'F':
        next_x, next_y = cur_x - diff_y, cur_y - diff_x
    return next_x, next_y


vertices = [(s_x, s_y)]
points = [(s_x, s_y)]

# Part 1
count = 1
cur_x, cur_y = (s_x - 1, s_y)  # Hardcoded start point
prev_x, prev_y = s_x, s_y
while data[cur_y][cur_x] != 'S':
    if data[cur_y][cur_x] in 'LJ7F':
        vertices.append((cur_x, cur_y))
    points.append((cur_x, cur_y))
    cur_x_tmp, cur_y_tmp = next_pos(cur_x, cur_y, prev_x, prev_y)
    prev_x, prev_y = cur_x, cur_y
    cur_x, cur_y = cur_x_tmp, cur_y_tmp
    count += 1
vertices.append((s_x, s_y))
print(count/2)


# Part 2
def check_is_in_polygon(x, y, vertices):
    cnt = 0
    for i in range(len(vertices) - 1):
        v1 = vertices[i]
        v2 = vertices[i+1]
        cnt += check_intersect(x, y, v1, v2)
    return cnt % 2 != 0


def check_intersect(x, y, v1, v2):
    if y == v1[1] and y == v2[1] and x < v1[0] and x < v2[0]:
        if set([data[v1[1]][v1[0]], data[v2[1]][v2[0]]]) in [{'L', '7'}, {'F', 'J'}]:
            return 1
        return 2

    if x < v1[0] and x < v2[0] and (v1[1] < y < v2[1] or v2[1] < y < v1[1]):
        return 1
    return 0


dots = []
count = 0

for i in range(x):
    for j in range(y):
        if (i, j) not in points:
            dots.append((i, j))

for i, j in dots:
    if check_is_in_polygon(i, j, vertices):
        count += 1
print(count)
