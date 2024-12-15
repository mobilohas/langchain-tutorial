from langchain.document_loaders import PyMuPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import SpacyTextSplitter
from langchain.vectorstores import Chroma

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=300, # 분할할 크기
    pipeline="ko_core_news_sm" # 분할에 사용할 언어 모델을 설정
)
splitted_documents = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(
    model="text-embedding-ada-002"
)

database = Chroma(
    persist_directory="./.data",
    embedding_function=embeddings,
)

database.add_documents(
    splitted_documents,
)

print("데이터베이스 생성이 완료되었습니다.")
