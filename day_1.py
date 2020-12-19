
# find the two entries that sum to 2020 and then multiply those two numbers together

def day_1_part_1(filename):
    with open(filename, "r") as f:
        values = f.readlines()

    values = [int(v) for v in values]
    for i in values:
        for j in values:
            s = i + j
            if s == 2020:
                print(f"i = {i}, j = {j}")
                return i * j


def day_1_part_2(filename):
    with open(filename, "r") as f:
        values = f.readlines()

    values = [int(v) for v in values]
    for i in values:
        for j in values:
            for k in values:
                s = i + j + k
                if s == 2020:
                    print(f"i = {i}, j = {j}, k = {k}")
                    return i * j * k

if __name__ == "__main__":
    print(day_1_part_1("expense_report.txt"))
    print(day_1_part_2("expense_report.txt"))