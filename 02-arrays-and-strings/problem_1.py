# Problem: Reverse a string without using Python's built-in reversal ([::-1] or reversed()).
# Approach: Two-pointer technique — swap characters from both ends moving inward.
# Time: O(n)  |  Space: O(n) (strings are immutable, so we build a new list/string)

def reverse_string(s):
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


print(reverse_string("harsh"))
print(reverse_string("dsa journey"))