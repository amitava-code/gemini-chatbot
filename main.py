from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API"))

messages = []

while  True:

    user_input= input("Enter Your  Prompt Here --->")

    messages.append({

        "role":"user",
        "content":user_input

    })

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=list(map( lambda message: message["role"] + ":" + message["content"], messages))
    )

    messages.append({
        "role":"ai",
        "content":response.text
    })

    print(response.text)


