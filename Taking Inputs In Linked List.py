# creat a class node
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




# first = node(1)
# second = node(2)
# third = node(3)

# first.next = second
# second.next = third
# third.next = None

first = take_input()
print_ll(first)