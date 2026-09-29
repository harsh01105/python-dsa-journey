# 02 - Arrays and Strings

**Status:** In progress
**Recommended practice problems:** 3 (Easy, Medium, Hard/Interview-style)

## Notes
- In Python, a **list** is the dynamic-array equivalent — unlike arrays in C/Java, it can grow/shrink and hold mixed types.
- **Indexing** is O(1) — Python lists are stored as contiguous memory blocks internally.
- **Strings are immutable** — every "modification" (like `.replace()`) actually creates a new string in memory.
- Two very common array/string patterns for interviews:
  - **Two Pointers** — one pointer from the start, one from the end, moving toward each other.
  - **Sliding Window** — a moving sub-range (window) over the array/string, expanding or shrinking as you go.
- Common operations and their complexity:

| Operation | Complexity | Note |
|---|---|---|
| Access by index `lst[i]` | O(1) | Direct memory lookup |
| Append `lst.append(x)` | O(1) amortized | Occasionally resizes internally |
| Insert at front `lst.insert(0, x)` | O(n) | Shifts every element |
| Search `x in lst` | O(n) | Checks each element |
| Slice `lst[a:b]` | O(k) | k = size of the slice |