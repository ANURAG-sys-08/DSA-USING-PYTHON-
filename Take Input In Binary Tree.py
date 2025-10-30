# Take input into the binary tree
# This approch is not level wise🤡

from helper import BinaryTreeNode,print_binary_tree

# creating the function to create node
def take_input_binary_tree():
    data = int(input("Enter the data "))

    if (data == -1):
        return None
    else:
        node = BinaryTreeNode(data)

        # for taking input in left node
        print(f"Enter the value in Left Node of {node.data}")
        node.left = take_input_binary_tree()

        # for taking input in right node
        print(f"Enter the value in right node of {node.data}")
        node.right = take_input_binary_tree()

# calling the take input function
root = take_input_binary_tree()

# Printing the Binary Tree
print_binary_tree(root)