def parse_input():
    parsed_input = []
    with open("input.txt", "r") as f:
        text = f.read()
        parsed_input = text.split("\n\n")
    # replace newline with whitespace
    for index, input in enumerate(parsed_input):
        parsed_input[index] = input.replace("\n", "")
    return parsed_input


def parse_input_1():
    parsed_input = []
    with open("input.txt", "r") as f:
        text = f.read()
        parsed_input = text.split("\n\n")
    return parsed_input


def solve(answers):
    count = 0
    for answer in answers:
        unique_answer = set(list(answer))
        count += len(unique_answer)
    return count


def solve_1(answers):
    count = 0
    for answer in answers:
        answers_per_person = answer.split("\n")
        all_yes = answers_per_person[0]
        for answer_person in answers_per_person[1:]:
            common = ''
            for charac in answer_person:
                if charac in all_yes:
                    common += charac
            all_yes = common
        # print(all_yes)
        count += len(all_yes)
    return count


def main():
    parsed_input = parse_input()
    print(solve(parsed_input))
    parsed_input_1 = parse_input_1()
    print(solve_1(parsed_input_1))


if __name__ == "__main__":
    main()
