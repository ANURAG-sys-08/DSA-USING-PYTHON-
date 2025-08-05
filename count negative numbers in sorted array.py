# Count negative numbers in a sorted matrix

# Description:
# You are given an m x n matrix grid where each row and column is sorted in non-increasing order. Your task is to return the number of negative numbers present in the matrix.

# Example:

# Input: grid = [[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]] 
# Output: 7 
# Explanation: There are 7 negative numbers in the matrix.
 
# Input: grid = [[3, 2], [1, 0]] 
# Output: 0 
# Explanation: There are no negative numbers in the matrix.

def countNegatives(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]<0:
                count+=1
    return count

countNegatives([[4, 3, 2, 1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]])