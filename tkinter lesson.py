'''from tkinter import *

window=Tk()

window.title("sample window")
window.geometry("400x200")

window.mainloop()'''

from tkinter import *
from datetime import date

root=Tk()

root.title("sample window")
root.geometry("400x200")

#add widgets and labels
lbl=Label(text="hey there!", fg="white",bg="#072F5F", height=1, width=300)

# add label for getting name as input from user
# use entry widget
name_lbl=Label(text="Full name",bg='#3895D3')
name_entry=Entry()

# function to display messsage
def display():

    # read input given by user
    name=name_entry.get()

    # declaring a global variable
    global message
    message="welcome to the application \nTodays date is: "
    greet="hello "+name+"\n"

    # display details in textbox
    text_box.insert(END, greet)
    text_box.insert(END, message)
    text_box.insert(END, date.today())

# add a text widget to display informatin or messages
text_box=Text(height=3)

# add button and give value of command as name of the function
# press button display function will be called automatically
btn=Button(text="begin", command=display,height=1,bg="#1261A0",fg="white")

# organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()



