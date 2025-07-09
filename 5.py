# Inverted Right Angled Triangle
# Example:
# Input: 3
# Output: ['***', '**', '*']
# Input: 5
# Output: ['*****', '****', '***', '**', '*']

def generate_inverted_triangle(n):
    gen_triangle=[]
    for i in range(n):
        for j in range(n,0,-1):
            gen_triangle.append("*"*(j))
        break
    return gen_triangle
