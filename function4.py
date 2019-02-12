'''
Function 4
Team:
Dominic
Guang Jun
Jun Ming
Xiu Qi
Yeo Han, Jordan
'''

import requests
import json
import time
#from loadingscreen import *

def processBook(userdict, maindict):
    profiledict = maindict
    userbooks = userdict['Books']
    profilepoints = {}
    #print("~~~~~~~~~~ Start User's books")
    # #print("User's Books : ",type(userbooks),userbooks)
    y = len(userbooks)
    p = 0
    userbooklist = [] #user's book list
    for i in userbooks:
        print "Hi"
        while y > p:
            #print(userbooks[p])
            urlstring = "https://www.googleapis.com/books/v1/volumes?q=%22intitle:" + str(userbooks[p])
            data = requests.get(urlstring).json()
            try:
                #print("Title        : " + str(data.get("items")[0]['volumeInfo'].get("title"))) #title
                utitle = str(data.get("items")[0]['volumeInfo'].get("title"))
            except:
                #print("Title        : N/A")
                utitle = "N/A"
            try:
                #print("Author(s)    : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]) #author(s)
                uauthor = str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]
            except:
                #print("Author(s)    : N/A")
                uauthor = "N/A"
            try:
                #print("Categories   : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]) #category(s)
                ucategory = str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]
            except:
                #print("Categories   : N/A")
                ucategory = "N/A"
            userbooklist.append(str(utitle))
            userbooklist.append(str(uauthor))
            userbooklist.append(str(ucategory))
            time.sleep(2)
            p+=1
    if "N/A" in userbooklist:
        userbooklist.remove("N/A")

    for i in profiledict:
        print "Hey"
        currentuserpoints = 0
        profilebooks = profiledict[i]['Books']
        #print(profiledict[i]['Name'],profilebooks)
        profilebooklist = [] # profile's book list
        y = len(profiledict[i]['Books'])
        p = 0
        while y > p:
            #print(profiledict[i]['Books'][p])
            urlstring = "https://www.googleapis.com/books/v1/volumes?q=%22intitle:" + str(profilebooks[p])
            data = requests.get(urlstring).json()
            try:
                #print("Title        : " + str(data.get("items")[0]['volumeInfo'].get("title"))) #title
                ptitle = str(data.get("items")[0]['volumeInfo'].get("title"))
            except:
                #print("Title        : N/A")
                ptitle = "N/A"
            try:
                #print("Author(s)    : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]) #author(s)
                pauthor = str(json.dumps(data.get("items")[0]['volumeInfo'].get("authors")[0:]))[2:-2]
            except:
                #print("Author(s)    : N/A")
                pauthor = "N/A"
            try:
                #print("Categories   : " + str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]) #category(s)
                pcategory = str(json.dumps(data.get("items")[0]['volumeInfo'].get("categories")[0:]))[2:-2]
            except:
                #print("Categories   : N/A")
                pcategory = "N/A"
            profilebooklist.append(str(ptitle))
            profilebooklist.append(str(pauthor))
            profilebooklist.append(str(pcategory))
            time.sleep(2)
            p+=1
        if "N/A" in profilebooklist:
            profilebooklist.remove("N/A")
        #print(str(profiledict[i]['Name'])+"'s booklist : "+str(profilebooklist)) # print profile's book list
        same_values = set(userbooklist) & set(profilebooklist)
        currentuserpoints = (len(same_values)*10)#profile's points
        #print(str(profiledict[i]['Name'])+"'s Current Pts : ", currentuserpoints)
        profilepoints[str("".join(profiledict[i]['Name']))] = currentuserpoints
    return(profilepoints)

