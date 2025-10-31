from helper import BinaryTreeNode, print_binary_tree
from collections import deque

def take_input_level_wise():
    root_data = int(input("Enter the value in root node -> "))

    if root_data == -1:
        return None

    root = BinaryTreeNode(root_data)
    queue = deque([root])

    while queue:  # ✅ loop until queue is empty
        current_node = queue.popleft()

        # take input in the left node
        left_child_data = int(input(f"Enter the data in left node of {current_node.data} -> "))
        if left_child_data != -1:
            left_child = BinaryTreeNode(left_child_data)
            current_node.left = left_child
            queue.append(left_child)

        # take input in the right node
        right_child_data = int(input(f"Enter the data in right node of {current_node.data} -> "))
        if right_child_data != -1:
            right_child = BinaryTreeNode(right_child_data)
            current_node.right = right_child
            queue.append(right_child)

    return root  # ✅ move outside loop


# Driver code
root = take_input_level_wise()
print_binary_tree(root)
