## Space Complexity- As my input size increaes, how
# much *more* space do we take up? 
# not counting the original memory taken up
# aka as the functin runs, does it occupy more memory?
# How much more stuff does it put into memory as we
# increase the array size?

arr = [1, 2, 3, 4, 5]

arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def counter(arr):
    total = 0
    for thing in arr:
        total += 1

    return total

# Time Complexity - 
## Linear
## Double input, double the steps we took
## O(n)

# Space complexity - 
## Double input, no extra space
## We only made one variable (total)
## Constant O(1)

def duplicate(arr):
    copy_arr = []
    for thing in arr:
        copy.arr.append(thing)
    return copy_arr

# Time Complexity - 
## Linear O(n)

# Space Complexity - 
## Also linear O(n)
## because when we append we're taking up new space

def times_table(n):
    times_table = []
    
    for i in range(n):
        row = []

        for j in range(n):
            row.append(i * j)
        
        times_table.append(row)
    return times_table

# Time Complexity
# Space Complexity
## Both O(n^2)

# Oftentimes you trade time and space
# But also they're often the same

# space == memory

matrix = [[1, 2, 3, 4, 5], 
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15]]

first_row = matrix[0]
one = first_row[0]