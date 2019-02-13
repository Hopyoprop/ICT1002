'''
Function 5
Team:
Dominic
Guang Jun
Jun Ming
Xiu Qi
Yeo Han, Jordan
'''
def processMatches(acceptedcountry, likesdislikes, books, userdict, maindict):
	
	acceptedcountry = ['Teresa', 'Carol', 'Rose', 'Shelley', 'Jenny Wang', 'Angela Little', 'Lisa Marie']
	likesdislikes = {'Angela Little': -80, 'Rose': 0, 'Jenny Wang': 140, 'Teresa': 140, 'Lisa Marie': 140, 'Carol': 180, 'Shelley': 0}
	books = {'Shelley': 20, 'Joel Jackson': 40, 'Lisa Marie': 0, 'Rose': 10, 'Carol': 20, 'Jenny Wang': 20, 'Teresa': 20, 'Kevin': 20}
	userdict = {'Name': ['Alpha Romero'], 'Gender': ['Male'], 'Age': ['27'], 'Dislikes': ['football', 'hunting', 'swimming'], 'Acceptable_age_range': ['18', '32'], 'Acceptable_country': ['UK', 'Singapore', 'China', 'USA'], 'Books': ['Human Philosohy', 'Nicomachean Ethics', 'Summa Theologiae', 'Meditations on First Philosophy', 'Essay Concerning Human Understanding', 'Principles of Human Knowledge', 'Enquiry Concerning Human Understanding', 'Social Contract', 'Phenomenology of Spirit'], 'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': ['Singapore']}
	maindict = {0: {'Name': ['Teresa'], 'Gender': ['F'], 'Age': ['22'], 'Dislikes': ['garlic', 'durian', 'swimming'], 'Acceptable_age_range': ['18', '30'], 'Acceptable_country': ['Singapore', 'China'], 'Books': ['Total Truth: Liberating Christianity from its Cultural Captivity', 'Reflections on the Psalms', 'Intercessory Prayer: How God Can Use Your Prayers to Move Heaven Earth', "God 's Favor - Breath Of Heaven", 'Letters to Malcolm: Chiefly on Prayer'], 'Likes': ['hotpot', 'chilli', 'chicken and chops', 'roses', 'movies'], 'Country': ['Singapore']}, 1: {'Name': ['Michael Jackson'], 'Gender': ['Male'], 'Age': ['29'], 'Dislikes': ['durian', 'garlic', 'swimming'], 'Acceptable_age_range': ['18', '29'], 'Acceptable_country': ['Singapore', 'China'], 'Books': ['Mere Christianity', 'Knowing God', 'The problem of Pain', 'The God who is there', 'The reason for God: belief in an age of skepticism', 'Experiencing God: knowing and doing the will of God', 'work book'], 'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': ['Singapore']}, 2: {'Name': ['Carol'], 'Gender': ['F'], 'Age': ['23'], 'Dislikes': ['football', 'hunting', 'swimming'], 'Acceptable_age_range': ['23', '50'], 'Acceptable_country': ['Singapore', 'China'], 'Books': ['Christian reflections', 'The red tent', 'The God who is there', 'God in the Dock: Essays on Theology and Ethics', 'Total truth: liberating christianity from its cultural captivity', 'Redeeming love', ''], 'Likes': ['Chicken rice', 'hotpot', 'Carrot cake', 'chilli crab', 'roses', 'movies'], 'Country': ['USA']}, 3: {'Name': ['Kevin'], 'Gender': ['Male'], 'Age': ['25'], 'Dislikes': ['curry', 'garlic', 'basketball'], 'Acceptable_age_range': ['10', '33'], 'Acceptable_country': ['Singapore'], 'Books': ['Human Philosohy', 'Adventures in Human Being', 'Meditations on the Philosophy', 'Essay Concerning Human topic', 'Principles of Human being'], 'Likes': ['fish', 'chicken', 'chocolate', 'roses', 'durian', 'movies'], 'Country': ['Singapore']}, 4: {'Name': ['Rose'], 'Gender': ['F'], 'Age': ['25'], 'Dislikes': ['chilli', 'garlic', 'basketball'], 'Acceptable_age_range': ['18', '35'], 'Acceptable_country': ['Singapore', 'China', 'UK'], 'Books': ['Human Philosohy book', 'Adventures in Human Being', 'Towards the Philosophy', 'Essay Related Human Topics', 'Human Being Shall Know Philosohy'], 'Likes': ['fish', 'honey', 'chocolate', 'roses', 'durian', 'running'], 'Country': ['Singapore']}, 5: {'Name': ['Shelley'], 'Gender': ['Female'], 'Age': ['24'], 'Dislikes': ['chilli', 'garlic', 'basketball'], 'Acceptable_age_range': ['18', '35'], 'Acceptable_country': ['Singapore', 'China', 'USA'], 'Books': ['Human Philosohy book', 'Adventures in Human Being', 'Towards the Philosophy', 'Essay Related Human Topics', 'Human Being Shall Know Philosohy'], 'Likes': ['fish', 'honey', 'chocolate', 'roses', 'durian', 'running'], 'Country': ['China']}, 6: {'Name': ['Joel Jackson'], 'Gender': ['Male'], 'Age': ['29'], 'Dislikes': ['durian', 'garlic', 'swimming'], 'Acceptable_age_range': ['18', '33'], 'Acceptable_country': ['Singapore', 'China', 'USA'], 'Books': ['Human Philosohy', 'Nicomachean Ethics', 'Summa Theologiae', 'Meditations on First Philosophy', 'Essay Concerning Human Understanding', 'Principles of Human Knowledge', 'Enquiry Concerning Human Understanding', 'Social Contract', 'Phenomenology of Spirit'], 'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': ['Singapore']}, 7: {'Name': ['Jenny Wang'], 'Gender': ['F'], 'Age': ['25'], 'Dislikes': ['durian', 'garlic', 'swimming'], 'Acceptable_age_range': ['23', '60'], 'Acceptable_country': ['China', 'USA', 'Singapore'], 'Books': ['Mere Christianity', 'Knowing God', 'How should we then live? the rise and decline of western thought and culture', 'The problem of Pain', 'The God who is there', 'The reason for God: belief in an age of skepticism', 'Experiencing God: knowing and doing the will of God', 'work book', ''], 'Likes': ['hotpot', 'chicken and chops', 'chilli', 'roses', 'movies'], 'Country': ['China']}, 8: {'Name': ['Angela Little'], 'Gender': ['F'], 'Age': ['22'], 'Dislikes': ['hotpot', 'chilli', 'roses', 'movies'], 'Acceptable_age_range': ['18', '30'], 'Acceptable_country': ['Singapore', 'China'], 'Books': ['Christian reflections', 'The red tent', 'The God who is there', 'God in the Dock: Essays on Theology and Ethics', 'Total truth: liberating christianity from its cultural captivity', 'Redeeming love'], 'Likes': ['garlic', 'durian', 'swimming', 'chicken and chops'], 'Country': ['Singapore']}, 9: {'Name': ['Lisa Marie'], 'Gender': ['F'], 'Age': ['22'], 'Dislikes': ['garlic', 'durian', 'swimming'], 'Acceptable_age_range': ['18', '30'], 'Acceptable_country': ['Singapore', 'China'], 'Books': ['Desiring God Meditations of a Christian Hedonist', 'God Knowing', 'God Favor: Breath of Heaven', 'The God is there', 'The reason for God: in an age of skepticism', 'Experiencing God: knowing the will of God', 'work book'], 'Likes': ['hotpot', 'chilli', 'chicken and chops', 'roses', 'movies'], 'Country': ['Singapore']}}

	country = []
	for c in acceptedcountry:							# Formatting for acceptedcountry list.
		country.append("".join(c))

	print("Accepted Countries: ",acceptedcountry)
	print("Accepted Countries: ",country)
	print("likesdislikes: ",likesdislikes)
	print("books: ",books)
	#print(userdict)
	#print(maindict)

	combine_matches = {}
	for i in country:									#For each user in acceptablecountry list,
		if i in likesdislikes:							# If user exists in likesdislikes dictionary,
			combine_matches[i] = likesdislikes.get(i)	#  Add user and points to ccombine_matches dict.
		if i in books:									# Or user exists in books dictionary,
			combine_matches[i] = books.get(i)			#  Add user and points to ccombine_matches dict.
	print("Combined Likes: ",combine_matches)
	#print(country)
	#print(likesdislikes)
	#print(books)

	if bool(combine_matches):																		#Check if combine_matches dict has keys:values.
			top_3 = pointsRanking(combine_matches,userdict,maindict,country,likesdislikes,books)	# If it has values, perform best_matching algo.
			print(top_3)
			return top_3
	else:																							# Else, return empty dictionary.
		print("There are no matches available for you at the moment. Please try again later.")
		return []


