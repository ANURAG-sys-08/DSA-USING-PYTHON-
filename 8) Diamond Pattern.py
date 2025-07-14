# Diamond Pattern
# Example:

# Input: 3
# Output: ['  *  ', ' *** ', '*****', ' *** ', '  *  ']
 
# Input: 5
# Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********', ' ******* ', '  *****  ', '   ***   ', '    *    ']

def generate_diamond(n):
    li = []
    for i in range(n):
        sp1 = " " * (n - (i + 1))
        row = "*" * (2 * i + 1)
        row1 = sp1 + row + sp1
        li.append(row1)
    for i in range(n - 2, -1, -1):
        sp1 = " " * (n - (i + 1))
        row = "*" * (2 * i + 1)
        row1 = sp1 + row + sp1
        li.append(row1)
    return li
print(generate_diamond(5))
