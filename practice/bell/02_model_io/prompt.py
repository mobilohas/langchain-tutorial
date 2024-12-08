from langchain import PromptTemplate

prompt = PromptTemplate(
    template="{product}는 어느 회사에서 개발한 제품인가요?",
    input_variables={
        "product"
    }
)

print(prompt.format(product="아이폰")) # 아이폰는 어느 회사에서 개발한 제품인가요?
print(prompt.format(product="갤럭시")) # 갤럭시는 어느 회사에서 개발한 제품인가요?
print(prompt.format()) # KeyError: 'product'
