''' March 5 2020
This problem was asked by Microsoft.

Given an array of numbers arr and a window of size k,
print out the median of each window of size k starting
from the left and moving right by one position each time.

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]
Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
Recall that the median of an even-sized list is
the average of the two middle numbers.
'''


import random
from collections import OrderedDict


def generate_list(maxim, minim, length):
    arr = []
    for i in range(length):
        arr.append(random.randint(minim, maxim))
    return arr


def calc_median(numbers):
    #organize list
    numbers.sort()
    #remove duplicates
    numbers = list(dict.fromkeys(numbers))
    print(numbers)
    if len(numbers) % 2 != 0: #odd number
        median = numbers[round(len(numbers)/2)-1]
    else: #even number
        median = (numbers[round(len(numbers)/2)-1] + numbers[round(len(numbers)/2)] )/2
    return median


def medians(array, q):
    for e in range(len(array)-q+1):
        part = array[e:e+q]
        print(part)
        print(calc_median(part))

'''
Parameters:
maximum number, 
minimum number,
length of list,
window size 'k', 
'''
def go(ma, mi, le, k):
    a = generate_list(ma, mi, le)
    print(a)
    medians(a, k)

# (maximum number, minimum number, length of list, window size)
go(10, -10, 10, 2)
