import os
import pymongo 
from dotenv import load_dotenv

import datetime

# Load environement variables
load_dotenv()

# Set Environmental Variables
MONGO_STRING = os.getenv("MONGODBCONNECTIONSTRING")

# Connect to MongoDB
client = pymongo.MongoClient(MONGO_STRING)

mydb = client["pixelmondb"]
mycol = mydb["chatgames"]

testentry = { 
    "message": "unscramble the word: "
    , "scramble": "etpig"
    , "answer": "tepig"
    , "abletosolve": "True"
    , "date_added": datetime.datetime.now().strftime("%H:%M:%S")
}

x = mycol.insert_one(testentry)

print(client.list_database_names())