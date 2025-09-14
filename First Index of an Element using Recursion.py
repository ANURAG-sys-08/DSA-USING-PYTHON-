# First Index of an Element using Recursion

# Problem Description:

# You are given an array and an element. Your task is to find the first index where the array contains that element using recursion. If the element is not found, return -1.

# Example:

# Input: arr = [1, 2, 3, 2, 4, 2], element = 2
# Output: 1
 
# Input: arr = [5, 6, 7, 8], element = 10
# Output: -1

def find_first_index(arr, element):
    if (len(arr) == 0):
        return -1
    if (arr[0] == element):
        return 0
    
    ansFromRecurssion = find_first_index(arr[1:],element)
    
    if (ansFromRecurssion == -1):
        return ansFromRecurssion
    else:
        return ansFromRecurssion + 1 
    