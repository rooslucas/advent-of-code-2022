import pandas as pd

advent_input = open('day_8/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

df = pd.DataFrame(columns=range(len(advent_data[0])))

for i in range(len(advent_data)):
    df.loc[i] = [int(i) for i in list(advent_data[i])]

# Part 1
counter = 0

for (column_name, column_data) in df.iteritems():
    for i in range(len(column_data)):
        column_check = list(column_data[i] > column_data)
        row_check = (column_data[i] > df.loc[[i]]).values[0]

        if (False not in column_check[:i]) or (False not in column_check[i+1:]) or (False not in row_check[:int(column_name)]) or (False not in row_check[int(column_name)+1:]):
            counter += 1

print(counter)

# Part 2
max = 0

for (column_name, column_data) in df.iteritems():
    for i in range(len(column_data)):
        column_check = list(column_data[i] > column_data)
        row_check = (column_data[i] > df.loc[[i]]).values[0].tolist()
        row_check = list(map(int, row_check))
        column_check = list(map(int, column_check))

        if (0 not in column_check[:i]):
            up = len(column_check[:i])
        else:
            up = list(reversed(column_check[:i])).index(0) + 1

        if (0 not in column_check[i+1:]):
            down = len(column_check[i+1:])
        else:
            down = (column_check[i+1:]).index(0) + 1

        if (0 not in row_check[:int(column_name)]):
            left = len(row_check[:int(column_name)])
        else:
            left = list(reversed(row_check[:int(column_name)])).index(0) + 1

        if (0 not in row_check[int(column_name)+1:]):
            right = len(row_check[int(column_name)+1:])
        else:
            right = (row_check[int(column_name)+1:]).index(0) + 1

        score = left*right*up*down

        if (score > max) & (i > 0) & (int(column_name) > 0):
            max = score

print(max)
