# FIND THE DIAMETER OF A TREE.
# THIS SOLUTION IS NOT OPTIMISED❌

from helper import print_binary_tree

def height(root):
    if root is None:
        return 0
    left_height = height(root.left)
    righ_height = height(root.right)
    height_of_tree = 1 + max(left_height,righ_height)
    return height_of_tree

def diameter_of_tree(root):
    if root is None:
        return 0
    left_height = height(root.left)
    right_height = height(root.right)

    left_diameter = diameter_of_tree(root.left)
    right_diameter = diameter_of_tree(root.right)
    ans = max(left_diameter,right_diameter,(left_height + right_height))
    
    return ans