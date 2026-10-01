# 03 - Searching (Linear and Binary Search)

**Video chapter:** Binary Search, Linked Lists and Complexity
**Status:** In progress
**Recommended practice problems:** 3 (Easy, Medium, Hard/Interview-style)

## Notes
- **Linear search:** check each element one by one. Works on any list (sorted or not). O(n) time.
- **Binary search:** repeatedly halve the search range by comparing with the middle element. Only works on a **sorted** list. O(log n) time.
- Binary search steps:
  1. Set `low = 0`, `high = len(lst) - 1`
  2. While `low <= high`: find `mid = (low + high) // 2`
  3. If `lst[mid] == target`, found it.
  4. If `lst[mid] < target`, search the right half (`low = mid + 1`)
  5. If `lst[mid] > target`, search the left half (`high = mid - 1`)
- A common bug: using `mid = (low + high) / 2` (float division) instead of `//` (integer division) — causes a `TypeError` when used as a list index.
- Binary search also works on "answer space" problems — not just finding a value in a list, but finding the smallest/largest value that satisfies some condition (a more advanced interview pattern).

| | Linear Search | Binary Search |
|---|---|---|
| Time complexity | O(n) | O(log n) |
| Requires sorted input? | No | Yes |
| Best for | Small/unsorted data | Large sorted data, repeated searches |