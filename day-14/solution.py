from collections import Counter, defaultdict

with open("input.txt") as f:
    template = list(f.readline().strip())

    raw_rules = [p.split(" -> ") for p in f.read().strip().splitlines()]
    raw_rules = sorted(raw_rules)
    rules = {k: k[0] + v + k[1] for k, v in raw_rules}


def solve(steps: int) -> int:
    pairs = Counter("".join(x) for x in zip(template, template[1:]))
    for i in range(steps):
        new_pairs = defaultdict(int)
        for k, v in pairs.items():
            new_pairs[rules[k][:2]] += v
            new_pairs[rules[k][1:]] += v
        pairs = new_pairs

    ctr = Counter()
    for (a, b), v in pairs.items():
        ctr[a] += v
        ctr[b] += v

    ctr[template[0]] += 1
    ctr[template[-1]] += 1

    for k, v in ctr.items():
        ctr[k] //= 2

    return ctr.most_common()[0][1] - ctr.most_common()[-1][1]


print(f"Part 1: {solve(10)}\nPart 2: {solve(40)}")
