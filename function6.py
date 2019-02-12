import csv
import sqlite3


def exportdata(name1,name2,name3):      # get top 3 best matched name
    conn = sqlite3.connect('userprofiles.db')        # connect to database
    # create cursor object, and assign it to variable called c
    c = conn.cursor() #pinpoint records in a database. 
    c.execute("SELECT Name,Gender,Country,Age,Likes,Dislikes,Books FROM profiles WHERE Name IN (?,?,?)",(name1,name2,name3))      # execute the sql to get top 3 best match data
    with open("top3.csv", "w") as csv_file: #For writing. Overwrites the file if the file exists. Otherwise, creates a new file for writing, and name for top3.csv
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in c.description]) # write headers
        csv_writer.writerows(c)
    conn.commit()
    conn.close()


#exportdata('Teresa','Carol','Kevin') # trying if function works