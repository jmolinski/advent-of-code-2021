with open("test_input.txt") as f:
    _, _, a, b = f.read().strip().replace(",", "").split(" ")
    xfrom, xto = map(int, a.split("=")[1].split(".."))
    yfrom, yto = map(int, b.split("=")[1].split(".."))
    x_range = range(xfrom, xto + 1)
    y_range = range(yfrom, yto + 1)


def simulate_trajectory(x_velocity, y_velocity) -> list[int] | None:
    ys = []
    x, y = 0, 0
    success = False
    while True:
        ys.append(y)
        x += x_velocity
        y += y_velocity
        if x_velocity != 0:
            x_velocity = x_velocity - 1 if x_velocity > 0 else x_velocity + 1
        y_velocity -= 1

        if x in x_range and y in y_range:
            success = True
        if y < yfrom and y_velocity < 0:
            break

    return ys if success else None


successes = []
for y_velocity_org in range(300, -200, -1):
    for x_velocity in range(300):
        ys = simulate_trajectory(x_velocity, y_velocity_org)
        if ys:
            successes.append(ys)

print("Part 1:", max(max(ys) for ys in successes))
print("Part 2:", len(successes))
