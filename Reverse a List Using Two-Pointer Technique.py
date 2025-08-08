# Reverse a List

# Description:
# Given a list of integers, write a function to reverse the order of elements in the list.

# Example:

# Input: lst = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]
 
# Input: lst = [10, 20, 30]
# Output: [30, 20, 10]
 
# Input: lst = [7, 8, 9]
# Output: [9, 8, 7]

def reverse_list(lst):
    left = 0
    right = len(lst)-1
    while left<right:
        lst[left],lst[right] = lst[right],lst[left]
        left +=1
        right -=1
    return lst

print(reverse_list([7, 8, 9]))