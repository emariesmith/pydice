# random is already a pre-installed module (you don't need to do anything for it)
import random

# also need to import pre-installed tkinter for an error message pop-up
from tkinter import *

import tkinter.messagebox

# set up the number generator messagebox
root = tkinter.Tk()

root.title("Number Generator")

root.geometry('300x100')


# open the text file where the number data is stored for reading and writing
def onClick():

    file1 = open("my_numbers.txt", "a+")

    # generate a random number
    number = str(random.randint(1, 12))

    tkinter.messagebox.showinfo("Number", number)
        # write the number to the text file
    file1.write(number + "\n")
    # close the text file
    file1.close()

# Create a button
button = Button(root, text="Generate Number", command=onClick, height=5, width=30)

#Put the button at the bottom of the window
button.pack(side='bottom')
# execute the application
root.mainloop()