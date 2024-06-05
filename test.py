import unittest

import os
import pymongo
from dotenv import load_dotenv

from groq import Groq
import json

# Load environement variables
load_dotenv()

# Set Environmental Variables
MONGO_STRING = os.getenv("MONGODBCONNECTIONSTRING")
GROQ_KEY = os.getenv("GROQ_API_KEY")

# Create a new client for the GROQ API
client = Groq(
    api_key=GROQ_KEY,
)

class TestAPI(unittest.TestCase):
    def test_api(self):
        # Setup an empty string to test against response to check if its working
        testdata = ""
        # Write a request to the api
        answer = create_request("What is the evolved form of tepig?")
        # Check if the response is not equal to the testdata (thus working)
        self.assertIsNot(answer, testdata)

# Define a function to create requests
def create_request(question):
    # Setup request to Groq API
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

    # Get response from the API & return it
    response = completion.choices[0].message.content
    answer = json.loads(response).get("answer")
    return answer


if __name__ == '__main__':
    unittest.main()