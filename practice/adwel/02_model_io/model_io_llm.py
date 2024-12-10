from langchain_openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm("맛있는 라면을",stop=".")

print(result);