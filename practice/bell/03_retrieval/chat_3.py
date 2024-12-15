import os
import chainlit as cl
from langchain_community.chat_models import ChatOpenAI
from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
        model="text-embedding-ada-002"
    )

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate(
    template="""문장을 바탕으로 질문에 답하세요.

문장:
{document}

질문: {query}
""",
    input_variables=["document", "query"],
)

text_splitter = SpacyTextSplitter(
    chunk_size=300,
    pipeline="ko_core_news_sm"
)

@cl.on_chat_start
async def on_chat_start():
    files = None

    while files is None:
        files = await cl.AskFileMessage(
            max_size_mb=20,
            content="PDF를 선택해주세요.",
            accept=["application/pdf"],
            raise_on_timeout=False,
        ).send()
    file = files[0]

    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    with open(f"tmp/{file.name}", "wb") as f:
        with open(file.path, "rb") as source:
            f.write(source.read())

    documents = PyMuPDFLoader(f"tmp/{file.name}").load()
    splitted_documents = text_splitter.split_documents(documents)

    # 영속화 X
    database = Chroma(
        embedding_function=embeddings,
    )
    database.add_documents(splitted_documents)

    cl.user_session.set(
        "database",
        database,
    )

    await cl.Message(content=f"'{file.name}' 로딩이 완료되었습니다. 질문을 입력하세요.").send()

@cl.on_message
async def on_message(input_message):
    print("입력된 메시지: " + input_message.content)

    database = cl.user_session.get("database")
    documents = database.similarity_search(input_message.content)

    documents_string = ""

    for document in documents:
        documents_string += f"""
    -------------------------------
    {document.page_content}
    """

    result = chat([
        HumanMessage(content=prompt.format(document=documents_string, query=input_message.content)),
    ])
    await cl.Message(content=result.content).send()
