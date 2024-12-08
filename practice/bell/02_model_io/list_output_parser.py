from langchain_community.chat_models import ChatOpenAI
from langchain.output_parsers import CommaSeparatedListOutputParser
from langchain.schema import HumanMessage

output_parser = CommaSeparatedListOutputParser()

chat = ChatOpenAI(model="gpt-3.5-turbo")

result = chat([
    HumanMessage(content="애플이 개발한 대표적인 제품 3개 알려주세요."),
    HumanMessage(content=output_parser.get_format_instructions()),
])

output = output_parser.parse(result.content)
for item in output:
    print("대표 상품: " + item)
