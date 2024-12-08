from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain import PromptTemplate

chat = ChatOpenAI(model="gpt-3.5-turbo")

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables={
        "product"
    }
)

result = chat([HumanMessage(content=prompt.format(product="아이폰"))])
print(result.content)
