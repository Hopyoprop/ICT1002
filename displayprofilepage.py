from Tkinter import *
import Tkinter as tk
from sqlfunctions import *
from globalvars import *
import globalvars as gv
import tkMessageBox as tkmessagebox

TITLE = ("Forte", 24)
LARGE_FONT = ("Times New Roman", 11)
LABEL_FONT = ("Comic Sans MS", 10)
BUTTON_FONT = ("Times New Roman",10)
FINDMATCH_FONT = ("Forte", 13)
LOGOUT_FONT = ("Forte", 11)

# definition for displaypage frame
class DisplayPage(tk.Frame):
    def __init__(self, dimensions, titleofwindow):
        main = tk.Tk()
        main.resizable(False, False)
        main.geometry(dimensions)
        main.title(titleofwindow)
        main.configure(background='lightblue')
        main.protocol("WM_DELETE_WINDOW", lambda: destroywindow())

        # list to store input x and y dimensions of window
        xANDy = dimensions.split("x")

        # getting coordinates for center of screen, then set them using Tk.geometry
        xposition = int(main.winfo_screenwidth() / 2 - int(xANDy[0]) / 2)
        yposition = int(main.winfo_screenheight() / 2 - int(xANDy[1]) / 2)

        # set the location of 'main'
        main.geometry("+%d+%d" % (xposition, yposition))


        columnlist = []
        profiledatalist = []

        # findmatch button click event function
        def findmatch():

            # get currentuser's username
            current_user_Username = str(gv.currentuser)

            # add the current user into a list (necessary to add into list as function to get profile requires a list)
            current_user_listholder = []
            current_user_listholder.append(current_user_Username)

            # call getuserprofiles() function with the list
            returned_profile_list = getuserprofiles(current_user_listholder)

            # process returned list into a dictionary
            # if no such user's record in the db, inform user they have to fill up their profile and update it
            if returned_profile_list == 0:
                tkmessagebox.showwarning("Cant find match","Please input your profile details (leave no blanks) and press 'Update Profile'")
                return
            # else if a list is returned:
            else:
                colList = getlistofcolumns('profiles')
                userdict = {}

                # for each column in profiles table, add the column name(string) and its corresponding field data into userdictionary
                for col_index in range(0, len(colList)):
                    templist = []

                    temp = returned_profile_list[col_index].split(",")
                    tt = []

                    # for each substring
                    for t in temp:
                        # remove all spaces infront of the substring
                        while str(t).startswith(" "):
                            t = str(t)[1:]
                        # remove all spaces behind the substring
                        while str(t).endswith(" "):
                            t = str(t)[:len(str(t)) - 1]
                        tt.append(str(t))
                    #templist.append(returned_profile_list[col_index])

                    userdict[str(colList[col_index])] = tt

                # set the userdict variable into global variable 'userdictionary'
                gv.setuserdictionary(userdict)

                # return the string description of next page for main.py to open
                setpagetodisplay("openLoadingScreen")

                main.quit()
                main.destroy()

        # update profile button click event function
        def updateprofile():
            textboxinputlist = []

            # append the Username of current user first as textboxes would not include that field
            textboxinputlist.append(str(gv.currentuser))

            # for each entry box (fields) created dynamically during intialization, get their field inputs
            for field in profiledatalist:
                if str(field.get()) is not "" and str(field.get()).strip(" ") is not "":
                    textboxinputlist.append(str(field.get()))
                else:
                    tkmessagebox.showerror("Empty Field(s) exists", "Empty fields exist, please make sure to not leave any field blank")
                    return
            # update or insert into user's profile in db, the strings in the entry box
            returnedvalue = adduserprofile(textboxinputlist)

            # if updated profile data successfully
            if returnedvalue == 1:
                tkmessagebox.showinfo("Update Success", "Your profile has been updated successfully")
            elif returnedvalue ==0:
                tkmessagebox.showwarning("Update Unsuccessful", "Something went wrong, your profile could not be updated")

        def logout():
            setpagetodisplay("openLoginPage")
            main.quit()
            main.destroy()

        def destroywindow():
            main.quit()
            main.destroy()
            exit()

        # call sqlfunctions.py's getlistofcolumns method for a list of columns from table 'profiles'
        listofcolumns = getlistofcolumns("profiles")
        # remove the 'Username' primary key field as we wont need to display it
        listofcolumns = listofcolumns[1:]

        # get current user's profile from the db
        userdatalist = getuserprofiles([gv.currentuser])


        ##################################################################################################################
        ########################################### Creating the widgets #################################################
        # labelframe here
        profilelabelframe = LabelFrame(main, bd=5, background="lightblue")


        # for each column found
        for columnindex in range(0, len(listofcolumns)):
            # pair its name with a label, and the corresponding field with a entry box
            columnlist.append(Label(profilelabelframe, text=str(listofcolumns[columnindex]), font=LABEL_FONT, background="lightblue", pady=5))
            profiledatalist.append(Entry(profilelabelframe, width=45, background="lightblue", font=LARGE_FONT))


        # if returned profile list is empty (length is empty), display empty entry boxes
        if userdatalist == 0:
            for index in range(0, len(columnlist)):
                columnlist[index].grid(row=index, column=0, sticky="W")
                profiledatalist[index].grid(row=index, column=1, padx=15, pady=6)
        else:
            # remove the 'Username' primary key data as we wont need to display it
            userdatalist = userdatalist[1:]
            for index in range(0, len(columnlist)):
                columnlist[index].grid(row=index, column=0, sticky="W")
                profiledatalist[index].insert(0, userdatalist[index])
                profiledatalist[index].grid(row=index, column=1, padx=15, pady=6)



        # defining components of the UI

        # string to store welcome message
        welcomelabeltext = str(gv.currentuser) + "'s\nHome\n"

        welcomelabel = Label(main,text=welcomelabeltext, font=TITLE, background="lightblue")
        updatebutton = Button(main, text="Update Profile", font=BUTTON_FONT, command=lambda: updateprofile())
        findmatchbutton = Button(main, text="Find a Match!", font=FINDMATCH_FONT, command=lambda: findmatch())
        logoutbutton = Button(main, text="<- Logout", font=LOGOUT_FONT, command=lambda: logout())

        welcomelabel.pack(fill=X)
        profilelabelframe.pack(fill=X)
        updatebutton.place(x=410, y=419)
        findmatchbutton.place(x=203, y=485)
        logoutbutton.place(x=35, y=488)

        ############################################ end of creating widgets #############################################
        ##################################################################################################################
        # bring window to front (have to do this because of the filedialog tk window processSample created)
        main.lift()
        main.attributes('-topmost', True)
        main.attributes('-topmost', False)
        main.mainloop()


# main function for testing code, not for production use
if __name__ == "__main__":
    gv.setcurrentusername("a")
    DisplayPage("500x570", "MatchMakeMe - My Profile")


