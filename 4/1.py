import fileinput


def expand(description: str) -> set[int]:
    """Given a textual description of a set of integers, create that set."""
    start, end = map(int, description.split('-'))
    return set(range(start, end + 1))


count = 0
for line in fileinput.FileInput():
    first, second = map(expand, line.strip().split(','))
    if first.issubset(second) or second.issubset(first):
        count += 1

print(count)
