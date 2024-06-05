import os
import pymongo 
from dotenv import load_dotenv

import datetime

from groq import Groq
import json

# Load environement variables
load_dotenv()

# Set Environmental Variables
MONGO_STRING = os.getenv("MONGODBCONNECTIONSTRING")
GROQ_KEY = os.getenv("GROQ_API_KEY")

# Connect to MongoDB
mongo = pymongo.MongoClient(MONGO_STRING)

mydb = mongo["pixelmondb"]
mycol = mydb["chatgames"]

# Create a new client for the GROQ API
client = Groq(
    api_key=GROQ_KEY,
)

# Define a function to create requests
def create_request(question):
    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {
                "role": "system",
                "content": "answer as JSON in the format {\"answer\": answer}, give one word answers where possible, dont just respond pikachu if you dont understand, please think about all pokemon from gen 1 to gen 9, only give real pokemon, ash did not catch pikachu"
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )

    # Print the completion
    response = completion.choices[0].message.content
    answer = json.loads(response).get("answer")
    return answer

# Create a new request
response = create_request("What is the evolved form of tepig?")
print(response)

testentry = { 
    "message": "unscramble the word: "
    , "scramble": "etpig"
    , "answer": "tepig"
    , "abletosolve": "True"
    , "date_added": datetime.datetime.now().strftime("%H:%M:%S")
}

x = mycol.insert_one(testentry)

print(mongo.list_database_names())