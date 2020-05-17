''' 5/7/2020

This problem was asked by Amazon.

Given a pivot x, and a list lst, 
partition the list into three parts.

The first part contains all elements 
in lst that are less than x
The second part contains all elements 
in lst that are equal to x
The third part contains all elements in 
lst that are larger than x
Ordering within a part can be arbitrary.

For example, given x = 10 and lst = [9, 12, 3, 5, 14, 10, 10], 
one partition may be [9, 3, 5, 10, 10, 12, 14].
'''


def pivot(x, lst):
	lists = [[], [], []]
	for item in lst:
		if item < x:
			lists[0].append(item)
		elif item == x:
			lists[1].append(item)
		else:
			lists[2].append(item)

	finished = []
	for l in lists:
		finished += l

	return finished


lst = [4,7,1,4,6,5,635,5]
print(pivot(5, lst))

