# Missing Number

# Description:
# Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

# Example:

# Input: nums = [3, 0, 1]
# Output: 2
 
# Input: nums = [0, 1]
# Output: 2
 
# Input: nums = [8, 7, 6, 4, 3, 2, 0, 1]
# Output: 5

def missingNumber(nums):
    n= len(nums)
    expected_sum = n*(n+1)//2
    actual_sum = sum(nums)
    return expected_sum-actual_sum