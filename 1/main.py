def take_input():
    inputs = []
    with open("input.txt", "r") as f:
        for line in f:
            inputs.append(int(line.rstrip()))
    return inputs


# Logic can't get any dumber
def main_logic_one(list_num):
    for x in list_num:
        for y in list_num:
            if x + y == 2020:
                print(x, y)
                return x*y


def main_logic_two(list_num):
    for x in list_num:
        for y in list_num:
            for z in list_num:
                if x + y + z == 2020:
                    print(x, y, z)
                    return x*y*z


def main():
    inputs = take_input()
    max_allowed = 2020 - min(inputs)
    filtered_input = list(filter(lambda x: x <= max_allowed, inputs))
    print(main_logic_one(filtered_input))
    print(main_logic_two(filtered_input))


if __name__ == '__main__':
    main()
