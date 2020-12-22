def is_valid(value, prev_vals):
    for check_val in prev_vals:
        if value - check_val in prev_vals:
            return True
    return False


def checkvals(values, value_to_match):
    pass


def day_9_part_1():

    with open("inputs/encoding_values.txt") as infile:
        values = [int(val) for val in infile.readlines()]

    preamble_length = 25
    index = preamble_length
    #print(values)
    valid_number = True
    while valid_number:
        value = values[index]
        #print(value, values[index-preamble_length:index], is_valid(value, values[index-preamble_length:index]))
        if not is_valid(value, values[index-preamble_length:index]):
            break
        index += 1
    #print(values[index])
    return values[index]


def day_9_part_2():
    with open("inputs/encoding_values.txt") as infile:
        values = [int(val) for val in infile.readlines()]
    value_to_match = day_9_part_1()

    index_min = 0
    index_max = 1

    value_found = False
    while not value_found:
        s = sum(values[index_min:index_max])
        if s == value_to_match:
            value_found = True
            index_max -= 1
        elif s > value_to_match:
            index_min += 1
            index_max = index_min + 1
        else:
            index_max += 1
    # print(values[index_min], values[index_max], s, value_to_match)
    return min(values[index_min:index_max]) + max(values[index_min:index_max])


if __name__ == "__main__":
    print(f"Day 1 answer: {day_9_part_1()}")
    print(f"Day 2 answer: {day_9_part_2()}")