import fileinput


def is_visible(trees, index):
    height = trees[index]
    return (
        index == 0 or
        index == len(trees) - 1 or
        all([t < height for t in trees[:index]]) or
        all([t < height for t in trees[index+1:]]))


forest_rows = []
for line in fileinput.FileInput():
    line = line.strip()
    forest_rows.append(list(map(int, line)))

forest_columns = list(zip(*forest_rows))

total = 0
for y in range(len(forest_rows)):
    for x in range(len(forest_columns)):
        total += (
            is_visible(forest_rows[y], x) or
            is_visible(forest_columns[x], y))

print(total)
