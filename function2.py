'''
Function 2
Team:
Dominic
Guang Jun
Jun Ming
Xiu Qi
Yeo Han, Jordan
'''
import itertools

def processUser(userdict, maindict):
    acceptedcountries = userdict['Acceptable_country']

    for i in range(0, len(maindict)):
        list = "".join(maindict[i]['Country'])
        if not any(list in s for s in acceptedcountries):
            maindict.pop(i)

    return maindict
