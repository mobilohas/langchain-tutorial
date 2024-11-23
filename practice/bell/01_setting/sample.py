import json
import os
from pyexpat.errors import messages

from openai import OpenAI

client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],
)

client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "iPhone13의 출시일을 알려주세요"
        }
    ]
)

print(completion.choices[0].text)
print(completion.choices[0].message.context)
