# Binary Tree Preorder Traversal

# Description:
# Given the root of a binary tree, return the preorder traversal of its nodes' values. In preorder traversal, the nodes are visited in this order: root node first, then left subtree, and then right subtree.

# Example: 
# Input:
#         1
#          \
#           2
#          /
#         3
 
# Output: [1, 2, 3]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root):
    if root is None:
        return []
    
    result = [root.val] 
    result += preorder_traversal(root.left)   
    result += preorder_traversal(root.right)  
    return result