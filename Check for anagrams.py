# Check for anagrams

# Problem Description:
# You are given two strings s and t. Your task is to determine if string t is an anagram of string s. An anagram is a word or phrase formed by rearranging the characters of a different word or phrase, using all the original characters exactly once.

# Example:

# Input: s = "anagram", t = "nagaram"
# Output: True
 
# Input: s = "rat", t = "car"
# Output: False

def is_anagram(s, t):
    if len(s) != len(t):
        return False
    elif s=="" and t == "":
        return True 
    else:
        for char in t:
            if char not in s:
                return False
            else:
                return True
print(is_anagram("anagram", "nagaram"))  # True
print(is_anagram("rat", "car"))          # False


