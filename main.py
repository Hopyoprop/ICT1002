import Tkinter as tk
import tkFileDialog as filedialog
from function2 import processUser
import sys

# Function will eventually return the keyed in data of the GUI.
def openMainWindow():
    #Return a dict of the main data.
    return
    ''' insert code for designing user input UI '''

def processSamples(maindict):

    # Initialise count for parsing values into dictionary
    dcount = 0

    #Initialise a GUI Object, not used yet.
    mainwin = tk.Tk()

    # open file dialog browser to select files to parse
    file_path = filedialog.askopenfilenames()

    # ^^^^^^^^^^^^^^^^^^^^^ remove once GUI is completed / not needed #
    # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ #

    # open files that were selected on top
    for path in file_path:
        file = open(path, "r")
        # counter to track progress after reaching
        counter = 0

        # initializing the sub-dictionary (which represents a file)
        maindict[dcount] = {}

        # initializing list that will contain 'Books' read by current user
        readbooks = []

        # for each line in the file
        for line in file:
            # if 'Books:' has already been iterated (as defined by counter =1), then
            if counter >= 1:
                # if line is not null
                if line != "" and line != " " and line != "\n":
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

        # increment the dcount counter
        dcount += 1

        # ----- end of 'for path in file_path'
    # return to main once done
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
        content = content.strip().split(",")
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
        content = content[:-1].strip().split('-')

        # for each substring in content, add to a list
        for a in content:
            data.append(a)
        # assign the field and data into the dictionary
        maindict[dcount][field] = data
    except:
        print "Exception occured within parseAgeRange function"
        exit()
    return


''' Main Function '''
if __name__ == "__main__":
    # Call function to instantiate GUI window tk() for user input
    openMainWindow()

    # Initialize variables
    maindict = {}

    # Function to process data from all sample files into a dictionary
    maindict = processSamples(maindict)

    # GUI to obtain user's profile and what is his profile
    # TO DO

    ##########################################################################################################
    # Function 2
    userlist = {}   # TEMPORARY PLACEHOLDER DICT. USERLIST WILL BE THE USER GUI INPUTTED VALUES
    acceptedcountry = {} # TEMPORARY LOCATION. TO BE MOVED. WILL STORE THE SCALED DOWN MAINDICT WITH USERS OF ACCEPTABLE
    # COUNTRY
    # First round of Processing for Acceptable Countries, returns a dict with accepted users
    acceptedcountry = processUser(userlist, maindict)
    '''
    for i in range(0, len(maindict)):
        name = "".join(maindict[i]['Name'])
        countryname = "".join(maindict[i]['Country'])
        print "Profiles Accepted from Country Check: %s: %s" % (name, countryname)
    '''
    ##########################################################################################################
    #Function 3
    #TO DO

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








