import logging
import copy

logging.basicConfig(filename="debug.log", format='%(message)s', filemode='w')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


class Stack():
    def __init__(self):
        self.stack = []

    def add(self, node):
        self.stack.append(node)

    def empty(self):
        return len(self.stack) == 0

    def remove(self):
        if self.empty():
            raise Exception("Empty Stack!!")
        else:
            node = self.stack[-1]
            self.stack = self.stack[:-1]
            return node


class Node:
    def __init__(self, bag, num):
        self.bag = bag
        self.num = num
        self.parent = None
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def add_parent(self, parent):
        self.parent = parent
        parent.add_child(self)

    def __repr__(self) -> str:
        return f"Node({self.bag}, {self.num})"

# if the line is
# dull blue bags contain 2 dotted green bags, 1 dull brown bag.
# Return the structure of form {"dull blue bag": {"dotted green bag": 2, "dull brown bag": 1}}
# {'shiny gold bag': {'bright lavender bag': 4, 'striped maroon bag': 1, 'plaid silver bag': 2}}
# ('shiny gold bag', [('bright lavender bag', 4), ('striped maroon bag', 1), ('plaid silver bag', 2)])


def parse_input():
    parsed_input = []
    with open('input.txt', 'r') as f:
        for line in f.readlines():
            if "no" in line:
                continue
            # [:-1] to  Remove . from the end
            bag, can_contain = [l.strip()
                                for l in line.strip()[:-1].split("contain")]
            # Remove the trailing s
            bag = bag[:-1]
            temp_bags = [bag.strip() for bag in can_contain.split(",")]
            contained_bags = []
            for contained_bag in temp_bags:
                # Remove the trailing s
                if contained_bag[-1] == "s":
                    contained_bag = contained_bag[:-1]
                num = contained_bag[0]
                bag_name = contained_bag[2:]
                # contained_bags[bag_name] = int(num)
                contained_bags.append((bag_name, int(num)))
            parsed_input.append((bag, contained_bags))
    return parsed_input

# Works don't ask me how please.


def solve(rules):
    shiny_rules = set()
    mutated_rules = copy.deepcopy(rules)
    for rule in rules:
        contained_bags_tuple = rule[1]
        contained_bags = [bag[0] for bag in contained_bags_tuple]
        if "shiny gold bag" in contained_bags:
            shiny_rules.add(rule[0])
            mutated_rules.remove(rule)
    rules = copy.deepcopy(mutated_rules)
    while True:
        shiny_rules_len = len(shiny_rules)
        for rule in rules:
            contained_bags_tuple = rule[1]
            contained_bags = [bag[0] for bag in contained_bags_tuple]
            mutated_shiny_rules = copy.deepcopy(shiny_rules)
            for shiny_rule in shiny_rules:
                if shiny_rule in contained_bags:
                    mutated_shiny_rules.add(rule[0])
            shiny_rules = copy.deepcopy(mutated_shiny_rules)
        if len(shiny_rules) == shiny_rules_len:
            break
        else:
            shiny_rules_len = len(shiny_rules)
    return shiny_rules


def construct_tree(bag, rules):
    root = Node(bag, 1)
    to_traverse = []
    for rule in rules:
        if bag == rule[0]:
            for rule_bag in rule[1]:
                node = Node(*rule_bag)
                node.add_parent(root)
                to_traverse.append(node)
    for node in to_traverse:
        for rule in rules:
            if node.bag == rule[0]:
                for rule_bag in rule[1]:
                    temp = Node(*rule_bag)
                    temp.add_parent(node)
                    to_traverse.append(temp)
    return root


def print_tree(root):
    to_traverse = root.children
    for node in to_traverse:
        logger.debug(f"{node.parent}: {node}")
        for child in node.children:
            to_traverse.append(child)


def calculate_bags(visited, node):
    if node not in visited:
        # logger.debug(f"{node.parent}: {node}")
        visited.add(node)
        sum = node.num
        for child in node.children:
            logger.debug(f"sum: {sum}")
            sum += node.num*calculate_bags(visited, child)
        return sum


def main():
    parsed_input = parse_input()
    print(len(solve(parsed_input)))
    root = construct_tree('shiny gold bag', parsed_input)
    sum = 0
    for child in root.children:
        sum += calculate_bags(set(), child)
    print(sum)


if __name__ == "__main__":
    main()
