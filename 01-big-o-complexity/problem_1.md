## Problem 1: What is the time complexity of this code?

```python
def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
```

**Your answer:** ______

**Explanation (write this after you attempt it):**
- How many times does the loop run relative to the input size?
- Does the runtime change if the list doubles in size?