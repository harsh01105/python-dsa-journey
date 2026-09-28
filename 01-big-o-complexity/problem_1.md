## Problem 1: What is the time complexity of this code?

```python
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
```

**Your answer:** O(n)

**Explanation:**
- The loop runs once for every element, so n items means n iterations.
- If the list doubles in size, the runtime roughly doubles (linear growth).
- Space complexity is O(1) since only one extra variable (max_val) is used.