from langchain.text_splitter import SpacyTextSplitter

def split_documents(documents, chunk_size = 1000, chunk_overlap = 50):
    splitter = SpacyTextSplitter(
        chunk_size = chunk_size,
        chunk_overlap = chunk_overlap,
    )

    chunks = splitter.split_documents(documents)
    print(f"Number of chunks: {len(chunks)}")
    return chunks