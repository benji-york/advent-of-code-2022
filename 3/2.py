import fileinput


def value(item):
    if item.isupper():
        return ord(item) - ord('A') + 27
    else:
        return ord(item) - ord('a') + 1


total = 0
for index, line in enumerate(fileinput.FileInput()):
    if index % 3 == 0:
        items = []
    line = line.strip()
    items.append(set(line))
    if index % 3 == 2:
        common, = items[0] & items[1] & items[2]
        total += value(common)

print(total)
