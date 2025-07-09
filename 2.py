# # Hollow Square of side 'N'
# Problem Description:

# Input: 3
# Output: ['***', '* *', '***']
 
# Input: 5
# Output: ['*****', '*   *', '*   *', '*   *', '*****']

# Your code here
def generate_hollow_square(n):
    hollow_square=[]
    for i in range(n):
        if i==0 or i==n-1:
            hollow_square.append("*"*n)
        else:
            hollow_square.append("*" + " "*(n-2)+"*")
    return hollow_square