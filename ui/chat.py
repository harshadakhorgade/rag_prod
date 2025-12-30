import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/chat"

st.set_page_config(page_title="RAG Chatbot")

st.title("RAG Chatbot")

query = st.text_input("You:")

if query:
    with st.spinner("Thinking..."):
        response = requests.post(
            API_URL,
            json={"question": query}
        )
        answer = response.json()["answer"]

    st.text_area("Bot:", value=answer, height=250)
