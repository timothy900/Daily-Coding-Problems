''' 
Tried a few weeks ago
Continued and finished on 5/18 - 5/19/20

When I initially tried doing this problem, I didn't know about
the stack data structure and couldn't solve it. 
After after a while, I decided to retry and search for a solution
on YouTube then found this video: https://www.youtube.com/watch?v=CCyEXcNamC4
It taught me that I could use the stack data structure, which I just learned a 
few days before from brilliant.org's data structures course.
This is my fourth re-do of this code.

#

This problem was asked by Facebook.

Given a string of parentheses, 
find the balanced string that can be produced 
from it using the minimum number of insertions and deletions. 
If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". 
Given "))()(", you could return "()()()()".
'''


# implement a stack data structure
class Stack:
	def __init__(self, list_):
		self.stack = list_
	
	def push(self, inp):
		self.stack.append(inp)
		return inp

	def pop(self):
		if len(self.stack) > 0:
			removed = self.stack.pop()
			return removed
		else: return None
	
	def peek(self):
		if len(self.stack) > 0:
			return self.stack[-1]
		else: return None


# balance the parentheses
def balance(string):
	str_stack = Stack([])
	add_parentheses = []
	# identify which parentheses to add to the string and where to add them
	for i, s in enumerate(string):
		if s == "(": 
			str_stack.push(s)
		if s == ")":
			if str_stack.peek() == "(":
				# cancel out the open parentheses
				str_stack.pop()
			else:
				str_stack.push(")")
				add_parentheses.append([i, "("])

	# for the opening parentheses at the end of the string
	for p in str_stack.stack:
		if p == "(":
			add_parentheses.append([-1, ")"])

	# balance the string based on the information in add_parentheses
	# turn string to list
	string = list(string)
	for i in range(len(add_parentheses)):
		# start from the end
		item = add_parentheses[-(i+1)]
		# add corresponding parentheses and index
		if item[0] == -1:
			string += item [1]
		else:
			string.insert(item[0], item[1])
	# turn list back to string
	string = ''.join(string)

	return string


print("\n")
parentheses = '(()))())(('
print("unbalanced:\n", parentheses)
print("balanced:\n", balance(parentheses))
print("\n")
parentheses = input("Try it: ")
print("unbalanced:\n", parentheses)
print("balanced:\n", balance(parentheses))
print("\n")
	

