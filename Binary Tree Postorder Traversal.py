# Binary Tree Postorder Traversal

# Description:
# Given the root of a binary tree, return the postorder traversal of its nodes' values. In postorder traversal, the nodes are visited in this order: first the left subtree, then the right subtree, and finally the root node.

# Example:

# Input:
#         1
#          \
#           2
#          /
#         3
 
# Output: [3, 2, 1]

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def postorder_traversal(root):
    if root is None:
        return []
    
    result = []
    result += postorder_traversal(root.left)   # 1️⃣ visit left subtree
    result += postorder_traversal(root.right)  # 2️⃣ visit right subtree
    result.append(root.val)                    # 3️⃣ visit root node
    return result
