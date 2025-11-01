# TRAVERSAL IN TREES

# PRE-ORDER TRAVERSAL IN TREE(FIRST PRINT ROOT AND THEN CHILD)
def pre_order(root):
    if root is None:
        return
    print(root.data,end = " ")
    pre_order(root.left)
    pre_order(root.right)

# POST-ORDER TRAVERSAL IN TREE(FIRST PRINT CHILD THEN PARENT)
def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.data,end = " ")

# INORDER TRAVERSAL IN TREE(FIRST LEFT CHILD THEN PARENT THEN RIGHT CHILD)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root,end=" ")
    inorder(root.right)
