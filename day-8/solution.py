with open("input.txt") as f:
    entries = []
    for l in f:
        a, b = l.split(" | ")
        entries.append((a.split(), b.split()))


def decode(digits, code):
    def find_matching(length, predicate=lambda x: True):
        return [a for a in digits if len(a) == length and predicate(a)][0]

    one = find_matching(2)
    four = find_matching(4)
    seven = find_matching(3)
    eight = find_matching(7)
    nine = find_matching(6, lambda d: four.issubset(d))
    two = find_matching(5, lambda d: len(nine - d) == 2)
    three = find_matching(5, lambda d: len(two - d) == 1)
    five = find_matching(5, lambda d: d not in [two, three])
    zero = find_matching(6, lambda d: d != nine and one.issubset(d))
    six = find_matching(6, lambda d: d not in [zero, nine])

    ds = [zero, one, two, three, four, five, six, seven, eight, nine]
    return int("".join(str(ds.index(d)) for d in code))


def part1() -> int:
    return sum(len(digit) in {2, 3, 4, 7} for _, output in entries for digit in output)


def part2() -> int:
    return sum(
        decode(
            [set(digit) for digit in digits],
            [set(digit) for digit in code],
        )
        for digits, code in entries
    )


print(f"Part 1: {part1()}\nPart 2: {part2()}")
