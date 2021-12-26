class ALU:
    def __init__(self):
        self.vars = {c: 0 for c in "wxyz"}
        self.input_stack = []

    def add_input(self, val):
        self.input_stack.append(val)

    def resolve(self, v):
        if v in self.vars:
            return self.vars[v]
        return int(v)

    def inp(self, r):
        self.vars[r] = self.input_stack[0]
        self.input_stack.pop(0)

    def add(self, r, v):
        self.vars[r] += self.resolve(v)

    def mul(self, r, v):
        self.vars[r] *= self.resolve(v)

    def div(self, r, v):
        sgn = -1 if self.vars[r] * self.resolve(v) < 0 else 1
        self.vars[r] = sgn * (abs(self.resolve(r)) // abs(self.resolve(v)))

    def mod(self, r, v):
        self.vars[r] %= self.resolve(v)

    def neq(self, r, v):
        self.vars[r] = int(self.resolve(r) != self.resolve(v))

    def eql(self, r, v):
        self.vars[r] = int(self.resolve(r) == self.resolve(v))

    def mov(self, r, v):
        self.vars[r] = self.resolve(v)

    def run(self, instrs):
        for instr, *args in instrs:
            print(instr, args, "\t|\t", self.vars)
            {
                "eql": self.eql,
                "inp": self.inp,
                "add": self.add,
                "mul": self.mul,
                "div": self.div,
                "mod": self.mod,
                "mov": self.mov,
                "neq": self.neq,
            }[instr](*args)


def parse_input(f):
    return [l.strip().split(" ") for l in f if l.strip()]


def part1() -> int:
    # free variables
    w1 = 5
    w2 = 9
    w3 = 6
    w4 = 9
    w6 = 9
    w8 = 4
    w13 = 9

    w5 = w4 - 7
    w7 = w6
    w9 = w8 + 5
    w10 = w3 + 3
    w11 = w2 - 5
    w12 = w1 + 4
    w14 = w13 - 1

    w = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14]
    return int("".join(str(x) for x in w))


def part2() -> int:
    # free variables
    w1 = 1
    w2 = 6
    w3 = 1
    w4 = 8
    w6 = 1
    w8 = 1
    w13 = 2

    w5 = w4 - 7
    w7 = w6
    w9 = w8 + 5
    w10 = w3 + 3
    w11 = w2 - 5
    w12 = w1 + 4
    w14 = w13 - 1

    w = [w1, w2, w3, w4, w5, w6, w7, w8, w9, w10, w11, w12, w13, w14]
    return int("".join(str(x) for x in w))


print(f"Part 1: {part1()}\nPart 2: {part2()}")
