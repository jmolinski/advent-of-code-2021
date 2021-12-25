with open("input.txt") as f:
    cucumbers = {}
    for y, line in enumerate(f.read().strip().splitlines()):
        ROWS = y + 1
        COLS = len(line)
        for x, char in enumerate(line.strip()):
            if char in ">v":
                cucumbers[(x, y)] = char


def run_iteration(current):
    d = {}
    east = {k for k, v in current.items() if v == ">"}
    south = {k for k, v in current.items() if v == "v"}
    for x, y in east:
        new_x = (x + 1) % COLS
        if (new_x, y) not in current:
            d[(new_x, y)] = ">"
        else:
            d[(x, y)] = ">"
    for x, y in south:
        new_y = (y + 1) % ROWS
        if (x, new_y) not in south and (x, new_y) not in d:
            d[(x, new_y)] = "v"
        else:
            d[(x, y)] = "v"

    return d


def solve() -> int:
    global cucumbers
    i = 0
    while True:
        i += 1
        new_cucumbers = run_iteration(cucumbers)
        if new_cucumbers == cucumbers:
            return i
        cucumbers = new_cucumbers


print("Part 1:", solve(), "\nPart 2: hurray!")
