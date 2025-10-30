# Traverse A Tree
class treenode:
    def __init__(self,Data):
        self.data = Data
        self.child = []

root = treenode("Boss")
node1 = treenode("(l1 A)")
node2 = treenode("(l1 B)")
node3 = treenode("(l1 C)")
node4 = treenode("(l1 D)")

root.child.append(node1)
root.child.append(node2)
root.child.append(node3)
node3.child.append(node2)
# Print an tree
def print_tree(root):
    if root is None:
        return
    
    print(root.data,end=" ")

    for eachchild in root.child:
        print(eachchild.data,end=" ")

    print()
    
    for _ in root.child:
        print_tree(_)

print_tree(root)

# PRE-ORDER TRAVERSAL (WHERE PARENT COMES FIRST AND THEN CHILD)
def pre_order_traverse(root):
    print(root.data,end = " ")

    for eachchild in root.child:
        pre_order_traverse(eachchild)

pre_order_traverse(root)
# POST-ORDER TRAVERSAL (WHERE CHILD COMES FIRST AND THEN PARENT)
print()
def post_order_traverse(root):
    for eachchild in root.child:
        post_order_traverse(eachchild)
    print(root.data,end=" ")
post_order_traverse(root)