import sqlite3
import os.path
import time

##########################################################################################################
# definition to check if it is the first time Application is running / if 'userprofiles.db' exists
# and to initiate a db connection
def login(username, password):
    # try to connect to the .db file
    try:
        # call function to check if user exists in db
        returnvalue = authenticateUser(username,password)

        # if returned value from authenticateUser() is 0 (no such username and password)
        if returnvalue == 0:
            # print "No such user!"
            return 0
        elif returnvalue == 1:
            # print "User found!"
            # ------- call function to close/hide login UI, and call function to process sample files into db #
            return 1
        elif returnvalue == 2:
            # print "Database has more than one such username and password!"
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
                   "column_name_2 datatype> --!>\n#userprofs\nusername varchar primary key,password varchar\n#profiles"
                   "\nUsername varchar primary key,Name varchar,Gender varchar,Country varchar,Acceptable_country "
                   "varchar,Age varchar,Acceptable_age_range varchar,Likes varchar,Dislikes varchar,Books varchar")
        # close the filestream
        file.close()

        # call function to read the file
        dictionaryFromFileContents = read()

        # return the dictionary
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
    c.execute("SELECT 1 FROM userprofs WHERE username = (?) AND password = (?)", [str(username), str(password)])
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

    try:
        # check if user already exists:
        exist = c.execute("SELECT * FROM userprofs WHERE username = (?)", (username,)).fetchall()
        # if exist
        if len(exist) > 0:
            return 2
        # if does not exist
        elif len(exist) == 0:
            # insert a row of data
            c.execute("INSERT INTO userprofs (username, password) VALUES (?,?)", (username, password))
            # commit changes (instructions given to the cursor)
            conn.commit()
        return 1

    except:
        print "In exit"
        return 0

    # close the connection
    conn.close()


##########################################################################################################
# definition to delete a single profile (login credentials) into the 'userprofs' table
def deleteuser(user):
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    try:
        # delete row of data in the table with same username and password
        c.execute("DELETE FROM userprofs WHERE username = (?)",(user,))

        # commit changes (instructions given to the cursor)
        conn.commit()
    except:
        conn.close()
        return 0

    # close the connection
    conn.close()
    return 1

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
# definition to get list of column names from database based on specified table name
def getlistofcolumns(table_name):
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # pragma the specified sql table for its column names
    c.execute("PRAGMA table_info(%s)" % table_name)
    columnnames = (str(a[1]) for a in c.fetchall())

    conn.commit()
    conn.close()

    columns=[]
    for col in columnnames:
        columns.append(str(col))

    return columns

##########################################################################################################
# definition to get dictionaries of specified users' profile
def getuserprofiles(listofuserstofind):
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')

    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # concatenate all usernames in 'listofusertofind' into a single string
    users = str(", ".join(listofuserstofind))
    #print str(users)

    statement = "SELECT * FROM profiles WHERE Username in (?)"
    # get all records from db where any specified username matches a record in 'Username' of table 'profiles' in db
    c.execute(statement, (users,))
    fetchedrecords = c.fetchall()

    listofuserdata = []
    # if none of the users found
    if len(fetchedrecords) == 0:
        return 0
    else:
        for record in fetchedrecords:
            for indexval in record:
                listofuserdata.append(str(indexval))
    conn.commit()
    conn.close()

    return listofuserdata


##########################################################################################################
# definition to retrieve all records in db and return as a dictionary
def createmaindictionary():
    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')

    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    c.execute("SELECT * FROM profiles")
    fetchedrecords  = c.fetchall()

    maindictionary = {}

    # call function to get list of column names for the profiles table, then slice away the first field (primary key)
    listofcolumns = getlistofcolumns('profiles')
    listofcolumns = listofcolumns[1:]

    # if no records - worst case scenario
    if len(fetchedrecords) == 0:
        return 0
    # else when records are found
    else:
        dcount = 0
        for record in fetchedrecords:
            # get the name of user of current record
            #nameofuser = record[1]
            #nameofuser = str(nameofuser).replace("u'","'")

            # slice the record (remove first field which represents the primary key 'Username')
            temprecordlist = record[1:]

            # create the dictionary entry for current user
            maindictionary[dcount] = {}

            # for each column, add the column name as a sub-dictionary and the field data as a list into the maindictioanry
            for index in range(0, len(listofcolumns)):
                maindictionary[dcount][str(listofcolumns[index])] = {}
                # initialize list, dump the string (data of specific column) into it, so that we can add it into
                # sub-dictionary as a list

                tempfieldlist = []
                # split them nicely and add each substring separated by a ',' as  an element in the sublist
                temp = str(temprecordlist[index]).split(",")
                tt = []
                # for each substring
                for t in temp:
                    # remove all spaces infront of the substring
                    while str(t).startswith(" "):
                        t=str(t)[1:]
                    # remove all spaces behind the substring
                    while str(t).endswith(" "):
                        t = str(t)[:len(str(t))-1]
                    tt.append(str(t))


                tempfieldlist.append(temp)

                # assign the list to the particular field representing a specific column of the table
                maindictionary[dcount][str(listofcolumns[index])] = tt

            dcount+=1  #  increment counter by 1

    conn.commit()
    conn.close()

    return maindictionary

