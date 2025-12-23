import streamlit as st
import sys
import os

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.rag import rag_answer  # RAG = retrieval + Hugging Face LLM

st.set_page_config(page_title="RAG Chatbot", page_icon="💬")

st.title("RAG Chatbot")
st.write("Ask me anything about your ingested PDFs!")

# User input
query = st.text_input("You:", "")

if query:
    with st.spinner("Thinking..."):
        answer = rag_answer(query)

    st.text_area("Bot:", value=answer, height=250)
