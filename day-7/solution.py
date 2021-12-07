with open("input.txt") as f:
    crabs = [int(a) for a in f.read().strip().split(",")]


def get_cost(f):
    minc, maxc = min(crabs), max(crabs)
    return min(sum(f(abs(c - i)) for c in crabs) for i in range(minc, maxc + 1))


print(f"Part 1: {get_cost(abs)}\nPart 2: {get_cost(lambda x: x * (x + 1) // 2)}")
