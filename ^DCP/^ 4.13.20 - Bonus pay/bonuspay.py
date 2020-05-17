
def bonus_pay(employees):
	bonus = []

	for i in range(len(employees)):
		
		if not i == len(employees)-1:
			next_ = employees[i+1]

		employee = employees[i]
		# first employee
		if i == 0: 
			if employee > next_:
				bonus.append(2)

			else:
				bonus.append(1)

		prev = employees[i-1]
		# last employee
		if i == len(employees) - 1: 
			if employee > prev:
				bonus.append(bonus[-1]+1)
			elif employees[i] == prev:
				bonus.append(bonus[-1])
			else:
				bonus.append(bonus[-1]-1)

		# middle employees
		if not i == 0 and not i == len(employees)-1: 
			if employee > prev:
				if employee > next_:
					bonus.append(bonus[i-1]+2) # 1 3 2
				else:
					bonus.append(bonus[i-1]+1) # 1 2 2, 1 2 3
			if employee < prev:
				if employee > next_:
					bonus.append(bonus[i-1]-1) # 3 2 1
				else:
				 	bonus.append(bonus[i-1]-2) # 3 1 2

	return bonus



employees_code = [10, 40, 200, 1000, 60, 30]

print(bonus_pay(employees_code))
