# Check for Even Number

# You are given an integer n. Your task is to check whether the number is even or not. Return True if the number is even, and False otherwise.

# Example:

# Input: n = 4
# Output: True
 
# Input: n = 7
# Output: False

def is_even(n):
    if (n%2==0):
        return True
    else:
        return False
is_even(4)