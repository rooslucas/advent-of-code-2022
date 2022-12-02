advent_input = open('day_2/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

# Part 1
win = len([i for i in advent_data if (i == 'A Y')
          or (i == 'B Z') or (i == 'C X')]) * 6
draw = len([i for i in advent_data if (i == 'A X')
           or (i == 'B Y') or (i == 'C Z')]) * 3
loss = len([i for i in advent_data if (i == 'A Z')
           or (i == 'B X') or (i == 'C Y')]) * 0
rock = len([i for i in advent_data if 'X' in i]) * 1
paper = len([i for i in advent_data if 'Y' in i]) * 2
scissors = len([i for i in advent_data if 'Z' in i]) * 3

print(win+draw+loss+scissors+paper+rock)

# Part 2
# X means lose (0), Y means draw (3), Z means win (6)
lose = [i for i in advent_data if 'X' in i]
draw = [i for i in advent_data if 'Y' in i]
win = [i for i in advent_data if 'Z' in i]

rocks = (len([i for i in lose if 'B' in i]) +
         len([i for i in draw if 'A' in i]) + len([i for i in win if 'C' in i])) * 1
papers = (len([i for i in lose if 'C' in i]) +
          len([i for i in draw if 'B' in i]) + len([i for i in win if 'A' in i])) * 2
scissorss = (len([i for i in lose if 'A' in i]) +
             len([i for i in draw if 'C' in i]) + len([i for i in win if 'B' in i])) * 3

print(rocks + papers + scissorss + (len(lose)*0) +
      (len(draw) * 3) + (len(win) * 6))
