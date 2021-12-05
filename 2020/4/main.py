# First Thoughts:
# Can parse the file using regex and take segments between empty lines, to seperate different
# passport data
# After that merge the multiple lines into a single line and match regex to check validity.
# But that is too ugly and fuck that regex shit.
# Can also make a parser to parse passport data. That sounds pretty and amazing.
# Not gonna say i like this code but whatever
import string


def parse_input():
    parsed_input = []
    with open("input.txt", "r") as f:
        text = f.read()
        parsed_input = text.split("\n\n")
    # replace newline with whitespace
    for index, input in enumerate(parsed_input):
        parsed_input[index] = input.replace("\n", " ")
    return parsed_input


def answer(parsed_input):
    def is_present(passport):
        return "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport

    def is_valid(passport):
        passport_fields = passport.split()
        valid_field = []
        for field in passport_fields:
            field_name, field_value = field.split(":")
            if "byr" == field_name:
                year = int(field_value.strip())
                # print(f"Checking for byr with year {year}")
                valid_field.append(1920 <= year <= 2002)
            elif "iyr" == field_name:
                year = int(field_value.strip())
                # print(f"Checking for iyr with year {year}")
                valid_field.append(2010 <= year <= 2020)
            elif "eyr" == field_name:
                year = int(field_value.strip())
                # print(f"Checking for eyr with year {year}")
                valid_field.append(2020 <= year <= 2030)
            elif "hgt" == field_name:
                # print(f"Checking for hgt with value {field_value}")
                if "in" in field_value:
                    hgt = int(field_value.strip()[:-2])
                    valid_field.append(59 <= hgt <= 76)
                elif "cm" in field_value:
                    hgt = int(field_value.strip()[:-2])
                    valid_field.append(150 <= hgt <= 193)
                else:
                    valid_field.append(False)

            elif "hcl" == field_name:
                # print(f"Checking for hcl with value {field_value}")
                valid_field.append("#" == field_value[0] and all(
                    c in string.hexdigits for c in field_value[1:]))
            elif "ecl" == field_name:
                # print(f"Checking for ecl with value {field_value}")
                valid_field.append("amb" == field_value or "blu" == field_value or "brn" == field_value or "gry" ==
                                   field_value or "grn" == field_value or "hzl" == field_value or "oth" == field_value)
            elif "pid" == field_name:
                try:
                    # print(f"Checking for pid with value {field_value}")
                    valid_field.append(len(field_value.strip())
                                       == 9 and int(field_value.strip()))
                except ValueError:
                    valid_field.append(False)
        return all(valid_field)

    valid_pass_nums = 0
    for passport in parsed_input:
        if is_present(passport) and is_valid(passport):
            valid_pass_nums += 1
    return valid_pass_nums


def main():
    parsed_input = parse_input()
    print(len(parsed_input))
    print(answer(parsed_input))


if __name__ == "__main__":
    main()
