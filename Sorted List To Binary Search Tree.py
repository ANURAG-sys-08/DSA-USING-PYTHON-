# Write a code to convert a sorted list into BST
class BSTnode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def ConvertListToBST(l1):
    if len(l1) ==0 :
        return None
    mid = len(l1)//2
    rootdata = l1[mid]
    root = BSTnode(rootdata)
    root.left = ConvertListToBST(l1[:mid])
    root.right = ConvertListToBST(l1[mid+1:])
    return root

# *NOTE* This code will work but it will only work for sorted array 