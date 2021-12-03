from collections import Counter


with open("input.txt") as f:
    numbers = [l.strip() for l in f]


def get_freq(nums):
    freq = [Counter() for _ in range(len(nums[0]))]

    for num in nums:
        for i, d in enumerate(num):
            freq[i][d] += 1

    return freq


def part1():
    freq = get_freq(numbers)
    most_common = "".join(ctr.most_common()[0][0] for ctr in freq)
    least_common = "".join(ctr.most_common()[1][0] for ctr in freq)

    return int(most_common, 2) * int(least_common, 2)


def part2():
    oxygen_generator, scrubber = numbers.copy(), numbers.copy()

    bit_no = 0
    while len(oxygen_generator) > 1 or len(scrubber) > 1:
        if len(oxygen_generator) > 1:
            (first, first_cnt), (last, last_cnt) = get_freq(oxygen_generator)[bit_no].most_common()
            bit = "1" if (first_cnt == last_cnt or first == "1") else "0"
            oxygen_generator = [n for n in oxygen_generator if n[bit_no] == bit]

        if len(scrubber) > 1:
            (first, first_cnt), (last, last_cnt) = get_freq(scrubber)[bit_no].most_common()
            bit = "0" if (first_cnt == last_cnt or first == "1") else "1"
            scrubber = [n for n in scrubber if n[bit_no] == bit]

        bit_no += 1

    return int(oxygen_generator[0], 2) * int(scrubber[0], 2)


print(f"Part 1: {part1()}\nPart 2: {part2()}")
