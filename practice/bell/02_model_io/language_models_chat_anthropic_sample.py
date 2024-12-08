from langchain_community.chat_models import ChatAnthropic
from langchain.schema import HumanMessage

chat = ChatAnthropic()

result = chat([HumanMessage(content="안녕하세요!")])
print(result)
