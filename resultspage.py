from globalvars import *
import globalvars as gv
import Tkinter as tk
from Tkinter import *
import ttk
from Tkinter import *
import tkMessageBox as tkmessagebox
from function6 import *

TITLE_FONT = ("Forte", 22)
LABEL_FONT = ("Forte", 10)
FOUNDMATCHESLABEL_FONT = ("Forte", 12)
DATA_FONT = ("Times New Roman", 10)
LOGOUT_FONT = ("Forte", 11)
RETURNHOME_FONT = ("Forte", 13)

class ResultsPage():
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

        def destroywindow():
            main.quit()
            main.destroy()
            exit()

        # definition to return to loginpage
        def logout():
            gv.setpagetodisplay("openLoginPage")
            main.quit()
            main.destroy()

        # definition to return to homepage
        def returnhome():
            setpagetodisplay("openDisplayPage")
            main.quit()
            main.destroy()

        # definition to generate CSV file based on the results (Function 6)
        def generateCSV():
            # get the list of sub-lists of users that were displayed
            # (basically the users that we want to make CSV file with)
            list_of_users_to_generateCSV = gv.getshortlisteduserslist()

            exportdata(list_of_users_to_generateCSV)

        # definition to make label on main reflect how many matches were found
        def foundmatchescount_labelupdate(number):
            self.foundmatchescountlabel.config(text="%s Matches Found!" % str(number))


        ################################################################################################################
        ########################################### Designing the UI####################################################
        # defining components of the UI
        self.titlelabel = Label(main, text="Matches Found", bg='lightblue', font=TITLE_FONT)
        self.titlelabel.place(x=180,y=5)

        self.sortbylabel = Label(main, text="Sort By: ", bg='lightblue', font=LABEL_FONT)
        self.sortbylabel.place(x=5, y=55)

        self.logoutbutton = Button(main, text="<- Logout", font=LOGOUT_FONT, command=lambda: logout())
        self.logoutbutton.place(x=20, y=650)

        self.returntoprofilepagebutton = Button(main, text="Return to My Home", font=RETURNHOME_FONT, command=lambda: returnhome())
        self.returntoprofilepagebutton.place(x=205, y=640)

        self.foundmatchescountlabel = Label(main, text="0 Matches Found!", bg='lightblue', font=FOUNDMATCHESLABEL_FONT)
        self.foundmatchescountlabel.place(x=285, y=55)

        self.makeCSVbutton = Button(main, text="Generate CSV", font=LOGOUT_FONT, command=lambda: generateCSV())
        self.makeCSVbutton.place(x=415, y=650)

        ################################################################################################################
        ############################################# Combo Box Filter #################################################

        # defining combobox style
        self.combostyle = ttk.Style()

        self.combostyle.theme_create('combostyle', parent='alt',
                                     settings={'TCombobox':
                                                   {'configure':
                                                        {'relief': 'raised'
                                                         }}})
        # set the style
        self.combostyle.theme_use('combostyle')

        # defining the filters for users to select from
        self.filteroptions = ["Function 1", "Function 2", "Function 3", "Function 4", "Function 5"]

        self.filtercombobox = ttk.Combobox(main, width=20, state="readonly", values=self.filteroptions)
        self.filtercombobox['values'] = self.filteroptions
        self.filtercombobox.unbind_class("TCombobox", "<MouseWheel>")
        self.filtercombobox.current(0)
        self.filtercombobox.place(x=70, y=57)

        ################################################################################################################
        ################################################################################################################



        ################################################################################################################
        ############################################# Making maincanvas ################################################
        # defining the main canvas
        self.maincanvas = tk.Canvas(main, borderwidth=0, highlightthickness=0, bg="lightblue", width=550, height=530)
        self.vertscroll = tk.Scrollbar(self.maincanvas, orient='vertical', command=self.maincanvas.yview)
        self.maincanvas.configure(yscrollcommand=self.vertscroll.set)
        self.vertscroll.pack(side="right", fill="y")

        # pack maincanvas onto UI
        self.maincanvas.pack(side="left", padx=5)

      ###################################### functions for scrolling the canvas ########################################

        def onFrameConfigure(canvas):
            canvas.configure(scrollregion=canvas.bbox("all"))

        # set the canvas
        def width(event, canvasframe):
            canvas_width = event.width
            self.maincanvas.itemconfig(canvasframe, width=canvas_width)

        # keeps track of the mouse scrolling action
        def mouse_scroll(event, maincanvas):
            if event.delta:
                maincanvas.yview_scroll(-1 * (event.delta / 120), 'units')
            else:
                if event.num == 5:
                    move = 1
                else:
                    move = -1

                maincanvas.yview_scroll(move, 'units')
        ################################################################################################################
        # bind event of filterbox changing to call function

        # bind events to main
        main.bind('<Configure>', lambda event, canvas=self.maincanvas: onFrameConfigure(canvas))
        main.bind_all('<MouseWheel>', lambda event, canvas=self.maincanvas: mouse_scroll(event, canvas))
        main.bind_all('<Button-4>', lambda event, canvas=self.maincanvas: mouse_scroll(event, canvas))
        main.bind_all('<Button-5>', lambda event, canvas=self.maincanvas: mouse_scroll(event, canvas))
        ################################################################################################################
        ################################################################################################################


        # get the list of users to display
        list_of_users_to_display = gv.getshortlisteduserslist()

        # INITIALIZE AND DISPLAY DEFAULT WINDOW (displays function 2 results)
        function1frame = tk.Frame(self.maincanvas, borderwidth=0, background="lightblue")
        self.create_labelframes_in_frame(list_of_users_to_display[0], function1frame, self.foundmatchescountlabel)
        f1window = self.maincanvas.create_window((0, 0), window=function1frame, anchor="nw")
        self.maincanvas.bind('<Configure>', lambda event, canvasframe=f1window: width(event, canvasframe))
        self.maincanvas.update()


        ################################################################################################################
        ################################################################################################################
        # definition to keep track of option selected in combobox
        def filterchanged():
            newfilter = self.filtercombobox.get()

            # set the canvas
            def width(event, canvasframe):
                canvas_width = event.width
                self.maincanvas.itemconfig(canvasframe, width=canvas_width)

            # get the list of users to display
            list_of_users_to_display = gv.getshortlisteduserslist()

            if str(newfilter) == "Function 1":
                self.maincanvas.delete("all")

                # if list_of_users_to_display[0] is not an empty list (has things to display), create the frame
                if len(list_of_users_to_display[0]) > 0:
                    function1frame = tk.Frame(self.maincanvas, borderwidth=0, background="lightblue")
                    self.create_labelframes_in_frame(list_of_users_to_display[0], function1frame, self.foundmatchescountlabel)
                    f1window = self.maincanvas.create_window((0, 0), window=function1frame, anchor="nw")
                    self.maincanvas.bind('<Configure>', lambda event, canvasframe=f1window: width(event, canvasframe))
                    self.maincanvas.update()

                # else list is empty, call function that only updates label on main to reflect '0 matches'
                else:
                    print "list is empty: " + str(list_of_users_to_display[0])
                    foundmatchescount_labelupdate(0)
                    self.maincanvas.update()

            elif str(newfilter) == "Function 2":
                self.maincanvas.delete("all")

                # if list_of_users_to_display[1] is not an empty list (has things to display), create the frame
                if len(list_of_users_to_display[1]) > 0:
                    function2frame = tk.Frame(self.maincanvas, borderwidth=0, background="lightblue")
                    self.create_labelframes_in_frame(list_of_users_to_display[1], function2frame, self.foundmatchescountlabel)
                    f2window = self.maincanvas.create_window((0, 0), window=function2frame, anchor="nw")
                    self.maincanvas.bind('<Configure>', lambda event, canvasframe=f2window: width(event, canvasframe))
                    self.maincanvas.update()

                # else list is empty, call function that only updates label on main to reflect '0 matches'
                else:
                    print "list is empty: " + str(list_of_users_to_display[1])
                    foundmatchescount_labelupdate(0)
                    self.maincanvas.update()

            elif str(newfilter) == "Function 3":
                self.maincanvas.delete("all")

                # if list_of_users_to_display[2] is not an empty list (has things to display), create the frame
                if len(list_of_users_to_display[2]) > 0:
                    function3frame = tk.Frame(self.maincanvas, borderwidth=0, background="lightblue")
                    self.create_labelframes_in_frame(list_of_users_to_display[2], function3frame, self.foundmatchescountlabel)
                    f3window = self.maincanvas.create_window((0, 0), window=function3frame, anchor="nw")
                    self.maincanvas.bind('<Configure>', lambda event, canvasframe=f3window: width(event, canvasframe))
                    self.maincanvas.update()

                # else list is empty, call function that only updates label on main to reflect '0 matches'
                else:
                    print "list is empty: " + str(list_of_users_to_display[2])
                    foundmatchescount_labelupdate(0)
                    self.maincanvas.update()

            elif str(newfilter) == "Function 4":
                self.maincanvas.delete("all")
                # if list_of_users_to_display[3] is not an empty list (has things to display), create the frame
                if len(list_of_users_to_display[3]) > 0:
                    function4frame = tk.Frame(self.maincanvas, borderwidth=0, background="lightblue")
                    self.create_labelframes_in_frame(list_of_users_to_display[3], function4frame, self.foundmatchescountlabel)
                    f4window = self.maincanvas.create_window((0, 0), window=function4frame, anchor="nw")
                    self.maincanvas.bind('<Configure>', lambda event, canvasframe=f4window: width(event, canvasframe))
                    self.maincanvas.update()

                # else list is empty, call function that only updates label on main to reflect '0 matches'
                else:
                    print "list is empty: " + str(list_of_users_to_display[3])
                    foundmatchescount_labelupdate(0)
                    self.maincanvas.update()

            elif str(newfilter) == "Function 5":
                self.maincanvas.delete("all")

                # if list_of_users_to_display[4] is not an empty list (has things to display), create the frame
                if len(list_of_users_to_display[4]) > 0:
                    function5frame = tk.Frame(self.maincanvas, borderwidth=0, background="lightblue")
                    self.create_labelframes_in_frame(list_of_users_to_display[4], function5frame, self.foundmatchescountlabel)
                    f5window = self.maincanvas.create_window((0, 0), window=function5frame, anchor="nw")
                    self.maincanvas.bind('<Configure>', lambda event, canvasframe=f5window: width(event, canvasframe))
                    self.maincanvas.update()

                # else list is empty, call function that only updates label on main to reflect '0 matches'
                else:
                    print "list is empty: " + str(list_of_users_to_display[4])
                    foundmatchescount_labelupdate(0)
                    self.maincanvas.update()


        self.filtercombobox.bind("<<ComboboxSelected>>", lambda _: filterchanged())

        # mainloop
        main.mainloop()

    ################################################################################################################
    ######################################## function to create the frames #########################################
    # definition to draw labelframes and sub-widgets on given canvas using given list of users
    def create_labelframes_in_frame(self, userstodisplay, frame, foundmatchescountlabel):
        # set the foundmatchescountlabel to the length of the current function's list (will be more than 0)
        foundmatchescountlabel.config(text="%s Matches Found!" % str(len(userstodisplay)))

        # canvas label and entry boxes creation
        for i in userstodisplay:
            # for each user match, create a LabelFrame
            labelframe = LabelFrame(frame, bd=5, bg='lightblue', width=540, pady=3)

            # initalize temp lists
            labellist = []
            entryboxlist = []
            maindictionary = gv.getmaindictionary()

            # append field name labels into 'labellist' temp list
            labellist.append(Label(labelframe, text="Name:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Gender:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Country:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Acceptable_country:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Age:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(
                Label(labelframe, text="Acceptable_age_range:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Likes:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Dislikes:", font=LABEL_FONT, bg="lightblue", pady=2))
            labellist.append(Label(labelframe, text="Books:", font=LABEL_FONT, bg="lightblue", pady=2))

            # append entry boxes and store into 'entryboxlist' temp list
            for index in range(0, 9):
                entryboxlist.append(Entry(labelframe, width=63, background="lightblue", font=DATA_FONT))

            # iterate maindictionary, find the main key (primarykey) whose sub-key 'Name' is the same as the user we want to display
            for primarykey,primaryvalue in maindictionary.items():
                # if name of user in maindictionary matches the one we are finding, append his profile info into entry box
                if str(maindictionary[primarykey]['Name']).replace("['","").replace("']","") == str(i):

                    # for each entry box in list, insert text into it
                    entryboxlist[0].insert(0, str(maindictionary[primarykey]['Name']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[1].insert(0, str(maindictionary[primarykey]['Gender']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[2].insert(0, str(maindictionary[primarykey]['Country']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[3].insert(0,
                                           str(maindictionary[primarykey]['Acceptable_country']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[4].insert(0, str(maindictionary[primarykey]['Age']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[5].insert(0, str(maindictionary[primarykey]['Acceptable_age_range']).replace("['", "").replace("']",
                                                                                                                       "").replace("'",""))
                    entryboxlist[6].insert(0, str(maindictionary[primarykey]['Likes']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[7].insert(0, str(maindictionary[primarykey]['Dislikes']).replace("['", "").replace("']", "").replace("'",""))
                    entryboxlist[8].insert(0, str(maindictionary[primarykey]['Books']).replace("['", "").replace("']", "").replace("'",""))

                    # break out of for loop
                    break

            # for each created label in corresponding entrybox, place them using grid at specific rows (index)
            for index in range(0, len(labellist)):
                labellist[index].grid(row=index, column=0, sticky="w")
                entryboxlist[index].grid(row=index, column=1)

            # pack the label frame (this is the record of one user)
            labelframe.pack()




# main function for testing code, not for production use
if __name__ == "__main__":
    listofuserlists = [["Teresa","Rose","Carol","Kevin","Shelley","Ho Xiu Qi","Test"],["Rose","Carol","Kevin","Shelley","Ho Xiu Qi","Test"],["Rose","Carol","Kevin","Shelley","Ho Xiu Qi"],
                                     ["Rose","Carol","Kevin","Shelley"], ["Rose","Carol","Kevin"]]
    gv.setlist_of_shortlisted_users(listofuserlists)
    gv.setmaindictionary({'Angela Little': {'Name': ['Angela Little'], 'Gender': ['F'], 'Age': ['22'], 'Dislikes': ['hotpot, chilli, roses, movies'], 'Acceptable_age_range': ['18,30'], 'Acceptable_country': ['Singapore, China'], 'Books': ['Christian reflections,The red tent,The God who is there,God in the Dock: Essays on Theology and Ethics,Total truth: liberating christianity from its cultural captivity,Redeeming love'], 'Likes': ['garlic, durian, swimming, chicken and chops'], 'Country': ['Singapore']}, 'Joel Jackson': {'Name': ['Joel Jackson'], 'Gender': ['Male'], 'Age': ['29'], 'Dislikes': ['durian, garlic, swimming'], 'Acceptable_age_range': ['18,33'], 'Acceptable_country': ['Singapore, China, USA'], 'Books': ['Human Philosohy,Nicomachean Ethics,Summa Theologiae,Meditations on First Philosophy,Essay Concerning Human Understanding,Principles of Human Knowledge,Enquiry Concerning Human Understanding,Social Contract,Phenomenology of Spirit'], 'Likes': ['hotpot, chicken and chops, chilli, roses, movies'], 'Country': ['Singapore']}, 'Rose': {'Name': ['Rose'], 'Gender': ['F'], 'Age': ['25'], 'Dislikes': ['chilli,garlic,basketball'], 'Acceptable_age_range': ['18,35'], 'Acceptable_country': ['Singapore, China, UK'], 'Books': ['Human Philosohy book,Adventures in Human Being,Towards the Philosophy,Essay Related Human Topics,Human Being Shall Know Philosohy'], 'Likes': ['fish, honey, chocolate, roses, durian, running'], 'Country': ['Singapore']}, 'Jenny Wang': {'Name': ['Jenny Wang'], 'Gender': ['F'], 'Age': ['25'], 'Dislikes': ['durian, garlic, swimming'], 'Acceptable_age_range': ['23,60'], 'Acceptable_country': ['China, USA,Singapore'], 'Books': ['Mere Christianity,Knowing God,How should we then live? the rise and decline of western thought and culture,The problem of Pain,The God who is there,The reason for God: belief in an age of skepticism,Experiencing God: knowing and doing the will of God, work book,'], 'Likes': ['hotpot, chicken and chops, chilli, roses, movies'], 'Country': ['China']}, 'Teresa': {'Name': ['Teresa'], 'Gender': ['F'], 'Age': ['22'], 'Dislikes': ['garlic, durian, swimming'], 'Acceptable_age_range': ['18,30'], 'Acceptable_country': ['Singapore, China'], 'Books': ["Total Truth: Liberating Christianity from its Cultural Captivity,Reflections on the Psalms,Intercessory Prayer: How God Can Use Your Prayers to Move Heaven Earth,God 's Favor - Breath Of Heaven,Letters to Malcolm: Chiefly on Prayer"], 'Likes': ['hotpot, chilli, chicken and chops, roses, movies'], 'Country': ['Singapore']}, 'Test': {'Name': ['Test'], 'Gender': ['Memale'], 'Age': ['69'], 'Dislikes': ['no 6'], 'Acceptable_age_range': ['69,96'], 'Acceptable_country': ['SSG'], 'Books': ['how to 6'], 'Likes': ['6'], 'Country': ['SGGGGGG']}, 'Lisa Marie': {'Name': ['Lisa Marie'], 'Gender': ['F'], 'Age': ['22'], 'Dislikes': ['garlic, durian, swimming'], 'Acceptable_age_range': ['18,30'], 'Acceptable_country': ['Singapore, China'], 'Books': ['Desiring God Meditations of a Christian Hedonist,God Knowing,God Favor: Breath of Heaven,The God is there,The reason for God: in an age of skepticism,Experiencing God: knowing the will of God, work book'], 'Likes': ['hotpot, chilli, chicken and chops, roses, movies'], 'Country': ['Singapore']}, 'Ho Xiu Qi': {'Name': ['Ho Xiu Qi'], 'Gender': ['Male'], 'Age': ['21'], 'Dislikes': ['Aloysius Chong'], 'Acceptable_age_range': ['18-24'], 'Acceptable_country': ['Singapore,Japan,Korea'], 'Books': ['Reigokai,Mushoku Tensei'], 'Likes': ['Games,Anime,Basketball,Badminton'], 'Country': ['Singapore']}, 'Carol': {'Name': ['Carol'], 'Gender': ['F'], 'Age': ['23'], 'Dislikes': ['football, hunting, swimming'], 'Acceptable_age_range': ['23,50'], 'Acceptable_country': ['Singapore, China'], 'Books': ['Christian reflections,The red tent,The God who is there,God in the Dock: Essays on Theology and Ethics,Total truth: liberating christianity from its cultural captivity,Redeeming love,'], 'Likes': ['Chicken rice,hotpot, Carrot cake, chilli crab, roses, movies'], 'Country': ['USA']}, 'Shelley': {'Name': ['Shelley'], 'Gender': ['Female'], 'Age': ['24'], 'Dislikes': ['chilli,garlic,basketball'], 'Acceptable_age_range': ['18,35'], 'Acceptable_country': ['Singapore, China, USA'], 'Books': ['Human Philosohy book,Adventures in Human Being,Towards the Philosophy,Essay Related Human Topics,Human Being Shall Know Philosohy'], 'Likes': ['fish, honey, chocolate, roses, durian, running'], 'Country': ['China']}, 'Kevin': {'Name': ['Kevin'], 'Gender': ['Male'], 'Age': ['25'], 'Dislikes': ['curry,garlic,basketball'], 'Acceptable_age_range': ['10,33'], 'Acceptable_country': ['Singapore'], 'Books': ['Human Philosohy,Adventures in Human Being,Meditations on the Philosophy,Essay Concerning Human topic,Principles of Human being'], 'Likes': ['fish,chicken, chocolate, roses, durian, movies'], 'Country': ['Singapore']}, 'Michael Jackson': {'Name': ['Michael Jackson'], 'Gender': ['Male'], 'Age': ['29'], 'Dislikes': ['durian, garlic, swimming'], 'Acceptable_age_range': ['18,29'], 'Acceptable_country': ['Singapore, China'], 'Books': ['Mere Christianity,Knowing God,The problem of Pain,The God who is there,The reason for God: belief in an age of skepticism,Experiencing God: knowing and doing the will of God, work book'], 'Likes': ['hotpot, chicken and chops, chilli, roses, movies'], 'Country': ['Singapore']}})
    ResultsPage("550x700", "MatchMakeMe - Match Results")