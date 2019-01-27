import sqlite3
import os.path


##########################################################################################################
# definition to check if it is the first time Application is running / if 'userprofiles.db' exists
# and to initiate a db connection
def login(username, password):
    # try to connect to the .db file
    try:
        # call function to retrieve from a .txt file, which stores names of tables to create, and their column names
        dbinfo = pull()
        # call function to create the DB file with respective tables and names
        createDBfile(dbinfo)
        # call function to check if user exists in db
        returnvalue = authenticateUser(username,password)

        # if returned value from authenticateUser() is 0 (no such username and password)
        if returnvalue == 0:
            print "No such user"
            return 0
        elif returnvalue == 1:
            print "User found"
            # ------- call function to close/hide login UI, and call function to process sample files into db #
            return 1
        elif returnvalue == 2:
            print "Database has more than one such username and password!"
            return 0

    except sqlite3.Error():
        print "Error opening the .db file"      ################ Replace with messagebox instead of print once GUI done

##########################################################################################################
# definition to pull table names and column names into list from "dbinfo.txt" text file in same directory
def pull():
    # if the 'dbinfo.txt' file does not exist, create a default version of it
    if os.path.exists("./dbinfo.txt") == False:
        file = open("./dbinfo.txt", "w")
        # **** if there are more tables to create by default, remember to add below in file.write()
        # use '#'at start of line to indicate table name,
        # separate each column name entry with a ','  -> e.g.   'date_of_creation_field,valid_input,hey'
        # *DO NOT* at any point in time include a space in the string(s)
        file.write("<!-- NOTE: Strictly follow the format: #<table_name> - go to next line - <column_name_1 datatype,"
                   "column_name_2 datatype> --!>\n#userprofs\nusername varchar primary key,password varchar")
        # close the filestream
        file.close()

        # call function to read the file
        dictionaryFromFileContents = read()

        # return the dictionary to function 'InitializeDBconnection()'
        return dictionaryFromFileContents

    # else if the 'dbinfo.txt' file exists, read from it
    else:
        # call function to read the file
        dictionaryFromFileContents = read()

        # return the dictionary to function 'InitializeDBconnection()'
        return dictionaryFromFileContents


# definition for reading dbinfo.txt
def read():
    # read contents of file into variable, line by line
    file = open("./dbinfo.txt", "r")

    # initiate dictionary for storing table names and column names, where key = table name & value = column names (list)
    fileinput = {}
    listoflines = []

    # this is to parse lines in the file into a list as strings for easier manipulation******
    for line in file:
        listoflines.append(line)

    # for each string in listoflines:
    for mstring in listoflines:
        # for each line, check if it is either starting with a '#'(table name)
        if mstring[0] == '#':
            # format the next line by splitting it based on the specified delimiter:
            # (refer to function 'pull()' where format of the data and delimiter usage is shown)
            listofcolumnnames = listoflines[listoflines.index(mstring)+1].split(",")

            # assign the list of column names as the value to the key (table name)
            fileinput[mstring[1:]] = {}
            fileinput[mstring[1:]] = listofcolumnnames

    # return the dictionary to function 'pull()'
    return fileinput

##########################################################################################################
# definition to create a .db file 'userprofiles.db' in current directory
def createDBfile(dbinfo):
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # for each key in the dictionary
    for n in dbinfo:
        # replace the 'next line' character with null, store result into a string variable
        ppp = str(n).replace("\n", "")

        # create a table with its respective column names
        stringofcolumnnames = ",".join(str(a) for a in dbinfo[n])
        c.execute("CREATE TABLE IF NOT EXISTS {:} ({:})".format(ppp, stringofcolumnnames))

    # commit changes (instructions given to the cursor)
    conn.commit()
    # close the connection
    conn.close()
    return

##########################################################################################################
# definition to authenticate user (see if the user's input username and password exists in userprofiles.db
def authenticateUser(username,password):
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # checks if username and password (credentials) exists in the database
    c.execute("SELECT 1 FROM userprofs WHERE username = (?) AND password = (?)", [username, password])
    result = c.fetchall()

    # if a match is not found, return a 0
    if len(result) == 0:
        return 0
    # if a match is found, return a 1
    elif len(result) == 1:
        return 1
    # if more than 1 match is found, return a 2
    else:
        return 2

    conn.commit()
    conn.close()


##########################################################################################################
# definition to insert a single profile (login credentials) into the 'userprofs' table
def addnewuser(username, password):
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # insert a row of data
    c.execute("insert or ignore into userprofs (username, password) VALUES (?,?)", (username,password))


    # commit changes (instructions given to the cursor)
    conn.commit()

    # close the connection
    conn.close()

##########################################################################################################
# definition to select all user profiles (accounts) and display from database - for coding use only
def viewusers():
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    c.execute("SELECT * FROM userprofs")
    print c.fetchall()
    conn.commit()
    conn.close()

##########################################################################################################


# main function for testing code purposes
if __name__ == "__main__":
    # try to login with hardcoded username and password (below)
    r = login("swaglord", "1g0t@BBC!")

    # add new user(s) manually through hardcoding
    addnewuser("swaglord","1g0t@BBC!")
    addnewuser("xiuqiho","password")

    viewusers()
