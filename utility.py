'''
Author: Hana Wills
Date: 5/20/2023
Description:
A simple python application.

'''
import sqlite3

from tkinter import *
import tkinter as tk
from tkinter.ttk import Combobox

MODEL_TABLE = "models.db"

# ======================================================

def create_database():
    # Initialize Database
    # filename to form database
    file = MODEL_TABLE

    try:
        conn = sqlite3.connect(file)
        print("Database " + str(MODEL_TABLE) + " formed.")
    except:
        print("Database " + str(MODEL_TABLE) + " not formed.")

# -----End of create_database() ------------------------



# Initialize Main Window -------------------------------
 
create_database()

connection = sqlite3.connect(MODEL_TABLE)

# Create window Tkinter
window = tk.Tk()
# Give window a title
window.title(" Simple Setup ")

# Size window W x H
window.geometry("1200x700")
#window.attributes('-fullscreen', True)

# Window Title
newlabel = tk.Label(text = "MODEL SETUP")
newlabel.place(x=50,y=20)
# -----------------------------------------------------

# Textbox
newlabel = tk.Label(text = "Select Database").place(x=50,y=50)
txtfld=Entry(window, text=" dbid ", bd=5)  #bd = Border
txtfld.place(x=50, y=70)

# Combo box
newlabel = tk.Label(text = "Combo Box").place(x=50,y=150)
var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=50, y=170)

# List Box
newlabel = tk.Label(text = "List Box").place(x=50,y=250)
lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=50, y=270)

# Radio buttons
newlabel = tk.Label(text = "Radio Buttons").place(x=50,y=400)
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=50,y=420)
r2.place(x=50, y=440)

# Check boxes
newlabel = tk.Label(text = "Check Box").place(x=50,y=500)
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=50, y=520)
C2.place(x=50, y=540)

# Quit button
btn=Button(window, text="       Quit       ", fg='blue').place(x=20, y=650)


window.mainloop()
