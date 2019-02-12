import Tkinter as tk
import tkFileDialog as filedialog
import glob                             # for opening files
import os                               # for opening files
from function2 import processUser
from function2 import printCountries
from function3 import processInterest
from function3 import printLikesDislikes
from function4 import processBook
from function5 import processMatches
from sqlfunctions import *
from loginpage import *
from displayprofilepage import *
from loadingscreen import *
from resultspage import *
import globalvars as gv
from PIL import Image, ImageTk, ImageSequence

def processSamples(maindict):

    # Initialise count for parsing values into dictionary
    dcount = 0

    # purpose of defining this 'root' is so that file dialog box can be  hidden
    root = Tk()
    root.withdraw()
    tkmessagebox.showinfo("Input Directory to open Files from", "Please navigate to the FOLDER with data samples in the following prompt and click OK")

    # open file dialog browser to select files to parse
    dir_path = filedialog.askdirectory()

    if dir_path != "":

        # open files from chosen directory, which are of '.txt' type
        for file in glob.glob(os.path.join(dir_path, '*.txt')):
            #print str(file)
            f = open(file, "r")
            # counter to track progress after reaching
            counter = 0

            # initializing the sub-dictionary (which represents a file)
            maindict[dcount] = {}

            # initializing list that will contain 'Books' read by current user
            readbooks = []

            # for each line in the file
            for line in f:
                # if 'Books:' has already been iterated (as defined by counter =1), then
                if counter >= 1:
                    # if line is not null
                    if line != "" and line != " " and line != "\n" and line.startswith(" ") is False:
                        # adds the line into the readbooks list after removing \n and whitespace
                        readbooks.append(line[:-1].rstrip(' '))
                        counter += 1
                        continue

                # if line does not start with books/acceptable_age_range/null value (since they will be using a diff funct)
                elif not (line.lower().startswith("books")) and not(line.lower().startswith("acceptable_age_range")) and \
                    line != "\n":
                    # call function to parse current line
                    parseCurrentLine(line, dcount)

                elif line.lower().startswith("acceptable_age_range"):
                    # call function to parse current line which has values for age range
                    parseAgeRange(line, dcount)

                elif line.lower().startswith("books:"):
                    counter += 1

            # create dictonary entry for books that this user (dcount) reads
            field = "Books"
            maindict[dcount][field] = readbooks
            #print readbooks

            # increment the dcount counter
            dcount += 1

            # ----- end of 'for path in file_path'
    # return to main once done
    root.quit()
    root.destroy()

    return maindict


# function definition for parsing any field other than 'Books'/'Acceptable_age_range'/NULL
def parseCurrentLine(line, dcount):
    try:
        # get the field of the line
        field = line.split(": ")[0]
        # get the content portion of the line
        content = line.split(": ")[1]

        data = []

        # further split the contents based on delimiter of ","
        content = filter(None, content.lstrip().rstrip().split(","))
        for a in content:
            data.append(a)

        # assign the field and data into the dictionary
        maindict[dcount][field] = data

    except Exception, e:
        print "Exception occured within parseCurrentLine function: " + str(e)
        exit()
    return

# function definition for parsing acceptable_age_range field specifically
def parseAgeRange(line, dcount):
    try:
        # get the field of the line
        field = line.split(": ")[0]
        # get the content portion of the line
        content = line.split(": ")[1]

        data = []
        # further split the contents based on delimiter of "-"
        content = content[:-1].lstrip(' ').rstrip(' ').split('-')

        # for each substring in content, add to a list
        for a in content:
            data.append(a)
        # assign the field and data into the dictionary
        maindict[dcount][field] = data
    except:
        print "Exception occured within parseAgeRange function"
        exit()
    return


######################################################################################################################
####################################### Windows Looping Functions ####################################################

# definition to create a window
def createwindow(classofwindow, dimensions, titleofwindow):
    classofwindow(dimensions, titleofwindow)


# definition to traverse the pages (keep the program alive and allow dynamic navigation of pages)
def windowtraverser():
    while str(gv.showpagecommand) is not "shutdown":
        if str(gv.showpagecommand) == "openLoginPage":
            createwindow(LoginPage, "500x300", "MatchMakeMe - Login")

        elif str(gv.showpagecommand) == "openDisplayPage":
            createwindow(DisplayPage, "500x570", "MatchMakeMe - My Profile")

        elif str(gv.showpagecommand) == "openLoadingScreen":
            createwindow(LoadingScreen, "400x400", "MatchMakeMe - Loading")

        elif str(gv.showpagecommand) == "openFindMatchResultsPage":
            createwindow(ResultsPage, "550x700", "MatchMakeMe - Matched Results")

######################################################################################################################
######################################################################################################################


######################################################################################################################
################################################ Main Function #######################################################
######################################################################################################################

