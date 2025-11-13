# Same Tree

# Description:
# Given the roots of two binary trees p and q, write a function to check if they are the same or not. Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

# Example:

# Input:
#     Tree 1:
#         1
#        / \
#       2   3
 
#     Tree 2:
#         1
#        / \
#       2   3
 
# Output: True

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def is_same_tree(p, q):
    if p is None and q is None:
        return True
    if p is None or q is None:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)    