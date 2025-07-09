# Pyramid Pattern
# Example:

# Input: 3
# Output: ['  *  ', ' *** ', '*****']
 
# Input: 5
# Output: ['    *    ', '   ***   ', '  *****  ', ' ******* ', '*********'

def generate_pyramid(n):
    for i in range(n):
        for j in range(n):
            