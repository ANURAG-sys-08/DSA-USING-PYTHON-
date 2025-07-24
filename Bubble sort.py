#-------------bubble sort-----------------

def bubble_sort(arr):
    n = len(arr)
    print(n)
    for passes in range(0,n):
        for j in range(0,n-1-passes):
            if (arr[j]>arr[j+1]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
    return arr
print(bubble_sort([23,45,78,12,34]))