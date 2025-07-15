# Line Equation
# Problem Description:

#     You are given the slope m and the y-intercept b of a line, along with a value x.
#     Your task is to calculate and return the value of y using the equation of a line in slope-intercept form:
#         y=mx+b
def calculate_y(slope, intercept, x):
    y = slope*x + intercept
    return y