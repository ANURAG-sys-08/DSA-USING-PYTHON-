# # Right Angled Triangle with Numbers
# # Example:

# # Input: 5
# # Output: ['1', '22', '333', '4444', '55555']
 
# # Input: 3
# # Output: ['1', '22', '333']

def generate_number_triangle(n):
    gen_num = []
    for i in range(1, n+1):
        row = str(i) * i
        gen_num.append(row)
    return gen_num
