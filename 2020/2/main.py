def take_input():
    inputs = []
    with open("input.txt", "r") as f:
        for line in f:
            inputs.append(line.rstrip())
    return inputs


# returns the parsed password policy in the form of [min, max, char, password]
def get_parsed_password_policy(password_str):
    split1 = password_str.split()
    split2 = split1[0].split("-")
    return [int(split2[0]), int(split2[1]), split1[1][0], split1[2]]


# takes the parsed password policy and returns true if the password is valid and false otherwise
def check_password(password_policy):
    min_allowed = password_policy[0]
    max_allowed = password_policy[1]
    char_to_check = password_policy[2]
    password = password_policy[3]
    return min_allowed <= password.count(char_to_check) <= max_allowed


# takes the parsed password policy and returns true if the password is valid and false otherwise
def check_password_2(password_policy):
    pos_1 = password_policy[0] - 1
    pos_2 = password_policy[1] - 1
    char_to_check = password_policy[2]
    password = password_policy[3]
    if pos_1 + 1 > len(password) or pos_2 + 1 > len(password):
        return False
    # 5head logic to check if only one is true basically an xor.
    return (password[pos_1] == char_to_check) != (password[pos_2] == char_to_check)


def main_logic(password_policies):
    valid_passwords = []
    for password_policy in password_policies:
        parsed_password_policy = get_parsed_password_policy(password_policy)
        if check_password_2(parsed_password_policy):
            valid_passwords.append(password_policy)
    return valid_passwords


def main():
    password_policies = take_input()
    answer = main_logic(password_policies)
    print(len(answer))


if __name__ == "__main__":
    main()
