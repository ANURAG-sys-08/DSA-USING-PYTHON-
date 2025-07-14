# Hollow Right Triangle
# Example:

# Input: 4
# Output: ['*', '**', '* *', '****']
 
# Input: 5
# Output: ['*', '**', '* *', '*  *', '*****']
def generate_hollow_right_angled_triangle(n):
    li = []
    for i in range(1,n+1):
        if i == 1:
            li.append("*")
        elif i == n:
            li.append("*"*n)
        else:
            li.append("*" + " "*(i-2) + "*")
    return li