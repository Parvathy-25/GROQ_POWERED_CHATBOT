import streamlit as st
from groq import Groq

#initialize Groq client
client=Groq(api_key="YOUR_GROO_API_KEY")

st.set_page_config(page_title="Groq Chatbot")
st.title("Groq-Powered Chatbot")

#chat history

if "messages" not in st.session_state:
    st.session_state.messages=[]

#display messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

#user input

user_input=st.chat_input("Ask me anything...")

if user_input:
    st.session_state.messages.append(
        {"role":"user","content":user_input}
    )
    with st.chat_message("user"):
        st.markdown(user_input)

    response=client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=st.session_state.messages
    )
    bot_reply=response.choices[0].message.content

    st.session_state.messages.append(
        {"role":"assistant","content":bot_reply}
    )
    with st.chat_message("assistant"):
        st.markdown(bot_reply)