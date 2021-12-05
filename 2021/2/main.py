from os import DirEntry


def take_input():
    inputs = []
    with open("input.txt", "r") as f:
        for line in f:
            inputs.append(line.rstrip())
    return inputs


def get_direction(command):
    return command.split(' ')[0]


def get_magnitude(command):
    return int(command.split(' ')[1])


def sol_1(commands):
    horizontal = 0
    depth = 0
    for command in commands:
        direction, magnitude = get_direction(command), get_magnitude(command)
        if direction == "forward":
            horizontal += magnitude
        elif direction == "up":
            depth -= magnitude
        elif direction == "down":
            depth += magnitude
    return horizontal * depth


def sol_2(commands):
    aim = 0
    horizontal = 0
    depth = 0
    for command in commands:
        direction, magnitude = get_direction(command), get_magnitude(command)
        if direction == "forward":
            horizontal += magnitude
            depth += aim*magnitude
        elif direction == "up":
            aim -= magnitude
        elif direction == "down":
            aim += magnitude
    return horizontal * depth


def main():
    commands = take_input()
    print(sol_1(commands))
    print(sol_2(commands))


if __name__ == "__main__":
    main()
