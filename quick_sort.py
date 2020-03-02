def quick_sort(A) :
    #call of the recursive function
    quick_sort2(A, 0, len(A) - 1)
#recursive function
def quick_sort2(A, low, hi) :
    # if there is more than one item to be sorted
    #then divide the list using partition function
    if low < hi :
        p = partition(A, low, hi)
        #for the items on left of the pivot we call quicksort
        #recursively
        quick_sort2(A, low, p - 1)
        #for the items on right of the pivot we call quicksort
        #recursively
        quick_sort2(A, p + 1, hi)

def get_pivot(A, low, hi) : 
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid] :
        if A[mid] < A[hi] :
            pivot = mid
    elif A[low] < A[hi] :
        pivot = low
    return pivot

def partition(A, low, hi) :
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi + 1) :
        if A[i] < pivotValue :
            border += 1
            A[i], A[border] = A[border], A[i]
    
    A[low], A[border] = A[border], A[low]

    return (border)


list = [50, 54, 10, 100, 102, 2, 1, 5]
quick_sort(list)
for i in range(0, len(list)) :
    print(list[i])