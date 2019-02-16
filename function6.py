'''
Function 6
Team:
Dominic Gian
Guang Jun
Jun Ming
Ho Xiu Qi
Yeo Han, Jordan
'''

import csv
import sqlite3
import datetime as dt
import tkMessageBox as tkmessagebox


def exportdata(list, number):  # get function 2 to 5 best matched
    try:
        conn = sqlite3.connect('userprofiles.db')  # connect to database
        # create cursor object, and assign it to variable called c
        c = conn.cursor()  # pinpoint records in a database.
        placeholder = '?'
        placeholders = ', '.join(placeholder for unused in list)  # place in ? when list has item
        query = "SELECT Name,Gender,Country,Acceptable_country,Age,Acceptable_age_range,Likes,Dislikes,Books FROM profiles WHERE Name IN (%s)" % placeholders
        c.execute(query, list)  # execute the sql to get best matched data
        outputfilename = 'bestmatch_{}.csv'.format(
            dt.datetime.now().strftime('%Y%m%d%H%M%S'))  # make a unique file everytime user export data
        functionList = []  # make a list to output string as 1 column
        functionText = "Function %d" % number  # function 2 or 3 or 4 or 5
        functionList.append(functionText)  # add functionText into functionList
        with open(outputfilename, "a") as csv_file:  # For append and name it bestmatch.csv
            csv_writer = csv.writer(csv_file, lineterminator='\n')
            csv_writer.writerow(functionList)  # write function number
            csv_writer.writerow([i[0] for i in c.description])  # write headers
            csv_writer.writerows(c)  # write user data
            csv_writer.writerow('\n')  # blank row after last userdata
        conn.commit()
        conn.close()
        return 1
    except:
        return 0

def getFunctionList(receivedlist):
    # do 4 times for four functions (function 2-5)
    for i in range(0, 4):
        # call function, and get a status code
        returnstatus = exportdata(receivedlist[i+1], i+2)
        # if returned code is 0 (an error/exception occured), notify user and exit this function getFunctionList()
        if returnstatus == 0:
            tkmessagebox.showerror("Error Occurred",
                                   "An error occured when generating a CSV file. Failed to create CSV.")
            return

    # if nothing happened when trying to generate a CSV file using the sub-lists of profiles from receivedlist
    # notify user that a CSV file was successfully generated in the same directory as 'main.py' script
    tkmessagebox.showinfo("CSV File Generated","CSV file has successfully been generated in current directory of script!")
    return
