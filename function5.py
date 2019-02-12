'''
Function 5
Team:
Dominic
Guang Jun
Jun Ming
Xiu Qi
Yeo Han, Jordan
'''
"""
1. Takes in age_range() + func2 + func3 + func4
			= age_range + acceptedcountry + acceptedlikesdislikes + acceptedbooks
			= <list:names> + <list:names> + <dict:names+points> + <dict:names+points>

2. Check if users in acceptedcountry exists in acceptedlikesdislikes.
	2a. If exists, append key:value to newDict.
	2b. Else, move to (4).

3. Check if users in (2) exists in acceptedbooks.
	3a. If exists, add value to respective key in newDict.
	3b. Else, move to (4).

4. Check if newDict has keys:values.
	4a. If it has values, move to (5).
	4b. Else, print("There are no matches available for you at the moment.\nPlease try again later.")

5. Sort newDict by values and return the top 3 usernames with the highest points values.
	5a. If same values, take the username nearest to age.
"""
def processAgeRange(userdict, maindict):
	# Check if userdict_acceptableAge is in maindict_age <for range>
	# If yes, store name into list
	# Return list
	return True


def processMatches(acceptedcountry, likesdislikes, books, userdict, maindict):
	country = []
	for c in acceptedcountry:								# Formatting for acceptedcountry list.
		country.append("".join(c))

	print acceptedcountry
	print likesdislikes
	print books
	print userdict
	print maindict

	combine_matches = {}
	for i in country:
		if i in likesdislikes:
			combine_matches[i] = likesdislikes.get(i)
		if i in books:
			combine_matches[i] = books.get(i)
	print(combine_matches)

	if bool(combine_matches):													#4. Check if newDict has keys:values.
			top_3 = pointsRanking(combine_matches,userdict,maindict,country,likesdislikes,books)	# If it has values, return bestMatched()
			return top_3
	else:																# Else, return empty dictionary
		print("There are no matches available for you at the moment. Please try again later.")
		return []


def pointsRanking(matched_dict,userdict,maindict,country,likesdislikes,books):
	points_ranked_names = []
	points_ranked_values = []
	for name, points in sorted(matched_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):	# Sort dict by values in desc order with Lambda
		points_ranked_names.append(name)
		points_ranked_values.append(points)

	#Scenario: Top 5 matches might have the same points/values.
	#Objective: For those with same points, sort by priority order (if user exists in both likesdislikes and books dictionary).
#priority_sort = priorityRanking(points_ranked_names,points_ranked_values,country,likesdislikes,books)
	#Objective: For those with same points, sort by abs() between user's age and maindict's avg age range.
	sorted_match = sortRanking(points_ranked_names,points_ranked_values,userdict,maindict,country,likesdislikes,books)

	return sorted_match[:3]


def priorityRanking(namelist,likesdislikes,books,userdict,maindict):
	priority_list = []
	for i in namelist:  # For user in namelist:
		if i in likesdislikes and i in books:  # 2. Check if users in acceptedcountry exists in acceptedlikesdislikes and acceptedbooks.
			priority_list.append(i)

	print("namelist:",namelist)
	print("likesdislikes:",likesdislikes)
	print("books:",books)

	if len(priority_list) > 1:
		priority = ageChecker(priority_list, userdict, maindict)
		return priority
	elif len(priority_list) == 1:
		return priority_list
	else:
		return namelist


def sortRanking(namelist,pointslist,userdict,maindict,country,likesdislikes,books):
	"""
	1. Given namelist & pointslist.
	2. Check if pointslist[0] == pointslist[i].
		2a. If yes, check if pointslist[0] == pointslist[i++]. Repeat.
		2b. If no, store the index number.
			2bi. Check if pointslist[i++] == pointslist[(i++1)]
		2c. Slice list and push to ageChecker().
		2d. ageChecker() returns same list of names, but sorted by abs() between user's age and maindict's avg age range.
	"""	
	x = 0		# Set index to 0
	y = 1		# Set index to 1
	z = 1		# Set index to 1
	count = 0																	# Iterate pointslist and check if first index
	while count < len(pointslist):												#  is same as second index, then third index, etc. 
		if x < len(pointslist) and pointslist[0] == pointslist[x]:
			x += 1
		elif x+y < len(pointslist) and pointslist[x] == pointslist[x+y]:
			y += 1
		elif x+y+z < len(pointslist) and pointslist[x+y] == pointslist[x+y+z]:
			z += 1
		else:
			break
		count += 1
		
	sliced_list1 = namelist[0:x]		# Group values of unique first index.
	sliced_list2 = namelist[x:x+y]		# Group values of unique second index.
	sliced_list3 = namelist[x+y:x+y+z]	# Group values of unique third index.

	if len(sliced_list1) > 1:									# If there is more than 1 count of first index,
		rank_priority = priorityRanking(sliced_list1,likesdislikes,books,userdict,maindict)
		print("Priority SLiced 1: ", rank_priority)
		print("Sliced List:",sliced_list1)
		if sliced_list1 != rank_priority:
			for name in rank_priority:
				print(rank_priority)
				print(name)
				sliced_list1.remove(name)
		print("Sliced List:",sliced_list1)
		if len(rank_priority) > 1 and len(rank_priority) <= 3 and len(sliced_list1) == 1:
			priority1 = ageChecker(rank_priority,userdict,maindict)
			priority1.append(sliced_list1)
		elif len(rank_priority) > 1 and len(rank_priority) <= 3 and len(sliced_list1) > 1:
			priority1 = ageChecker(rank_priority, userdict, maindict)
			names1 = ageChecker(sliced_list1, userdict, maindict)
			for i in names1:
				priority1.append(i)
		elif len(rank_priority) <= 1 and len(sliced_list1) > 1:
			priority1 = []
			priority1.append(rank_priority)
			names1 = ageChecker(sliced_list1, userdict, maindict)
			for i in names1:
				priority1.append(i)
		else:
			names1 = ageChecker(sliced_list1, userdict, maindict)
			return names1
		return priority1
		#DONE

		"""if len(names1) <= 3 and len(sliced_list1) == 1:
			names1 = ageChecker(sliced_list1,userdict,maindict)		# Call ageChecker() and sort names by abs() between user's age and maindict's avg age range.
			if len(names1) <= 3 and len(sliced_list2) == 1:			# If first index count is not more than 3 and second index count has only 1,
				for i in sliced_list2:
					names1.append(i)								# Append names of of second index count to names of first index count.
			elif len(names1) <= 3 and len(sliced_list2) > 1:		# Elif first index count is not more than 3 and second index count is more than 1,
				names2 = ageChecker(sliced_list2,userdict,maindict)	# Call ageChecker() and sort names by abs() between user's age and maindict's avg age range.
				for i in names2:
					names1.append(i)								# Append names of of second index count to names of first index count.
				#DONE"""
	
	elif len(sliced_list2) > 1:									# Elif there is more than 1 count of second index AND there is only 1 count of first index,
		rank_priority = priorityRanking(sliced_list2,likesdislikes,books,userdict,maindict)
		for name in rank_priority:
			sliced_list2.remove(name)
