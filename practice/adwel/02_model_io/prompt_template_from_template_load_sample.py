from langchain.prompts import load_prompt

load_prompt = load_prompt("prompt.json")

print(load_prompt.format(product="아이폰"))