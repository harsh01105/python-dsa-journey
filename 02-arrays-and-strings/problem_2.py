# Problem: Given a list of numbers and a target, find all unique pairs that add up to the target.
# Approach: Use a set to track numbers we've seen, so each pair is found in a single pass.
# Time: O(n)  |  Space: O(n)

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.append((complement, num))
        seen.add(num)

    return pairs


numbers = [2, 7, 4, 1, 9, 5, 3]
result = find_pairs(numbers, 10)
print(f"Pairs that sum to 10: {result}")