from langchain.document_loaders import PyMuPDFLoader
from langchain.text_splitter import SpacyTextSplitter

loader = PyMuPDFLoader("./sample.pdf")
documents = loader.load()

text_splitter = SpacyTextSplitter(
    chunk_size=300, # 분할할 크기
    pipeline="ko_core_news_sm" # 분할에 사용할 언어 모델을 설정
)
splitted_documents = text_splitter.split_documents(documents)

print(f"분할 전 문서 개수: {len(documents)}")
print(f"분할 후 문서 개수: {len(splitted_documents)}")
