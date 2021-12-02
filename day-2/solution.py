with open("input.txt") as f:
    commands = []
    for l in f:
        cmd, v = l.split()
        commands.append((cmd, int(v)))


def part1():
    depth, pos = 0, 0

    for cmd, v in commands:
        if cmd == "forward":
            pos += v
        elif cmd == "up":
            depth -= v
        else:
            depth += v

    return depth * pos


def part2():
    depth, pos, aim = 0, 0, 0

    for cmd, v in commands:
        if cmd == "forward":
            pos += v
            depth += aim * v
        elif cmd == "up":
            aim -= v
        else:
            aim += v

    return depth * pos


print("Part 1", part1())
print("Part 2", part2())
