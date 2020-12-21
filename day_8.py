def execute_instructions(instructions):
    # Returns True if execution reaches end of instructions (index > len(instructions)), otherwise returns False if loop
    acc = 0
    index = 0
    indices_used = []
    max_index = 0

    while index not in indices_used:
        if index >= len(instructions):
            print("PING")
            return acc, True

        rule = instructions[index]
        print(rule, index, acc)
        indices_used.append(index)

        if rule[0] == "nop":
            index += 1
        if rule[0] == "acc":
            if "+" in rule[1]:
                acc += int(rule[1].strip("+"))
            elif "-" in rule[1]:
                acc -= int(rule[1].strip("-"))
            index += 1
        if rule[0] == "jmp":
            if "+" in rule[1]:
                index += int(rule[1].strip("+"))
            elif "-" in rule[1]:
                index -= int(rule[1].strip("-"))
        if index > max_index:
            max_index = index

    print(f"Index: {index}\nMax Index: {max_index}\nACC: {acc}")
    return acc, False


def day_8_part_1(instructions):
    acc, reached_end = execute_instructions(instructions)
    print(acc, reached_end)
    print()


def day_8_part_2(instructions):
    indices_tried = []
    execution_ended = False
    index = -1
    while not execution_ended:
        index += 1
        instruction = instructions[index]
        if instruction[0] == 'jmp' and index not in indices_tried:
            indices_tried.append(index)
            instructions[index][0] = 'nop'
            acc, execution_ended = execute_instructions(instructions)
            instructions[index][0] = 'jmp'
    print("finished executing instructions")
    #acc, reached_end = execute_instructions(instructions)
    print(acc, execution_ended)
    print()


def parse_instructions(filename):
    with open(filename, "r") as instruction_file:
        instructions = [rule.strip() for rule in instruction_file.readlines()]
    instructions = [rule.split(" ") for rule in instructions]
    return instructions


if __name__ == "__main__":
    instructions = parse_instructions("inputs/instructions.txt")

    day_8_part_1(instructions)
    day_8_part_2(instructions)