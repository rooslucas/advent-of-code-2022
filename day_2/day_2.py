advent_input = open('day_2/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

# Part 1
win = sum([6 for i in advent_data if (i == 'A Y')
          or (i == 'B Z') or (i == 'C X')])
draw = sum([3 for i in advent_data if (i == 'A X')
           or (i == 'B Y') or (i == 'C Z')])
loss = sum([0 for i in advent_data if (i == 'A Z')
           or (i == 'B X') or (i == 'C Y')])

rock = sum([1 for i in advent_data if 'X' in i])
paper = sum([2 for i in advent_data if 'Y' in i])
scissors = sum([3 for i in advent_data if 'Z' in i])

print(win+draw+loss+scissors+paper+rock)

# Part 2
# X means lose (0), Y means draw (3), Z means win (6)
lose = [i for i in advent_data if 'X' in i]
draw = [i for i in advent_data if 'Y' in i]
win = [i for i in advent_data if 'Z' in i]

rocks = sum([1 for i in lose if ('B' in i)]) + \
    sum([1 for i in draw if 'A' in i]) + sum([1 for i in win if 'C' in i])
papers = sum([2 for i in lose if 'C' in i]) + \
    sum([2 for i in draw if 'B' in i]) + len([2 for i in win if 'A' in i])
scissorss = sum([3 for i in lose if 'A' in i]) + \
    sum([3 for i in draw if 'C' in i]) + sum([3 for i in win if 'B' in i])

print(rocks + papers + scissorss + (len(lose)*0) +
      (len(draw) * 3) + (len(win) * 6))
