# import necessaary libraries
from tkinter import *
from tkinter import messagebox

# setup tkinter window
root=Tk()
root.geometry("200x200")

# functiom for diaplaying warning message
# this will be called once the button is clicked

def msg():
    messagebox.showwarning("alert", "stop !! virus found.")

# adding button widget to window
button=Button(root, text='scan for virus', command=msg)
button.place(x=40, y=80)

root.mainloop()