import os
import pymongo 
from dotenv import load_dotenv

from tkinter import *
from tkinter import ttk
from tkinter import Listbox

# Load environement variables
load_dotenv()

# Set Environmental Variables
MONGO_STRING = os.getenv("MONGODBCONNECTIONSTRING")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_STRING)

# Create a onclick event for the frame to get us the frame that is clicked 
def onClick(event):
    print(event.widget.__name__)

# Create a new window
root = Tk()

# Make the window not resizable
root.resizable(False, False)

# Set the minimum size of the window (in our case the size in general)
root.minsize(500, 500)

# Set the database and collection
mydb = client["pixelmondb"]
collection = mydb["chatgames"]

for entry in collection.find():
    print(entry)

frame = Frame(root, bg="#333333")
frame.configure(highlightbackground="#666A86", highlightthickness=5)
frame.__name__="frame"
frame.grid(columnspan=3, rowspan=1)

frame.bind("<Button>", onClick)

lblMessage = Label(frame, text="Resolved", font=('Helvetica', 8), justify=LEFT, bg="#333333", fg="#00FF00")
lblMessage.grid(column=2, row=0)

txtScramble = Label(frame, text="Etpig", font=('Helvetica', 24), bg="#333333", fg="#ffffff")
txtScramble.grid(column=1, row=1, padx=100, pady=10)

txtAnswer = Label(frame, text="Tepig", font=('Helvetica', 24), bg="#333333", fg="#ffffff")
txtAnswer.grid(column=3, row=1, padx=100, pady=10)

txtTimeStamp = Label(frame, text="5 Mins Ago", font=('Helvetica', 8), bg="#333333", fg="#ffffff")
txtTimeStamp.grid(column=2, row=2)

root.mainloop()







    