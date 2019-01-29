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
    profiledict = maindict  # Creating function copy of maindict as any modification here will modify maindict as well.
    acceptedcountries = userdict['Acceptable_country'] # Obtain the user's Accepted Countries
    gender = userdict['Gender'][0][0]

    for i in range(0, len(profiledict)):
        list = "".join(profiledict[i]['Country']) #Obtain the profile's country of birth
        checkgender = profiledict[i]['Gender'][0][0] # Obtain the Initial of the Gender

        # Perform check of both, opposite gender and if the profile is in acceptable country of user.
        if not any(list in s for s in acceptedcountries) or not(checkgender != gender):
            profiledict.pop(i) #Remove from maindict for further processing

    return profiledict

def printCountries(userdict, acceptedcountry):
    print "Accepted Countries from User Profile: %s" % (",".join(userdict['Acceptable_country']))
    for i in acceptedcountry:
        name = "".join(acceptedcountry[i]['Name'])
        countryname = "".join(acceptedcountry[i]['Country'])

        print "Profiles Accepted from Country Check: %s from %s" % (name, countryname)
    if not acceptedcountry:
        print "No profiles found compatible!"
