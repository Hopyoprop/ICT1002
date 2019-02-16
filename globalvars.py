'''
Global Variables.py
Team:
Chua Guang Jun
Dominic Keeley Gian
Ho Xiu Qi
Lee Jun Ming
Yeo Han, Jordan
'''

def init():
    global currentuser
    global showpagecommand
    global userdictionary
    global maindictionary
    global list_of_shortlisted_users

# function to update global variable containing user's account username
def setcurrentusername(a):
    global currentuser
    currentuser = a

# function to update global variable containing name of page to display
def setpagetodisplay(a):
    global showpagecommand
    showpagecommand = a
    #print showpagecommand

# function to update global variable containing main dictionary (used by functions)
def setuserdictionary(a):
    global userdictionary
    userdictionary = a

# function to update global variable containing main dictionary (used by functions)
def setmaindictionary(a):
    global maindictionary
    maindictionary = a

# function to update global variable that is type list, which contains sublists with usernames of shortlisted users
def setlist_of_shortlisted_users(a):
    global list_of_shortlisted_users
    list_of_shortlisted_users = a


def getshortlisteduserslist():
    global list_of_shortlisted_users
    a = list_of_shortlisted_users
    return a

def getmaindictionary():
    global maindictionary
    a = maindictionary
    return a

def printglobalvariables():
    print currentuser
    print showpagecommand
