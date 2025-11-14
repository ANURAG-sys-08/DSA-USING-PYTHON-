class BSTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def print_BST(root):
    if root is None:
        return
    print(root.left.data)
    print_BST(root.data,end ="")
    print(root.right)
