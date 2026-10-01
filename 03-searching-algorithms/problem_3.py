# Problem: In a sorted list with duplicate values, find the first and last index
# of a target value, in O(log n) time (not O(n)).
# Approach: Run binary search twice — once biased to find the leftmost match,
# once biased to find the rightmost match.
# Time: O(log n)  |  Space: O(1)

def find_first_last(lst, target):
    def find_bound(find_first):
        low, high = 0, len(lst) - 1
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if lst[mid] == target:
                result = mid
                if find_first:
                    high = mid - 1  # keep searching left
                else:
                    low = mid + 1   # keep searching right
            elif lst[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return result

    first = find_bound(find_first=True)
    last = find_bound(find_first=False)
    return (first, last)


data = [1, 2, 2, 2, 3, 4, 7, 7, 8]
print(find_first_last(data, 2))
print(find_first_last(data, 7))
print(find_first_last(data, 5))