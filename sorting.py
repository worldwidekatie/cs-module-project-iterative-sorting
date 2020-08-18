arr = [98, 99, 5, 2, 3, 1, 0, 4]
# Pseudocode for insertion sort
def insertion_sort(arr):
## start looping at the second element
    for idx in range(1, len(arr)):
        ## pick up the current element and hold it
        current_element = arr[idx]
        current_idx = idx
## while current element is less than its left sibling,
        while current_idx > 0 and current_element < arr[current_idx -1]:
           #  copy left sibling to the right
            arr[current_idx] = arr[current_idx -1]
## decrement index
            current_idx -= 1
## finally, put our current element down
        arr[current_idx] = current_element


insertion_sort(arr)
print(arr)

# time complexity of insertion sort?
# at worst case we're swapping n times
# n * (1 + 1 + (n * 2) + 1)
# n * (3+ 2n)
# 3n + 2n^2
# O(n + n^2)
# O(n^2)
# Insertion sort is not very good.