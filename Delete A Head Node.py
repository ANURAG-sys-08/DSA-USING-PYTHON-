# INSERT AT TAIL OF A LINKED LIST
class node:
    def __init__(self,value):
        self.value = value
        self.next = None
# creating a function to print node
def print_ll(head):
    temp = head
    while(temp!=None):
        print(temp.value)
        temp = temp.next
    return

def take_input():
    value = int(input("Enter the value of node:- "))
    head = None
    while(value!=-1):
        newnode = node(value)
        if(head == None):
            head = newnode
        else:
            temp = head
            while(temp.next!=None):
                temp = temp.next
            temp.next = newnode
        value = int(input("Enter the value"))
    return head

def insert_at_tail(head,data):
    newNode = node(data)
    if (head is None):
        return newNode
    temp = head
    while(temp.next!=None):
        temp = temp.next
    temp.next = newNode
    return head

def delete_head_node(head):
        if head is None:
            return None
        newhead = head.next
        return newhead
head = take_input()
print_ll(head)

print("after inserting at tail")
head = delete_head_node(head) 
print_ll(head)