def pointsRanking(matched_dict,userdict,maindict,country,likesdislikes,books):
	points_ranked_names = []
	points_ranked_values = []
	for name, points in sorted(matched_dict.iteritems(), key=lambda (k,v): (v,k), reverse=True):	# Sort dict by values in desc order with Lambda
		points_ranked_names.append(name)
		points_ranked_values.append(points)

	# 7 users only
	points_ranked_values = [0,0,0,0,0,0,-200]

	#Scenario: Top 5 matches might have the same points/values.
	#Objective 1: For those with same points, sort by priority order (if user exists in both likesdislikes and books dictionary).
	#Objective 2: After priority order, sort by abs() difference between current user's acceptable_age_range and maindict's age.
	print(points_ranked_names)
	print(points_ranked_values)
	sorted_match = sortRanking(points_ranked_names,points_ranked_values,userdict,maindict,country,likesdislikes,books)

	return sorted_match[:3]


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
	count = 0
	# Given namelist & pointslist,
	while count < len(pointslist):												#Iterate pointslist and check if first index
		if x < len(pointslist) and pointslist[0] == pointslist[x]:				# is same as second index, then third index, etc. 
			x += 1
		elif x+y < len(pointslist) and pointslist[x] == pointslist[x+y]:		#
			y += 1
		elif x+y+z < len(pointslist) and pointslist[x+y] == pointslist[x+y+z]:
			z += 1
		else:
			break
		count += 1
		
	sliced_list1 = namelist[0:x]		# Group first unique set of values.
	sliced_list2 = namelist[x:x+y]		# Group second unique set of values.
	sliced_list3 = namelist[x+y:x+y+z]	# Group third unique set of values.

	"""
	Test Cases: To return top 3 best matches, len(namelist) must amount to 3 or more.
				priorityRanking() achieves this by sorting based on 2 conditions.
	1. sliced1 >= 3										return
	2. sliced1 == 2 and sliced2 == 1					return
	3. sliced1 == 1 and sliced2 >=2						return
	4. sliced1 == 1 and sliced2 == 1 and sliced3 >=1	return
	5. else, the only case left is when sliced1 <= 0	return empty.
	"""

	#Test Case 1 -- if sliced_list1 >= 3, return.
	if len(sliced_list1) >= 3:
		rank_priority = priorityRanking(sliced_list1,likesdislikes,books,userdict,maindict)
		return rank_priority

	#Test Case 2 -- if sliced_list1 == 2 and sliced_list2 == 1, return.
	elif len(sliced_list1) == 2 and len(sliced_list2) == 1:
		rank_priority = priorityRanking(sliced_list1,likesdislikes,books,userdict,maindict)
		rank_priority += sliced_list2
		return rank_priority

	#Test Case 3 -- if sliced_list1 == 1 and sliced_list2 >=2, return.
	elif len(sliced_list1) == 1 and len(sliced_list2) >= 2:
		rank_priority = priorityRanking(sliced_list2,likesdislikes,books,userdict,maindict)
		for user in rank_priority:
			sliced_list1.append(user)
		return sliced_list1

	#Test Case 4 -- if sliced_list1 == 1 and sliced_list2 == 1 and sliced_list3 >=1, return.
	elif len(sliced_list1) == 1 and len(sliced_list2) == 1 and len(sliced_list3) > 1:
		rank_priority = priorityRanking(sliced_list3,likesdislikes,books,userdict,maindict)
		sliced_list1 += sliced_list2
		for user in rank_priority:
			sliced_list1.append(user)
		return sliced_list1

	#Test Case 5 -- else, the remaining case important to us is when all sliced_list are == 0, append all list and return.
	else:
		return sliced_list1+sliced_list2+sliced_list3


