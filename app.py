import streamlit as st
from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API"))

if "messages" not in st.session_state:
    st.session_state.messages=[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


user_input = st.chat_input("Write prompt here ........")

if user_input:

    st.session_state.messages.append({"role": "user", "content" : user_input})

    with st.chat_message("user"):
        st.markdown(user_input)


    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=list(
            map( lambda message: message["role"] + ":" + message["content"],
                st.session_state.messages,
                          ))
    )

    st.session_state.messages.append({
        "role":"ai",
        "content":response.text
    })

    with st.chat_message("ai"):
        st.markdown(response.text)
