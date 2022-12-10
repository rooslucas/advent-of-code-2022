advent_input = open("day_10/input.txt")
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip().split(' ') for x in a_list]

x = 1
cycles = 0
signal_strength = 0
six_signals = [20, 60, 100, 140, 180, 220]
Flag = True

for command in advent_data:
    Flag = True
    if command[0] == 'noop':
        cycles += 1

    elif command[0] == 'addx':
        for i in range(2):
            cycles += 1
            if cycles in six_signals:
                signal_strength = signal_strength + (x * cycles)
                Flag = False

        x += int(command[1])

    if (cycles in six_signals) & Flag:
        signal_strength = signal_strength + (x * cycles)

print(signal_strength)

# Part 2

pos_x = [1, 2, 3]

cycles2 = 0
six_signals2 = [40, 80, 120, 160, 200, 240]
Flag = True
picture = []
current_line = ''
place = 1

for command in advent_data:
    Flag = True
    if command[0] == 'noop':
        cycles2 += 1
        if place in pos_x:
            current_line += '#'
        else:
            current_line += '.'
        place += 1

    elif command[0] == 'addx':
        for i in range(2):
            cycles2 += 1
            if place in pos_x:
                current_line += '#'
            else:
                current_line += '.'
            place += 1

            if cycles2 in six_signals2:
                picture.append(current_line)
                current_line = ''
                Flag = False
                place = 1

        pos_x = [(x + int(command[1])) for x in pos_x]

    if (cycles2 in six_signals2) & Flag:
        picture.append(current_line)
        current_line = ''
        place = 1

for lin in picture:
    print(lin)
