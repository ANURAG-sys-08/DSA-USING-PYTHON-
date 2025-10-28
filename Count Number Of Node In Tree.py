# Define a function to count the number of nodes in a tree

def count_node(root):
    if root == None:
        return 0
    numb_of_node = 1
    for eachchild in root.children:
        numb_of_node = numb_of_node + count_node(eachchild)
        
    return numb_of_node 