# LETS SEE HOW TO PRINT LINKED LIST
class node:
    def __init__(self,value):
        self.value = value
        self.next = None

# create the nodes
first = node(10)
second = node(20)
third = node(30)

# link the nodes
first.next = second
second.next = third
third.next = None
head = first

# function to print a linked list 
def print_ll(head):
    temp = head
    while(temp!=None):
        print(temp.value)
        temp = temp.next
    return

# calling the function that prints a linked list and giving it head as a argument
print_ll(head= head)
