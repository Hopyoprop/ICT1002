import Tkinter as tk
import tkFileDialog as filedialog
import sys

# open file dialog browser to select files to parse
mainwin = tk.Tk()
file_path = ()
file_path = filedialog.askopenfilenames()

# open files that were selected on top
for path in file_path:
    file = open(path, "r")
    counter = 0
    # for each line in the file
    for line in file:
        # if 'Books:' has already been iterated (as defined by counter =1), then
        if counter >= 1:
            print line,
            counter += 1
            continue

        # checking for which rows the line belongs to
        if line.lower().startswith("name:"):
            print line.split(": ")[1],

        elif line.lower().startswith("gender:"):
            print line.split(": ")[1],

        elif line.lower().startswith("country:"):
            print line.split(": ")[1],

        elif line.lower().startswith("acceptable_country:"):
            splitted = line.split(": ")[1].split(", ")

            for acceptablecountry in splitted:
                print acceptablecountry,

        elif line.lower().startswith("age:"):
            print line.split(": ")[1],

        elif line.lower().startswith("acceptable_age_range:"):
            splitted = line.split(": ")[1].split("-")

            for age in splitted:
                print age,

        elif line.lower().startswith("likes:"):
            splitted = line.split(": ")[1].split(", ")

            for like in splitted:
                print like,

        elif line.lower().startswith("dislikes:"):
            splitted = line.split(": ")[1].split(", ")
            for dislike in splitted:
                print dislike,

        elif line.lower().startswith("books:"):
            counter += 1
            





