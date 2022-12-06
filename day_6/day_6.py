# start of packet marker is 4 different characters
import re

advent_input = open('day_6/input.txt')
a_list = list(advent_input)
advent_input.close()

# Part 1
previous = ''
for letter in a_list[0]:
    if letter not in previous:
        previous += letter
    else:
        previouss = previous[previous.index(letter)+1:]
        previous = previouss + letter

    if len(previous) == 4:
        print(a_list[0].index(previous) + 4)
        break

# Part 2
previous = ''
for letter in a_list[0]:
    if letter not in previous:
        previous += letter
    else:
        previouss = previous[previous.index(letter)+1:]
        previous = previouss + letter

    if len(previous) == 14:
        print(a_list[0].index(previous) + 14)
        break
