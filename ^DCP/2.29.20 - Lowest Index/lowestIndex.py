''' February 29, 2020

This problem was asked by Amazon.

Given a sorted array arr of distinct integers,
return the lowest index i for which arr[i] == i.
Return null if there is no such index.

For example, given the array [-5, -3, 2, 3],
return 2 since arr[2] == 2. Even though arr[3] == 3,
we return 2 since it's the lowest index.
'''

import random

# make array
def generate_array(num_of_items):
    min_number = -10
    max_number = 10
    array = []
    for i in range(num_of_items):
        array.append(random.randint(min_number,max_number))
    return array

# search array
def search_array(arr):
    e = 0
    for i in arr:
        if i == e:
            e = i
            break
        else:
            e += 1
        if e == len(arr):
            e = None
    return e

ee= generate_array(10)
print(ee)
print(search_array(ee))
