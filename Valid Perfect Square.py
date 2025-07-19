# Valid Perfect Square

# You are given a positive integer num. Your task is to check whether num is a perfect square or not. A perfect square is an integer that is the square of an integer (e.g., 1, 4, 9, 16, ...). Return True if num is a perfect square, and False otherwise.


# Example:

# Input: num = 16
# Output: True
 
# Input: num = 14
# Output: False

# You can check if the square of any integer i equals num. Iterate through integers starting from 1 up to sqrt(num) to check if i * i equals num.

def is_perfect_square(num):
    if num<=1:
        return False
    i = 1
    while i*i<=num:
        if i * i == num:
            return True
        i = i + 1
    return False
print(is_perfect_square(14))