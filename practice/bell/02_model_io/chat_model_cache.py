import time
import langchain
from langchain.cache import InMemoryCache
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache()

chat = ChatOpenAI(model="gpt-3.5-turbo")

start = time.time()
result = chat([HumanMessage(content="안녕하세요!")])
end = time.time()

print(result.content)
print(f"실행 시간: {end-start}초")

start = time.time()
result = chat([HumanMessage(content="안녕하세요!")])
end = time.time()

print(result.content)
print(f"실행 시간: {end-start}초")