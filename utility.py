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

DATABASE = "DATAMACHINE.db"

# ======================================================

def create_database(dbtable):
    # Initialize Database
    # filename to form database
    file = dbtable

    try:
        conn = sqlite3.connect(file)
        print("Database " + str(dbtable) + " formed.")
    except:
        print("Database " + str(dbtable) + " not formed.")

# -----End of create_database() ------------------------


# ======================================================

def create_tables():

    connection = sqlite3.connect(DATABASE)
    # cursor object
    cursor = connection.cursor()
 
    # Drop the GEEK table if already exists.
    #cursor.execute("DROP TABLE IF EXISTS MODELS")
 
    # Creating tables
    table = """ CREATE TABLE IF NOT EXISTS MODELS (
	    modelid  INTEGER NOT NULL,
	    instance VARCHAR(255) NOT NULL,
   	    modelname VARCHAR(255) NOT NULL,
	    intf_modelid INTEGER,
	    intf_fieldorder INTEGER,
	    fieldorder INTEGER,
	    fieldname VARCHAR(255),
	    fieldtype VARCHAR(255),
	    required VARCHAR(255)
        ); """

    table2 = """ CREATE TABLE IF NOT EXISTS MODEL_ASSIGNMENTS (
	    instance VARCHAR(255) NOT NULL,
   	    modelid INTEGER NOT NULL,
	    sectiontype VARCHAR(255) NOT NULL
        ); """

    table3 = """ CREATE TABLE IF NOT EXISTS IDM_SETTINGS (
	    instance VARCHAR(255) NOT NULL,
   	    sectiontype VARCHAR(255) NOT NULL,
	    incoming_path VARCHAR(255),
	    sectionname VARCHAR(255),
        lockflag VARCHAR(10),
        scholarly VARCHAR(10),
        custom VARCHAR(10),
        check_header VARCHAR(10)
        ); """
 
    cursor.execute(table)
    cursor.execute(table2)
    cursor.execute(table3)

    if connection:
        connection.close()
        print("the sqlite connection is closed")

# -----End of create_tables() ------------------------

# Initialize Database --------------------------------
create_database(DATABASE)
create_tables()

# Initialize Main Window -----------------------------

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
