import itertools
import functools
from collections import Counter


with open("input.txt") as f:
    p1_start, p2_start = [int(l.strip().split(": ")[-1]) for l in f.readlines()]


class DeterministicDie:
    def __init__(self):
        self.gen = itertools.cycle(range(1, 101))
        self.times_rolled = 0

    def get_next(self):
        self.times_rolled += 1
        return next(self.gen)


class Player:
    def __init__(self, starting_pos):
        self.pos = starting_pos - 1
        self.score = 0

    def make_turn(self, die) -> bool:
        s = die.get_next() + die.get_next() + die.get_next()
        self.pos = (self.pos + s) % 10
        self.score += self.pos + 1
        return self.score >= 1000


def part1() -> int:
    players = [Player(p1_start), Player(p2_start)]
    die = DeterministicDie()

    game_finished = False
    while not game_finished:
        for player in players:
            if player.make_turn(die):
                game_finished = True
                break

    losing = min(players, key=lambda p: p.score)
    return losing.score * die.times_rolled


possible_3_rolls_sums = Counter(
    sum(x) for x in list(itertools.product([1, 2, 3], [1, 2, 3], [1, 2, 3]))
)


@functools.cache
def play(a_score, b_score, a_pos, b_pos):
    if a_score >= 21:
        return 1, 0
    if b_score >= 21:
        return 0, 1

    score = (0, 0)
    for rolls_sum, times in possible_3_rolls_sums.items():
        new_a_pos = (a_pos + rolls_sum) % 10
        p2_wins, p1_wins = play(
            b_score,
            a_score + new_a_pos + 1,
            b_pos,
            new_a_pos,
        )
        score = (score[0] + p1_wins * times, score[1] + p2_wins * times)
    return score


def part2() -> int:
    return max(play(0, 0, p1_start - 1, p2_start - 1))


print(f"Part 1: {part1()}\nPart 2: {part2()}")