def priorityRanking(namelist,likesdislikes,books,userdict,maindict):
	priority_list = []
	for i in namelist:  						#For each user in namelist:
		if i in likesdislikes and i in books:	# Check if user exists in acceptedlikesdislikes and acceptedbooks.
			priority_list.append(i)				# If they do, append to priority_list.

	#print("namelist:",namelist)
	#print("likesdislikes:",likesdislikes)
	#print("books:",books)

	if len(priority_list) > 1:										#If there is more than 1 names in priority_list,
		priority = ageChecker(priority_list, userdict, maindict)	# Call ageChecker() to perform another round of sorting,
		return priority[:3]											# And return the sorted list of names.

	elif len(priority_list) == 1:									#Elif there is only 1 name in priority_list,
		return priority_list										# Return that name only.

	else:															#Else, if there are 0 names in priority_list,
		priority = ageChecker(namelist, userdict, maindict)			# Call ageChecker() on original namelist.
		return priority


def ageChecker(namelist,userdict,maindict):			# Tie breaker to sort users if points are the same.
	abs_age_dict = {}
	abs_age_list = []
	acceptedAge = userdict["Acceptable_age_range"]	# Retrieve user's accepted_age_range.
	minAge = int(acceptedAge[0])					# Store minimum accepted age.
	maxAge = int(acceptedAge[1])					# Store maximum accepted age.
	acceptable_range_avg = abs(maxAge+minAge) / 2	# Find out avg acceptable_age_range of user.

	for user in namelist:											# For each name in namelist,
		for index,main in maindict.iteritems():
			if user in main["Name"]:								# Compare between matched username (namelist) and maindict name.
				checkAge = int("".join(main["Age"]))				#  Find out maindict's user age.
				abs_age_apart = abs(checkAge-acceptable_range_avg)	#  Find out abs() between avg acceptable_age_range of user and maindict's user age.
				abs_age_list.append(abs_age_apart)					#  Append to list.
	
	counter = 0
	for user in namelist:							# For each name in namelist,
		abs_age_dict[user] = abs_age_list[counter]	#  Append name:abs_difference to dictionary. This could result in an unsorted order.
		counter += 1

	sorted_name_list = []
	sorted_age_list = []
	for name,age in sorted(abs_age_dict.iteritems(), key=lambda (k,v): (v,k)):	# Sort dict by values in asce order with Lambda
		sorted_name_list.append(name)
		sorted_age_list.append(age)
	
	return sorted_name_list


if __name__ == "__main__":
	process_Matches = processMatches("","","","","")
	
