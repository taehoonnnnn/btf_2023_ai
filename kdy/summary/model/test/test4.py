import os
import openai
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")  # os.environ.get 대신 os.getenv 사용
print(api_key)

# openai에 api key 설정
openai.api_key = api_key

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {
      "role": "system",
      "content": "정상적으로 작동하는지 궁금해"
    },
    {
      "role": "user",
      "content": "user"
    },
  ],
  temperature=1,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
print(response['choices'][0]['message']['content'])

