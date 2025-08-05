# Minimum in Rotated Sorted Array

# Description:
# Given a sorted array that has been rotated, find the minimum element in the array. The array was originally sorted in ascending order and then rotated at some pivot.

# Example:

# Input: nums = [4, 5, 6, 7, 0, 1, 2] 
# Output: 0 
# Explanation: The minimum element is 0.

# Input: nums = [11, 13, 15, 17] 
# Output: 11 
# Explanation: The array was not rotated, and the minimum element is the first element.

def findMin(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
                left = mid + 1
        else:
            right = mid
        return nums[left]