##########################################################################################################
# definition to add user matchmake profiles into db
def adduserprofile(profiledatainlist):
    tuplevalues = tuple(profiledatainlist)

    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # Insert user data into userprofs.
    table = "profiles"

    # execute insert statement using the obtained tuple into the 'profiles' table
    try:
        c.execute(
            """INSERT OR REPLACE INTO %s (Username, Name, Gender, Country, Acceptable_country, Age, Acceptable_age_range, Likes, Dislikes, Books) VALUES (?,?,?,?,?,?,?,?,?,?)""" % table,
            (tuplevalues))
        # commit changes (instructions given to the cursor)
        conn.commit()
        # close the connection
        conn.close()
        return 1
    except:
        return 0

##########################################################################################################
##########################################################################################################
# definition to insert all user profile data into the 'userprofs' table
def insert_profile(maindicti):

    # Before inserting data, check if db table exists. If not, create one.
    # check_table_exists(maindicti)

    user_values_list = []

    # For each user (type: <dict>), retrieve the data values (type: <list>).
    # Iterate through key's values (type: <string>) and append to a string.
    # Append each string for that user to a list.
    for key, value in maindicti.items():
        user_string = ""

        # append once (this is assuming that 'Name' field is the first field)
        if str(key) == "Name":
            user_values_list.append(str(maindicti[key]).replace("['","").replace("']",""))

        # for each item in list contained at current field
        for element in value:
            user_string += "%s," % element

        user_string = user_string[:-1]
        user_values_list.append(user_string)

    # Convert list to tuple.
    user_values_tuple = tuple(user_values_list)

    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # Insert user data into userprofs.
    table = "profiles"

    # execute insert statement using the obtained tuple into the 'profiles' table
    #command = """INSERT OR IGNORE INTO %s VALUES """ % table
    #c.execute(command+"(?,?,?,?,?,?,?,?,?,?)", (user_values_tuple))
    c.execute("""INSERT OR IGNORE INTO %s (Username, Name, Gender, Age, Dislikes, Acceptable_age_range, Acceptable_country, Books, Likes, Country) VALUES (?,?,?,?,?,?,?,?,?,?)""" % table, (user_values_tuple))
    # commit changes (instructions given to the cursor)
    conn.commit()
    # close the connection
    conn.close()


##########################################################################################################
# definition to check if 'profiles' table exists. If not, create table.
def check_table_exists(maindict):
    dict_key = []
    column_names = ""

    # Append maindict keys (type: <dict>) as a list.
    for p_key, profile in maindict.items():
        for k, v in profile.items():
            dict_key.append(k)

    # Append keys (type: <str>) to a list. This will be used as the table's column names.
    # Break if the next key-to-append is already declared (eg. same as the first column).
    column_names += "%s varchar primary key," % dict_key[0]
    for k in dict_key[1:]:
        if k != dict_key[0]:
            column_names += "%s varchar," % k
        else:
            break
    column_names = column_names[:-1]

    # try to connect (this action will create a .db file in same directory if it does not exist)
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()

    # create a table with its respective column names
    table = "profiles"
    c.execute("""CREATE TABLE IF NOT EXISTS {:} ({:})""".format(table,column_names))

    # commit changes (instructions given to the cursor)
    conn.commit()
    # close the connection
    conn.close()


##########################################################################################################


# main function for testing code purposes
if __name__ == "__main__":
    # try to login with hardcoded username and password (below)
    #r = login("swaglord", "1g0t@BBC!")

    # add new user(s) manually through hardcoding
    #addnewuser("swaglord","1g0t@BBC!")
    #addnewuser("xiuqiho","password")
    #deleteuser("aaa")
    #authenticateUser("xiuqiho","password")

    '''tempdict = {'Teresa':{'Name': ['Teresa'],
                           'Gender': ['F'],
                           'Age': ['22'],
                           'Dislikes': ['garlic', ' durian', ' swimming'],
                           'Acceptable_age_range': ['18', '30'],
                           'Acceptable_country': ['Singapore', ' China'],
                           'Books': ['Total Truth: Liberating Christianity from its Cultural Captivity',
                                'Reflections on the Psalms', 'Intercessory Prayer: How God Can Use Your Prayers to Move Heaven Earth',
                                     "God 's Favor - Breath Of Heaven", 'Letters to Malcolm: Chiefly on Prayer'],
                           'Likes': ['hotpot', ' chilli', ' chicken and chops', ' roses', ' movies'],
                           'Country': ['Singapore']}}
    adduserprofile(tempdict)
    viewusers()'''
    #print getlistofcolumns('profiles')

    result = createmaindictionary()


