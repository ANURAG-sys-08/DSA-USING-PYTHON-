# Maximum Element in a List.

# Description:
# Given a list of integers, write a function to find the maximum element in the list.

# Example:

# Input: lst = [3, 5, 2, 9, 6]
# Output: 9
 
# Input: lst = [-1, -2, -3, -4]
# Output: -1
 
# Input: lst = [7]
# Output: 7

def find_max_element(lst):
        max = 0
        for i in range(len(lst)):
                if lst[i]>lst[max]:
                        max = i
        return lst[max]
