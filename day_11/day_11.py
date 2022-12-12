import re
from tqdm import tqdm
import gc

advent_input = open('day_11/input.txt')
a_list = list(advent_input)
advent_input.close()
advent_input = [x.rstrip() for x in a_list]

monkey_data = [advent_input[x:x+6] for x in range(0, len(advent_input), 7)]


class Monkey:
    def __init__(self, starting_items, operation, test, true, false, inspection_items):
        self.starting_items = starting_items
        self.operation = operation
        self.test = test
        self.true = true
        self.false = false
        self.inspection_items = inspection_items

    def operation_execution(self, old):
        if self.operation[2] == 'old':
            value = int(old)
        else:
            value = int(self.operation[2])

        if self.operation[1] == '*':
            return (int(old) * value)
        elif self.operation[1] == '+':
            return (int(old) + value)

    def output(self, old):
        new = self.operation_execution(old)  # // 3 For part 1
        self.inspection_items += 1

        if new % int(self.test[0]) == 0:
            # return (new), int(self.true[0])  # for part 1
            # -(-new // int(self.test[0])), int(self.true[0])
            return new, int(self.true[0])
        else:
            return new, int(self.false[0])
            # return int(self.test[0]) - (int(new) % int(self.test[0])), int(self.false[0])
            # return new % int(self.test[0]), int(self.false[0])


number_extract_pattern = "\\d+"
monkeys = []

for monkey in monkey_data:
    operation = monkey[2].split(' ')[5:]
    monkey = [re.findall(number_extract_pattern, item) for item in monkey]
    monkey[2] = operation
    monkeys.append(Monkey(monkey[1], monkey[2],
                   monkey[3], monkey[4], monkey[5], 0))


for round in tqdm(range(0, 10000), desc='tqdm() Progress Bar'):
    gc.collect()
    for monkey in monkeys:
        delete = []

        for item in monkey.starting_items:
            value, index = monkey.output(item)
            monkeys[index].starting_items.append(value)
            delete.append(item)

        monkey.starting_items = [
            elem for elem in monkey.starting_items if elem not in delete]


for monkey in monkeys:
    print(monkey.inspection_items)

# print(254 * 263)

# Part 2
