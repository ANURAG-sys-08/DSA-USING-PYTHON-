# Find First and Last Position of Element in Sorted Array

# Description:
# Given an array of integers nums sorted in non-decreasing order, and an integer target, find the starting and ending position of the given target value. If target is not found in the array, return [-1, -1].

# Example:

# Input: nums = [5, 7, 7, 8, 8, 10], target = 8 
# Output: [3, 4] 
# Explanation: The target 8 appears from index 3 to index 4.
 
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6 
# Output: [-1, -1] 
# Explanation: The target 6 is not found in the array.

def searchRange(nums, target):
    li = []
    if target in nums:
        for i in range(len(nums)):
            if (nums[i] == target):
                li.append(i)
    else:
        return [-1,-1]
    return [li[0],li[len(li)-1]]