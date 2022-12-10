advent_input = open("day_9/input.txt")
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip().split(' ') for x in a_list]


def check_distance(h, t):
    move = 0
    direction = 0
    if (h[0] != t[0]) & (h[0] > (t[0] + 1)):
        direction = 0
        move = 1
    elif (h[0] != t[0]) & (h[0] < (t[0] - 1)):
        direction = 0
        move = -1
    elif (h[1] != t[1]) & (h[1] > (t[1] + 1)):
        direction = 1
        move = 1
    elif (h[1] != t[1]) & (h[1] < (t[1] - 1)):
        direction = 1
        move = -1

    return move, direction


# Part 1
pos_h = [0, 0]
pos_t = [0, 0]
visited = []

for i in advent_data:
    for x in range(int(i[1])):
        if i[0] == 'L':
            pos_h[0] -= 1
        elif i[0] == 'R':
            pos_h[0] += 1
        elif i[0] == 'D':
            pos_h[1] -= 1
        elif i[0] == 'U':
            pos_h[1] += 1

        if (pos_h[0] != pos_t[0]) & (pos_h[1] != pos_t[1]):
            if pos_h[0] == (pos_t[0] + 2):
                pos_t[0] += 1
                if pos_h[1] == (pos_t[1] + 1):
                    pos_t[1] += 1
                elif pos_h[1] == (pos_t[1] - 1):
                    pos_t[1] -= 1
            elif pos_h[0] == (pos_t[0] - 2):
                pos_t[0] -= 1
                if pos_h[1] == (pos_t[1] + 1):
                    pos_t[1] += 1
                elif pos_h[1] == (pos_t[1] - 1):
                    pos_t[1] -= 1

            if pos_h[1] == (pos_t[1] + 2):
                pos_t[1] += 1
                if pos_h[0] == (pos_t[0] + 1):
                    pos_t[0] += 1
                elif pos_h[0] == (pos_t[0] - 1):
                    pos_t[0] -= 1

            elif pos_h[1] == (pos_t[1] - 2):
                pos_t[1] -= 1
                if pos_h[0] == (pos_t[0] + 1):
                    pos_t[0] += 1
                elif pos_h[0] == (pos_t[0] - 1):
                    pos_t[0] -= 1

        else:
            m, d = check_distance(pos_h, pos_t)
            pos_t[d] += m

        if pos_t not in visited:
            visited.append(pos_t.copy())


print(len(visited))

# Part 2


def check_distance09(pos_h, pos_t):
    if (pos_h[0] != pos_t[0]) & (pos_h[1] != pos_t[1]):
        if pos_h[0] == (pos_t[0] + 2):
            pos_t[0] += 1
            if pos_h[1] == (pos_t[1] + 1):
                pos_t[1] += 1
            elif pos_h[1] == (pos_t[1] - 1):
                pos_t[1] -= 1
        elif pos_h[0] == (pos_t[0] - 2):
            pos_t[0] -= 1
            if pos_h[1] == (pos_t[1] + 1):
                pos_t[1] += 1
            elif pos_h[1] == (pos_t[1] - 1):
                pos_t[1] -= 1

        elif pos_h[1] == (pos_t[1] + 2):
            pos_t[1] += 1
            if pos_h[0] == (pos_t[0] + 1):
                pos_t[0] += 1
            elif pos_h[0] == (pos_t[0] - 1):
                pos_t[0] -= 1

        elif pos_h[1] == (pos_t[1] - 2):
            pos_t[1] -= 1
            if pos_h[0] == (pos_t[0] + 1):
                pos_t[0] += 1
            elif pos_h[0] == (pos_t[0] - 1):
                pos_t[0] -= 1

    else:
        m, d = check_distance(pos_h, pos_t)
        pos_t[d] += m

    return pos_t


pos_h = [0, 0]
pos_1 = [0, 0]
pos_2 = [0, 0]
pos_3 = [0, 0]
pos_4 = [0, 0]
pos_5 = [0, 0]
pos_6 = [0, 0]
pos_7 = [0, 0]
pos_8 = [0, 0]
pos_t = [0, 0]
visited2 = []

for i in advent_data:
    # print(i)
    for x in range(int(i[1])):
        if i[0] == 'L':
            pos_h[0] -= 1
        elif i[0] == 'R':
            pos_h[0] += 1
        elif i[0] == 'D':
            pos_h[1] -= 1
        elif i[0] == 'U':
            pos_h[1] += 1

        pos_1 = check_distance09(pos_h, pos_1)
        pos_2 = check_distance09(pos_1, pos_2)
        pos_3 = check_distance09(pos_2, pos_3)
        pos_4 = check_distance09(pos_3, pos_4)
        pos_5 = check_distance09(pos_4, pos_5)
        pos_6 = check_distance09(pos_5, pos_6)
        pos_7 = check_distance09(pos_6, pos_7)
        pos_8 = check_distance09(pos_7, pos_8)
        pos_t = check_distance09(pos_8, pos_t)

        # print(pos_h, pos_1, pos_2, pos_3, pos_4,
        #   pos_5, pos_6, pos_7, pos_8, pos_t)

        if pos_t not in visited2:
            visited2.append(pos_t.copy())

print(len(visited2))
