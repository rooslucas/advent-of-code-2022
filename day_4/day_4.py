advent_input = open('day_4/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_data = [x.rstrip() for x in a_list]

places = [i.split(',') for i in advent_data]
places = [[i.split('-') for i in place] for place in places]

# Part 1
count = 0

# Readable solution part 1
for place in places:
    p1 = int(place[0][0])
    p2 = int(place[0][1])
    p3 = int(place[1][0])
    p4 = int(place[1][1])

    if ((p3 >= p1) & (p4 <= p2)) or ((p3 <= p1) & (p4 >= p2)):
        count += 1

# Shortes solution part 1
count2 = sum([1 for place in places if ((int(place[1][0]) >= int(place[0][0])) & (int(place[1][1]) <= int(
    place[0][1]))) or ((int(place[1][0]) <= int(place[0][0])) & (int(place[1][1]) >= int(place[0][1])))])

print(count2)

# Part 2
# Readable solution
count3 = 0
for place in places:
    p1 = int(place[0][0])
    p2 = int(place[0][1])
    p3 = int(place[1][0])
    p4 = int(place[1][1])

    if ((p3 >= p1) & (p3 <= p2)) or ((p4 >= p1) & (p4 <= p2)) or ((p1 >= p3) & (p1 <= p4)) or ((p2 >= p3) & (p2 <= p4)):
        count3 += 1

print(count3)

# Shortest solution
count4 = sum([1 for place in places if ((int(place[1][0]) >= int(place[0][0])) & (int(place[1][0]) <= int(place[0][1]))) or (
    (int(place[1][1]) >= int(place[0][0])) & (int(place[1][1]) <= int(place[0][1]))) or ((int(place[0][0]) >= int(place[1][0]))
                                                                                         & (int(place[0][0]) <= int(place[1][1]))) or ((int(place[0][1]) >= int(place[1][0])) & (int(place[0][1]) <= int(place[1][1])))])

print(count4)
