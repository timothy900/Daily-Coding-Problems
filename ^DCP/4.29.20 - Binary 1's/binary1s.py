''' 4/29/2020

This problem was asked by Facebook.

Given an integer n, find the next biggest integer 
with the same number of 1-bits on. For example, 
given the number 6 (0110 in binary), return 9 (1001).
'''


def n1_digits(n):
	
	# parameter converted to binary
	binary_n = str(bin(n))
	n1 = 0
	# count the amount of 1's in binary_n
	for digit in binary_n:
		if digit == "1":
			n1 += 1

	# loop until condition is met
	while True:
		
		# convert to binary after adding one
		n += 1
		b_n2 = str(bin(n))
		# count the amount of 1's again
		n2 = 0
		for d in b_n2:
			if d == "1":
				n2 += 1

		# if condition is met, end loop
		if n2 == n1:
			return n
			break


print(n1_digits(6))
