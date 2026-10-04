# Problem: Sort a list of numbers using Selection Sort.
# Approach: Repeatedly find the minimum element in the unsorted part
# of the list, and swap it into its correct position at the front.
# Time: O(n^2)  |  Space: O(1)

def selection_sort(lst):
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


numbers = [29, 10, 14, 37, 13]
print(selection_sort(numbers))