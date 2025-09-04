def factorial(num):
    if num == 1 or num == 0:
        return 1 
    ans = num*factorial(num-1)
    return ans