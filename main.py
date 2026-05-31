from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API"))

while  True:

    user_input= input("Enter Your  Prompt Here --->")

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    print(response.text)


