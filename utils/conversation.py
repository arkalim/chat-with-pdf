from langchain_openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

def get_conversation_chain(vector_db):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_db.as_retriever(search_type="mmr", search_kwargs={"k": 5}),
        memory=ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        ),
    )

    return conversation_chain