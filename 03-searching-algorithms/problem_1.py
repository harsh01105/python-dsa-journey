# Problem: Return the index of a target in a list, or -1 if not found.
# Approach: Linear search — check every element in order.
# Time: O(n)  |  Space: O(1)

def linear_search(lst, target):
    for i, value in enumerate(lst):
        if value == target:
            return i
    return -1


numbers = [4, 2, 9, 7, 1, 5]
print(linear_search(numbers, 7))
print(linear_search(numbers, 10))