import numpy as np
import pandas as pd
import copy

advent_input = open('day_5/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

positions = [[], [], [], [], [], [], [], [], []]
for i in advent_data[0:8]:
    l = i.replace('    ', ' ').split(' ')
    index = 0

    for q in l:
        if q != '':
            positions[index].insert(0, q)
        index += 1


# Part 1
for move in advent_data[10:]:
    move = move.replace('move ', '').replace(
        ' from ', ' ').replace(' to ', ' ').split(' ')
    for i in range(int(move[0])):
        old_list = positions[int(move[1]) - 1]

        new_list = positions[int(move[2]) - 1]

        new_list.append(old_list[-1])
        del old_list[-1]


# print('\n')
# for l in positions:
#     print(l[-1])

# Part 2

positions2 = [[], [], [], [], [], [], [], [], []]
for i in advent_data[0:8]:
    l = i.replace('    ', ' ').split(' ')
    index = 0

    for q in l:
        if q != '':
            positions2[index].insert(0, q)
        index += 1

for move in advent_data[10:]:
    move = move.replace('move ', '').replace(
        ' from ', ' ').replace(' to ', ' ').split(' ')

    old_list = positions2[int(move[1]) - 1]
    new_list = positions2[int(move[2]) - 1]
    values = old_list[-(int(move[0])):]

    for value in values:
        new_list.append(value)

    del old_list[-(int(move[0])):]

print('\n')
for l in positions2:
    print(l[-1])
