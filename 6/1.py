import fileinput

for line in fileinput.FileInput():
    line = line.strip()
    for i in range(4, len(line)):
        if len(set(line[i-4:i])) == 4:
            print(i)
            break
