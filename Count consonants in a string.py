# Count consonants in a string

# You are given a string s. Your task is to count the number of consonants in the string and return the total count. A consonant is any alphabetic character that is not a vowel (a, e, i, o, u).

# Example:

# Input: "Hello, World!"
# Output: 7
 
# Input: "Python Programming"
# Output: 13

def count_consonants(s):
    str = ["a","e","i","o","u",","," ","!"]
    ch = s.lower()
    count = 0
    for char in ch:
        if char not in str:
            count = count + 1
        else:
            count = count + 0
    return count
print(count_consonants("Hello, World!"))
