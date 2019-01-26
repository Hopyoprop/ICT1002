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
    userdict = {'Name': ['Michael Morton'], 'Gender': ['Male'], 'Age': ['29'], 'Dislikes': ['durian', ' garlic', ' swimming'], 'Acceptable_age_range': ['18', '29'], 'Acceptable_country': ['Singapore', ' China'], 'Books': ['Mere Christianity', 'Knowing God', 'The problem of Pain', 'The God who is there', 'The reason for God: belief in an age of skepticism', 'Experiencing God: knowing and doing the will of God, work book'], 'Likes': ['hotpot', ' chicken and chops', ' chilli', ' roses', ' movies'], 'Country': ['Singapore']}
    acceptedcountries = userdict['Acceptable_country']
    print maindict
    for i in range(0, len(maindict)):
        list = "".join(maindict[i]['Country'])
        if not any(list in s for s in acceptedcountries):
            maindict.pop(i)
    print maindict
    return maindict
