'''
This problem was asked by Amazon.

Given a linked list, remove all consecutive nodes that sum to zero.
Print out the remaining nodes.

For example, suppose you are given the input
3 -> 4 -> -7 -> 5 -> -6 -> 6.
In this case, you should first remove
3 -> 4 -> -7, then -6 -> 6, leaving only 5.
'''

'''
Made by Timothy on 12/27-28/19
'''

import random


# create a list -of a given length- of random numbers
# the numbers in the list range from a given minimun and maximum number.
def generate_list(length, maxim, minim):
    li = []
    for i in range(length):
        li.append(random.randint(minim, maxim))
    return li


# go through items in a list, starting from a given index
# until their sum equals zero.
# then remove all the first items, starting from the
# given index, that sum to zero.
# repeat until there are no more sums of zero starting from the given index
def find_sum_zero(lis, ind):
    while True:
        starting_length = len(lis[ind:])
        p = 0
        # amount of items iterated through
        n = 0
        # sum of first n items
        s = 0
        # reset deleted_sum to false
        deleted_sum = False
        # iterate through list lis, starting from given index
        for item in lis[ind:]:
            # count how many iterations
            n += 1
            # add item to sum
            s += item

            p = len(lis[ind:])
            
            # check if sum = 0
            # remove sum only if the current number in the list is not equal to zero
            if s == 0 and not item == 0:
                print(f"Removed {lis[ind:ind+n]} from list. Index = {ind}")
                # remove first n items in lis, starting from given index
                del lis[ind:ind+n]
                print(lis)
                deleted_sum = True
                p = len(lis[ind:])
                # exit for loop
                break
        # after deleting sum of zero starting from index, or going through list:
        # if deleted sum of zero, check if deleted starting index. if not, repeat.
        if deleted_sum:
            # check if index is present in list
            if ind >= len(lis):
                # end loop if given index till end of list was deleted
                break
        # but if iterated through entire list, starting from index, without
        # finding sum, end while loop
        elif p == starting_length:
            break
    # done


# run the function find_sum_zero(),
# increasing the given starting index each time whenever
# the function doesn't find the sum of zero in the list
# until it reaches the end of the list
def remove_sum_zeros(ls):
    for i in range(len(ls)):
        find_sum_zero(ls, i)
    # return ls


x = generate_list(20,20,-20)
print(x)
remove_sum_zeros(x)
