from queue import PriorityQueue

with open("input.txt") as f:
    matrix = [[int(x) for x in line.strip()] for line in f.readlines()]


def djikstra(data) -> int:
    pq = PriorityQueue()
    visited = set()
    dist = {}

    for a in range(len(data)):
        for b in range(len(data[a])):
            dist[(a, b)] = 10 ** 9
            pq.put((10 ** 9, (a, b)))

    dist[(0, 0)] = 0
    pq.put((0, (0, 0)))

    while not pq.empty():
        u_dist, u = pq.get()
        visited.add(u)

        for neighbor in [
            (u[0] + 1, u[1]),
            (u[0] - 1, u[1]),
            (u[0], u[1] + 1),
            (u[0], u[1] - 1),
        ]:
            if 0 <= neighbor[0] < len(data) and 0 <= neighbor[1] < len(data[0]):
                if neighbor not in visited:
                    alt = u_dist + data[neighbor[0]][neighbor[1]]
                    if alt < dist[neighbor]:
                        pq.put((alt, neighbor))
                        dist[neighbor] = alt

    return dist[(len(data) - 1, len(data[0]) - 1)]


def part1(data) -> int:
    return djikstra(data)


def part2() -> int:
    def wrapval(val):
        return val if val < 10 else val - 9

    extended_data = []
    for data_line in matrix:
        new_line = []
        for i in range(5):
            new_line.extend([wrapval(x + i) for x in data_line])
        extended_data.append(new_line)

    for i in range(1, 5):
        for line_no in range(len(matrix)):
            next_line = [wrapval(x + i) for x in extended_data[line_no]]
            extended_data.append(next_line)

    return djikstra(extended_data)


print(f"Part 1: {djikstra(matrix)}\nPart 2: {part2()}")
