from __future__ import annotations

import dataclasses
import functools
import operator
from copy import deepcopy


@dataclasses.dataclass
class Node:
    value: int
    left: Node | None = None
    right: Node | None = None

    @property
    def is_regular(self) -> bool:
        return self.left is None and self.right is None

    @property
    def magnitude(self) -> int:
        if self.is_regular:
            return self.value
        return 3 * self.left.magnitude + 2 * self.right.magnitude

    def __add__(self, other: Node) -> Node:
        return Node(0, deepcopy(self), deepcopy(other)).reduced()

    def reduced(self) -> Node:
        n = deepcopy(self)
        n.reduce()
        return n

    def reduce(self) -> None:
        while True:
            ctx = {}
            exploded = self.explode(ctx, 0)
            if exploded is not None:
                v = []
                self.serialize_nums(v)
                i = [idx for idx, n in enumerate(v) if n is exploded][0]
                if i >= 1:
                    v[i - 1].value += ctx["add_to_left"]
                if i < len(v) - 1:
                    v[i + 1].value += ctx["add_to_right"]
            else:
                self.split(ctx)
                if not ctx.get("split"):
                    break

    def explode(self, ctx, depth=0) -> Node | None:
        if ctx.get("exploded") is not None or self.is_regular:
            return

        if depth > 3:
            ctx["exploded"] = True
            ctx["add_to_left"] = self.left.value
            ctx["add_to_right"] = self.right.value
            self.value = 0
            self.left = None
            self.right = None
            return self
        else:
            l = self.left.explode(ctx, depth + 1)
            r = self.right.explode(ctx, depth + 1)
            return l or r

    def split(self, ctx: dict) -> None:
        if ctx.get("split"):
            return
        elif self.is_regular and self.value > 9:
            self.left = Node(self.value // 2)
            self.right = Node((self.value + 1) // 2)
            self.value = 0
            ctx["split"] = True
        elif not self.is_regular:
            self.left.split(ctx)
            self.right.split(ctx)

    def __repr__(self) -> str:
        if self.is_regular:
            return str(self.value)
        return f"[{self.left},{self.right}]"

    def serialize_nums(self, v: list):
        if self.is_regular:
            v.append(self)
        else:
            self.left.serialize_nums(v)
            self.right.serialize_nums(v)


def parse_number(s: str) -> Node:
    if s[0] != "[":
        v = 0
        for c in s:
            v = v * 10 + int(c)
        return Node(v)

    depth = 0
    for pos, c in enumerate(s[1:], start=1):
        if c == "," and depth == 0:
            return Node(0, parse_number(s[1:pos]), parse_number(s[pos + 1 : -1]))
        if c == "[":
            depth += 1
        if c == "]":
            depth -= 1


def get_input() -> list[Node]:
    with open("input.txt") as f:
        return [parse_number(s.strip()) for s in f.readlines() if s.strip()]


def part1(data) -> int:
    return functools.reduce(operator.add, data).magnitude


def part2(data) -> int:
    max_magnitude = 0
    for i, a in enumerate(data):
        for j, b in enumerate(data):
            if j != i:
                max_magnitude = max(max_magnitude, (a + b).magnitude)
    return max_magnitude


print(f"Part 1: {part1(get_input())}\nPart 2: {part2(get_input())}")
