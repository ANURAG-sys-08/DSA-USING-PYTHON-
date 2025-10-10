# Description:
# You are given the head of a singly linked list and an integer k. Your task is to find the index of the first node in the linked list whose value equals k. If no such node exists, return -1.

# The index starts at 0 for the head of the list.

# Example:

# Input: head = [1 -> 2 -> 3 -> 4], k = 3
# Output: 2
 
# Input: head = [1 -> 2 -> 3 -> 4], k = 5
# Output: -1
 
# Input: head = [], k = 3
# Output: -1

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_index(head, k):
    temp = head
    index = 0
    while temp is not None:
        if temp.val == k:
            return index
        temp = temp.next
        index += 1
    return -1  

def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage
head = build_linked_list([1, 2, 3, 5])
print(find_index(head , k = 4))




