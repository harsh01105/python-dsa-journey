# 01 - Big-O and Complexity Analysis

**Reference course:** freeCodeCamp - Data Structures and Algorithms in Python
**Video chapter:** "Binary Search, Linked Lists and Complexity"

## Notes
- **Time complexity** measures how an algorithm's runtime grows as input size (n) grows.
- **Space complexity** measures how much extra memory an algorithm uses as n grows.
- Big-O describes the **worst-case upper bound** — how bad it can get, not the average case.
- We care about growth rate, not exact operation counts — constants and lower-order terms are dropped.
  e.g. `3n + 5` becomes `O(n)`; `n² + 100n` becomes `O(n²)`.

### Common complexities (fastest to slowest)
| Notation | Name | Example |
|---|---|---|
| O(1) | Constant | Accessing a list by index: `my_list[0]` |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | A single loop through a list |
| O(n log n) | Log-linear | Merge sort, Quicksort (average case) |
| O(n²) | Quadratic | Nested loops (e.g. bubble sort) |
| O(2ⁿ) | Exponential | Naive recursive Fibonacci |

### How to estimate complexity quickly
- One loop over n items → O(n)
- A loop inside a loop, both over n → O(n²)
- Cutting the problem in half each time (like binary search) → O(log n)
- A function calling itself twice per call (like naive recursion) → often O(2ⁿ)