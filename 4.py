# # Right Angled Triangle
# Example:

# Input: 3
# Output: ['*', '**', '***']
 
# Input: 5
# Output: ['*', '**', '***', '****', '*****']

def generate_triangle(n):
    gen_triangle=[]
    for i in range(n):
        for j in range(n):
            gen_triangle.append("*"*(j+1))
        break
    return gen_triangle