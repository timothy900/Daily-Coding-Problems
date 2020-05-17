''' 4/11/2020

This problem was asked by Google.

You are in an infinite 2D grid where 
you can move in any of the 8 directions:

 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)

You are given a sequence of points and 
the order in which you need to cover the points. 
Give the minimum number of steps in which you can achieve it. 
You start from the first point.

Example:

Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). 
It takes one more step to move from (1, 1) to (1, 2).

'''


import random


class Grid:

	def __init__(self, x, y):
		# Parameters:
		# x = Width of grid
		# y = Height of grid
		self.x = x
		self.y = y


	def generate_points(self, length):
		# Parameters:
		# length = Number of random points to generate
		points_ = []
		for i in range(length):
			xy = (random.randint(0, self.x - 1), random.randint(0, self.y - 1))
			points_.append(xy)
		return points_


	def min_steps(self, length):
		# Parameters: 
		# length = Length of list of points to be generated
		points = self.generate_points(length)
		print(points)

		distance = 0
		for e in range(len(points)-1):
			# Calculate the distance between the current and next point
			x_distance = abs(points[e][0] - points[e+1][0])
			y_distance = abs(points[e][1] - points[e+1][1])
			
			# The distance is the greater difference
			if x_distance >= y_distance:
				distance += x_distance
			else: 
				distance += y_distance
		
		return distance


# create a 10x10 grid
grid = Grid(10, 10)
print(grid.min_steps(3))
