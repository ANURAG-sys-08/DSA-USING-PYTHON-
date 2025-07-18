# Rotate a List

# You are given a list of integers and an integer k. Write a Python function to rotate the list to the right by k positions without using slicing. A rotation shifts elements from the end of the list to the front.

# Example:

# Input: lst = [1, 2, 3, 4, 5], k = 2
# Output: [4, 5, 1, 2, 3]

# Input: lst = [10, 20, 30, 40, 50], k = 3
# Output: [30, 40, 50, 10, 20]

def rotate_list(lst, k):
    ls = []
    ls1 = []
    ls2 = []
    k = k % len(lst)
    for i in range(len(lst)):
        if i>=len(lst)-k:
            ls.append(lst[i])
        else:
            ls1.append(lst[i])
    ls2 = ls + ls1
    return ls2

print(rotate_list([10, 20, 30, 40, 50],6))