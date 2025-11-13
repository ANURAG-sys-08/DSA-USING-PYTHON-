# Maximum Depth of a Binary Tree

# Description:
# Given the root of a binary tree, return its maximum depth. The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example:

# Input:
#         3
#        / \
#       9   20
#          /  \
#         15   7
 
# Output: 3

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root):
    if root is None:
        return 0
    depth = 1
    dpth = max(max_depth(root.left),max_depth(root.right))
    depth = depth + dpth
    return depth

