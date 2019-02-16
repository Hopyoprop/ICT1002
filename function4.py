'''
Function 4
Team:
Chua Guang Jun
Dominic Keeley Gian
Ho Xiu Qi
Lee Jun Ming
Yeo Han, Jordan
'''

import requests
import json
import time


def processBook(userdict, maindict):
    profiledict = maindict
    userbooks = userdict['Books']
    profilepoints = {}
    gender = userdict['Gender'][0][0].upper()
    age = userdict['Acceptable_age_range']
    # print("~~~~~~~~~~ Start User's books")
    # print("User's Books : ",type(userbooks),userbooks)
    y = len(userbooks)
    p = 0
    userbooklist = [] # user's book list
    for i in userbooks:
        print "Hi"
        while y > p:
            # print(userbooks[p])
            urlstring = "https://www.googleapis.com/books/v1/volumes?q=%22intitle:" + str(userbooks[p])
            data = requests.get(urlstring).json()
            try:
                # print("Title        : " + str(data.get("items")[0]['volumeInfo'].get("title"))) #title
                utitle = str(data.get("items")[0]['volumeInfo'].get("title"))
            except:
                # print("Title        : N/A")
                utitle = "N/A"
            try:
                # print("Author(s)    : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]) #author(s)
                uauthor = str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]
            except:
                # print("Author(s)    : N/A")
                uauthor = "N/A"
            try:
                # print("Categories   : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]) #category(s)
                ucategory = str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]
            except:
                # print("Categories   : N/A")
                ucategory = "N/A"
            userbooklist.append(str(utitle))
            userbooklist.append(str(uauthor))
            userbooklist.append(str(ucategory))
            time.sleep(2)
            p += 1
    if "N/A" in userbooklist:
        userbooklist.remove("N/A")

    for i in profiledict:
        print "Hey"
        currentuserpoints = 0
        profilebooks = profiledict[i]['Books']
        # print(profiledict[i]['Name'],profilebooks)
        profilebooklist = [] # profile's book list
        y = len(profiledict[i]['Books'])
        p = 0

        checkgender = maindict[i]['Gender'][0][0]  # Obtain the Initial of the Gender
        print(checkgender)
        checkage = int("".join(maindict[i]['Age']))

        # Gender check and Age check for if current profile is correct gender and inside acceptable age of user.
        if (checkgender == gender) or not(int(age[0]) <= int(checkage) <= int(age[1])):
            continue
        
        while y > p:
            # print(profiledict[i]['Books'][p])
            urlstring = "https://www.googleapis.com/books/v1/volumes?q=%22intitle:" + str(profilebooks[p])
            data = requests.get(urlstring).json()
            try:
                # print("Title        : " + str(data.get("items")[0]['volumeInfo'].get("title"))) #title
                ptitle = str(data.get("items")[0]['volumeInfo'].get("title"))
            except:
                # print("Title        : N/A")
                ptitle = "N/A"
            try:
                # print("Author(s)    : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]) #author(s)
                pauthor = str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]
            except:
                # print("Author(s)    : N/A")
                pauthor = "N/A"
            try:
                # print("Categories   : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]) #category(s)
                pcategory = str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]
            except:
                # print("Categories   : N/A")
                pcategory = "N/A"
            profilebooklist.append(str(ptitle))
            profilebooklist.append(str(pauthor))
            profilebooklist.append(str(pcategory))
            time.sleep(2)
            p+=1
        if "N/A" in profilebooklist:
            profilebooklist.remove("N/A")
        # print(str(profiledict[i]['Name'])+"'s booklist : "+str(profilebooklist)) # print profile's book list
        same_values = set(userbooklist) & set(profilebooklist)
        currentuserpoints = (len(same_values)*10)# profile's points
        # print(str(profiledict[i]['Name'])+"'s Current Pts : ", currentuserpoints)
        profilepoints[str("".join(profiledict[i]['Name']))] = currentuserpoints

    return profilepoints
