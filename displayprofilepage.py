from Tkinter import *
import Tkinter as tk
from sqlfunctions import *
from globalvars import *
import globalvars as gv


TITLE = ("Forte", 35)
LARGE_FONT = ("Forte", 11)
LABEL_FONT = ("Forte", 13)


# definition for displaypage frame
class DisplayPage(tk.Frame):
    def __init__(self, parent):
        # initializing the displaypage frame
        tk.Frame.__init__(self, parent)

        listofcolumns = ()
        columndictionary = []

        # findmatch button click event function
        def findmatch():
            setpagetodisplay("openLoginPage")
            self.quit()
            self.destroy()

        # update profile button click event function
        def updateprofile():
            setpagetodisplay("shutdown")
            self.quit()
            self.destroy()

        # function to get list of column names
        def getcolumnnamesfromdb():
            global listofcolumns
            # call sqlfunctions.py's getlistofcolumns method for a list of columns from table 'profiles'
            listofcolumns = getlistofcolumns("profiles")

            # for each column found
            for column in listofcolumns:
                keyname = str(column) + "_label"
                # pair its name_label with a Label object
                columndictionary.append(Label(text=str(column), font=LABEL_FONT, background="lightblue", pady=15))

            x = 30
            y = 150

            for label in columndictionary:
                label.place(x=x, y=y)
                y += 35

            templist = [str(gv.currentuser)]

            # call sqlfunctions.py's getuserprofile method for the profile data of current user
            allfoundprofiles = getuserprofiles(templist)




        # string to store welcome message
        welcomelabeltext = gv.currentuser + "'s\nHome"

        # defining components of the UI
        welcomelabel = Label(text=welcomelabeltext, font=TITLE, background="lightblue")
        updatebutton = Button(text="Update Profile", font=LARGE_FONT, command=lambda: getcolumnnamesfromdb())
        findmatchbutton = Button(text="Find Match!", font=LARGE_FONT, command=lambda: findmatch())

        welcomelabel.pack(fill=X)
        updatebutton.place(x=250, y=750)
        findmatchbutton.place(x=400, y=750)



if __name__ == "__main__":
    root = tk.Tk()
    frame = DisplayPage(root, "xiuqiho")
    root.mainloop()


