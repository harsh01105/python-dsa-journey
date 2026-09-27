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

**Your answer:** Which is faster for a list of 1,000,000 items, and what's each one's Big-O?