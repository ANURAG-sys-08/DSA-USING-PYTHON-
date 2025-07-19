# Check for Prime Number

# You are given an integer n. Your task is to check whether the number is prime or not. A prime number is a number greater than 1 that has no divisors other than 1 and itself. Return True if the number is prime, and False otherwise.

# Example:

# Input: n = 5
# Output: True
 
# Input: n = 4
# Output: False
import math
def is_prime(n):
    if n <= 1:
        return False 
    for i in range(2, int(math.sqrt(n)) + 1):
        if n %i == 0:
            return False
    return True
for i in range(0,11):
    print(f"the number {i} is {is_prime(i)}")