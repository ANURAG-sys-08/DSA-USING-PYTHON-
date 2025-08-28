# Matrix obtained by Rotation or not?

# Description:
# You are given two n x n binary matrices mat and target. Your task is to determine whether it is possible to make mat equal to target by rotating mat in 90-degree increments (clockwise). You can rotate mat by 90, 180, or 270 degrees, or leave it unchanged

# Example:

# Input: mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]], target = [[1, 1, 1], [0, 1, 0], [0, 0, 0]]
# Output: True
 
# Input: mat = [[0, 1], [1, 1]], target = [[1, 0], [0, 1]]
# Output: False

from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate_90(matrix):
            n = len(matrix)
            rotated = [[0] * n for _ in range(n)]
            for i in range(n):
                for j in range(n):
                    rotated[j][n - 1 - i] = matrix[i][j]
            return rotated

        for _ in range(4):
            if mat == target:
                return True
            mat = rotate_90(mat)
        return False
