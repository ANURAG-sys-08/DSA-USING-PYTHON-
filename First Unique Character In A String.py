# First Unique Character In A String 

# Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

#  Example 1:

# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1

from collections import Counter
def firstUniqChar(s):
    count = Counter(s)
    for i, ch in enumerate(s):
        if count[ch] == 1:
            return i
            
    return -1
print(firstUniqChar("loveleetcode"))
    