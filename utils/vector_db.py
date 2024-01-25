from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores.chroma import Chroma

def vectorize(chunks):
    # create a fresh vector_db using OpenAI embedding model
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding = OpenAIEmbeddings()
    )

    print(f"Number of vectors: {vector_db._collection.count()}")

    return vector_db
