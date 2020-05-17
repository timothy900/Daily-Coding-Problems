''' 12/26/19 - failed solution
'''



import random


def generate_list(length, maxim, minim):
    liszt = []
    for i in range(length):
        liszt.append(random.randint(minim, maxim))
    return liszt


def remove_consecutive(liist):
    end = False
    while not end == True:
        for least in range(len(liist)):
            if least == len(liist):
                end = True
            r = 0
            # iterate through list
            for e in range(least, len(liist)):
                # sum items until get zero
                r += liist[e]
                if r == 0:
                    # remove items from liist[least] to liist[e]
                    ##############################
                    break
            if r == 0:
                break
    return liist


a = generate_list(15, 15, -15)
print(a)
a = remove_consecutive(a)
print(a)


