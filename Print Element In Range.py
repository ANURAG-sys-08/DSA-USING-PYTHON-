# You have a Binary Search Tree and a range, lets say = [20,50] so you have to print all the elements btw this range. 

def print_bst_elem_in_range(root,low,high):
    if root is None:
        return

    if (low<root.data):
        print_bst_elem_in_range(root.left,low,high)

    if (low<=root.data<high):
        print(root.data,end=" ")
    
    if (high>root.data):
        print_bst_elem_in_range(root.right,low,high)