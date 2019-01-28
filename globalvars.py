def init():
    global currentuser
    global showpagecommand

# function to update global variable containing user's account username
def setcurrentusername(a):
    global currentuser
    currentuser = a


# function to update global variable containing name of page to display
def setpagetodisplay(a):
    global showpagecommand
    showpagecommand = a


def printglobalvariables():
    print currentuser
    print showpagecommand