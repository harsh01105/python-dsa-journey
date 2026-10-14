# Problem: Find the k-th smallest element in an unsorted list, without
# fully sorting it.
# Approach: QuickSelect - like Quicksort, but only recurse into the
# partition that contains the k-th position, ignoring the other side.
# Time: O(n) average, O(n^2) worst  |  Space: O(log n)

def quickselect(lst, k):
    if len(lst) == 1:
        return lst[0]

    pivot = lst[-1]
    smaller = [x for x in lst[:-1] if x <= pivot]
    larger = [x for x in lst[:-1] if x > pivot]

    if k < len(smaller):
        return quickselect(smaller, k)
    elif k == len(smaller):
        return pivot
    else:
        return quickselect(larger, k - len(smaller) - 1)


def kth_smallest(lst, k):
    return quickselect(lst, k - 1)  # convert to 0-indexed


numbers = [7, 10, 4, 3, 20, 15]
print(f"1st smallest: {kth_smallest(numbers, 1)}")
print(f"3rd smallest: {kth_smallest(numbers, 3)}")
print(f"5th smallest: {kth_smallest(numbers, 5)}")