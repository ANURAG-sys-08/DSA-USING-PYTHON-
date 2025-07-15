# Number of Rounds of Lift

# Problem Description:

#     You are given n, the total number of people, and capacity, 
#     the maximum number of people the lift can carry at a time.
#     All people want to go from the ground floor to the top floor.
#     Your task is to calculate the number of rounds the lift has to make to transport all the people to the top floor.
import math
def calculate_lift_rounds(n, capacity):
    rounds = math.ceil(n/capacity)
    return rounds
print(calculate_lift_rounds(10,3))

