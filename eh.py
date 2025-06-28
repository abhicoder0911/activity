# import necessary libraries
from tkinter import *

# create window
window=Tk()
window.title("evnt handler")
window.geometry('750x500')

# event handler
def handle_keypress(event):
    # print the character associated to the key pressed
     print(event.char)

# cind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)   

# event handler for button click
def handle_click(event):
     print("\n the button was clicked")

button=Button(text='Click me!',bg="#d0efff")
button.pack()


button.bind("<Button-1>", handle_click)

window.mainloop()