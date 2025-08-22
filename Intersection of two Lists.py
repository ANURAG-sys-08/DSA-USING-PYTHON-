# Intersection of two Lists

# Description:
# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique, and you may return the result in any order.

# Example:

# Input: nums1 = [1, 2, 3], nums2 = [4, 5, 6]
# Output: []

# Input: nums1 = [1, 2, 2, 1], nums2 = [2, 2]
# Output: [2]

# Input: nums1 = [4, 9, 5], nums2 = [9, 4, 9, 8, 4]
# Output: [9, 4]

def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))