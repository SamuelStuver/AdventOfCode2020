import re

credentials_rules = {
    'ecl':r"amb|blu|brn|gry|grn|hzl|oth",
    'pid':r"[0-9]{9}",
    'eyr':[r"[0-9]{4}", 2020, 2030],
    'hcl':r"#[0-9a-f]{6}",
    'byr':[r"[0-9]{4}", 1920, 2002],
    'iyr':[r"[0-9]{4}", 2010, 2020],
    'cid':r".*",
    'hgt':[r"[0-9]+cm|[0-9]+in", (150, 193), (59, 76)]
}


def read_passports(passfile_name):
    with open(passfile_name, "r") as passfile:
        text = passfile.read()
    lines = text.split("\n\n")
    lines_corrected = []
    for line in lines:
        line = line.replace("\n", " ")
        lines_corrected.append(line)
    return lines_corrected


def is_valid(passport):
    regex = r"([a-z]{3}):([#a-zA-Z0-9]+)"
    matches = re.findall(regex, passport)
    match_dict = {}
    for match in matches:
        match_dict[match[0]] = match[1]
    if len(match_dict) < 7:
        return False
    elif set(match_dict.keys()) == set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']):
        return True
    elif set(match_dict.keys()) == set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']):
        return True


def is_valid_with_credentials(passport):
    if not is_valid(passport):
        return False
    regex = r"([a-z]{3}):([#a-zA-Z0-9]+)"
    matches = re.findall(regex, passport)
    match_dict = {}
    for match in matches:
        match_dict[match[0]] = match[1]
    assert (set(match_dict.keys()) == set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']) or set(['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']))
    results = {}
    for field in match_dict.keys():
        # print(credentials_rules[field])
        if field in ['hcl', 'ecl', 'pid']:
            result = re.search(credentials_rules[field], match_dict[field]) is not None
        elif 'yr' in field:
            min_year = int(credentials_rules[field][1])
            max_year = int(credentials_rules[field][2])
            result = check_year(int(match_dict[field]), min_year, max_year)
        elif field == 'hgt':
            result = check_height(match_dict[field], credentials_rules[field][1], credentials_rules[field][2])
        else:
            result = True
        results[field] = result
        print(field, match_dict[field], result)
    if False in results.values():
        return False
    else:
        return True


def is_valid_with_credentials_2(passport):
    if not is_valid(passport):
        return False
    regex = r"([a-z]{3}):([#a-zA-Z0-9]+)"
    matches = re.findall(regex, passport)
    match_dict = {}
    for match in matches:
        match_dict[match[0]] = match[1]

    if not check_height(match_dict['hgt'], credentials_rules['hgt'][1], credentials_rules['hgt'][2]):
        return False
    for field in ['byr', 'iyr', 'eyr']:
        min_year = credentials_rules[field][1]
        max_year = credentials_rules[field][2]
        if not check_year(int(match_dict[field]), min_year, max_year):
            return False
    for field in ['hcl', 'ecl', 'pid']:
        if not check_regex(match_dict[field], field):
            return False

    return True
    #print(match_dict)

def check_height(value, rules_cm, rules_in):
    match = re.search(r"([0-9]+)(in|cm)", value)
    if not match:
        return False
    val = int(match.group(1))
    unit = match.group(2)
    if unit == "cm":
        rules = rules_cm
    elif unit == "in":
        rules = rules_in
    else:
        return False
    # print(rules, val, unit)
    return int(rules[0]) <= val <= int(rules[1])


def check_year(value, min_year, max_year):
    return min_year <= value <= max_year


def check_regex(value, field):
    regex = credentials_rules[field]
    assert type(regex) is str
    if re.search(regex, value):
        return True
    else:
        return False

def day_4_part_1():
    passports = read_passports("passports.txt")
    n_valid = 0
    for passport in passports:
        if is_valid(passport):
            n_valid += 1
    print(f"{n_valid} valid passports out of {len(passports)}")


def day_4_part_2():
    passports = read_passports("passports.txt")
    n_valid = 0
    n_invalid = 0
    for passport in passports:
        if is_valid_with_credentials_2(passport):
            n_valid += 1
        else:
            n_invalid += 1
    print(f"{n_valid} valid passports out of {len(passports)}")
    print(f"{n_invalid} invalid passports out of {len(passports)}")



if __name__ == "__main__":
    day_4_part_2()