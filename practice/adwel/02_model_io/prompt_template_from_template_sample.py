from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate.from_template("{product}는 어느 회사에서 개발한 제품인가요?")

print(prompt.format(product="갤럭시"))


