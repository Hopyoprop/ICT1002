'''
Function 3
Team:
Dominic
Guang Jun
Jun Ming
Xiu Qi
Yeo Han, Jordan
'''

def processInterest(userdict, maindict):
    profiledict = maindict  # Creating function copy of maindict as any modification here will modify maindict as well.
    userlikes = userdict['Likes']
    userdislikes = userdict['Dislikes']
    profilepoints = {}

    for i in profiledict:
        currentuserpoints = 0
        profilelikes = profiledict[i]['Likes']
        profiledislikes = profiledict[i]['Dislikes']
        # print userlikes, profilelikes,userdislikes, profiledislikes
        # Run through check for User Likes
        for L1 in userlikes:
            for L2 in profilelikes:
                if L2.lstrip(' ') in L1.lstrip(' '):
                    currentuserpoints += 20

        # Run through check for User Dislikes
        for D1 in userdislikes:
            for D2 in profiledislikes:
                if D2.lstrip(' ') in D1.lstrip(' '):
                    currentuserpoints += 40

        # Run through check for Conflicting Likes and Dislikes
        for L1 in userlikes:
            for D2 in profiledislikes:
                if D2.lstrip(' ') in L1.lstrip(' '):
                    currentuserpoints -= 20
        for D1 in userdislikes:
            for L2 in profilelikes:
                if L2.lstrip(' ') in D1.lstrip(' '):
                    currentuserpoints -= 20
        profilepoints[str("".join(profiledict[i]['Name']))] = currentuserpoints
    return profilepoints
