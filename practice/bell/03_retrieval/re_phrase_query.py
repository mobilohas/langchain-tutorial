from langchain_community.chat_models import ChatOpenAI
from langchain_community.retrievers import WikipediaRetriever
from langchain.retrievers import RePhraseQueryRetriever

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

retriever = WikipediaRetriever(
    lang="ko",
    doc_content_chars_max=500
)

llm_chain = LLMChain(
    llm = ChatOpenAI(
        temperature=0
    ),
    prompt = PromptTemplate(
        input_variables=["question"],
        template="""아래 질문에서 위키백과에 검색할 키워드를 추출해 주세요.
질문: {question}
"""
))

re_phrase_query_retriever = RePhraseQueryRetriever(
    llm_chain = llm_chain,
    retriever = retriever,
)

question = "나는 라면을 좋아합니다. 그런데 소주란 무엇인가요?"
documents = re_phrase_query_retriever.get_relevant_documents(question)

print(documents)