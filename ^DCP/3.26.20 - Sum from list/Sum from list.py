'''
March 26, 2020

This problem was asked by Goldman Sachs.

Given a list of numbers L, implement a method sum(i, j)
which returns the sum from the sublist L[i:j]
(including i, excluding j).

For example, given L = [1, 2, 3, 4, 5], sum(1, 3)
should return sum([2, 3]), which is 5.

You can assume that you can do some pre-processing.
sum() should be optimized over the pre-processing step.
'''

import random

# L
L = [2,8,1,9,23,9,4,7,56,2,8,4]

# sum all items in liszt[start:end] (including start, excluding end)
def summ(liszt, start, end):
    s = 0
    for i in liszt[start:end]:
        s += i
        print(i)
    print("")
    print(f"sum: {s}")

summ(L,2,6)
