'''
Function 2
Team:
Dominic
Guang Jun
Jun Ming
Xiu Qi
Yeo Han, Jordan
'''

def processUser(userdict, maindict):
    profilelist = []  # Creating function copy of maindict as any modification here will modify maindict as well.
    acceptedcountries = userdict['Acceptable_country']  # Obtain the user's Accepted Countries
    gender = userdict['Gender'][0][0]
    age = userdict['Acceptable_age_range']

    for key,value in maindict.items():
        list = "".join(maindict[key]['Country'])  # Obtain the profile's country of birth
        checkgender = maindict[key]['Gender'][0][0]  # Obtain the Initial of the Gender
        checkage = int("".join(maindict[key]['Age']))
        #print age, checkage
        # Gender check and Age check for if current profile is correct gender and inside acceptable age of user.
        if (checkgender == gender) or not(int(age[0]) <= int(checkage) <= int(age[1])):
            continue

        # Perform check of both, opposite gender and if the profile is in acceptable country of user.
        elif any(list in s for s in acceptedcountries):
            profilelist.append(str(maindict[key]['Name']).replace("['","").replace("']",""))  # Remove from maindict for further processing

    return profilelist

def printCountries(userdict, acceptedcountry):
    print "Accepted Countries from User Profile: %s" % (",".join(userdict['Acceptable_country']))
    for i in acceptedcountry:
        name = "".join(i)
        # countryname = "".join(acceptedcountry[i]['Country'])

        print "Profiles Accepted from Country Check: %s from (To Obtain from SQL)" % name
    if not acceptedcountry:
        print "No profiles found compatible for acceptable country!"
