from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser, OutputFixingParser
from langchain.schema import HumanMessage
from pydantic import BaseModel, Field, field_validator

chat = ChatOpenAI()

class SmartPhone(BaseModel):
    release_date: str = Field(description="스마트폰 출시일")
    screen_inches: str = Field(description="스마트폰의 화면 크기(인치)")
    os_installed: str = Field(description="스마트폰에 설치된 OS")
    model_name: str = Field(description="스마트폰 모델명")

    @field_validator("screen_inches")
    def validate_screen_inches(cls, field):
        if field <= 0:
            raise ValueError("Screen inches must be a positive number")
        return field
    
# parser = PydanticOutputParser(pydantic_object=SmartPhone)

parser = OutputFixingParser.from_llm(
    parser=PydanticOutputParser(pydantic_object=SmartPhone),
    llm=chat
)


print(parser.get_format_instructions());

# result = chat([
#     HumanMessage(content="안드로이드 스마트폰 1개를 꼽아주세요"),
#     HumanMessage(content=parser.get_format_instructions())
# ])

# parsed_result = parser.parse(result.content)

# print(f"모델명: {parsed_result.model_name}")
# print(f"화면크기: {parsed_result.screen_inches}")
# print(f"OS: {parsed_result.os_installed}")
# print(f"스마트폰 출시일: {parsed_result.release_date}")