# Program to print an binary tree
class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)

# function to print the binary tree
def print_binary_tree(root):
    if root is None:
        return
    
    print(root.data,end=" ")
    
    # 
    if root.left is not None:
        print(f"L->{root.left.data} R -> {root.right.data}", end=", ")
    else:
        print(f"L-> None R-> None",end=",")

    # 
    if root.right is not None:
        print(f"L->{root.left.data} R -> {root.right.data}")
    else:
        print(f"L-> None R-> None")
    
    print_binary_tree(root.left)
    print_binary_tree(root.right)

# calling the print function 
print_binary_tree(root)