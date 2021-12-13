with open("input.txt") as f:
    raw_coords, raw_folds = f.read().strip().split("\n\n")

    original_coords = {
        tuple(int(x) for x in l.strip().split(",")) for l in raw_coords.splitlines()
    }

    folds = [l.split(" ")[-1].split("=") for l in raw_folds.splitlines()]


def fold(axis, point, coords):
    new_coords = set()
    if axis == "x":
        for (x, y) in coords:
            if x > point:
                new_coords.add((2 * point - x, y))
            elif x < point:
                new_coords.add((x, y))
    elif axis == "y":
        for (x, y) in coords:
            if y > point:
                new_coords.add((x, 2 * point - y))
            elif y < point:
                new_coords.add((x, y))

    return new_coords


def part2():
    coords = original_coords
    for axis, point in folds:
        coords = fold(axis, int(point), coords)

    minx = min(x for (x, y) in coords)
    miny = min(y for (x, y) in coords)
    maxx = max(x for (x, y) in coords)
    maxy = max(y for (x, y) in coords)

    for y in range(miny, maxy + 1):
        for x in range(minx, maxx + 1):
            if (x, y) in coords:
                print("##", end="")
            else:
                print("  ", end="")
        print()


print("Part 1:", len(fold(folds[0][0], int(folds[0][1]), original_coords)))
print("Part 2:")
part2()
