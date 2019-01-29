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

    for i in profiledict:
        likes = profiledict[i]['Likes']
        dislikes = profiledict[i]['Dislikes']
