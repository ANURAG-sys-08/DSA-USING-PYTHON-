# Sandglass Pattern
# Example:
# Input: 3
# Output: ['*****', ' *** ', '  *  ', ' *** ', '*****'] 
# Input: 4
# Output: ['*******', ' ***** ', '  ***  ', '   *   ', '  ***  ', ' ***** ', '*******']

def generate_sandglass(n):
    li = []
    for i in range(n):
        beg = " "*i
        mid = (2*n-1-2*i)*"*"
        end = " "*i
        li.append(beg+mid+end)

    for i in range(n-2,-1,-1):
        beg = " "*i
        mid = (2*n-1-2*i)*"*"
        end = " "*i
        li.append(beg+mid+end)

    return li
print(generate_sandglass(5))
        