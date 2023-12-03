import string

with open('day1/day1.txt', 'r') as f:
    data = [x.strip() for x in f.readlines()]


# Part 1
class Del:
    def __init__(self, keep=string.digits):
        self.comp = dict((ord(c), c) for c in keep)

    def __getitem__(self, k):
        return self.comp.get(k)


DD = Del()
print(sum([int(i.translate(DD)[0] + i.translate(DD)[-1]) for i in data]))


# Part 2
help_dict = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

sm = 0
for i in data:
    first, last = 0, 0
    for l in range(len(i)):
        if (i[l].isdigit()):
            if (first == 0):
                first = i[l]
            last = i[l]
        for m in help_dict.keys():
            if (i[l: l+len(m)] == m):
                if (first == 0):
                    first = help_dict[m]
                last = help_dict[m]
    sm += int(first + last)

print(sm)
