# Count Even and Odd Numbers in a List

# You are given a list of integers. 
# Write a Python program that counts and returns the number of even and odd numbers in the list.

# Example:

# Input: lst = [1, 2, 3, 4, 5]
# Output: (2, 3)
def count_even_odd(lst):
    even_count = 0
    odd_count = 0
    empty_tuple = ()
    for i in lst:
        if i%2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    new_tuple = empty_tuple + (even_count,odd_count)
    return new_tuple

print(count_even_odd([4, 2, 4, 4, 4]))
# NOTE : After seeing the solution i realised there is another way to do it which basically just `return even_count, odd_count`.
# Which will ultimately return a tuple 