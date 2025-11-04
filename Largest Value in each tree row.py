# Largest Value in each tree row

# Description:

# Given the root of an N-ary tree, return a list of the largest value in each row of the tree. An N-ary tree is a tree where each node can have at most N children.

# Example:

# root = Node(1, [
#     Node(3, [Node(5), Node(6)]),
#     Node(2),
#     Node(4)
# ])
# Output : [1,4,6]

from collections import deque
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
def largest_values(root):
    if not root:
        return []
    result = []
    queue = deque([root])  
    while queue:
        level_size = len(queue)
        max_val = float('-inf')
        for _ in range(level_size):
            node = queue.popleft()
            max_val = max(max_val, node.val)
            for child in node.children:
                queue.append(child)
        result.append(max_val)
    return result
