# Print A Tree
class tree:
    def __init__(self,data):
        self.data = data
        self.children = []

# Define the root node
root = tree(1)

# Defining the child nodes
children1 = tree(2)
children2 = tree(3)
children3 = tree(4)

# Connect children nodes to the root node
root.children.append(children1)
root.children.append(children2)
root.children.append(children3)

# print tree but its not a good approch❌
def print_tree(root):
    if (root==None):
        return
    print(root.data)
    for eachchild in root.children:
        print(eachchild.data)

print_tree(root)

print("//////////////////////////////")


# Lets print the tree with recursion , i.e. correct method✅
def print_tree_detailed(root):
    if root == None:
        return
    # To print the data of root node
    print(root.data,end=":")


    for eachchild in root.children:
        print(eachchild.data, end=" ")

    print()
    # to print the children of child nodes
    for eachchild in root.children:
        print_tree_detailed(eachchild)

print_tree_detailed(root)