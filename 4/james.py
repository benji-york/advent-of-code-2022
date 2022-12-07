with open("input.txt", "r") as f:
    data = [[[int(k) for k in j.split("-")] for j in i.strip().split(",")] for i in f.readlines()]

ranges = [[set(range(j[0], j[1] + 1)) for j in i] for i in data]

# Part One
contains = sum([1 if set.intersection(*i) in i else 0 for i in ranges])
assert contains == 431
contains = sum([set.intersection(*i) in i for i in ranges])
assert contains == 431
contains = sum(set.intersection(*i) in i for i in ranges)
assert contains == 431
print(contains)

# Part Two
overlaps = sum([0 if set.intersection(*i) == set() else 1 for i in ranges])
assert overlaps == 823
overlaps = sum(bool(set.intersection(*i)) for i in ranges)
assert overlaps == 823
print(overlaps)
