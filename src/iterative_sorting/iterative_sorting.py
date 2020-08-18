# TO-DO: Complete the selection_sort() function below

###Algorithm
"""
1. Start with current index = 0

2. For all indices EXCEPT the last index:

    a. Loop through elements on right-hand-side 
    of current index and find the smallest element

    b. Swap the element at current index with the
    smallest element found in above loop"""

def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # loop over the rest of the elements
        for n in range(cur_index, len(arr)):
            # compare each element with the 
            # element at smallest index
            if arr[n] < arr[smallest_index]:
                smallest_index = n
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr
        
        # current = arr[i]
        # Min = arr[i]
        # for var in range(i+1, len(arr)-1):
        #     if arr[var] < Min:
        #         Min = arr[var]
        # a = current
        # arr[i] = Min
        # Min = a
        # cur_index = i
        # smallest_index = cur_index
        # for var in range(i, len(arr)-1):
        #     if arr[smallest_index] > arr[var]:
        #         arr[smallest_index] = arr[var]
        #     arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    # return arr
arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(selection_sort(arr))
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here


        # TO-DO: swap
        # Your code here

# TO-DO:  implement the Bubble Sort function below

### Algorithm
"""
1. Loop through your array
    - Compare each element to its neighbor
    - If elements in wrong position (relative to each other, swap them)
2. If no swaps performed, stop. Else, go back to the element at index 0 and repeat step 1.
"""

def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for idx in range(len(arr)-1):
            num1 = arr[idx]
            num2 = arr[idx + 1]
            if num1 > num2:
                arr[idx], arr[idx+1] = arr[idx+1], arr[idx]
                swapped = True
    return arr

arr = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]

print(bubble_sort(arr))
'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
