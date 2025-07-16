# Remove Duplicate in a List

# You are given a list of integers. 
# Write a Python program that removes any duplicate elements from the list and returns a new list with only unique elements.
# The order of elements in the list should be maintained.

# Example:

# Input: lst = [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]

# Input: lst = [4, 5, 5, 4, 6, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(lst):
    li = []
    for elem in lst:
        if elem not in li:
            li.append(elem)
    return li
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))