import sys
import streamlit as st
from dotenv import load_dotenv

from utils.data_loader import load_pdfs
from utils.splitter import split_documents
from utils.vector_db import vectorize
from utils.conversation import get_conversation_chain

def main():
    load_dotenv()

    st.set_page_config(page_title="Chat with PDFs", page_icon="📝")

    st.header(body="Chat with PDFs 📝")

    question = st.text_input(label="Ask questions", placeholder="Ask a question...", label_visibility="hidden")
    if question:
        if "conversation" not in st.session_state:
            st.error(body="Please upload a PDF document before asking questions!!!")
            sys.exit(0)
        response = st.session_state.conversation({"question": question})
        st.session_state.chat_history = response["chat_history"]

        for i, message in enumerate(st.session_state.chat_history):
            if i % 2 == 0:
                st.write(f"👨🏻: {message.content}")
            else:
                st.write(f"🤖: {message.content}")

    with st.sidebar:
        st.subheader(body="Upload PDFs 📝")
        pdfs = st.file_uploader(label="Upload PDFs", label_visibility="hidden", accept_multiple_files=True)
        if st.button(label="Analyze"):
            with st.spinner(text="Analyzing..."):
                documents = load_pdfs(pdfs)
                chunks = split_documents(documents)
                vector_db = vectorize(chunks)

                # save the conversation chain in the session state to prevent reinitialization on reload
                st.session_state.conversation = get_conversation_chain(vector_db)
            

if __name__ == "__main__":
    main()