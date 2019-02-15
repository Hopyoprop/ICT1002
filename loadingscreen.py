from Tkinter import *
import Tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import tkMessageBox as tkmessagebox
import time
from sqlfunctions import *
from globalvars import *
import globalvars as gv
from function2 import *
from function3 import *
from function4 import *
from function5 import *
import operator
import copy
from threading import Thread
from events import Events


LABEL_FONT = ("Forte", 13)
TEXT_FONT = ("Forte", 13)


# definition for displaypage frame
class LoadingScreen():
    def __init__(self, dimensions, titleofwindow):
        def destroywindow():
            main.quit()
            main.destroy()
            exit()

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

        ##################################################################################################################
        ##################################################################################################################
        # gif definition
        #self.parent = main
        #self.canvas = tk.Canvas(main, width=400, height=300, background='lightblue', highlightthickness=0)
        #self.image = ImageTk.PhotoImage(Image.open("./loading.png"))
        #self.canvas.pack()


        ##################################################################################################################
        ##################################################################################################################

        # label definitions
        loadingtext = Label(main, text="We are processing your matches, it will take some time", font=LABEL_FONT, background='lightblue')
        loadingtext.pack(anchor='center')

        progresstext = Label(main, text="Loading...", font=TEXT_FONT, background='lightblue', fg='darkgreen')
        progresstext.pack(anchor='center')



        # call function to execute functions 1-5
        def call_all_functions(userdict, maindict):

            ##################################################################################################################
            ############################################# Call functions #####################################################
            ##################################################################################################################

            # define list of shortlisted users from each function called (all results are stored as list, and appended into this list)
            lists_from_each_functions = []

            ##################################################################################################################
            ############################################# Function 1
            templist = []
            # for each user, append their 'Name' into a temp list first, which will be appended into lists_from_each_functions
            # this represents function 1 (list all the profiles, their names, gender and age)
            for key, value in maindict.items():
                templist.append(str(maindict[key]['Name']).replace("['", "").replace("']", "").replace("\"", ""))

            lists_from_each_functions.append(templist)

            ##########################################################################################################
            ############################################# Function 2

            # Call function 2 (returns a list with accepted users based on currentuser's accepted_countries)
            list_accepted_profiles_based_on_country = processUser(userdict, maindict)
            # print list_accepted_profiles_based_on_country

            # print "countries (not narrowed down to 3): " + str(list_accepted_profiles_based_on_country)
            # add this list to lists_from_each_functions
            lists_from_each_functions.append(list_accepted_profiles_based_on_country)

            # print lists_from_each_functions

            # printCountries(userdict, list_accepted_profiles_based_on_country)

            # after finish function 2, update the progresstext label
            progresstext.config(text="25% done..")

            ##########################################################################################################
            ############################################# Function 3

            # dictionary that holds filtered profiles based on likes and dislikes
            dict_accepted_profiles_based_on_likesdislikes = processInterest(userdict, maindict)
            # init list that will contain top 3 profiles based on likes and dislikes
            listoftop3_accepted_profiles_based_on_likesdislikes = []

            copyof_dict_accepted_profiles_based_on_likesdislikes = {}
            # make a copy of the dictionary made by function 3 (shortlisted profiles based on likes and dislikes)
            copyof_dict_accepted_profiles_based_on_likesdislikes = copy.deepcopy(
                dict_accepted_profiles_based_on_likesdislikes)

            # repeat 3 times to get top 3 matches based on likes & dislikes
            for i in range(0, 3):
                # if dictionary not empty and if highest value is > 0 (meaning point is more than 0)
                if len(copyof_dict_accepted_profiles_based_on_likesdislikes) != 0 and \
                        max(copyof_dict_accepted_profiles_based_on_likesdislikes.iteritems(),
                            key=operator.itemgetter(1))[1] > 0:
                    # get key (profile) with highest score, if theres a tie, only one of the profiles is returned
                    profile_with_highest_score = \
                    max(copyof_dict_accepted_profiles_based_on_likesdislikes.iteritems(), key=operator.itemgetter(1))[0]

                    # append this profile into listoftop3_accepted_profiles_based_on_likesdislikes
                    listoftop3_accepted_profiles_based_on_likesdislikes.append(str(profile_with_highest_score))

                    # delete profile with highest score from the dictionary
                    del copyof_dict_accepted_profiles_based_on_likesdislikes[str(profile_with_highest_score)]

            # delete the copy of the dicitonary (dont waste space)
            del copyof_dict_accepted_profiles_based_on_likesdislikes

            # print "top3_likesdislikes: " + str(listoftop3_accepted_profiles_based_on_likesdislikes)
            # add this list to lists_from_each_functions
            lists_from_each_functions.append(listoftop3_accepted_profiles_based_on_likesdislikes)
            # print "lists_from_each_functions: " + str(lists_from_each_functions)

            # printLikesDislikes(dict_accepted_profiles_based_on_likesdislikes)

            # after finish function 3, update the progresstext label
            progresstext.config(text="50% done..")

            ##########################################################################################################
            ############################################# Function 4

            dict_accepted_profiles_based_on_books = processBook(userdict, maindict)
            # init list that will contain top 3 profiles based on books
            listoftop3_accepted_profiles_based_on_books = []

            # make a copy of the dictionary made by function 3 (shortlisted profiles based on likes and dislikes)
            copyof_dict_accepted_profiles_based_on_books = copy.deepcopy(dict_accepted_profiles_based_on_books)
            # repeat 3 times to get top 3 matches based on likes & dislikes
            for i in range(0, 3):
                # if dictionary not empty and if highest value is > 0 (meaning point is more than 0)
                if len(copyof_dict_accepted_profiles_based_on_books) != 0 and \
                        max(copyof_dict_accepted_profiles_based_on_books.iteritems(), key=operator.itemgetter(1))[1] > 0:
                    print copyof_dict_accepted_profiles_based_on_books
                    # get key (profile) with highest score, if theres a tie, only one of the profiles is returned
                    profile_with_highest_score = \
                    max(copyof_dict_accepted_profiles_based_on_books.iteritems(), key=operator.itemgetter(1))[0]

                    # append this profile into listoftop3_accepted_profiles_based_on_likesdislikes
                    listoftop3_accepted_profiles_based_on_books.append(str(profile_with_highest_score))
                    # delete profile with highest score from the dictionary
                    del copyof_dict_accepted_profiles_based_on_books[profile_with_highest_score]

            # delete the copy of the dicitonary (dont waste space)
            del copyof_dict_accepted_profiles_based_on_books

            # add this list to lists_from_each_functions
            lists_from_each_functions.append(listoftop3_accepted_profiles_based_on_books)

            ################################################################################################################
            ######################### DELETE THIS HARDCODED FUNCTION 4 DICTIONARY AND LIST (FOR TEST USE ONLY) #############
            '''dict_accepted_profiles_based_on_books = {'Jenny Wang': 20, 'Rose': 10, 'Kevin': 20, 'Teresa': 20,
                                                     'Joel Jackson': 40, 'Carol': 20, 'Shelley': 20, 'Lisa Marie': 0}
            listoftop3_accepted_profiles_based_on_books = ['Joel Jackson', 'Carol', 'Shelley']

            #listoftop3_accepted_profiles_based_on_books = []
            lists_from_each_functions.append(listoftop3_accepted_profiles_based_on_books)'''

            ################################################################################################################


            ##########################################################################################################
            ############################################# Function 5

            bestMatched = processMatches(list_accepted_profiles_based_on_country,
                                         dict_accepted_profiles_based_on_likesdislikes,
                                         dict_accepted_profiles_based_on_books, userdict, maindict)

            # print "bestMatched: " + str(bestMatched)
            lists_from_each_functions.append(bestMatched)
            # print "updated list: " + str(lists_from_each_functions)

            # after finish function 5, update the progresstext label
            progresstext.config(text="Done!!")

            ########################################### end of call functions ################################################
            ##################################################################################################################

            # update global variables with list of shortlisted Usernames
            # ^ once function 5 is done executing and global vars are updated
            # (list of shortlisted Usernames from each function)
            gv.setlist_of_shortlisted_users(lists_from_each_functions)


            main.quit()
            main.destroy()

        # end of function definition of call_all_functions()



        ##################################################################################################################

        # get user's dictionary from global variable 'userdictionary'
        # (this was added at 'displayprofilepage' upon clicking 'Find Match!' button
        userdict = gv.userdictionary
        userdict.pop('Username', None)  # remove user's 'Username' field from the his/her own profile dictionary

        # get maindictionary
        maindict = gv.maindictionary

        main.mainloop()
        # set stop command to a default value (other than "stop" which would stop the UI)
        call_all_functions(userdict,maindict)
        print "Hi in main thread"

        #main.mainloop()

        #gif_thread.is_alive = False
        gv.setpagetodisplay("openFindMatchResultsPage")



# main function for testing code, not for production use
if __name__ == "__main__":
    LoadingScreen("400x400", "MatchMakeMe - Loading")



