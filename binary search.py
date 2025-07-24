def binary_search(arr,target):
    size = len(arr)
    lower_bound  = 0
    upper_bound = size-1

    while (lower_bound<=upper_bound):
        mid = (lower_bound+upper_bound)//2
        if (arr[mid] == target):
            return mid
        elif (arr[mid]>target):
            upper_bound = mid - 1
        elif (arr[mid]<target):
            lower_bound = mid + 1
    return -1

print(binary_search([10,20,30,40,50],50))