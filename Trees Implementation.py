# Tree implementation using list
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