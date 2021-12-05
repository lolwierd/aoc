def take_input():
    inputs = []
    with open("input.txt", "r") as f:
        for line in f:
            inputs.append(int(line.rstrip()))
    return inputs


def sol_1(depths):
    incr_count = 0
    for index in range(1, len(depths)):
        if depths[index] > depths[index-1]:
            incr_count += 1
    return incr_count


def sol_2(depths):
    transformed_depths = []
    for index in range(2, len(depths)):
        transformed_depths.append(
            depths[index] + depths[index - 1] + depths[index - 2])
    return sol_1(transformed_depths)


def main():
    depths = take_input()
    print(sol_1(depths))
    print(sol_2(depths))


if __name__ == "__main__":
    main()
