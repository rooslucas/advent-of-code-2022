import numpy as np

advent_input = open('day_3/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Part 1
total = 0
for backpack in advent_data:
    part1, part2 = set(backpack[:int(len(backpack)/2)]
                       ), set(backpack[int(len(backpack)/2):])
    total += (letters.index(list(part1.intersection(part2))[0]) + 1)

print(total)

# Part 2
total2 = 0

groups = np.arange(0, len(advent_data), 3)

for group in groups:
    elf1 = set(advent_data[group])
    elf2 = set(advent_data[group+1])
    elf3 = set(advent_data[group+2])
    total2 += (letters.index(list(elf1.intersection(elf2, elf3))[0]) + 1)

print(total2)
