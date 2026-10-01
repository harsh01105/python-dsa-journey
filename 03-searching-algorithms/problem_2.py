# Problem: Implement binary search on a sorted list, returning the index or -1.
# Approach: Repeatedly halve the search range based on comparison with the middle.
# Time: O(log n)  |  Space: O(1)

def binary_search(lst, target):
    low, high = 0, len(lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


sorted_numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17]
print(binary_search(sorted_numbers, 13))
print(binary_search(sorted_numbers, 4))