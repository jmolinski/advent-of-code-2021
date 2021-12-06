from collections import Counter

with open("input.txt") as f:
    initial_fish = [int(a) for a in f.read().strip().split(",")]


def run_simulation(days: int) -> int:
    fish = Counter(initial_fish)

    for _ in range(days):
        new_fish = dict()

        zero = fish.get(0, 0)
        for k, v in fish.items():
            if k != 0:
                new_fish[k - 1] = v
        new_fish[8] = zero
        new_fish[6] = new_fish.get(6, 0) + zero

        fish = new_fish

    return sum(v for v in fish.values())


print(f"Part 1: {run_simulation(80)}\nPart 2: {run_simulation(256)}")
