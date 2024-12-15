from langchain.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(lang="ko")
documents = retriever.get_relevant_documents("대형 언어 모델")

print({f"검색 결과: {len(documents)}"})

for document in documents:
    print("-------------------검색한 메타데이터-------------------")
    print(document.metadata)
    print("-------------------검색한 텍스트-------------------")
    print(document.page_content[:100])
