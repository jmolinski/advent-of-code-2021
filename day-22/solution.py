with open('input.txt') as f:
    instructions = []
    for l in f:
        cmd, args = l.strip().split(" ")
        args = [[int(x) for x in a[2:].split("..")] for a in args.split(",")]
        instructions.append((cmd, args))


def part1() -> int:
    up_to_50 = [
        (cmd, args)
        for cmd, args in instructions
        if all(abs(a) <= 50 and abs(b) <= 50 for (a, b) in args)
    ]
    pts = set()
    for cmd, args in up_to_50:
        xr, yr, zr = args
        for x in range(xr[0], xr[1] + 1):
            for y in range(yr[0], yr[1] + 1):
                for z in range(zr[0], zr[1] + 1):
                    if cmd == "on":
                        pts.add((x, y, z))
                    elif (x, y, z) in pts:
                        pts.remove((x, y, z))

    return len(pts)


print(f"Part 1: {part1()}")
