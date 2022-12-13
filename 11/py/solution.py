import sys
import json
import copy

'''
For operation "old * 19", dict like:
{
    "val1": "old",
    "val2": "19",
    "op": "*
}
'''

class Monkey:
    def __init__(self, starting_items, operation, test, true_op, false_op):
        self.items = starting_items
        self.operation = operation
        self.test = test
        self.true_op = true_op
        self.false_op = false_op

    def add_item(self, item):
        self.items.append(item)

    
def parseInput(fName):
    with open(fName, 'r') as f:
        input = f.readlines()
        input = [l.rstrip().lstrip() for l in input]
    
    monkeys = []
    for i in range(0, len(input), 7):
        starting_items = input[i+1].split(': ')[1].split(' ')
        starting_items = list(map(lambda x: int(x.replace(',','')), starting_items))
        operation_raw = input[i+2].split(' = ')[1].split(' ')
        operation = {
            "val1": operation_raw[0],
            "op": operation_raw[1],
            "val2": operation_raw[2]
        }
        test = int(input[i+3].split(' ')[3])
        true_monkey = int(input[i+4].split(' ')[5])
        false_monkey = int(input[i+5].split(' ')[5])
        monkey = Monkey(starting_items, operation, test, true_monkey, false_monkey)
        monkeys.append(monkey)
    return monkeys

def calcNewWorry(old, op):
    if (op["val2"] == "old"):
        if (op["op"] == "*"):
            return old*old
        else:
            return old+old
    elif (op["op"] == "*"):
        return old*int(op["val2"])
    elif (op["op"] == "+"):
        return old+int(op["val2"])

def solvePart1(input):
    monkey_inspections = [0 for i in input]
    for round in range(20):
        for m, monkey in enumerate(input):
            starting_item_len = len(monkey.items)
            for i in range(starting_item_len):
                # count the monkey's inspection
                monkey_inspections[m] += 1
                # get the item
                item = monkey.items.pop(0)
                # calculate the new worry
                item = int(calcNewWorry(item, monkey.operation) / 3)
                # test the item
                if (item % monkey.test == 0):
                    input[monkey.true_op].add_item(item)
                else:
                    input[monkey.false_op].add_item(item)
        # print(f"Round #: {round}")
        # for i, monkey in enumerate(input):
        #     print(f"Monkey: {i}, Items: {monkey.items}")
    monkey_inspections.sort()
    return monkey_inspections[-1] * monkey_inspections[-2]


def solvePart2(input):
    # calculate the combined divisor for all monkey's tests
    combined_divisor = 1
    for monkey in input:
        combined_divisor *= monkey.test

    monkey_inspections = [0 for i in input]
    for round in range(10000):
        for m, monkey in enumerate(input):
            starting_item_len = len(monkey.items)
            for i in range(starting_item_len):
                # count the monkey's inspection
                monkey_inspections[m] += 1
                # get the item
                item = monkey.items.pop(0)
                # calculate the new worry
                item = int(calcNewWorry(item, monkey.operation)) % combined_divisor
                # test the item
                if (item % monkey.test == 0):
                    input[monkey.true_op].add_item(item)
                else:
                    input[monkey.false_op].add_item(item)
        # print(f"Round #: {round}")
        # for i, monkey in enumerate(input):
        #     print(f"Monkey: {i}, Items: {monkey.items}")
    monkey_inspections.sort()
    return monkey_inspections[-1] * monkey_inspections[-2]
    

input = parseInput(sys.argv[1])
part1soln = solvePart1(copy.deepcopy(input))
print(f"Part 1 solution: {part1soln}")
part2soln = solvePart2(copy.deepcopy(input))
print(f"Part 2 solution: {part2soln}")