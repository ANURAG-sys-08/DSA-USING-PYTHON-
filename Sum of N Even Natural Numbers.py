# Sum of N Even Natural Numbers
# Problem Description:

# You are given an integer n. Your task is to calculate and return the sum of the first n even natural numbers. The even natural numbers are: 2, 4, 6, 8, ...

# Example:

# Input: n = 3
# Output: 12  # (2 + 4 + 6)
 
# Input: n = 5
# Output: 30  # (2 + 4 + 6 + 8 + 10)

def sum_of_even_numbers(n):
    return n * (n + 1)

print(sum_of_even_numbers(4))  

