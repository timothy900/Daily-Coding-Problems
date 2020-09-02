''' 5/21/20
Notes:
- if there is more than one period where the building is busiest, it returns the last(most recent) one
- the busiestPeriod() function assumes the following:
	- that the data is organized by timestamp in ascending order
	- that the last item in the dataset is not the answer(the busiest period)


Problem:

This problem was asked by Amazon.

You are given a list of data entries that represent entries and 
exits of groups of people into a building. An entry looks like this:

{"timestamp": 1526579928, count: 3, "type": "enter"}

This means 3 people entered the building. An exit looks like this:

{"timestamp": 1526580382, count: 2, "type": "exit"}

This means that 2 people exited the building. timestamp is in Unix time.

Find the busiest period in the building, that is, the time with the most 
people in the building. Return it as a pair of (start, end) timestamps. 
You can assume the building always starts off and ends up empty, i.e. 
with 0 people inside.
'''

# data entries that i made up. the number of people in the building starts and ends at 0
# data is organized by timestamp in ascending order
# note: i actually used the UNIX time at the time i made this
data = [{"timestamp": 1590047062, "count": 2, "type": "enter"},
		{"timestamp": 1590047760, "count": 6, "type": "enter"},
		{"timestamp": 1590047846, "count": 2, "type": "exit"},
		{"timestamp": 1590047965, "count": 4, "type": "exit"},
		{"timestamp": 1590048043, "count": 5, "type": "enter"},
		{"timestamp": 1590048161, "count": 4, "type": "exit"},
		{"timestamp": 1590048374, "count": 3, "type": "exit"},
		{"timestamp": 1590048473, "count": 6, "type": "enter"},
		{"timestamp": 1590048669, "count": 6, "type": "exit"},
		]

# notes:
# this function assumes the following:
# 	that the data is organized by timestamp in ascending order
#	that the last item in the dataset is not the answer/the busiest period
# if there is more than one period where the building is busiest, it returns the last one
def busiestPeriod(data):
	# keep track of the number of people in the building
	n_people = 0
	# stores the highest number of people and the timestamps of the period
	highest_n = [0, 0, 0]

	for i, item in enumerate(data):
		# add/subtract people
		if item["type"] == "enter":
			n_people += item["count"]
		else:
			n_people -= item["count"]
		# store the highest amount of people, 
		# with its time stamp and the timestamp of the next item
		if highest_n[0] < n_people:
			highest_n = [n_people, item["timestamp"], data[i+1]["timestamp"]]

	return highest_n[1], highest_n[2]
	

print(busiestPeriod(data))

