import itertools
import random
from collections import Counter


def make_rotations(a: int, b: int, c: int):
    return [
        # positive x
        (+a, +b, +c),
        (+a, -c, +b),
        (+a, -b, -c),
        (+a, +c, -b),
        # negative x
        (-a, -b, +c),
        (-a, +c, +b),
        (-a, +b, -c),
        (-a, -c, -b),
        # positive y
        (+b, +c, +a),
        (+b, -a, +c),
        (+b, -c, -a),
        (+b, +a, -c),
        # negative y
        (-b, -c, +a),
        (-b, +a, +c),
        (-b, +c, -a),
        (-b, -a, -c),
        # positive z
        (+c, +a, +b),
        (+c, -b, +a),
        (+c, -a, -b),
        (+c, +b, -a),
        # negative z
        (-c, -a, +b),
        (-c, +b, +a),
        (-c, +a, -b),
        (-c, -b, -a),
    ]


class Scanner:
    def __init__(self, pts):
        self.rotations = list(
            [tuple(t) for t in zip(*[make_rotations(*p) for p in pts])]
        )
        self.right_rotation = None


def vec_diff(a, b):
    return tuple([x - y for x, y in zip(a, b)])


def vec_sum(a, b):
    return tuple([x + y for x, y in zip(a, b)])


def try_match(rot1, rot2):
    c = Counter(vec_diff(p, q) for (q, p) in itertools.product(rot1, rot2))
    possible_diffs = {k for k, v in c.items() if v >= 12}

    for diff in possible_diffs:
        cnt = 0
        for r1 in rot1:
            for r2 in rot2:
                if vec_diff(r2, r1) == diff:
                    cnt += 1
                    if cnt >= 12:
                        return diff
                    break


def solve(scanners):
    random.shuffle(scanners)
    merge_scanner, scanners = scanners[0], scanners[1:]
    merge_scanner.right_rotation = merge_scanner.rotations[0]

    scanner_positions = [(0, 0, 0)]
    while scanners:
        random.shuffle(scanners)
        diff = None
        matched_rotation = None
        matched_scanner = None
        for scanner in scanners:
            if diff is not None:
                break
            for rotation in scanner.rotations:
                # try match rotation with merge_scanner
                diff = try_match(rotation, merge_scanner.right_rotation)
                if diff is not None:
                    matched_rotation = rotation
                    matched_scanner = scanner
                    break

        assert diff is not None
        scanner_positions.append(diff)
        merge_scanner.right_rotation = tuple(
            set(merge_scanner.right_rotation)
            | {vec_sum(p, diff) for p in matched_rotation}
        )
        scanners.remove(matched_scanner)

    max_dst = max(
        sum(abs(v) for v in vec_diff(p, q))
        for (q, p) in itertools.product(scanner_positions, scanner_positions)
        if q != p
    )

    return len(merge_scanner.right_rotation), max_dst


with open("input.txt") as f:
    scanners = []
    positions = []
    for l in f:
        if l.strip() == "":
            scanners.append(Scanner(positions))
            positions = []
        elif not l.startswith("---"):
            positions.append([int(x) for x in l.strip().split(",")])
    scanners.append(Scanner(positions))

print("Part 1: {}\nPart 2: {}".format(*solve(scanners)))
