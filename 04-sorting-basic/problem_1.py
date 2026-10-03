# Problem: Sort a list of numbers using Bubble Sort.
# Approach: Repeatedly step through the list, swapping adjacent elements
# that are out of order. After each full pass, the largest unsorted
# element "bubbles" to its correct position at the end.
# Time: O(n^2)  |  Space: O(1)

def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:  # already sorted, stop early
            break
    return lst


numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))