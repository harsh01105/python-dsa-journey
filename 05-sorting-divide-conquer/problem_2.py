# Problem: Sort a list of numbers using Quicksort.
# Approach: Pick the last element as pivot, partition the list so
# smaller elements go left and larger go right, then recursively
# sort each partition.
# Time: O(n log n) average, O(n^2) worst  |  Space: O(log n)

def quicksort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[-1]
    smaller = [x for x in lst[:-1] if x <= pivot]
    larger = [x for x in lst[:-1] if x > pivot]

    return quicksort(smaller) + [pivot] + quicksort(larger)


numbers = [10, 7, 8, 9, 1, 5]
print(quicksort(numbers))