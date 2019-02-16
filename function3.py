'''
Function 3
Team:
Dominic Gian
Guang Jun
Jun Ming
Ho Xiu Qi
Yeo Han, Jordan
'''

def processInterest(userdict, maindict):
    profiledict = maindict  # Creating function copy of maindict as any modification here will modify maindict as well.
    userlikes = userdict['Likes']
    userdislikes = userdict['Dislikes']
    gender = userdict['Gender'][0][0]
    age = userdict['Acceptable_age_range']
    profilepoints = {}

    for i in profiledict:
        currentuserpoints = 0
        profilelikes = profiledict[i]['Likes']
        profiledislikes = profiledict[i]['Dislikes']
        checkgender = maindict[i]['Gender'][0][0]  # Obtain the Initial of the Gender
        checkage = int("".join(maindict[i]['Age']))

        # Gender check and Age check for if current profile is correct gender and inside acceptable age of user.
        if (checkgender == gender) or not(int(age[0]) <= int(checkage) <= int(age[1])):
            continue

        # print userlikes, profilelikes,userdislikes, profiledislikes
        # Run through check for User Likes
        for L1 in userlikes:
            for L2 in profilelikes:
                if (L2.lstrip(' ')).lower() in (L1.lstrip(' ')).lower():
                    currentuserpoints += 20

        # Run through check for User Dislikes
        for D1 in userdislikes:
            for D2 in profiledislikes:
                if (D2.lstrip(' ')).lower() in (D1.lstrip(' ')).lower():
                    currentuserpoints += 40

        # Run through check for Conflicting Likes and Dislikes
        for L1 in userlikes:
            for D2 in profiledislikes:
                if (D2.lstrip(' ')).lower() in (L1.lstrip(' ')).lower():
                    currentuserpoints -= 20
        for D1 in userdislikes:
            for L2 in profilelikes:
                if (L2.lstrip(' ')).lower() in (D1.lstrip(' ')).lower():
                    currentuserpoints -= 20
        profilepoints[str("".join(profiledict[i]['Name']))] = currentuserpoints
    return profilepoints


def printLikesDislikes(profilepoints):
    for i in profilepoints:
        name = "".join(i)

        print "Profiles Accepted from Likes Dislikes Check: %s from (To Obtain from SQL)" % name
    if not profilepoints:
        print "No profiles found compatible for Likes and Dislikes!"
