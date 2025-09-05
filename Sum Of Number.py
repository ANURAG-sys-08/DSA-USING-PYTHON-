def sum_of_natural_numbers(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        shortanswer = sum_of_natural_numbers(n-1)
        answer = shortanswer + n
    return answer
print(sum_of_natural_numbers(15))