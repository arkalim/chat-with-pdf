import os
import shutil
from langchain_community.document_loaders import PyPDFLoader

def load_pdfs(pdfs):

    # temporary directory to read and save PDFs
    pdf_dir = "pdf"
    if not os.path.exists(pdf_dir):
        os.makedirs(pdf_dir)

    # save the uploaded PDFs as files
    documents = []
    for pdf in pdfs:
        file_path = os.path.join(pdf_dir, pdf.name)
        with open(file_path, 'wb') as pdf_file:
            pdf_file.write((pdf).read())
        documents.extend(PyPDFLoader(file_path).load())

    print(f"Number of documents: {len(documents)}")

    # delete the temporary directory
    shutil.rmtree(pdf_dir)

    return documents