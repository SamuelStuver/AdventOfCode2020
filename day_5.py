# For first 7 characters of inputs, F means take Lower half, B means take Upper half
# For last 3 characters of inputs, L means take Lower half, R means take Upper half


def upper_half(seats):
    length = len(seats)
    if length == 2:
        return [seats[-1]]
    return seats[int(length/2):]


def lower_half(seats):
    length = len(seats)
    if length == 2:
        return [seats[0]]
    return seats[0:int(length/2)]


def find_row(input_string):
    nrows = 128
    possible_rows = list(range(nrows))
    input_string = input_string[0:7]
    string_index = 0
    while len(possible_rows) > 1 and string_index < len(input_string):
        if input_string[string_index] == 'F':
            possible_rows = lower_half(possible_rows)
        elif input_string[string_index] == 'B':
            possible_rows = upper_half(possible_rows)
        string_index += 1
    return possible_rows[0]


def find_column(input_string):
    ncols = 8
    possible_cols = list(range(ncols))
    input_string = input_string[7:]
    string_index = 0
    while len(possible_cols) > 1 and string_index < len(input_string):
        if input_string[string_index] == 'L':
            possible_cols = lower_half(possible_cols)
        elif input_string[string_index] == 'R':
            possible_cols = upper_half(possible_cols)
        string_index += 1
    return possible_cols[0]


def calc_seat_id(boarding_pass):
    row = find_row(boarding_pass)
    column = find_column(boarding_pass)
    return (row * 8) + column


def day_5_part_1():
    with open("inputs/boarding_passes.txt", "r") as boarding_passes:
        pass_list = boarding_passes.readlines()
    seat_ids = []
    for bp in pass_list:
        seat_ids.append(calc_seat_id(bp))
    print(max(seat_ids))


def day_5_part_2():
    with open("inputs/boarding_passes.txt", "r") as boarding_passes:
        pass_list = boarding_passes.readlines()
    seat_ids = []
    for bp in pass_list:
        seat_ids.append(calc_seat_id(bp))
    for i in range(min(seat_ids), max(seat_ids)+1):
        if i not in seat_ids:
            print(i)


if __name__ == "__main__":
    day_5_part_1()
    day_5_part_2()
    # print(find_column("FBFBBFFRLR"))