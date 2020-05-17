''' 4/15/2020 

This problem was asked by Microsoft.

A number is considered perfect if its digits sum up to exactly 10.

Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28.

'''

def perfect_number(n):
	num = 18
	nth = 0
	while True:

		if n == 0:
			print("0 is an invalid input.")
			num = 0
			break

		num += 1
		
		sum_digits = 0
		for digit in str(num):
			sum_digits += int(digit)

		if sum_digits == 10:
			nth += 1
			if nth == n:
				break
			
	return num

print(perfect_number(15))
