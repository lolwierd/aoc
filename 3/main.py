# First Thoughts:
# Every line can be represented as a progression and the numbers are occurances of trees.
# ......##....#...#..#.#....#....
# (7, 8, 13, 17, 20, 22, 27) + 31
import copy


def repeater(line):
    repeated_line = copy.copy(line)
    for number in line:
        repeated_line.append(number+31)
    return repeated_line


def is_tree(line, position):
    # print(f"Is Tree called for position {position} for line {line}")
    position = position % 31
    return line.count(position) > 0


def parse_input():
    parsed_inputs = []
    with open('input.txt', 'r') as file:
        for line in file.readlines():
            parsed_line = []
            for index, char in enumerate(list(line)):
                if char == "#":
                    parsed_line.append(index)
            parsed_inputs.append(parsed_line)
    return parsed_inputs


def solve(parsed_inputs):
    position = 3
    num_trees = 0
    enum = enumerate(parsed_inputs)
    # To skip the first iteration
    next(enum, None)
    for index, parsed_input in enum:
        if is_tree(parsed_input, position):
            # print(f"Tree in row: {index}")
            num_trees += 1
        position += 3
    return num_trees


def solve_1(parsed_inputs):
    position = 1
    num_trees = 0
    enum = enumerate(parsed_inputs)
    # To skip the first iteration
    next(enum, None)
    for index, parsed_input in enum:
        if is_tree(parsed_input, position):
            # print(f"Tree in row: {index}")
            num_trees += 1
        position += 1
    return num_trees


def solve_2(parsed_inputs):
    position = 5
    num_trees = 0
    enum = enumerate(parsed_inputs)
    # To skip the first iteration
    next(enum, None)
    for index, parsed_input in enum:
        if is_tree(parsed_input, position):
            # print(f"Tree in row: {index}")
            num_trees += 1
        position += 5
    return num_trees


def solve_3(parsed_inputs):
    position = 7
    num_trees = 0
    enum = enumerate(parsed_inputs)
    # To skip the first iteration
    next(enum, None)
    for index, parsed_input in enum:
        if is_tree(parsed_input, position):
            # print(f"Tree in row: {index}")
            num_trees += 1
        position += 7
    return num_trees


def solve_4(parsed_inputs):
    position = 1
    num_trees = 0
    enum = enumerate(parsed_inputs)
    # To skip the first iteration
    next(enum, None)
    next(enum, None)
    for index, parsed_input in enum:
        next(enum, None)
        if is_tree(parsed_input, position):
            # print(f"Tree in row: {index}")
            num_trees += 1
        position += 1
    return num_trees


def answer(parsed_inputs):
    return solve(parsed_inputs) * solve_1(parsed_inputs) * solve_2(parsed_inputs) * solve_3(parsed_inputs) * solve_4(parsed_inputs)


def main():
    parsed_inputs = parse_input()
    print(answer(parsed_inputs))


if __name__ == "__main__":
    main()
