import fileinput

tree = {('/',): []}
contents = []
pwd = ['/']
for line in list(fileinput.FileInput()) + ['$ done']:
    line = line.strip()
    if line.startswith('$'):
        for item in contents:
            first, second = item.split()
            if first == 'dir':
                tree[tuple(pwd + [second])] = []
            else:
                path = pwd[:]
                while path:
                    tree[tuple(path)].append(int(first))
                    path.pop()
        contents = []
        _, command, *arguments = line.split()
        if command == 'cd':
            if arguments[0] == '..':
                pwd.pop()
            elif arguments[0] == '/':
                pwd = ['/']
            else:
                pwd.append(arguments[0])
    else:
        contents.append(line)

total = 0
for path, contents in tree.items():
    size = sum(contents)
    if size <= 100_000:
        total += size

print(total)
