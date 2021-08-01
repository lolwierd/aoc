import logging
import copy

logging.basicConfig(filename="debug.log", format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def parse_input():
    parsed_input = []
    with open('input.txt', 'r') as f:
        parsed_input = [int(num.strip()) for num in f.readlines()]
    return list(sorted(parsed_input))


def test_input(string):
    parsed_input = [int(num.strip()) for num in string.split('\n')]
    return list(sorted(parsed_input))


def solve(adapters, chain, choices):
    # logger.debug(f"Solving for chain {chain} and choices {choices}")

    def get_choices(chain):
        choices = []
        for adapter in adapters:
            if adapter - 1 == chain[-1] or adapter - 2 == chain[-1] or adapter - 3 == chain[-1]:
                choices.append(adapter)
            elif adapter > chain[-1]:
                break
        # logger.debug(f"Returning with choices {choices}")
        return choices

    # No chain therefore the first iteration.
    if len(chain) == 0:
        chain = [0]
        choices = get_choices(chain)
        return solve(adapters, chain, choices)

    # This means the the chain is found.
    if chain[-1] == adapters[-1]:
        return chain

    for choice in choices:
        # logger.debug(chain)
        chain.append(choice)
        choices = get_choices(chain)
        # This means the selected choice is wrong go ahead with next one.
        if len(choices) == 0 and len(chain) != 0:
            continue
        solve(adapters, chain, choices)
    return chain


def solve_all(adapters, chain, choices):
    def get_choices(chain):
        choices = []
        for adapter in adapters:
            if adapter - 1 == chain[-1] or adapter - 2 == chain[-1] or adapter - 3 == chain[-1]:
                choices.append(adapter)
            elif adapter > chain[-1]:
                break
        return choices

    # No chain therefore the first iteration.
    if len(chain) == 0:
        chain = [0]
        choices = get_choices(chain)
        return solve_all(adapters, chain, choices)

    # This means the the chain is found.
    if chain[-1] == adapters[-1]:
        return chain

    for choice in choices:
        chain.append(choice)
        choices = get_choices(chain)
        if choice == adapters[-1]:
            break
        # This means the selected choice is wrong go ahead with next one.
        if len(choices) == 0 and len(chain) != 0:
            logger.debug(f"Skipping choice: {choice} in the chain: {chain}")
            continue
        solve_all(adapters, chain, choices)
    return chain


def get_diff(chain):
    count_one = 0
    count_three = 1
    for idx in range(0, len(chain)):
        if idx == len(chain) - 1:
            continue
        if chain[idx + 1] - chain[idx] == 1:
            count_one += 1
        elif chain[idx + 1] - chain[idx] == 3:
            count_three += 1
    return count_one * count_three


def get_choices(adapters, num):
    choices = []
    for adapter in adapters:
        if adapter - 1 == num or adapter - 2 == num or adapter - 3 == num:
            choices.append(adapter)
        elif adapter > num:
            break
    return choices


def main():
    parsed_input = parse_input()
    test = '''16
10
15
5
1
11
7
19
6
12
4'''
    test_1 = '''28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3'''
    # [logger.debug(num) for num in parsed_input]
    parsed_input = test_input(test)
    choices_len = [get_choices(parsed_input, 0)]
    for num in parsed_input[:-1]:
        choices_len.append(get_choices(parsed_input, num))
    parsed_input.insert(0, 0)
    print(parsed_input)
    print(choices_len)
    # print(get_diff(solve(parsed_input, [], [])))
    # chains = solve_all(parsed_input, [], [])
    # print(chains.count(parsed_input[-1]))


if __name__ == "__main__":
    main()
