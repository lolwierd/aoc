import logging
import copy

logging.basicConfig(filename="debug.log", format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def parse_input():
    parsed_input = []
    with open('input.txt', 'r') as f:
        parsed_input = [int(x.strip()) for x in f.readlines()]
    return parsed_input


def solve(xmas_data, premble_len):
    index = 0
    flag = False
    for num_to_check in xmas_data[premble_len:]:
        logger.debug(f"Checking for {num_to_check}")
        for num_1 in xmas_data[index:index+premble_len]:
            if flag:
                logger.debug("\tFound the sum!!")
                break
            for num_2 in xmas_data[index: index+premble_len]:
                if flag:
                    break
                if num_2 == num_1:
                    continue
                logger.debug(
                    f"\tChecking for sum of {num_1} and {num_2} which is {num_1+num_2}")
                if num_1 + num_2 == num_to_check:
                    flag = True
        if not flag:
            return num_to_check
        flag = False
        index += 1


def get_weakness(xmas_data, invalid_num):
    min_index = 0
    max_index = 2
    while True:
        total_sum = sum(xmas_data[min_index:max_index])
        if total_sum == invalid_num:
            return min(xmas_data[min_index:max_index]) + max(xmas_data[min_index:max_index])
        elif total_sum > invalid_num:
            min_index += 1
            max_index = min_index + 2
        else:
            max_index += 1


def main():
    parsed_input = parse_input()
    invalid_num = solve(parsed_input, 25)
    print(get_weakness(parsed_input, invalid_num))


if __name__ == "__main__":
    main()
