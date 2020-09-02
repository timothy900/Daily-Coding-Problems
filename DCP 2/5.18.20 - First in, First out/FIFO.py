''' 5/18/2020
This problem was asked by Apple.

Implement a queue using two stacks. 
Recall that a queue is a FIFO (first-in, first-out) 
data structure with the following methods: enqueue, 
which inserts an element into the queue, and dequeue, 
which removes it.
'''
class queue:
	def __init__(self, items):
		# 0th index is the first in
		self.items = items

	def enqueue(self, item):
		self.items.append(item)

	def dequeue(self):
		item = self.items[0]
		self.items.pop(0)
		return item


line = queue([2, 4, 5])
print(line.items)
# add 0 to end of the line
line.enqueue(0)
print(line.items)
# remove item at beginning of line
line.dequeue()
print(line.items)
# remove item from beginning of line, then add it to the end
line.enqueue(line.dequeue())
print(line.items)
# remove item at the beginning of the line
line.dequeue()
print(line.items)

