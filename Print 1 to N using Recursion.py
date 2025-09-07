# Print 1 to N using Recursion

# Problem Description:

# You are given a positive integer n. Your task is to return a list of integers from 1 to n using recursion.

# Example:

# Input: n = 5
# Output: [1, 2, 3, 4, 5]
 
# Input: n = 3
# Output: [1, 2, 3]

def count_to_n(n):
    if n <= 0:
        return []
    return count_to_n(n - 1) + [n]