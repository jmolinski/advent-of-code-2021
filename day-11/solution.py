from copy import deepcopy

with open("input.txt") as f:
    original_matrix = [
        [int(x) for x in line.strip()] for line in f.read().split("\n") if line.strip()
    ]

NEIGHBOR_VECTORS = [
    (a, b) for a in range(-1, 2) for b in range(-1, 2) if not (a == 0 and b == 0)
]


def solve(steps: int, exit_on_simultaneous_flash: bool = False) -> int:
    matrix = deepcopy(original_matrix)
    flashes = 0
    for step_id in range(steps):
        for a in range(len(matrix)):
            for b in range(len(matrix[a])):
                matrix[a][b] += 1

        flashed = set()
        while True:
            ready_to_flash = []
            for a in range(len(matrix)):
                for b in range(len(matrix[a])):
                    if matrix[a][b] > 9:
                        if (a, b) not in flashed:
                            ready_to_flash.append((a, b))

            if not ready_to_flash:
                break

            for a, b in ready_to_flash:
                flashes += 1
                flashed.add((a, b))
                for da, db in NEIGHBOR_VECTORS:
                    x, y = a + da, b + db
                    if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                        matrix[x][y] += 1

        for a, b in flashed:
            matrix[a][b] = 0

        if exit_on_simultaneous_flash and len(flashed) == len(matrix) * len(matrix[0]):
            return step_id + 1

    return flashes


print(f"Part 1: {solve(100)}\nPart 2: {solve(2**64, True)}")
