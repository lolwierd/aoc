from types import MethodWrapperType


def parse_input():
    parsed_input = []
    with open("input.txt", "r") as f:
        parsed_input = [line.strip() for line in f.readlines()]
    return parsed_input


def get_seat_id(boarding_pass):

    def get_row(boarding_pass):
        min = 0
        max = 127
        # print(f"Called get row with boarding pass {boarding_pass}")
        for index, char in enumerate(list(boarding_pass)):
            mid = (max+min) // 2
            # print(
            #     f"Index: {index}, Char: {char}, Min: {min}, Max: {max}, Mid: {mid}")
            if max == min+1:
                # to_return = min if char == "F" else max
                # print(f"Returning: {to_return}")
                return min if char == "F" else max
            if char == "F":
                # print(f"Current char is F, setting max to mid")
                max = mid
            else:
                # print(f"Current char is B, setting max to mid")
                min = mid + 1
            # print(f"Keeping rows {min} - {max}")
        return -1

    def get_col(boarding_pass):
        # print(f"Called get col with boarding pass {boarding_pass}")
        min = 0
        max = 7
        # print(f"Called get row with boarding pass {boarding_pass}")
        for index, char in enumerate(list(boarding_pass)):
            mid = (max+min) // 2
            # print(
            #     f"Index: {index}, Char: {char}, Min: {min}, Max: {max}, Mid: {mid}")
            if max == min+1:
                # to_return = min if char == "L" else max
                # print(f"Returning: {to_return}")
                return min if char == "L" else max
            if char == "L":
                # print(f"Current char is F, setting max to mid")
                max = mid
            else:
                # print(f"Current char is B, setting max to mid")
                min = mid + 1
            # print(f"Keeping rows {min} - {max}")
        return -1

    return get_row(boarding_pass[0:7]) * 8 + get_col(boarding_pass[-3:])


def solve(boarding_passes):
    max = -1
    seat_ids = []
    # temp = get_seat_id("BBFBBFBRRL")
    # print(temp)
    for boarding_pass in boarding_passes:
        seat_id = get_seat_id(boarding_pass)
        seat_ids.append(seat_id)
        max = seat_id if seat_id > max else max
    return max, seat_ids


def solve_2(max_seat_id, seat_ids):
    nums = list(range(0, max_seat_id+1))
    empty_seats = []
    for x in nums:
        if x not in seat_ids:
            empty_seats.append(x)
    return empty_seats


def main():
    parsed_input = parse_input()
    max_seat_id, seat_ids = solve(parsed_input)
    print(max_seat_id)
    print(solve_2(max_seat_id, seat_ids))


if __name__ == "__main__":
    main()
