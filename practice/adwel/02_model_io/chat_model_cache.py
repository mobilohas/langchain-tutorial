import time
import langchain

from langchain.cache import InMemoryCache 
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

langchain.llm_cache = InMemoryCache()

chat = ChatOpenAI()
start = time.time()
result = chat([
    HumanMessage(content="안녕하세요!")
])

end = time.time()
print(result.content)
print(f"실행 시간: {end-start}초")

start = time.time()
result = chat([
    HumanMessage(content="안녕하세요!")
])

end = time.time()
print(result.content)
print(f"실행 시간: {end-start}초")
