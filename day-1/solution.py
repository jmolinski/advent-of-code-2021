with open("input.txt") as f:
    nums = [int(i) for i in f]

print("Part 1", sum(a < b for a, b in zip(nums, nums[1:])))
triplets = [sum(abc) for abc in zip(nums, nums[1:], nums[2:])]
print("Part 2", sum(a < b for a, b in zip(triplets, triplets[1:])))
