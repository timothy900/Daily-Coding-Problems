""" 5/21/20 - 5/22/20 
There was a bug that was causing the runtime to grow exponentially. 
It was due to the way I added items to the list of active cells.

Problem:

This problem was asked by Dropbox.

Conway's Game of Life takes place on an infinite 
two-dimensional board of square cells. Each cell is either 
dead or alive, and at each tick, the following rules apply:

Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.

Implement Conway's Game of Life. It should be able to be initialized 
with a starting list of live cell coordinates and the number of steps 
it should run for. Once initialized, it should print out the board 
state at each step. Since it's an infinite board, print out only the relevant coordinates, 
i.e. from the top-leftmost live cell to bottom-rightmost live cell.

You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).
"""

import os
import time

class Board:
	def __init__(self, cell_coordinates):
		# Parameters:
		# cell_coordinates: coordinates of the first cells
		# e.g.: [[x1, y1], [x2, y2], ... [xn, yn]]
		self.cell_coords = cell_coordinates

	# count the active neighbours of a cell
	def count_neighbours(self, cell):
		neighbours = [[-1, -1], [0, -1], [1, -1], [-1, 0],\
					  [1, 0], [-1, 1], [0, 1], [1, 1]]
		n_neighbours = 0
		for neighbour in neighbours:
			if [cell[0]+neighbour[0], cell[1]+neighbour[1]] in self.cell_coords:
				n_neighbours += 1
		return n_neighbours

	# returns the dead cells that should be born
	def born(self, n_required_neighbors):
		# Parameters:
		# n_required_neighbors: required number of active neighbors for cell to be born

		# all empty neighbors of every cell
		empty_cells = []
		neighbours = [[-1, -1], [0, -1], [1, -1], [-1, 0],\
						  [1, 0], [-1, 1], [0, 1], [1, 1]]

		# put all the empty neighbours of the currently active cells in empty_cells
		for cell in self.cell_coords:
			# look at every neighbor
			for neighbour in neighbours:
				# coordinates of neighbour cell
				neighbour_cell = [cell[0]+neighbour[0], cell[1]+neighbour[1]]
				# if neighbour cell is empty
				if not neighbour_cell in self.cell_coords:
					# if not already in empty_cells
					if not neighbour_cell in empty_cells:
						# put in empty cells
						empty_cells.append(neighbour_cell)

		born_cells = []
		# count which neighbour should be born
		for empty_cell in empty_cells:
			# count amount of neighbors
			n_neighbours = self.count_neighbours(empty_cell)
			if n_neighbours == n_required_neighbors:
				born_cells.append(empty_cell)
		return born_cells

	def update(self):
		new_cells = []
		neighbours = [[-1, -1], [0, -1], [1, -1], [-1, 0],\
					  [1, 0], [-1, 1], [0, 1], [1, 1]]
		# for each cell
		for cell in self.cell_coords:
			# count amount of neighbors
			n_neighbours = 0
			for neighbour in neighbours:
				if [cell[0]+neighbour[0], cell[1]+neighbour[1]] in self.cell_coords:
					n_neighbours += 1

			# rule 1 - Any live cell with less than two live neighbours dies.
			if n_neighbours < 2:
				# don't put cell in new_cells, because it dies
				pass
			# rule 2 - Any live cell with two or three live neighbours remains living.
			elif n_neighbours == 2 or n_neighbours == 3:
				# put in new_cells, because cell stays alive
				new_cells.append(cell)
			# rule 3 - Any live cell with more than three live neighbours dies.
			elif n_neighbours == 3:
				# die
				pass
			# rule 4 - Any dead cell with exactly three live neighbours becomes a live cell.
			# rule 4 is implemented when when replacing the existing cells with the new ones

		self.cell_coords = new_cells + self.born(3)

	def draw(self):
		cell_coordinates = self.cell_coords
		# figure out dimensions of board
		# find min x and max x
		max_x = max([coordinate[0] for coordinate in cell_coordinates])
		min_x = min([coordinate[0] for coordinate in cell_coordinates])
		# find min y and max y
		max_y = max([coordinate[1] for coordinate in cell_coordinates])
		min_y = min([coordinate[1] for coordinate in cell_coordinates])
		x_dimension, y_dimension = abs(min_x-max_x) + 1, abs(min_y-max_y) + 1

		for y in range(min_y, min_y + y_dimension):
			# print every row
			row = ''
			for x in range(min_x, min_x + x_dimension):
				# if coordinate is lit/on/occupied
				if [x, y] in cell_coordinates:
					row += "*"
				else: row += "."
	
			print(row)


def clear():
	os.system('cls')
def update_screen(board):
	clear()
	board.draw()
	board.update()
def main_loop(pause_time, board, n_steps=None):
	start_time = time.time()
	i = 0
	if n_steps == None:
	# run infinitely
		while True:
			update_screen(board)

			time.sleep(pause_time)
	else:
	# run for n_steps amount of steps
		for s in range(n_steps):
			update_screen(board)
			print(i)
			i += 1

			time.sleep(pause_time)

	# stop after 1 second - for recording fps
	# if (time.time() - start_time) >= 1:
	# 	print((time.time() - start_time))
	# 	break



# different starting configurations of boards

# glider
# board = Board([[1,2], [2, 2], [3, 2], [3, 1], [2, 0]])

# repeating pattern
# board = Board([[1, 2], [2, 2], [3, 2],\
# 			   [1, 3], [2, 3], [3, 3],\
# 			   [1, 4], [2, 4], [3, 4]])

# repeating pattern
board = Board([[1, 0], [2, 0], [3, 0],\
			   [0, 1], [4, 1],\
			   [0, 2], [4, 2],\
			   [0, 3], [4, 3],\
			   [1, 4], [2, 4], [3, 4]])

# seed? - grows into large thing
# board = Board([[1, 0], [2, 0],\
# 			  [0, 1], [1, 1],\
# 			  [1, 2]])

# number of steps it should run for
n_steps = 300
main_loop(.1, board, n_steps=n_steps)

# run for infinity
# main_loop(.2, board)
