with open("input.txt") as f:
    pattern = f.readline().strip()
    f.readline()
    original_light = set()
    for y, line in enumerate(f):
        for x, char in enumerate(line.strip()):
            if char == "#":
                original_light.add((x, y))


def enhance_image(d, default):
    min_x, max_x = min(x for (x, y) in d), max(x for (x, y) in d)
    min_y, max_y = min(y for (x, y) in d), max(y for (x, y) in d)

    lit = set()
    dark = set()
    for y in range(min_y - 1, max_y + 2):
        for x in range(min_x - 1, max_x + 2):
            num = 0
            for dy in (-1, 0, 1):
                for dx in (-1, 0, 1):
                    num <<= 1
                    xx, yy = x + dx, y + dy
                    if (default == ".") == ((xx, yy) in d):
                        num += 1

            if pattern[num] == "#":
                lit.add((x, y))
            else:
                dark.add((x, y))

    return lit, dark


def simulate(iterations):
    lit = original_light

    for _ in range(iterations // 2):
        lit, dark = enhance_image(lit, default=".")
        lit, dark = enhance_image(dark, default="#")

    return len(lit)


print(f"Part 1: {simulate(2)}\nPart 2: {simulate(50)}")
