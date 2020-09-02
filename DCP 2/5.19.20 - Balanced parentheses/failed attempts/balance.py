

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


def balance(string):
	parentheses = Stack([])
	add_parentheses = []
	# loop through every character
	i = 0
	for s in string:
		if s == "(":
			parentheses.push(s)
		if s == ")":
			# if the stack is empty
			if parentheses.pop() == None:
				add_parentheses.append([s, i])
			# cancel out the open parentheses
			else:
				parentheses.pop()
		i += 1

	# fix the string
	for parentheses in add_parentheses:
		if parentheses[1] != len(string)-1:
			string.insert(parentheses[1], ")")
		else:
			string+=")"

	print(add_parentheses)
	print(string)
	print(parentheses.stack)

balance('())')



'''
e = Stack([2,5,3])
print(e.stack)
print(e.pop())
print(e.stack)
print(e.push(0))
print(e.stack)
print(e.pop())
print(e.pop())
print(e.pop())
print(e.peek())
print(e.stack)
print(e.push(1))
print(e.stack)
'''
