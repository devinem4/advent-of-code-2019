def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


class IntcodeCpu:
    def __init__(self, initial_state):
        self.state = [int(c) for c in initial_state.split(",")]

    def process(self):
        for i in range(0, len(self.state), 4):
            if self.state[i] == 99:
                return ",".join([str(instr) for instr in self.state])

            param1 = self.state[self.state[i + 1]]
            param2 = self.state[self.state[i + 2]]
            target_address = self.state[i + 3]

            # print(self.state[i], param1, param2, target_address)
            if self.state[i] == 1:
                self.state[target_address] = add(param1, param2)
            elif self.state[i] == 2:
                self.state[target_address] = multiply(param1, param2)

        return ",".join([str(instr) for instr in self.state])


if __name__ == "__main__":
    with open("inputs/day02") as f:
        initial_state = f.read()

    cpu = IntcodeCpu(initial_state)
    # replace position 1 with the value 12
    cpu.state[1] = 12
    # replace position 2 with the value 2
    cpu.state[2] = 2
    cpu.process()

    print(f"final answer = { cpu.state[0] }")
