import streamlit as st

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