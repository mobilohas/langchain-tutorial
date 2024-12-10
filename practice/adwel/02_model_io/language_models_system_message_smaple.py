from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, AIMessage, SystemMessage


chat = ChatOpenAI(
    model = "gpt-3.5-turbo"
)

result = chat(
    [
        SystemMessage(content="당신은 친한 친구 입니다. 존댓말을 쓰지 말고 솔직하게 답해주세요."),
        HumanMessage(content="안녕"),
        
    ]
)

print(result.content);