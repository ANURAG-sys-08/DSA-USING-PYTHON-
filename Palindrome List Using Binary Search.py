# Palindrome List

# Description:
# Given a list of integers, determine if it is a palindrome. A list is considered a palindrome if it reads the same forward and backward.

# Example:

# Input: lst = [7, 8, 9, 8, 7]
# Output: True
 
# Input: lst = [1, 2, 3, 4, 5]
# Output: False
 
# Input: lst = [1, 2, 3, 2, 1]
# Output: True

# def is_palindrome(lst):
#     for i in range(len(lst)):
#         if (lst[i]==lst[-(i+1)]):
#             return True
#         return False
def is_palindrome(lst):
    left = 0
    right = len(lst)-1
    while left<=right:
        if (lst[left] != lst[right]):
            return False
        left +=1
        right -=1
    return True
print(is_palindrome([1, 2, 3, 4, 5]))