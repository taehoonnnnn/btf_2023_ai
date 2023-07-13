import os
import openai
import pandas as pd
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("api_key")  # os.environ.get 대신 os.getenv 사용
# print(api_key)

# openai에 api key 설정
openai.api_key = api_key

# output.csv 파일에서 첫 번째 열의 값을 읽어옵니다.
df = pd.read_csv('output.csv')
first_column_value = df.iloc[0, 0]  

# 모델 및 매개변수 정의
# 사용 가능 모델
#  gpt-4, 
#  gpt-4-0613, 
#  gpt-4-32k, 
#  gpt-4-32k-0613, 
#  gpt-3.5-turbo, 
#  gpt-3.5-turbo-0613, 
#  gpt-3.5-turbo-16k, 
#  gpt-3.5-turbo-16k-0613
model = "gpt-3.5-turbo"
# 0~2, 높을 수록 출력이 무작위화 된다.
temperature = 1
# 생성 최대 토큰 수
max_tokens = 256
# 핵샘플링, 0~1, 0.1은 상위 10% 확률 질량을 구성하는 토큰만 고려된다.
top_p = 1
# -2~2, 높을 수록 새로운 단어로 이야기 할 가능성을 높인다.
frequency_penalty = 0
# -2~2, 높을 수록 새로운 주제에 대해 이야기할 가능성을 높인다.
presence_penalty = 0

response = openai.ChatCompletion.create(
  model=model,
  messages=[
    {
      "role": "system",
      "content": "다음 뉴스 기사를 3문장으로 요약해줘"
    },
    {
      "role": "system",
      "content": first_column_value  
    },
    {
      "role": "user",
      "content": "reporter"
    },
  ],
  temperature=temperature,
  max_tokens=max_tokens,
  top_p=top_p,
  frequency_penalty=frequency_penalty,
  presence_penalty=presence_penalty
)
print(response['choices'][0]['message']['content'])

# 컬럼 이름 생성
column_name = f"{model}_temperature{temperature}_maxtokens{max_tokens}_topp{top_p}_frequencypenalty{frequency_penalty}_presencepenalty{presence_penalty}"

# output.csv 파일에 결과를 추가합니다.
df[column_name] = response['choices'][0]['message']['content']
df.to_csv('output.csv', index=False)
