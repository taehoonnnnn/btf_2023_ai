import os
import openai
from dotenv import load_dotenv


load_dotenv()
api_key = os.environ.get("api_key")
print(api_key)

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv(api_key)


response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
# role: system, user, assiatant
    {
      "role": "system",
      "content": "you are news reporter"
    },
    {
      "role": "user",
      "content": "다음 내용을 3줄로 요약하라"
    },
    {
      "role": "user",
      "content": "다음 내용을 3줄로 요약하라"
    },
  ],
# 높을 수록 무작위성이 높아진다(0~2)/기본값 1
  temperature=1,
# 채팅 완료시 생성할 최대 토큰 수/ 기본값 256
  max_tokens=256,
# 핵 샘플링, 1은 상위 100% 확률 질량을 구성하는 토큰만 고려/ 기본값 1
  top_p=1,
# 같은 단어를 반복할 가능성(-2~2)/ 기본값 0
  frequency_penalty=0,
# 같은 주제에 대해 이야기할 가능성(-2~2)/ 기본값 0
  presence_penalty=0
)
print(response)