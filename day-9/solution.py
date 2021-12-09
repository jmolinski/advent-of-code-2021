from collections import Counter
from copy import deepcopy

from commontools import add_vec

with open("input.txt", "r") as f:
    matrix = [[int(a) for a in l.strip()] for l in f]


def get_neigh(a, b):
    def is_in_board(v):
        return 0 <= v[0] < len(matrix) and 0 <= v[1] < len(matrix[0])

    mv = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    return [n for x in mv if is_in_board(n := add_vec((a, b), x))]


def mark_all_in_basin(i, j, id, dt):
    dt[i][j] = id
    queue = [((i, j), x) for x in get_neigh(i, j)]
    explored = {(i, j)}

    while queue:
        adder, me = queue.pop(0)
        my_val = matrix[me[0]][me[1]]
        if me not in explored:
            explored.add(me)
            if my_val != 9:
                queue.extend([(me, x) for x in get_neigh(me[0], me[1])])
                dt[me[0]][me[1]] = id
                if my_val > matrix[adder[0]][adder[1]]:
                    dt[me[0]][me[1]] = id
                    queue.extend([(me, x) for x in get_neigh(me[0], me[1])])


def basin_explorer():
    centers = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if all(matrix[i][j] < matrix[x][y] for (x, y) in get_neigh(i, j)):
                centers.append((i, j))

    yield sum(1 + int(matrix[i][j]) for i, j in centers)

    basins_map = deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            basins_map[i][j] = 0

    for i, (x, y) in enumerate(centers):
        mark_all_in_basin(x, y, i + 1, basins_map)

    basin_sizes = Counter(v for line in basins_map for v in line if v != 0)
    a, b, c = [v for (_, v) in basin_sizes.most_common()][:3]
    yield a * b * c


solution = basin_explorer()
print(f"Part 1: {next(solution)}\nPart 2: {next(solution)}")
