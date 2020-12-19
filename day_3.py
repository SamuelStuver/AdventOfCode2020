import math


def read_treefile(treefile):
    with open("tree_patten.txt", "r") as treefile:
        rows = treefile.readlines()
    for i in range(len(rows)):
        rows[i] = rows[i].strip()
    return rows


def day_3_part_1_and_2():

    rows = read_treefile("tree_pattern.txt")
    nrows = len(rows)
    ncols = len(rows[0])

    results = []
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for slope in slopes:
        n_trees = 0
        xpos = 0
        ypos = 0
        while ypos < nrows:
            row = rows[ypos]
            current_tile = row[xpos]
            if current_tile == "#":
                n_trees += 1
            ypos += slope[1]
            xpos = (xpos + slope[0]) % ncols
        results.append(n_trees)
    print(f"Trees hit: {results}")
    result = math.prod(results)
    print(result)


if __name__ == "__main__":
    day_3_part_1_and_2()