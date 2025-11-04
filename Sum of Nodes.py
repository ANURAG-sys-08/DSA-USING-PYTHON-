# # Sum of Nodes

# Description:
# Given the root of an N-ary tree, return the sum of all the nodes' values. An N-ary tree is a tree in which each node has at most N children.

# Example:

# Input: root = Node(1, [Node(3, [Node(5), Node(6)]), Node(2), Node(4)])
# Output: 21
 
# Input: root = Node(10, [])
# Output: 10
 
# Input: root = Node(1, [Node(2, [Node(3)]), Node(4)])
# Output: 10

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def sum_of_nodes(root):
    if root is None:
        return 0
    total = root.val
    for child in root.children:
        total = total + sum_of_nodes(child)
    return total


