# INSERTION SORT

def insertion_sort(arr):
    n = len(arr)
    for card in range(1,n):
        currentCard = arr[card]
        correct_position = card-1

        while correct_position>=0:
            if (arr[correct_position]<currentCard):
                break
            else:
                arr[correct_position+1] = arr[correct_position]
                correct_position -=1
                arr[correct_position+1] = currentCard 
    return arr
print(insertion_sort([12,25,11,34,90,22]))