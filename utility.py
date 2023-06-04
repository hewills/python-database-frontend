'''
Author: Hana Wills
Date: 5/20/2023
Description:
A simple python application.
GUI database front-end

'''
import sqlite3

from tkinter import *
import tkinter as Tk
from tkinter.ttk import Combobox
 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

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
 
    # Drop the table if already exists.
    cursor.execute("DROP TABLE IF EXISTS MODELS;")
    cursor.execute("DROP TABLE IF EXISTS MODEL_ASSIGNMENTS;")
    cursor.execute("DROP TABLE IF EXISTS SETTINGS;")
 
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
    cursor.execute('''INSERT INTO SETTINGS VALUES ('demohana', 'major', '/incoming/files','Majors Section','1','','Y','')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('demohana', 'degree', '/incoming/files','Degrees','2','','','Y')''')
    cursor.execute('''INSERT INTO SETTINGS VALUES ('xyz', 'grants', '/incoming/grants/files','Grants','2','','','Y')''')

    #Insert into Model Assignments
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('abc', '5', 'major')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('abc', '6', 'minor')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('abc', '7', 'work')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('mac', '8', 'degree')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('mac', '9', 'system')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('demohana', '10', 'major')''')
    cursor.execute('''INSERT INTO MODEL_ASSIGNMENTS VALUES ('demohana', '11', 'degree')''')
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
create_tables()
load_tables()
view_data()

'''
# Initialize Main Window -----------------------------

# Create window Tkinter
window = Tk.Tk()
# Give window a title
window.title(" Simple Setup ")

# Size window W x H
window.geometry("1200x700")
#window.attributes('-fullscreen', True)

# Window Title
newlabel = Tk.Label(text = "SELECT INSTANCE")
newlabel.place(x=500,y=20)
# -----------------------------------------------------

# Selector Combo Box
var = StringVar()
var.set("")
data=("","abc", "demohana", "mac", "xyc")
cb=Combobox(window, values=data)
cb.place(x=500, y=75)

# Selector Button
btn=Button(window, text="       OK       ", fg='blue').place(x=660, y=70)



# -----------------------------------------------------
#  SAMPLE CODE BELOW
# -----------------------------------------------------
# Textbox
newlabel = Tk.Label(text = "Select Database").place(x=50,y=50)
txtfld=Entry(window, text=" dbid ", bd=5)  #bd = Border
txtfld.place(x=50, y=70)

# Combo box
newlabel = Tk.Label(text = "Combo Box").place(x=50,y=150)
var = StringVar()
var.set("one")
data=("one", "two", "three", "four")
cb=Combobox(window, values=data)
cb.place(x=50, y=170)

# List Box
newlabel = Tk.Label(text = "List Box").place(x=50,y=250)
lb=Listbox(window, height=5, selectmode='multiple')
for num in data:
    lb.insert(END,num)
lb.place(x=50, y=270)

# Radio buttons
newlabel = Tk.Label(text = "Radio Buttons").place(x=50,y=400)
v0=IntVar()
v0.set(1)
r1=Radiobutton(window, text="male", variable=v0,value=1)
r2=Radiobutton(window, text="female", variable=v0,value=2)
r1.place(x=50,y=420)
r2.place(x=50, y=440)

# Check boxes
newlabel = Tk.Label(text = "Check Box").place(x=50,y=500)
v1 = IntVar()
v2 = IntVar()
C1 = Checkbutton(window, text = "Cricket", variable = v1)
C2 = Checkbutton(window, text = "Tennis", variable = v2)
C1.place(x=50, y=520)
C2.place(x=50, y=540)

# Quit button
btn=Button(window, text="       Quit       ", fg='blue',command = window.destroy).place(x=20, y=650)


window.mainloop()
'''

 

class Model():
 
    def __init__(self):
        self.xpoint = 200
        self.ypoint = 200
        self.res = None
 
    def calculate(self):
        x, y = np.meshgrid(np.linspace(-5, 5, self.xpoint),
                           np.linspace(-5, 5, self.ypoint))
        z = np.cos(x**2*y**3)
        self.res = {"x": x, "y": y, "z": z}
 
 
class View():
    def __init__(self, master):
        self.frame = Tk.Frame(master)
        self.fig = Figure(figsize=(7.5, 4), dpi=80)
        self.ax0 = self.fig.add_axes(
            (0.05, .05, .90, .90), facecolor=(.75, .75, .75), frameon=False)
        self.frame.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.sidepanel = SidePanel(master)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        self.canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)
        self.canvas.draw()
 
 
class SidePanel():
    def __init__(self, root):
        self.frame2 = Tk.Frame(root)
        self.frame2.pack(side=Tk.LEFT, fill=Tk.BOTH, expand=1)
        self.plotBut = Tk.Button(self.frame2, text="Plot ")
        self.plotBut.pack(side="top", fill=Tk.BOTH)
        self.clearButton = Tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top", fill=Tk.BOTH)
 
 
class Controller():
    def __init__(self):
        self.root = Tk.Tk()
        self.model = Model()
        self.view = View(self.root)
        self.view.sidepanel.plotBut.bind("<Button>", self.my_plot)
        self.view.sidepanel.clearButton.bind("<Button>", self.clear)
 
    def run(self):
        self.root.title("Tkinter MVC example")
        self.root.deiconify()
        self.root.mainloop()
 
    def clear(self, event):
        self.view.ax0.clear()
        self.view.fig.canvas.draw()
 
    def my_plot(self, event):
        self.model.calculate()
        self.view.ax0.clear()
        self.view.ax0.contourf(
            self.model.res["x"], self.model.res["y"], self.model.res["z"])
        self.view.fig.canvas.draw()
 
 
if __name__ == '__main__':
    c = Controller()
    c.run()




