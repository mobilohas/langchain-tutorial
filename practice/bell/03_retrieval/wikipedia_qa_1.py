from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.retrievers import WikipediaRetriever

chat = ChatOpenAI()

retriever = WikipediaRetriever(
    lang="ko",
    doc_content_chars_max=500,  # 검색할 텍스트의 최대 글자수를 지정
    top_k_results=2,          # 검색 결과 중 상위 몇 건을 가져올 것인지
)

chain = RetrievalQA.from_llm(
    llm=chat,                      # 사용할 Chat models 지정
    retriever=retriever,           # 사용할 Retriever 지정
    return_source_documents=True,  # 정보를 가져온 원본 문서를 반환
)

result = chain("소주란?")

source_documents = result["source_documents"]

print({f"검색 결과: {len(source_documents)}건"})
for document in source_documents:
    print("-------------------검색한 메타데이터-------------------")
    print(document.metadata)
    print("-------------------검색한 텍스트-------------------")
    print(document.page_content[:100])
print("------------------응답-------------------")
print(result["result"])
