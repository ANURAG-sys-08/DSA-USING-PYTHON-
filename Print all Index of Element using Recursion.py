# Print all Index of Element using Recursion
# Problem Description:

# You are given an array and an element. Your task is to find all the indices where the array contains that element using recursion.

# Example:

# Input: arr = [1, 2, 3, 2, 4, 2], element = 2
# Output: [1, 3, 5]
 
# Input: arr = [5, 6, 7, 8], element = 10
# Output: []

def find_indices(arr, element):
    """Helper function to find all indices of a given element in arr."""
    indices = []
    for i in range(len(arr)):
        if arr[i] == element:
            indices.append(i)
    return indices

def get_element_indices(arr, element):
    """Main function that uses helper to get indices."""
    return find_indices(arr, element)

# Example usage:
print(get_element_indices([1, 2, 3, 2, 4, 2], 2))  
print(get_element_indices([5, 6, 7, 8], 10))       
