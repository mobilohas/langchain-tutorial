from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings,
)

retriever = database.as_retriever()

qa = RetrievalQA.from_llm(
    llm=chat,
    retriever=retriever,
    return_source_documents=True,
)

result = qa("비행 자동차의 최고 속도는?")

print(result["result"])
print(result["source_documents"])
