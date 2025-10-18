# Remove Duplicate Elements from Linked List

# Description:
# Given the head of a sorted singly linked list, write a function to remove all duplicates such that each element appears only once. The linked list is sorted in non-decreasing order, so all duplicates will be adjacent. Return the linked list sorted as well.

# Example:

# Input: head = [1 -> 1 -> 2 -> 3 -> 3]
# Output: [1 -> 2 -> 3]
 
# Input: head = [1 -> 1 -> 1 -> 2 -> 3]
# Output: [1 -> 2 -> 3]
 
# Input: head = [1 -> 2 -> 3]
# Output: [1 -> 2 -> 3]

# Definition for singly linked list node.

from helper import print_ll,make_ll

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

head = make_ll([1,1,1,2, 3])
print_ll(head)

def delete_duplicates(head):
    temp  = head
    while temp.next:
        if (temp.val == temp.next.val):
            temp.next = temp.next.next
        else:
            temp = temp.next
        return head

head1 = delete_duplicates(head)
print_ll(head1)









