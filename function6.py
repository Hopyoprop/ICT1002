import csv
import sqlite3
import datetime as dt 

def exportdata(list,number):      #get function 2 to 5 best matched

    conn = sqlite3.connect('userprofiles.db')        # connect to database
    # create cursor object, and assign it to variable called c
    c = conn.cursor()       #pinpoint records in a database. 
    placeholder= '?' 
    placeholders= ', '.join(placeholder for unused in list) # place in ? when list has item
    query = "SELECT Name,Gender,Country,Age,Likes,Dislikes,Books FROM profiles WHERE Name IN (%s)" %placeholders
    c.execute(query,list)       #execute the sql to get best matched data
    outputfilename = 'bestmatch_{}.csv'.format( dt.datetime.now().strftime('%Y%m%d%H%M%S') )        #make a unique file everytime user export data
    functionList = []       #make a list to output string as 1 column
    functionText = "Function %d" %number # function 2 or 3 or 4 or 5
    functionList.append(functionText)       #add functionText into functionList
    with open(outputfilename, "a") as csv_file:     #For append and name it bestmatch.csv
        csv_writer = csv.writer(csv_file,lineterminator='\n')
        csv_writer.writerow(functionList)       #write function number
        csv_writer.writerow([i[0] for i in c.description])      #write headers
        csv_writer.writerows(c)     #write user data
        csv_writer.writerow('\n')       #blank row after last userdata
    conn.commit()
    conn.close()
    
def getFunctionList(receivedlist):
    functionNo = 0
    function2list = receivedlist[0]
    function3list = receivedlist[1]
    function4list = receivedlist[2]
    function5list = receivedlist[3]
 
    if function2list >= 0: 
        functionNo = 2
        exportdata(function2list,functionNo)

    if function3list >= 0:
        functionNo = 3
        exportdata(function3list,functionNo)

    if function4list >= 0:
        functionNo = 4
        exportdata(function4list,functionNo)

    if function5list >= 0:
        functionNo = 5
        exportdata(function5list,functionNo)

        
list = [['Michael Jackson', 'Lisa Marie', 'Teresa', 'Carol', 'Kevin', 'Rose', 'Shelley', 'Joel Jackson', 'Jenny Wang', 'Angela Little'],[], ['Angela Little', 'Joel Jackson', 'Rose'], ['Teresa', 'Lisa Marie', 'Carol']]
list1 = [['Michael Jackson', 'Lisa Marie', 'Teresa', 'Carol', 'Kevin', 'Rose', 'Shelley', 'Joel Jackson', 'Jenny Wang', 'Angela Little'],[],[],[]]
getFunctionList(list) # trying if function works
