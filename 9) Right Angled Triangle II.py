# Right Angled Triangle II
# Example:

# Input: 4
# Output: ['   *', '  **', ' ***', '****']
 
# Input: 3
# Output: ['  *', ' **', '***']

def generate_right_angled_triangle(n):
    li = []
    for i in range(1,n+1):
        sp1 = " "*(n-i)
        sp2 = "*"*i
        row = sp1 + sp2
        li.append(row)
    return li
