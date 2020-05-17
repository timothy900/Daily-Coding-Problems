# Started 3.28.20
# Finished 3.29.20(with help of gitHub)
'''
This problem was asked by Twitter.

A strobogrammatic number is a positive
number that appears the same after being
rotated 180 degrees. For example,
16891 is strobogrammatic.

Create a program that finds all
strobogrammatic numbers with N digits.
'''


################## this fuction is from GitHub:
################## https://github.com/shiyanhui/Algorithm/blob/master/LeetCode/Python/246%20Strobogrammatic%20Number.py
def isStrobogrammatic(num):
        table, n = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}, len(num)
        for i in range((n >> 1) + 1):
            if num[i] not in table or table[num[i]] != num[n - i - 1]:
                return False
        return True
###################
################### the following code(below) is by me 


def strobo(N):
    count = 0
    for i in range((10**N)):
        i = str(i)
        if isStrobogrammatic(i) == True and len(i) == N:
            print(i)
            count += 1
    print(f"amount: {count}")


strobo(3)


# my attempt at strobogrammatic thing. i gave up and looked up a way to do it
'''
        # 6, 9, 8, 1, 0
        if "6" in i: # find 9's in
            for e in range(len(i)):
                if i[(len(i)) - e] == 

        if "9" in i: # find 6's in same index as 9's
        
        if "8" in i: # find 8's

        if "1" in i: # find 1's

        if "0" in i: # find 0's
        
'''

        
