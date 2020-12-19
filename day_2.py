import re
# find how many passwords are valid according to their policies


def count_letter(word, letter_to_match):
    count = 0
    for letter in word:
        if letter == letter_to_match:
            count += 1
    return count


def is_password_valid_dayOne(password, minimum, maximum, letter):
    return minimum <= count_letter(password, letter) <= maximum


def is_password_valid_dayTwo(password, pos_1, pos_2, letter):
    pos_1 -= 1
    pos_2 -= 1
    print(f"{password} {pos_1} {pos_2} {letter} | {password[pos_1]} {password[pos_2]} {(password[pos_1] == letter or password[pos_2] == letter) and not (password[pos_1] == password[pos_2])}")
    return (password[pos_1] == letter or password[pos_2] == letter) and not (password[pos_1] == password[pos_2])


def day_2_part_1(filename):
    with open(filename, "r") as f:
        passwords_full = f.readlines()

    regex = r"([0-9]+)\-([0-9]+) ([a-z]): ([a-z]+)"
    valid_password_count = 0
    for pw in passwords_full:
        match = re.search(regex, pw)
        assert match, pw
        min_occurrences = int(match.group(1))
        max_occurrences = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)
        if is_password_valid_dayOne(password, min_occurrences, max_occurrences, letter):
            valid_password_count += 1
    return valid_password_count


def day_2_part_2(filename):
    with open(filename, "r") as f:
        passwords_full = f.readlines()

    regex = r"([0-9]+)\-([0-9]+) ([a-z]): ([a-z]+)"
    valid_password_count = 0
    for pw in passwords_full:
        match = re.search(regex, pw)
        assert match, pw
        pos_1 = int(match.group(1))
        pos_2 = int(match.group(2))
        letter = match.group(3)
        password = match.group(4)
        if is_password_valid_dayTwo(password, pos_1, pos_2, letter):
            valid_password_count += 1
    return valid_password_count


if __name__ == "__main__":
    print(day_2_part_1("passwords.txt"))
    print(day_2_part_2("passwords.txt"))