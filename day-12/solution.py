from collections import defaultdict
from string import ascii_uppercase


class Graph:
    def __init__(self, adjacency_list):
        self.adj = adjacency_list
        self.can_reenter = None

    def count_paths(self, s, d, allowed_to_reenter=None):
        self.can_reenter = allowed_to_reenter
        visited, paths, path = [], [], []

        self.count_paths_util(s, d, path, visited, paths)
        return paths

    def count_paths_util(self, u, d, path, visited, path_count):
        path.append(u)
        if u[0] not in ascii_uppercase and (self.can_reenter != u or path.count(u) > 1):
            visited.append(u)

        if u == d:
            path_count.append(path)
        else:
            for neighbor in self.adj[u]:
                if neighbor not in visited:
                    self.count_paths_util(neighbor, d, path.copy(), visited, path_count)

        if u in visited:
            visited.remove(u)


with open("input.txt") as f:
    adj = defaultdict(list)
    for line in f:
        a, b = line.strip().split("-")
        adj[a].append(b)
        adj[b].append(a)
    graph = Graph(adj)


def part1() -> int:
    return len(graph.count_paths("start", "end"))


def part2() -> int:
    paths = []
    for s in {k for k in adj if k[0] not in ascii_uppercase} - {"start", "end"}:
        paths += graph.count_paths("start", "end", s)

    return len(set(tuple(x) for x in paths))


print(f"Part 1: {part1()}\nPart 2: {part2()}")
