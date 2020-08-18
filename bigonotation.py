
# if we inrease input size, how many more steps
# does this function need to take?

my_list = [1, 2, 3, 4, 5]

def print_list(arr):
    for thing in arr:
        print(thing)

print_list(my_list) # Five steps

longer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print_list(longer_list) # 10 steps
# doubled input size which doubled
# the steps 1:1 ratio = linear O(n)

def nested_loop(arr):
    for thing in arr:
        for other_thing in arr:
            print(thing, other_thing)

nested_loop(my_list) #takes 25 steps
nested_loop(longer_list) #takes 100 steps
# doubled the input size
# quadrupled the steps 2:4 ratio?
# quadratic time complexity O(n^2)

nested_loop(list_100_long) # 10,000 steps
# 10x the input = 100x the steps 
# compared to an input of 10

"""Count all the steps
     Then calculate the Big O"""

def my_func(arr):
    a = 1
    b = 2
    c = a * b # First step (constant)

    for x in range(1000): # Second step (constant)
        print(x)
    
    for thing in arr: # Third step (not constant)
        x = 10
        y = 20
        z = x * y # Adding this adds three
                # More steps per item in array
        print(thing)

my_func(my_list) # 3 + 1000 + 5
my_func(longer_list) # 3 + 1000 + 10

# So with added steps in for loop 
my_func(my_list) # 3 + 1000 + 20 (4 * len(arr))
my_func(longer_list) # 3 + 1000 + 40 (4 * len(arr))

# If you get to len(arr) = TRILLIONs
# the idea of caring about 3 + 1000 is laughable

#O(3 + 1000 + 4(len(arr)))
# So Drop the constants O(len(arr))
# AKA O(n)

# (3 + 1000 + (4 * n)) ->
# (4n) ->
# (n) ->
# O(n) - linear time

# "On the order of"
# n, n^2, n^3, etc

def two_loops(arr):
    for x in range(1000000000):
        z = x * x
        print(z)

    for thing in arr:
        print(thing)

    for thing_again in arr:
        print(thing_again)

# Big O
# (1*e9) + (n) + (n) ->
# (2n) ->
# (n)

# Linke by line walkthrough
## (big_num * 2) + len(arr) + len(arr)
## (big_num * 2) + 2(len(arr))
# O(n)

# A. Problem One
def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)

# foo(6) --> 6 steps
# foo(100) --> 10 steps
# foo(10000) --> 100 steps
# Increases at slower than linear pace
# O(log(n)) # Logs are reverse exponents?

def bisect(n): # O(log(n))
    while n > 1:
        n = n/2

# 100
# 50
# 25
# 12.5
# 6.25
# 3
# 1.5
# 0.75
# Seven steps until we stopped though we
# Started at 100 2(**7) = 128, 2**6 = 64
# If we started at 200, we'd only have one extra step
# Double the input = add one step = log
# log means find me the exponent like (2**7)

# B. Problem Two
def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
                for k in range(x, x + 15):
                    sum += 1

# 1463 * (1 + (n * (15 * 1)))
# 1463 * (1 + 15n)
# 1463 + (1463 *15n)
# but it's still just O(n) at EOD

# C. Problem Three
def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')

# 1 + 1 + n/2 + 1,000
# O(n/2) or O(n * .5) # Drop the constant .5
# Still simplified to O(n), NOT O(log(n))

#Do both of these functions have the same runtime? (Notice the difference between their inputs)
## A.
def make_num_pairs(n):
    for num_one in range(n):
        for num_two in range(n):
            print(num_one, num_two)

## B.
def make_item_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)

def simple_recurse(n):
    if n <=1:
        return n
    simple_recurse(n-1)

simple_recurse(5) # 10 steps but still linear
# 5, 4, 3, 2, 1 
# then start over with 4, 3, 2, 1
# then with 3, 2, 1 etc
# Is still O(n)

def weird_recurse(n):
    if n <=1:
        return n
    simple_recurse(n-1) 
    simple_recurse(n-1)

# This is exponential 2^n
# If we did three simple_recurse(n-1)
# It would be 3^n

"""Khan Academy logarithmic guessing game
https://www.khanacademy.org/computing/computer-science/algorithms/intro-to-algorithms/a/a-guessing-game"""


"""SORTING"""
arr = [4, 0, 5, 2, 3, 1]

# O(n)
def find_num(arr, target_num):
    for x in arr:
        if x == target_num:
            return x
        return -1

find_num(arr, 1) # Have to check 6 things
# would assume worst case even if find_num(arr, 4)

arr = [1, 2, 3, 4, 5, 98, 99]
# if it's sorted you can start at the middle
# and do binary search. You're chopping it in 
# half every time so it's log(n)

"""Insertion Sorting"""
arr = [99, 98, 4, 0, 5, 2, 3, 1]
# Pseudocode for insertion sort
def insertion_sort(arr):
## start looping at the second element
    for idx in range(1, len(arr)):
        ## pick up the current element and hold it
        current_element = arr[idx]
        current_idx = idx
## while current element is less than its left sibling,
        while current_element < arr[current_idx -1]:
           #  copy left sibling to the right
            arr[current_idx] = arr[current_idx -1]
## decrement index
            current_idx -= 1
## finally, put our current element down
    arr[current_idx] == current_element
