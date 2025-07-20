# Count Vowels in a string

# You are given a string s. Your task is to count the number of vowels (both uppercase and lowercase) in the string and return the total count.

# Example:

# Input: "Hello, World!"
# Output: 3
 
# Input: "Python Programming"
# Output: 4

def count_vowels(s):
    str = s.lower()
    str2 = ["a","e","i","o","u"]
    con = 0
    for i in range(len(str)):
        if str[i] in str2:
            con = con+1
    return con

print(count_vowels("Python Programming"))