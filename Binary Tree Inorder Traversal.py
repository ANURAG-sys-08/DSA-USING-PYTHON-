# Binary Tree Inorder Traversal
# Description:
# Given the root of a binary tree, return the Inorder traversal of its nodes' values. Inorder traversal of a binary tree means visiting the left subtree, the root node, and then the right subtree recursively. The task is to implement this without using any in-built functions like inorder_traversal from Python's libraries.

# Example:
# Input:
#         1
#          \
#           2
#          /
#         3 
# Output: [1, 3, 2]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    result, stack = [], []
    current = root
    
    while current or stack:
        while current:              
            stack.append(current)
            current = current.left
        
        current = stack.pop()       
        result.append(current.val)
        
        current = current.right     
    
    return result

