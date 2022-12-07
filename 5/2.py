import fileinput

moves = []
num_stacks = None
stack_lines = []
for line in fileinput.FileInput():
    if line.startswith('move'):
        moves.append(map(int, line.split()[1::2]))
    elif len(line) > 1 and line[1] == '1':
        num_stacks = int(line.strip().rsplit(' ', 1)[-1])
        stacks = [[] for x in range(num_stacks)]
        for line in stack_lines:
            for index, item in enumerate(line[1::4]):
                if item.strip():
                    stacks[index].append(item)
    elif num_stacks is None:
        stack_lines.insert(0, line)

for count, source, destination in moves:
    source -= 1
    destination -= 1
    stacks[destination].extend(stacks[source][-count:])
    del stacks[source][-count:]

print(''.join(stack[-1] for stack in stacks))
