# if you just search once, don't need to sort
# if you search a lot, them sort b/c it saves time

# return index
def linear_search(arr, target):
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    if len(arr) == 0:
        return -1
    low = 0
    high = len(arr)-1
    mid = round(high/2)
    if arr[mid] == target:
        return mid
    elif arr[low] == target:
        return low
    elif arr[high] == target:
        return high
    else:
        while arr[mid] != target and target in arr:
            if target in arr[low:mid]:
                mid = round(mid/2)

            elif target in arr[mid:high]:
                mid = round(((high-mid)/2)+mid)
        
    return mid
    return -1  # not found

arr1 = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
print(binary_search(arr1, 8))
