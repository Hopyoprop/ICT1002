import csv
import sqlite3


def exportdata(name):
    conn = sqlite3.connect('userprofiles.db')
    # create cursor object, and assign it to variable called c
    c = conn.cursor()
    c.execute("SELECT %s FROM userprofs" % name)
    with open("top3.csv", "w", newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow([i[0] for i in cursor.description])  # write headers
        csv_writer.writerows(cursor)
    conn.commit()
    conn.close()
