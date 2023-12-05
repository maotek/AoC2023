with open('day5/day5.txt', 'r') as f:
    data = f.read().split("\n\n")

seeds = list(map(int, data[0].split(": ")[1].split()))

maps = []
for i in data[1:]:
    mappings = [list(map(int, x.split()))
                for x in i.split(":\n")[1].split("\n")]
    maps.append(mappings)

res = []
for i in seeds:
    num = i
    for j in maps:
        for k in j:
            if num in range(k[1], k[1] + k[2]):
                num = num + (k[0] - k[1])
                break
    res.append(num)
print(min(res))


# Part 2
maps = []
for i in data[1:]:
    mappings = [list(map(int, x.split()))
                for x in i.split(":\n")[1].split("\n")]
    mappings = list(
        map(lambda x: (x[0] - x[1], x[1], x[1] + x[2] - 1), mappings))
    maps.append(mappings)
pairs = list(zip(*(iter(seeds),) * 2))


def divide_conquer(start, end, mps):
    if len(mps) == 0:
        return [(start, end)]
    ranges = []
    i = mps[0]
    if start >= i[1] and end <= i[2]:
        ranges.append((start + i[0], end + i[0]))
    elif i[1] <= start <= i[2] and end > i[2]:
        ranges.append((start + i[0], i[2] + i[0]))
        ranges.extend(divide_conquer(i[2]+1, end, mps[1:]))
    elif start < i[1] and i[1] <= end <= i[2]:
        ranges.append((i[1] + i[0], end + i[0]))
        ranges.extend(divide_conquer(start, i[1] - 1, mps[1:]))
    elif start < i[1] and end > i[2]:
        ranges.extend(divide_conquer(start, i[1] - 1, mps[1:]))
        ranges.extend(divide_conquer(i[2]+1, end, mps[1:]))
        ranges.append((i[1] + i[0], i[2] + i[0]))
    else:
        ranges.extend(divide_conquer(start, end, mps[1:]))
    return ranges


tot_ranges = []
for start, end in pairs:
    ranges = [(start, end + start - 1)]
    for i in maps:
        new_ranges = []
        for j, k in ranges:
            new_ranges.extend(divide_conquer(j, k, i))
        ranges = new_ranges
    tot_ranges.extend(ranges)

print(min(tot_ranges, key=lambda x: x[0])[0])
