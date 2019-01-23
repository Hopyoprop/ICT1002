import Tkinter as tk
import tkFileDialog as filedialog
import sys

def openMainWindow():

    return
    ''' insert code for designing user input UI '''

def processSamples():

    # initialize main dictionary
    # maindict = {}
    dcount = 0

    # open file dialog browser to select files to parse
    mainwin = tk.Tk()
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
    return


# function definition for parsing any field other than 'Books'/'Acceptable_age_range'/NULL
def parseCurrentLine(line, dcount):
    try:

        # get the field of the line
        field = line.split(": ")[0]
        # get the content portion of the line
        content = line.split(": ")[1]

        templist = []

        # further split the contents based on delimiter of ","
        splittedcontent = content.rstrip('\n').split(",")
        for a in splittedcontent:
            templist.append(a.rstrip(' ').lstrip())


        # assign the field and templist into the dictionary
        maindict[dcount][field] = templist

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
        # further split the contents based on delimiter of ","
        splittedcontent = content[:-1].rstrip(' ').split("-")

        templist = []
        # for each substring in 'splittedcontent', add to a list
        for a in splittedcontent:
            templist.append(a)
        # assign the field and templist into the dictionary
        maindict[dcount][field] = templist
    except:
        print "Exception occured within parseAgeRange function"
        exit()
    return


''' Main Function '''
if __name__ == "__main__":
    # call function to instantiate GUI window tk() for user input
    openMainWindow()

    # initialize variables
    maindict = {}

    # call function to process data from all sample files into a dictionary
    processSamples()

    # once processing done, take dictionary/list of user input and compare with each dictionary of processed profile
    # DTF_Match()

    # print maindict
    print maindict[0]
    print maindict[1]
    print maindict[2]
    print maindict[3]
    print maindict[4]
    print maindict[5]
    print maindict[6]
    print maindict[7]
    print maindict[8]
    print maindict[9]








