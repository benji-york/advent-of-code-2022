import fileinput


def value(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


total = 0
for line in fileinput.FileInput():
    line = line.strip()
    num_items = len(line) // 2
    first = set(line[:num_items])
    second = set(line[num_items:])
    common, = first & second
    total += value(common)

print(total)
