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

    def __repr__(self) -> str:
        return f"{self.stack}"


def parse_input():
    parsed_input = []
    with open('input.txt', 'r') as f:
        parsed_input = [l.strip() for l in f.readlines()]
    return parsed_input


def trial(code):
    return [l.strip() for l in code.split("\n")]

# Solves the program and returns acc as soon as a duplicate instruction is encountered.


def solve(program, idx, acc, evaluated):
    logger.debug(
        f"Solving for {program[idx]} with acc: {acc}, index: {idx} and evaluated: {evaluated}")
    if (idx, program[idx]) in evaluated:
        logger.debug(f"Loop detected!! returning {acc}")
        return acc
    else:
        operation, argument = program[idx].split()
        evaluated.add((idx, program[idx]))
        if "nop" in operation:
            logger.debug(f"Statement is nop, setting idx to {idx+1}")
            return solve(program, idx+1, acc, evaluated)
        elif "acc" in operation:
            acc += int(argument)
            logger.debug(f"Statement is acc, setting acc to {acc}")
            return solve(program, idx+1, acc, evaluated)
        elif "jmp" in operation:
            idx += int(argument)
            logger.debug(f"Statement is jmp setting index to {idx}")
            return solve(program, idx, acc, evaluated)
        else:
            raise TypeError("Porgram invalid!!")


# Auxillary function for solve_jmp and solve_nop which checks the program for loops. If a loop is encountered,
#  None is returned, if no loop is found, and the program terminates, acc is returned.

def solve_aux(program, idx, acc, evaluated):
    if idx == len(program):
        return acc
    # logger.debug(
    #     f"Solving Aux for {program[idx]} with acc: {acc}, index: {idx} and evaluated: {evaluated}")
    if (idx, program[idx]) in evaluated:
        # logger.debug(f"Loop detected!! terminating!!")
        return None
    else:
        operation, argument = program[idx].split()
        evaluated.add((idx, program[idx]))
        if "nop" in operation:
            # logger.debug(f"Statement is nop, setting idx to {idx+1}")
            return solve_aux(program, idx+1, acc, evaluated)
        elif "acc" in operation:
            acc += int(argument)
            # logger.debug(f"Statement is acc, setting acc to {acc}")
            return solve_aux(program, idx+1, acc, evaluated)
        elif "jmp" in operation:
            idx += int(argument)
            # logger.debug(f"Statement is jmp setting index to {idx}")
            return solve_aux(program, idx, acc, evaluated)
        else:
            raise TypeError("Program invalid!!")


# Solves in a brute force manner by changing every jmp instruction to nop and checking if a loop is
# encountered. If a loop is found, next jmp is changed to nop and the program is simulated again.
def solve_jmp(program, idx, acc, evaluated, jmp_to_change, last_changed):
    # logger.debug(
    #     f"Solving for {program[idx]} with acc: {acc}, index: {idx} and evaluated: {evaluated}")
    ans = solve_aux(program, idx, acc, evaluated)
    if ans:
        [logger.debug(x) for x in program]
        return ans
    else:
        if jmp_to_change.empty():
            logger.debug("All JMPs exhausted")
            return None
        if last_changed:
            index_lc, operation_lc = last_changed
            program[index_lc] = operation_lc
        index = jmp_to_change.remove()
        last_changed = (index, program[index])
        _, argument = program[index].split()
        program[index] = "nop" + " " + argument
        return solve_jmp(program, 0, 0, set(), jmp_to_change, last_changed)


# Solves in a brute force manner by changing every nop instruction to nop and checking if a loop is
# encountered. If a loop is found, next nop is changed to jmp and the program is simulated again.
def solve_nop(program, idx, acc, evaluated, nop_to_change, last_changed):
    ans = solve_aux(program, idx, acc, evaluated)
    if ans:
        [logger.debug(x) for x in program]
        return ans
    else:
        if nop_to_change.empty():
            logger.debug("All NOPs exhausted")
            return None
        if last_changed:
            index_lc, operation_lc = last_changed
            program[index_lc] = operation_lc
        index = nop_to_change.remove()
        last_changed = (index, program[index])
        _, argument = program[index].split()
        program[index] = "jmp" + " " + argument
        return solve_nop(program, 0, 0, set(), nop_to_change, last_changed)


def main():
    parsed_input = parse_input()
#     code = '''nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6'''
#     parsed_input = trial(code)
    # print(solve(parsed_input, 0, 0, set()))
    jmps_index = Stack()
    nops_index = Stack()
    for index, line in enumerate(parsed_input):
        if "jmp" in line:
            jmps_index.add(index)
        elif "nop" in line:
            nops_index.add(index)
    print(solve_nop(copy.deepcopy(parsed_input), 0, 0, set(), nops_index, None))
    print(solve_jmp(copy.deepcopy(parsed_input), 0, 0, set(), jmps_index, None))


if __name__ == "__main__":
    main()