#names1 = ageChecker(sliced_list1,userdict,maindict)		# Call ageChecker() and sort names by abs() between user's age and
		names2 = ageChecker(sliced_list2,userdict,maindict)		#  maindict's avg age range individually for first and second index.
		for i in rank_priority:
			sliced_list1.append(i)
		for i in names2:
			sliced_list1.append(i)									# Append names of of second index count to names of first index count.
		return sliced_list1
		#DONE

	elif len(sliced_list3) > 1:									# Elif there is more than 1 count of third index AND there is only 1 count of first & second index,
		rank_priority = priorityRanking(sliced_list3,likesdislikes,books,userdict,maindict)
		for name in rank_priority:
			sliced_list3.remove(name)
#names1 = ageChecker(sliced_list1,userdict,maindict)		# Call ageChecker() and sort names by abs() between user's age
#names2 = ageChecker(sliced_list2,userdict,maindict)		#  and maindict's avg age range individually for first, second
		names3 = ageChecker(sliced_list3,userdict,maindict)		#  and third index.
		for i in rank_priority:
			sliced_list1.append(i)
		sliced_list1.append(sliced_list2)
		for i in names3:
			sliced_list1.append(i)									# Append names of third index count to names of first index count.
		return sliced_list1
		#DONE

	else:														# If no requirements are fulfilled, means that all points values
		return sliced_list1+sliced_list2+sliced_list3			#  are unique. Thus, return only 3 values.
	

def ageChecker(namelist,userdict,maindict):		# Tie breaker to sort users if points are the same.
	abs_age_dict = {}
	abs_age_list = []
	acceptedAge = userdict["Acceptable_age_range"]	# Retrieve the accepted_age_range from user.
	minAge = int(acceptedAge[0])					# Store minimum accepted age.
	maxAge = int(acceptedAge[1])					# Store maximum accepted age.
	
	for i in namelist:												# For each name in namelist,
		for index,main in maindict.iteritems():
			if i in main["Name"]:									# Compare between matched name (namelist) and maindict name.
				checkAge = int("".join(main["Age"]))				#  Find out maindict age.
				acceptable_range_avg = abs(maxAge+minAge) / 2		#  Find out acceptable_age_range of user.
				abs_age_apart = abs(checkAge-acceptable_range_avg)	#  Find out what is their absolute difference.
				abs_age_list.append(abs_age_apart)					#  Append to list.
	
	counter = 0
	for i in namelist:							# For each name in namelist,
		abs_age_dict[i] = abs_age_list[counter]	#  Append name:abs_difference to dictionary. This could be in unsorted order.
		counter += 1

	sorted_name_list = []
	sorted_age_list = []
	for name,age in sorted(abs_age_dict.iteritems(), key=lambda (k,v): (v,k)):	# Sort dict by values in asce order with Lambda
		sorted_name_list.append(name)
		sorted_age_list.append(age)
	
	return sorted_name_list


"""
if __name__ == "__main__":
	c = [['Jenny Wang'], ['Rose'], ['Shelley'],['Angela Little']]
	l = {'Rose': 20, 'Jenny Wang': 35, 'Joel Jackson': 220, 'Shelley': 50, 'Angela Little': 30}
	b = {'Angela Little': 40, 'Joel Jackson': 10, 'Rose': 0, 'Jenny Wang': 130, 'Teresa': 30, 'Lisa Marie': 50, 'Carol': 40, 'Shelley': 0, 'Kevin': 0, 'Michael Jackson': 130}
	print(addMatches(c,l,b,u,m))
	"""
