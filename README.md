# QUICK SORT Algorithm

1. how it works
2. Running time Complexity
3. Implementation Using Python

Quick sort is a sorting algorithm that follows the divide and conquer rule. It is recursive i.e it keeps calling itself until the list is sorted


* After selecting an element as pivot, which is the last index of the array in our case, we divide the array for the first time.
* In quick sort, we call this partitioning. It is not simple breaking down of array into 2 subarrays, but in case of partitioning, the array elements are so positioned that all the elements smaller than the pivot will be on the left side of the pivot and all the elements greater than the pivot will be on the right side of it.
* And the pivot element will be at its final sorted position.
* The elements to the left and right, may not be sorted.
* Then we pick subarrays, elements on the left of pivot and elements on the right of pivot, and we perform partitioning on them by choosing a pivot in the subarrays[1](https://www.studytonight.com/data-structures/quick-sort)

Example

In the array {52, 37, 63, 14, 17, 8, 6, 25}, we take 25 as pivot. So after the first pass, the list will be changed like this.

{6 8 17 14 25 63 37 52}

Hence after the first pass, pivot will be set at its position, with all the elements smaller to it on its left and all the elements larger than to its right. Now 6 8 17 14 and 63 37 52 are considered as two separate sunarrays, and same recursive logic will be applied on them, and we will keep doing this until the complete array is sorted[2](https://www.studytonight.com/data-structures/quick-sort).


## Big Oh Analysis

The worst case for quick sort is `O(n*n)`

Its average case is `O(n log n)`

And its performance depends on pivot selection.

## Python code

```py
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

# Testing
list = [50, 54, 10, 100, 102, 2, 1, 5]
quick_sort(list)
for i in range(0, len(list)) :
    print(list[i])
```

output

```script
1
2
5
10
50
54
100
102
```
