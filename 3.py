# Rectangle Pattern
# Input: n = 4, m = 5
# Output: ['*****', '*****', '*****', '*****']
 
# Input: n = 3, m = 2
# Output: ['**', '**', '**']

def generate_rectangle(n, m):
    generate_rectangle=[]
    for i in range(n):
        generate_rectangle.append("*"*m)
    return generate_rectangle
print(generate_rectangle(4,5))