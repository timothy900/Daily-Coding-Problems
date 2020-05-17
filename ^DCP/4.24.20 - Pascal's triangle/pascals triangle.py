''' Started on 4.24.20, retried on 4.25.20

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of 
integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum 
of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
'''


def pascals_triangle(n_rows):

	triangle = []

	for i in range(n_rows):
		row = []

		for e in range(i+1): # adding one because i starts at 0
			num = 1

			try:
				if not e == 0:
					prev_row = triangle[i-1]
					num = prev_row[e-1] + prev_row[e] 
			except IndexError:
				pass

			row.append(num)

		triangle.append(row)

	return triangle[-1]


print(pascals_triangle(15))


# 4.24.20 ORIGINAL CODE BELOW:

'''
def pascal_triangle(n_rows):
	
	triangle = [[1]] # 0th row

	for i in range(1, n_rows): # i'th row
		row = []
		
		for e in range(i+1): # e'th number in row
			num = 0
			
			if e == 0 or e == i+1: # if first or last number in layer
				num = 1
			else: # compute the sum
				try:
					num = triangle[i-1][e] + triangle[i][e+1]
				except IndexError:
					num = triangle[i][e]

			row.append(num)

		triangle.append(row)
		print(i)

	return triangle


print(pascal_triangle(4))
'''