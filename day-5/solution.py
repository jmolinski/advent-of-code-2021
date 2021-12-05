from collections import Counter

from more_itertools import chunked

with open("input.txt") as f:
    lines_coordinates = [
        int(a)
        for l in f
        for a in l.strip().replace("-> ", "").replace(",", " ").split(" ")
    ]


pts_hv, pts_diagonal = [], []

for x1, y1, x2, y2 in chunked(lines_coordinates, 4):
    if y1 != y2 and x1 != x2:
        x_d, y_d = (x2 - x1) // abs(x2 - x1), (y2 - y1) // abs(y2 - y1)

        pts_diagonal.append((x1, y1))
        while x1 != x2:
            x1, y1 = x1 + x_d, y1 + y_d
            pts_diagonal.append((x1, y1))

    elif y1 != y2:
        for y in range(min(y1, y2), max(y1, y2) + 1):
            pts_hv.append((x1, y))
    else:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            pts_hv.append((x, y1))

p1 = sum(v > 1 for v in Counter(pts_hv).values())
p2 = sum(v > 1 for v in Counter(pts_hv + pts_diagonal).values())

print(f"Part 1: {p1}\nPart 2: {p2}")
