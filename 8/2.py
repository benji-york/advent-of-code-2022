import fileinput
import itertools

def half_score(trees, height):
    score = 0
    for tree in trees:
        score += 1
        if tree >= height:
            break
    return score


def score(trees, index):
    height = trees[index]
    return (
        half_score(trees[index+1:], height) *
        half_score(reversed(trees[:index]), height))


forest_rows = []
for line in fileinput.FileInput():
    line = line.strip()
    forest_rows.append(list(map(int, line)))

forest_columns = list(zip(*forest_rows))

scores = []
for y in range(len(forest_rows)):
    for x in range(len(forest_columns)):
        scores.append(score(forest_rows[y], x) * score(forest_columns[x], y))

print(max(scores))
