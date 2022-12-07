import fileinput

for line in fileinput.FileInput():
    line = line.strip()
    for i in range(14, len(line)):
        if len(set(line[i-14:i])) == 14:
            print(i)
            break
