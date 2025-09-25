# INSERT A NODE AT A GIVEN INDEX OF THE LINKED LIST
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


def take_input_at_head(head,data):
    newNode = node(data)
    newNode.next = head
    head = newNode
    return head

def insert_at_index(head,data,index):
    if (index==0):
        return take_input_at_head(head,data)
    
    newNode = node(data)
    count = 0
    temp = head
    while temp is not None and count <index-1:
        temp = temp.next
        count += 1
    if (temp is None):
        print("PLEASE CHECK THE INDEX")
    newNode.next = temp.next
    temp.next = newNode
    return head
head = take_input()
print_ll(head)

print("AFTER INSERTING AT INDEX->")
head = insert_at_index(head,34,4)
print_ll(head)