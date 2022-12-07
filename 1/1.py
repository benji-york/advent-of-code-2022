import fileinput

counts = []
current_total = 0

for line in fileinput.FileInput():
    line = line.strip()
    if line:
        current_total += int(line)
    else:
        counts.append(current_total)
        current_total = 0


print(sum(sorted(counts)[-3:]))
