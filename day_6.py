def count_unique_letters(test_string):
    used_letters = []
    unique_letters = 0
    for letter in test_string:
        if letter not in used_letters:
            used_letters.append(letter)
            unique_letters += 1
    return unique_letters


def count_same_answers(group):

    # print(group)
    if len(group) == 1:
        return len(group[0])
    else:
        count = 0
        for answer in group[0]:
            if all([answer in person for person in group[1:]]):
                count += 1
        return count

    # for person in group:
    #     for answer in person:
    #         for


def day_6_part_1():
    with open("inputs/customs_answers.txt", "r") as customs_answers:
        #print([line.strip() for line in customs_answers.readlines() if line != "\n"])
        text = customs_answers.read()
    groups = [group.replace("\n", "") for group in text.split("\n\n")]
    sum_of_counts = 0
    for group in groups:
        sum_of_counts += count_unique_letters(group)
    print(sum_of_counts)

def day_6_part_2():
    with open("inputs/customs_answers.txt", "r") as customs_answers:
        # print([line.strip() for line in customs_answers.readlines() if line != "\n"])
        text = customs_answers.read()
    groups = [group.split("\n") for group in text.split("\n\n")]
    # print(groups)
    count = 0
    for group in groups:
        count += count_same_answers(group)
    print(count)
    # sum_of_counts = 0
    # for group in groups:
    #     sum_of_counts += count_unique_letters(group)
    # print(sum_of_counts)


if __name__ == "__main__":
    day_6_part_1()
    day_6_part_2()