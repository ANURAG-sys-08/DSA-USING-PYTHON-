# Remove Duplicates in a string

# You are given a string s. Your task is to remove duplicate characters from the string while preserving the order of the first occurrences and return the modified string.

# Example:

# Input: "programming"
# Output: "progamin"
 
# Input: "Hello, World!"
# Output: "Helo, Wrd!"

def remove_duplicates(s):
    str = ""
    for char in s:
        if char not in str:
            str = str + char
    return str
print(remove_duplicates("Hello, World!"))
