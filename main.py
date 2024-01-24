from dotenv import load_dotenv
import streamlit as st
from utils.data_loader import load_pdfs
from utils.splitter import split_documents

def main():
    load_dotenv()
    st.set_page_config(page_title="Chat with PDFs", page_icon="📝")

    st.header(body="Chat with PDFs 📝")
    st.text_input(label="Ask questions", placeholder="Ask a question...", label_visibility="hidden")

    with st.sidebar:
        st.subheader(body="Upload PDFs 📝")
        pdfs = st.file_uploader(label="Upload PDFs", label_visibility="hidden", accept_multiple_files=True)
        if st.button(label="Analyze"):
            with st.spinner(text="Analyzing..."):
                documents = load_pdfs(pdfs)
                chunks = split_documents(documents)

if __name__ == "__main__":
    main()