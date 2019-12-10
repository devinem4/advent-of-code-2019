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

    target = 19690720
    for noun in range(0, 100):
        for verb in range(0, 100):
            cpu = IntcodeCpu(initial_state)
            cpu.state[1] = noun
            cpu.state[2] = verb
            cpu.process()
            # final answer is position 0 of final state
            if target == cpu.state[0]:
                print(f"target achieved: { noun } { verb } = { noun * 100 + verb }")
