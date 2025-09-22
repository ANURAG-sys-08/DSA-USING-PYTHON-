# LENGTH OF LINKED LIST USING RECURSSION

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

def printll(head):
    temp = head
    while(temp!=None):
        print(temp.value)
        temp = temp.next
    return
def lengthofll(head):
    temp = head
    ans = 0
    while(temp!= None):
        temp = temp.next
        ans = ans + 1
    return ans

def length_Of_ll_recurssion(head):
    temp = head
    if (temp==None):
        return 0
    ans_from_recurssion = length_Of_ll_recurssion(head.next)
    
    return 1 + ans_from_recurssion

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)

n1.next = n2
n2.next = n3
n3.next = None
printll(n1)
length = lengthofll(n1)
print(length)

Recursion_length = length_Of_ll_recurssion(n1)
print(Recursion_length)