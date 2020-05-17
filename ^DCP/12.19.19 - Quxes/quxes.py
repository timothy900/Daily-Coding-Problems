'''
Daily Coding Problem - Dec 7, 2019
Easy
'''

'''
This problem was asked by Facebook.

On a mysterious island there are creatures known as
Quxes which come in three colors: red, green, and blue.
One power of the Qux is that if two of them are standing
next to each other, they can transform into a single
creature of the third color.

Given N Quxes standing in a line, determine the
smallest number of them remaining after any possible
sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'],
it is possible to end up with a single Qux through the
following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
'''

'''
Made by Timothy on 12/19/19
First one solved
'''

import random

quxes = []
colors = ['R', 'G', 'B']


def pickColor():
    return colors[random.randint(0,2)]


def makeQuxes(y):
    quxes.clear()
    for i in range(y):
         quxes.append(pickColor())
    return quxes


def transformQuxes(x):
    # generate a list of random quxes
    quxesList = makeQuxes(x)
    while True:
        while True:
            try:
                print(quxesList)
                #iterate through list of quxes until finds two unequal items
                for i in range(len(quxesList)):
                    colors = ['R', 'G', 'B']
                    if not quxesList[i] == quxesList[i+1]:
                        # remove color of qux and next qux from colors list
                        colors.remove(quxesList[i])
                        colors.remove(quxesList[i+1])
                        # turn colors, which is now a single-item list, into a string
                        color = ""
                        color = color.join(colors)
                        # remove both quxes, set the remaining color to the new qux
                        quxesList[i] = color
                        quxesList.remove(quxesList[i+1])
                        # restart for loop
                        end = False
                        break
            except IndexError:
                end = True
                break
        if end:
            break


print("Sequence: Iterate through the list from left to right")
print("until the current item is not equal to the next one. ")
print("After applying the transformation, restart the sequence.")
print("")
transformQuxes(5)
print("")
transformQuxes(10)
print("")
transformQuxes(15)


