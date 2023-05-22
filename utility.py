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
    #cursor.execute("DROP TABLE IF EXISTS MODELS;")
 
    # Creating tables
    table = """ CREATE TABLE IF NOT EXISTS MODELS (
	    modelid  INTEGER NOT NULL,
   	    modelname VARCHAR(255) NOT NULL,
        modeldesc VARCHAR(255) NOT NULL,
	    intf_modelid INTEGER,
	    intf_fieldorder INTEGER,
	    fieldorder INTEGER,
	    fieldname VARCHAR(255),
	    fieldtype VARCHAR(255),
	    required VARCHAR(255),
        keynum VARCHAR(255)
        ); """

    table2 = """ CREATE TABLE IF NOT EXISTS MODEL_ASSIGNMENTS (
	    instance VARCHAR(255) NOT NULL,
   	    modelid INTEGER NOT NULL,
	    sectiontype VARCHAR(255) NOT NULL
        ); """

    table3 = """ CREATE TABLE IF NOT EXISTS SETTINGS (
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

    sql_query = """SELECT name FROM sqlite_master WHERE type='table';"""
    cursor.execute(sql_query)

    print("\nList of Tables:\n")
    print(cursor.fetchall(),"\n")

    if connection:
        connection.close()
        print("the sqlite connection is closed")

# -----End of create_tables() -------------------------

def load_tables():

    connection = sqlite3.connect(DATABASE)
    # cursor object
    cursor = connection.cursor()
    
    # Queries to INSERT records.
    #Insert into Settings
    cursor.execute('''INSERT INTO SETTINGS VALUES ('abc', 'major', '/incoming/scholar/files','Majors','0','Y',NULL,'Y')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('abc', 'minor', '/incoming/scholar/files','Minors','1','Y',NULL,'Y')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('abc', 'work', '/incoming/files','Work Files','2',NULL,NULL,'Y')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('mac', 'degree', '/incoming/files','Degrees and More','1',NULL,NULL,NULL)''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('mac', 'system', '/incoming/system/files','System Section','0','','Y','')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('loc', 'major', '/incoming/files','Majors Section','1','','Y','')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('loc', 'degree', '/incoming/files','Degrees','2','','','Y')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('xyz', 'grants', '/incoming/grants/files','Grants','2','','','Y')''')

    #Insert into Model Assignments
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('abc', '5', 'major')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('abc', '6', 'minor')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('abc', '7', 'work')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('mac', '8', 'degree')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('mac', '9', 'system')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('loc', '10', 'major')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('loc', '11', 'degree')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('xyz', '12', 'grants')''')

    #Insert into Models
    cursor.execute('''INSERT INTO MODELS VALUES (1,'Master','majorminor',1,1,1,'R_ID','STRING','Y','1')''')
    cursor.execute('''INSERT INTO MODELS VALUES (1,'Master','majorminor',1,2,2,'EMP_ID','STRING','Y','2')''')
    cursor.execute('''INSERT INTO MODELS VALUES (1,'Master','majorminor',1,3,3,'TITLE','STRING','',NULL)''')
    cursor.execute('''INSERT INTO MODELS VALUES (1,'Master','majorminor',1,4,4,'STARTDATE','DATE','',NULL)''')
    cursor.execute('''INSERT INTO MODELS VALUES (1,'Master','majorminor',1,5,5,'ENDDATE','DATE','','')''')

    cursor.execute('''INSERT INTO MODELS VALUES (2,'Master','custom',1,1,1,'R_ID','STRING','Y','1')''')
    cursor.execute('''INSERT INTO MODELS VALUES (2,'Master','custom',1,2,2,'EMP_ID','STRING','Y','2')''')
    cursor.execute('''INSERT INTO MODELS VALUES (2,'Master','custom',1,3,3,'TITLE','STRING','',NULL)''')
    cursor.execute('''INSERT INTO MODELS VALUES (2,'Master','custom',1,4,4,'STARTDATE','DATE','',NULL)''')
    cursor.execute('''INSERT INTO MODELS VALUES (2,'Master','custom',1,5,5,'DESCRIPTION','STRING','Y','')''')

    cursor.execute('''INSERT INTO MODELS VALUES (3,'Master','grants',1,1,1,'R_ID','STRING','Y','1')''')
    cursor.execute('''INSERT INTO MODELS VALUES (3,'Master','grants',1,2,2,'EMP_ID','STRING','Y','2')''')
    cursor.execute('''INSERT INTO MODELS VALUES (3,'Master','grants',1,3,3,'GRANT TITLE','STRING','',NULL)''')
    cursor.execute('''INSERT INTO MODELS VALUES (3,'Master','grants',1,4,4,'AMOUNT','DATE','',NULL)''')
    cursor.execute('''INSERT INTO MODELS VALUES (3,'Master','grants',1,5,5,'GRANT ID','STRING','Y','')''')
    
    # Display data inserted
    print("\nData Inserted into the tables.")
  
    # Commit your changes in the database    
    connection.commit()
  
    if connection:
        connection.close()
        print("The sqlite connection is closed")

# --------- End of load_tables() -----------------------


def view_data():

    connection = sqlite3.connect(DATABASE)
    # cursor object
    cursor = connection.cursor()
    
    print("\nSETTINGS:\n")
    data=cursor.execute('''SELECT * FROM SETTINGS''')
    for row in data:
        print(row)

    print("\nMODEL_ASSIGNMENTS:\n")
    data=cursor.execute('''SELECT * FROM MODEL_ASSIGNMENTS''')
    for row in data:
        print(row)

    print("\nMODELS:\n")
    data=cursor.execute('''SELECT * FROM MODELS''')
    for row in data:
        print(row)

    if connection:
        connection.close()
        print("The sqlite connection is closed")

# --------- End of view_data() -----------------------



# Initialize Database --------------------------------

#create_database(DATABASE)
#create_tables()
#load_tables()
view_data()


# Initialize Main Window -----------------------------

# Create window Tkinter
window = tk.Tk()
# Give window a title
window.title(" Simple Setup ")

# Size window W x H
window.geometry("1200x700")
#window.attributes('-fullscreen', True)

# Window Title
newlabel = tk.Label(text = "SELECT INSTANCE")
newlabel.place(x=500,y=20)
# -----------------------------------------------------

# Selector Combo Box
var = StringVar()
var.set("")
data=("","abc", "loc", "mac", "xyc")
cb=Combobox(window, values=data)
cb.place(x=500, y=75)

# Selector Button
btn=Button(window, text="       OK       ", fg='blue').place(x=660, y=70)



# -----------------------------------------------------
#  SAMPLE CODE BELOW
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
btn=Button(window, text="       Quit       ", fg='blue',command = window.destroy).place(x=20, y=650)


window.mainloop()
