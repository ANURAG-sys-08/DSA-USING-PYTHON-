# Count Nodes in a N-arry Tree

# Description:
# You are given the root of an N-ary tree. Your task is to write a function to count the total number of nodes in the tree.

# An N-ary tree is a tree in which a node can have at most N children.

# Example:

# Input:
#       1
#     / | \
#    2  3  4
#       |
#       5
 
# Output: 5
 
 
# Input:
#       1
#     / | \ \
#    2  3  4  5
 
# Output: 5

# Definition for a Node in an N-ary tree.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def count_nodes(root):
    if root is None:
        return 0
    no_of_node = 1
    for child in root.children:
        no_of_node = no_of_node + count_nodes(child)
    return no_of_node
