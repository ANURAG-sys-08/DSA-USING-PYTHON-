# Reverse a string

# You are given a string s. Your task is to return the reversed version of the string.

# Example:

# Input: "hello"
# Output: "olleh"
 
# Input: "Python"
# Output: "nohtyP"

def reverse_string(s):
    str2 = ""
    for i in range(len(s)-1,-1,-1):
        str2 = str2 + s[i]
    return str2

print(reverse_string("hello"))
