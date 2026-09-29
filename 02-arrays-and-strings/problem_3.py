# Problem: Find the length of the longest substring without repeating characters.
# Approach: Sliding window — expand the window with 'right', and whenever a repeat
# is found, shrink from 'left' until the repeat is gone.
# Time: O(n)  |  Space: O(min(n, charset size))

def longest_unique_substring(s):
    seen = {}
    left = 0
    max_length = 0

    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1
        seen[char] = right
        max_length = max(max_length, right - left + 1)

    return max_length


print(longest_unique_substring("abcabcbb"))
print(longest_unique_substring("pwwkew"))
print(longest_unique_substring("harshcodes"))