if __name__ == "__main__":
    ##########################################################################################################
    # start up the GUI with loginpage
    gv.init() #uncomment
    # call function to retrieve from a .txt file, which stores names of tables to create, and their column names
    dbinfo = pull()
    # call function to create the DB file with respective tables and names
    createDBfile(dbinfo)

    # create the login page, and launch it
    createwindow(LoginPage, "500x300", "MatchMakeMe - Login")

    ##########################################################################################################
    # once login confirmed, come back to here (main.py) to execute processSamples() to let user add any new profiles
    maindict = {}     # Initialize variables

    # Function to process data from selected sample files into a dictionary
    maindict = processSamples(maindict)


    # Loop each user profile separately and insert data into db.
    i = 0
    for i in range(0, len(maindict.items())):
        insert_profile(maindict[i])
        i+=1

    # call function to create the main dictionary by retrieving all data from database
    result = createmaindictionary()
    #print result


    # try to get current user's profile from database
    currentuserdatalist = getuserprofiles([str(gv.currentuser)])

    # if there was a record of current user found in the db
    if currentuserdatalist != 0:
        #print str(currentuserdatalist[1])
        # pop the entry of the currentuser from the main dictionary as he does not need to be matched with himself
        templist = []
        copyofdict = {}
        copyofdict = result
        # to compare against element in maindict, the name has to be an element in a list, rather than just a string
        templist.append(str(currentuserdatalist[1]))
        #print templist

        for key,value in copyofdict.items():
            # if name in the dictionary matches user's name, remove his own record fromo maindictionary (result)

            #print copyofdict[key]['Name']
            #print templist
            if copyofdict[key]['Name'] == templist:
                del result[key]

    # call function to set global variable 'maindictionary'
    setmaindictionary(result)

    #listofuserlists = [["Teresa","Rose", "Carol", "Kevin", "Shelley", "Ho Xiu Qi", "Test"],
                       #["Rose", "Carol", "Kevin", "Shelley", "Ho Xiu Qi", "Test"],
                       #["Rose", "Carol", "Kevin", "Shelley", "Ho Xiu Qi"],
                       #["Rose", "Carol", "Kevin", "Shelley"], ["Rose", "Carol", "Kevin"]]
    #gv.setlist_of_shortlisted_users(listofuserlists)


    ##########################################################################################################
    # Once adding of user profiles (any) into db, continue with the program
    windowtraverser()

    exit()

    ##########################################################################################################
    ##########################################################################################################

    # if want to test your code, go to 'loadingscreen.py'. They are called there and not below here anymore  #

    ##########################################################################################################
    ##########################################################################################################

    ''''##########################################################################################################
    # Function 2
    # TEMPORARY PLACEHOLDER DICT. USERLIST WILL BE THE USER GUI INPUTTED VALUES
    maindict = gv.maindictionary
    userdict = {'Name': ['Michael Morton'], 'Gender': ['Male'], 'Age': ['29'],
                'Dislikes': ['durian', ' garlic', ' swimming'], 'Acceptable_age_range': ['18', '29'],
                'Acceptable_country': ['Singapore', ' China'],
                'Books': ['Mere Christianity', 'Knowing God', 'The problem of Pain', 'The God who is there',
                          'The reason for God: belief in an age of skepticism',
                          'Experiencing God: knowing and doing the will of God, work book'],
                'Likes': ['hotpot', ' chicken and chops', ' chilli', ' roses', ' movies'], 'Country': ['Singapore']}
    acceptedcountry = {} # TEMPORARY LOCATION. TO BE MOVED. WILL STORE THE SCALED DOWN MAINDICT WITH USERS OF ACCEPTABLE
    # COUNTRY
    # First round of Processing for Acceptable Countries, returns a dict with accepted users
    #acceptedcountry = processUser(userdict, maindict)

    #printCountries(userdict, acceptedcountry)
    ##########################################################################################################
    # Function 3
    #acceptedlikesdislikes = processInterest(userdict, maindict)

    #printLikesDislikes(acceptedlikesdislikes)
    ##########################################################################################################
    # Function 4
    acceptedbooks = processBook(userdict, maindict)
    print maindict
    print(acceptedbooks)
    ##########################################################################################################
    # Function 5
    bestMatched = processMatches(acceptedcountry, acceptedlikesdislikes, acceptedbooks, userdict, maindict)
    print(bestMatched)

    ##########################################################################################################
    # once processing done, take dictionary/list of user input and compare with each dictionary of processed profile
    # DTF_Match()

    # print maindict[0]
    # print maindict[1]
    # print maindict[2]
    # print maindict[3]
    # print maindict[4]
    # print maindict[5]
    # print maindict[6]
    # print maindict[7]
    # print maindict[8]
    # print maindict[9]

    # Output to a CSV File
    # TO DO

    #func 4 data
    #{'Angela Little': 40, 'Joel Jackson': 10, 'Rose': 0, 'Jenny Wang': 130, 'Teresa': 30, 'Lisa Marie': 50, 'Carol': 40, 'Shelley': 0, 'Kevin': 0, 'Michael Jackson': 130}'''

	








