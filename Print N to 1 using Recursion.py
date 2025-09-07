# Print N to 1 using Recursion
# Problem Description:

# You are given a positive integer n. Your task is to return a list of integers from n to 1 using recursion.

# Example:

# Input: n = 5
# Output: [5, 4, 3, 2, 1]
 
# Input: n = 3
# Output: [3, 2, 1]

def count_down(n):
    if n <= 0:
        return []
    return [n] + count_down(n - 1)

