from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
    model="gpt-3.5-turbo"
)

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables=[
        "product"
    ]
)

prompt_json = prompt.save("prompt.json")


