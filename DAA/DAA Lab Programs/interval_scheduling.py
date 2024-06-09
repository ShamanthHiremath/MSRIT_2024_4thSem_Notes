intervals = [(4, 5), (0, 2), (2, 7), (1, 3), (0, 4)] 

# sorting the intervals 
intervals.sort(key=lambda x: x[1]) 

print(intervals) 
# counting the events 
count = 0
# keeping track of ending of intervals 
end = 0
# list of the intervals in which person will attend the events 
answer = [] 

# traversing the list of intervals 
for interval in intervals: 
	# starting time of next interval will >= ending 
	# time of previous interval 
	if(end <= interval[0]): 
		# update the and 
		end = interval[1] 
		# increment the count by one 
		count += 1
		# insert the non-conflict interval in the list 
		answer.append(interval) 

# print statements will print non-conflict 
# intervals count as well intervals 
print("The maximum events a person can attend is : ", count) 
print("List of intervals in which person will attend events: ", answer)