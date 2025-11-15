# # Search in a Binary search Tree 

# Description:
# You are given the root of a binary search tree (BST) and an integer val. Your task is to find the node in the BST whose value equals val and return the subtree rooted with that node. If such a node does not exist, return null.
# A binary search tree (BST) is a binary tree in which for every node, all elements in the left subtree are smaller, and all elements in the right subtree are larger than the node's value.
    
# Example:
# Input:
#         4
#        / \
#       2   7
#      / \
#     1   3
# val = 2
 
# Output:
#       2
#      / \
#     1   3
 

# Input: 
#         4
#        / \
#       2   7
#      / \
#     1   3
# val = 5
 
# Output: None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_bst(root, val):
    if root is None:
        return 
    if (root.val == val):
        return root
    if (root.val>val):
        return search_bst(root.left,val)
    elif(root.val<val):
        return search_bst(root.right,val)