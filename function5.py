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

5. Sort newDict by values and return the top 3 usernames with the highest values.
	5a. If same values, take the username nearest to age.
"""
def processAgeRange(userdict, maindict):
	# Check if userdict_acceptableAge is in maindict_age <for range>
	# If yes, store name into list
	# Return list
	return True

def addMatches(acceptedcountry, likesdislikes, books):
	country = []
	for c in acceptedcountry:
		country.append("".join(c))
	matched = {}

	for i in country:
		if i in likesdislikes:
			matched[i] = likesdislikes.get(i)
			if i in books:
				matched[i] += books.get(i)

	if bool(matched):
			top_3 = bestMatched(matched)
			return top_3
	else:
		print("There are no matches available for you at the moment.\nPlease try again later.")

def bestMatched(matched_dict):
	best_matched = []
	for name,points in sorted(matched_dict.iteritems(), key=lambda (k,v): (v,k)):
		best_matched.append(name)
	reverse = list(reversed(best_matched))

	sorted_match = sortMatches(reverse)
	return sorted_match[:3]

def sortMatches(matched_dict):
	"""
	1. Given matched_dict<name:points>, create namelist[names] & pointslist[points].
	2. Check if first points is same as second.
		2a. If yes, check if first points is same as third. Repeat.
		2b. If no, store the index number.
		2c. Slice list and push to ageChecker().
	3. Check if second points is same as fourth.

	2. for p in pointslist:
			if p == pointslist[i]:
				i++
			else:
				break
		sliced_list = namelist[0,i]
		ageChecker(namelist)

		ageChecker:

	"""
	return matched_dict


if __name__ == "__main__":
	c = [['Jenny Wang'], ['Rose'], ['Shelley'],['Angela Little']]
	l = {'Rose': 20, 'Jenny Wang': 35, 'Joel Jackson': 220, 'Shelley': 50, 'Angela Little': 30}
	b = {'Angela Little': 40, 'Joel Jackson': 10, 'Rose': 0, 'Jenny Wang': 130, 'Teresa': 30, 'Lisa Marie': 50, 'Carol': 40, 'Shelley': 0, 'Kevin': 0, 'Michael Jackson': 130}
	print(addMatches(c,l,b))
