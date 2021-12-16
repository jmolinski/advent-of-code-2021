from __future__ import annotations
from typing import Callable

import itertools
import operator
from functools import reduce as fold_left
import dataclasses


with open("input.txt") as f:
    data = "".join(("0000" + bin(int(x, 16))[2:])[-4:] for x in f.read().strip())


def dec(s: str) -> int:
    return int(s, 2)


def make_stream(text: str) -> Callable[[int], str]:
    it = iter(text)
    return lambda n: "".join(itertools.islice(it, n))


@dataclasses.dataclass
class Packet:
    version: int
    type_id: int
    value: int = 0
    packets: list[Packet] = dataclasses.field(default_factory=list)


def parse_packet(take: Callable[[int], str]) -> Packet:
    packet = Packet(dec(take(3)), dec(take(3)))

    if packet.type_id == 4:
        while take(1) == "1":
            packet.value = (packet.value << 4) + dec(take(4))
        packet.value = (packet.value << 4) + dec(take(4))
    else:
        if take(1) == "0":
            payload_len = dec(take(15))
            payload = take(payload_len)
            subpackets_stream = make_stream(payload)
            try:
                while True:
                    packet.packets.append(parse_packet(subpackets_stream))
            except:
                pass
        else:
            subpackets_count = dec(take(11))
            for _ in range(subpackets_count):
                packet.packets.append(parse_packet(take))

    return packet


def eval_tree(node: Packet) -> None:
    for child in node.packets:
        eval_tree(child)

    match node.type_id:
        case 0:
            node.value = sum(child.value for child in node.packets)
        case 1:
            node.value = fold_left(operator.mul, [p.value for p in node.packets])
        case 2:
            node.value = min(child.value for child in node.packets)
        case 3:
            node.value = max(child.value for child in node.packets)
        case 5:
            node.value = int(node.packets[0].value > node.packets[1].value)
        case 6:
            node.value = int(node.packets[0].value < node.packets[1].value)
        case 7:
            node.value = int(node.packets[0].value == node.packets[1].value)


def part1() -> int:
    q = [parse_packet(make_stream(data))]
    s = 0
    while q:
        packet = q.pop(0)
        s += packet.version
        q.extend(packet.packets)

    return s


def part2() -> int:
    tree = parse_packet(make_stream(data))
    eval_tree(tree)

    return tree.value


print(f"Part 1: {part1()}\nPart 2: {part2()}")
