# Implement the Binary Tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data,
        self.left = None,
        self.right = None

# creating the root node
root = BinaryTreeNode(1)

# creating its childrens
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)

