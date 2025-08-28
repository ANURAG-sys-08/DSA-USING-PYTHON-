# Search a 2D Matrix

# Description:
# You are given an m x n integer matrix matrix with the following two properties:
# Each row is sorted in non-decreasing order.The first integer of each row is greater than the last integer of the previous row.Write a function that takes an integer target and returns True if target is in matrix, or False otherwise. You must solve this problem with a time complexity better than O(m * n)

# Example:

# Input: matrix = [[1, 3, 5, 7], 
#                  [10, 11, 16, 20], 
#                  [23, 30, 34, 60]], target = 13
# Output: False
 
# Input: matrix = [[1, 3, 5, 7], 
#                  [10, 11, 16, 20], 
#                  [23, 30, 34, 60]], target = 3
# Output: True

def search_matrix(matrix, target):
    li = []

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            li.append(matrix[i][j])
    
    if target in li:
        return True
    return False
     