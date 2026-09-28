## Problem 2: Which approach is more efficient for large n, and why?

**Approach A** — check if a value exists in a list:
```python
def contains(lst, target):
    for item in lst:
        if item == target:
            return True
    return False
```

**Approach B** — check if a value exists in a *sorted* list using binary search:
```python
def contains_sorted(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return True
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
```

**Your answer:** Approach B (binary search) is faster. A is O(n), B is O(log n).

**Explanation:**
- Linear search may check all 1,000,000 items in the worst case.
- Binary search halves the search space each step, so it needs about 20 comparisons.
- Binary search requires the list to be sorted, otherwise it gives wrong results.