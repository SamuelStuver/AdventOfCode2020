import re
import pprint as pp



class Node:
    def __init__(self, color, rules, parent=None):
        self.color = color
        self.parent = parent
        self.children = [Node(c, rules, parent=self) for c in rules[self.color]]

    def add(self, childNode):
        childNode.parent = self
        self.children.append(childNode)

    def find(self, color):
        if self.color == color:
            return self
        else:
            for child in self.children:
                match = child.find(color)
                if match:
                    return match

    def __repr__(self):
        return abbreviate(self.color)


def print_tree(node, indent):
    print(indent*">" + repr(node))
    for child in node.children:
        print_tree(child, indent+4)


def abbreviate(phrase):
    result = "|"
    words = phrase.split(" ")
    for word in words:
        result += word[0].upper()
        result += word[1].lower()
    result += "|"
    return result


def findall_in_tree(node, color):
    result = []  # Line 1
    if node.color == color:
        result.append(node)  # Line 2
    for child in node.children:
        result.extend(findall_in_tree(child, color))  # Line 3
    return result


def parse_rules(filename):
    with open(filename, "r") as rule_file:
        rules = [line.strip() for line in rule_file.readlines()]

    regex_parent = r"([a-z\s]+) bags contain"
    regex_children = r"[0-9]+ ([a-z\s]+) bag"

    rule_dict = {}
    for rule in rules:
        parent_color = re.search(regex_parent, rule).group(1)
        children_colors = re.findall(regex_children, rule)
        rule_dict[parent_color] = children_colors

    rule_dict["Master"] = list(rule_dict.keys())
    #pp.pprint(rule_dict)

    return rule_dict

    # master_node = Node(None)
    # color_nodes = []
    # for color in rule_dict.keys():
    #     color_nodes.append(Node(color))
    # #print(color_nodes)
    #
    #
    # for node in color_nodes:
    #     print(node, rule_dict[node.color])
    #     node.children = [Node(c) for c in rule_dict[node.color]]
    #     print(f"{node} -> {node.children}")


def day_7_part_1(rules):
    master_node = Node("Master", rules)
    color_to_find = "shiny gold"
    matching_nodes = findall_in_tree(master_node, color_to_find)
    unique_parents = []
    for node in matching_nodes:
        if node.color == "shiny gold" and node.parent.color == "Master":
            break
        while node.parent.color != "Master":
            node = node.parent
        if node.color not in unique_parents:
            unique_parents.append(node.color)
        # while parent.color != "Master":
        #     print(parent)
        #         break
        #     else:
        #         parent = parent.parent
    print(unique_parents)
    print(len(unique_parents))

def day_7_part_2(rules):
    pass


if __name__ == "__main__":
    rules = parse_rules("inputs/bag_rules.txt")
    day_7_part_1(rules)
    day_7_part_2(rules)