import streamlit as st

messages = [
    {
        "role":"user",
        "content":"Hello",
    },{
        "role":"ai",
        "content":"Hi, How can I help you today ?"
    }
]


for message in messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


st.chat_input("Write prompt here ........")