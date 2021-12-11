with open("input.txt", "r") as f:
    lines = [l.strip() for l in f.readlines()]


def solve() -> tuple[int, int]:
    part1_score = 0
    incomplete = []
    for line in lines:
        stack = []
        for c in line:
            if c in "([{<":
                stack.append(c)
            else:
                if c != {"{": "}", "(": ")", "[": "]", "<": ">"}[stack.pop()]:
                    part1_score += {")": 3, "]": 57, "}": 1197, ">": 25137}[c]
                    stack = []
                    break
        if stack:
            incomplete.append(stack)

    scores = []
    for stack in incomplete:
        line_score = 0
        for x in stack[::-1]:
            line_score = line_score * 5 + {"(": 1, "[": 2, "{": 3, "<": 4}[x]
        scores.append(line_score)

    return part1_score, sorted(scores)[len(scores) // 2]


print("Part 1: {}\nPart 2: {}".format(*solve()))
