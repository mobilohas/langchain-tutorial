from langchain_community.llms import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-instruct")

retult = llm("밋있는 라면을", stop=".")
print(retult)
