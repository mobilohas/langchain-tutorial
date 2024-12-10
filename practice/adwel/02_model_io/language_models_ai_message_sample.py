from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage


chat = ChatOpenAI(
    model = "gpt-3.5-turbo"
)

result = chat(
    [
        HumanMessage(content="계란찜 만드는 법을 알려줘"),
        AIMessage(content="{ChatModel의 답변인 계란찜 만드는 법}"),
        HumanMessage(content="영어로 번역해줘"),
        
    ]
)

print(result.content);