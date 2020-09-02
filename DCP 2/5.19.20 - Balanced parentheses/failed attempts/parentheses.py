'''
This problem was asked by Facebook.

Given a string of parentheses, find the balanced string that can be produced from it using the minimum number of insertions and deletions. If there are multiple solutions, return any of them.

For example, given "(()", you could return "(())". Given "))()(", you could return "()()()()".
'''

def balance(parentheses):
	# remove parentheses that cancel
	
	# add-to list
	a_list = list(parentheses)
	# remove-from list
	r_list = list(parentheses)

	loop = True
	while loop:

		# count if there are still parentheses that can be canceled
		openers = r_list.count("(")
		closers = r_list.count(")")

		# if no more can be cancelled
		openers_0 = openers == 0
		closers_0 = closers == 0

		if openers >= 1 and closers >= 1:

			iteration = -1
			for p in r_list:

				print(r_list)

				iteration += 1
				if p == "(":
					# find closing parentheses closest to end
					for i in range(len(r_list)):
						i += 1
						if r_list[-i] == ")":
							# cancel the two parentheses
							r_list.pop(-i)
							r_list.pop(iteration)

							'''
							# add to the add-to list#################
							a_list += ")"
							'''

							# restart search
							print(f"{iteration}: )")
							print(r_list, a_list, -i)
							break

				elif p == ")":
					# find opening parentheses closest to start
					for j in range(len(r_list)):
						if r_list[j] == "(":
							# cancel the two parentheses
							r_list.pop(j)
							r_list.pop(iteration)

							'''
							# add to the add-to list#################
							a_list[:0] = "("
							'''
	
							# restart search
							print(f"{iteration}: (")
							print(r_list, a_list, j)
							break

		# if either one of openers or closers are 0
		elif openers_0 ^ closers_0:
			if openers_0:
				for g in range(closers):
					# add an open parentheses at the start
					a_list[:0] = "("
					r_list.remove(")")
					print("openers_0")

			else:
				for h in range(openers):
					# add a closing parentheses at the end
					a_list.append(")")
					r_list.remove("(")
					print("closers_0")

		else:
			loop = False

	balanced = ''.join(a_list)

	return balanced


#print(balance("))()"))

print(balance("())(("))

'''
def balance(parentheses):
	
	# count open parntheses and closed parentheses
	openers = parentheses.count("(")
	closers = parentheses.count(")")
	# add open/closed parentheses until equal
	for i in range(abs(openers-closers)):
		if openers > closers:
			parentheses = ""
		else:
			parentheses = ""

	return parentheses
'''


