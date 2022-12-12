import numpy as np
advent_input = open('day_7/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

# Part 1

dirs = {}
current = []
nr = 1

for i in advent_data:
    split = i.split(' ')
    name = split[-1]

    if split[1] == 'cd':
        if name in dirs.keys():
            name = name + str(nr)
            nr += 1

        if name == '..':
            ('..')
            current = current[:-1]
        else:
            dirs[name] = ''
            current.append(name)

    elif split[1] == 'ls':
        pass

    elif split[0] == 'dir':
        pass

    else:
        for dir in current:
            dirs[dir] = dirs.get(dir) + ' ' + split[0]


total = 0
sizes = []
# dirs = dict(reversed(list(dirs.items())))

for y, x in dirs.items():
    content = x.split(' ')[1:]
    size = 0

    for file in content:
        size += int(file)

    dirs[y] = size
    sizes.append(size)

    if size <= 100000:
        total += size


print(total)

# Part 2
freeing = 30000000 - (70000000 - sizes[0])
dir_size = 30000000


for size in sizes:
    if (size >= freeing) & (size < dir_size):
        dir_size = size


print(dir_size)
