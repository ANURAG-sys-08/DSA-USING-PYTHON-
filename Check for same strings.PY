# Check for same strings

# You are given two strings s and t. Your task is to check if the two strings are equal. Two strings are considered equal if they have the same length and the same characters at each position. You are not allowed to use any built-in string comparison functions.

# Example:

# Input: s = "hello", t = "hello"
# Output: True
 
# Input: s = "hello", t = "world"
# Output: False

def are_equal_strings(s, t):
    if s == t:
        return True
    elif s!=t:
        return False
    else:
        None
print(are_equal_strings(s = "hello", t = "world"))