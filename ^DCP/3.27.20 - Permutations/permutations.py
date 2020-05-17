'''
March 27, 2020

This problem was asked by Twitter.

A permutation can be specified by an array P,
where P[i] represents the location of the element
at i in the permutation. For example, [2, 1, 0]
represents the permutation where elements at the
index 0 and 2 are swapped.

Given an array and a permutation,
apply the permutation to the array.
For example, given the array ["a", "b", "c"]
and the permutation [2, 1, 0],
return ["c", "b", "a"].
'''

import random

#P
P = ["a", "b", "c", "d", "e", "f", "g"]


# returns indices of list p 
def indices(p):
    r = []
    for i in range(len(p)):
        r.append(i)
    return r


def permutations(lis):
    # shuffle indices
    ind = indices(lis)
    random.shuffle(ind)
    print("permutation:")
    print(ind)
    new_lis = []
    # put all items in lis(or P) into the corresponding index in ind
    for e in ind:
        new_lis.append(lis[e])
    return new_lis

print(indices(P))
print(P)
print("")
print(permutations(P))
