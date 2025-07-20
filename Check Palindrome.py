# Check Palindrome

# You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.You are given a string s. Your task is to check if the string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring spaces, punctuation, and case.

# Example:

# Input: "A man a plan a canal Panama"
# Output: True
 
# Input: "Hello, World!"
# Output: False

def is_palindrome(s):
    s = s.replace(" ","").lower()
    str = ""
    for i in range(len(s)-1,-1,-1):
        str = str + s[i]
    if str == s:
        return True
    elif str != s:
        return False

print(is_palindrome("Hello, World!"))