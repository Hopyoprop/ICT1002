from Tkinter import *
import Tkinter as tk
import tkMessageBox as tkmessagebox
import re
from sqlfunctions import *
from copytomain import *
from globalvars import *


# defining font sizes
LARGE_FONT = ("Forte", 11)
TITLE = ("Forte", 35)

#######################################################################################################################
#######################################################################################################################

# definition for LoginPage frame, it will inherit a tk.Frame
class LoginPage(tk.Frame):
    # parent is our parent class (in this case it is 'Head')
    def __init__(self, parent):
        # initializing the loginpage frame
        tk.Frame.__init__(self, parent)
        # login button click event function
        def loginclick():
            logincode = login(usernamefieldentry.get(), passwordfieldentry.get())
            # if failed to login
            if logincode == 0:
                usernamefieldentry.delete(0, 'end')
                passwordfieldentry.delete(0, 'end')
                # show error message
                tkmessagebox.showerror("Error", "Try Again!")

            # if login was successful
            elif logincode == 1:
                # set the 'currentuser' variable on main.py
                setcurrentusername(usernamefieldentry.get())

                # return the string description of next page for main.py to open
                setpagetodisplay("openDisplayPage")

                # quit here to go back to 'main.py'
                self.quit()
                self.destroy()


            # if multiple records were found in the database (programming error)
            elif logincode == 2:
                print "Unable to login - Database Error"

        def adduserclick():
            if usernamefieldentry.get() != "" and passwordfieldentry.get() != "":
                if re.match('^[\w-]+$', str(usernamefieldentry.get())) is not None:
                    # call function to add user into db
                    addusercode = addnewuser(usernamefieldentry.get(), passwordfieldentry.get())

                    # if failed to add user
                    if addusercode == 0:
                        usernamefieldentry.delete(0, 'end')
                        passwordfieldentry.delete(0, 'end')
                        tkmessagebox.showerror("Error", "Unable to create user " + usernamefieldentry.get())

                    # else if successfully created
                    elif addusercode == 1:
                        tkmessagebox.showinfo("Success", "User " + usernamefieldentry.get() + " was created successfully!")

                    # else if user already exists
                    elif addusercode == 2:
                        tkmessagebox.showerror("Error", "User " + usernamefieldentry.get() + " already exists!")
                else:
                    tkmessagebox.showerror("Error", "Unable to create user: no special characters allowed for "
                                                    "usernames" + usernamefieldentry.get())

            else:
                usernamefieldentry.delete(0, 'end')
                passwordfieldentry.delete(0, 'end')
                tkmessagebox.showwarning("Warning", "Please only use alphanumerical characters for username, "
                                                    "and don't leave fields blank")


        # defining components of the UI
        titleofapp = Label(text="MatchMakeMe", font=TITLE, background="lightblue")
        titledesc = Label(text="for desperate people by desperate people", font=LARGE_FONT, background="lightblue")
        usernamefieldlabel = Label(text="Username:", font=LARGE_FONT, background="lightblue")
        passwordfieldlabel = Label(text="Password:", font=LARGE_FONT, background="lightblue")
        usernamefieldentry = Entry(width=35, background="lightblue")
        passwordfieldentry = Entry(width=35, background="lightblue")
        loginbutton = Button(text="Login", font=LARGE_FONT, command=lambda: loginclick())
        createaccountbutton = Button(text="Create Account", font=LARGE_FONT, command=lambda: adduserclick())

        titleofapp.place(x=90, y=40)
        titledesc.place(x=120, y=120)
        usernamefieldlabel.place(x=95, y=190)
        passwordfieldlabel.place(x=95, y=215)
        usernamefieldentry.place(x=195, y=190)
        passwordfieldentry.place(x=195, y=215)
        loginbutton.place(x=370, y=250)
        createaccountbutton.place(x=220, y=250)


#######################################################################################################################
#######################################################################################################################

if __name__ == "__main__":
    main = tk.Tk()
    cont = tk.Frame()
    LoginPage(cont)
    main.mainloop()