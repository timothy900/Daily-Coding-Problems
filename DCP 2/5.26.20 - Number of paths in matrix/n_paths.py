''' 5/26/2020 

Notes: 
This video from khan academy helped me solve the problem: 
https://www.khanacademy.org/math/math-for-fun-and-glory/puzzles/brain-teasers/v/path-counting-brain-teaser
At first, i thought that all you needed to do was take the factorial of M and N.
After a few minutes, i just searched for a solution.
I tried to write recursive and non-recursive versions of the function.
Only the non-recursive one worked.

# Problem:

This problem was asked by Facebook.

There is an N by M matrix of zeroes. 
Given N and M, write a function to count the 
number of ways of starting at the top-left 
corner and getting to the bottom-right corner. 
You can only move right or down.

For example, given a 2 by 2 matrix, you should 
return 2, since there are two ways to get to the bottom-right:

Right, then down
Down, then right

Given a 5 by 5 matrix, there are 70 ways to get to the bottom-right.

'''


# non-recursive way:
def n_ways(n, m):

	n_ways_matrix = []
	for i in range(n):
		row = []
		for j in range(m):
			try:
				item = n_ways_matrix[i-1][j] + row[j-1]
				row.append(item)
			except:
				if i == 0 and j == 0:
					row.append(0)
				elif i > 0 or j > 0:
					row.append(1)
		n_ways_matrix.append(row)

	return n_ways_matrix[n-1][m-1]


# recursive way:
def n_ways_recursive(n, m):
	if n == 1 and m == 1:
		return 0
	elif n == 1:
		return m-1
	elif m == 1:
		return n-1
	else:
		top = n_ways_recursive(n-1, m)
		left = n_ways_recursive(n, m-1)
		return top + left


# print("recursive: ", n_ways_recursive(5, 5))
print("non-recursive: ", n_ways(5, 5))
print("non-recursive: ", n_ways(500, 500))
