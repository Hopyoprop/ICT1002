from Tkinter import *
import Tkinter as tk
from sqlfunctions import *
from loginpage import *
from displayprofilepage import *
import globalvars as gv


# definition to create a window
def createwindow(classofwindow, dimensions, titleofwindow):

    # defining Tk() instance
    main = tk.Tk()
    main.resizable(False, False)
    main.geometry(dimensions)
    main.title(titleofwindow)
    main.configure(background='lightblue')

    # list to store input x and y dimensions of window
    xANDy = dimensions.split("x")


    # getting coordinates for center of screen, then set them using Tk.geometry
    xposition = int(main.winfo_screenwidth()/2 - int(xANDy[0])/2)
    yposition = int(main.winfo_screenheight()/2 - int(xANDy[1])/2)

    # set the location of 'main'
    main.geometry("+%d+%d" % (xposition, yposition))

    # defining a frame to work on (display things on)
    containerframe = tk.Frame()
    containerframe.grid(row=0, column=0, sticky="nsew")

    classofwindow(containerframe)
    main.mainloop()
    main.quit()

    # when exiting the loop, destroy all used resources if window still exists
    main.destroy()


def windowtraverser():
    while str(gv.showpagecommand) is not "shutdown":
        if str(gv.showpagecommand) == "openLoginPage":
            createwindow(LoginPage, "500x300", "MatchMakeMe - Login")

        elif str(gv.showpagecommand) == "openDisplayPage":
            createwindow(DisplayPage, "500x800", "MatchMakeMe - My Profile")


# main function
if __name__ == "__main__":
    gv.init()
    # call function to retrieve from a .txt file, which stores names of tables to create, and their column names
    dbinfo = pull()
    # call function to create the DB file with respective tables and names
    createDBfile(dbinfo)

    createwindow(LoginPage, "500x300", "MatchMakeMe - Login")




    windowtraverser()
    print "Program has successfully completed and shutdown!"




