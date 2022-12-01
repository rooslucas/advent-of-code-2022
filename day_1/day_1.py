advent_input = open('day_1/data1.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]
# print(advent_data)

# Part 1
max = 0
count = 0
for i in advent_data:
    if i != '':
        count += int(i)
    elif i == '':
        if count > max:
            max = count
        count = 0

print(max)

# Part 2
elfs = []
count = 0
for i in advent_data:
    if i != '':
        count += int(i)
    elif i == '':
        elfs.append(count)
        count = 0

print(elfs)
elfs.sort(reverse=True)
print(elfs[0:3])
print(elfs[0]+elfs[1]+elfs[2])
