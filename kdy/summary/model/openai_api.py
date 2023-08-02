import os
import openai
import pandas as pd
from dotenv import load_dotenv
import time

start = time.time()  # 시작 시간 저장

load_dotenv()
api_key = os.getenv("api_key") 
openai.api_key = api_key

df = pd.read_csv('자본시장_금융.csv')

# 모델 및 매개변수 정의
model = "gpt-3.5-turbo"
# default = 1
temperature = 1
# default = 256
max_tokens = 256
# default = 1
top_p = 1
# default = 0
frequency_penalty = 0
# default = 0
presence_penalty = 1

# Initialize new dataframe with desired column names
df_new = pd.DataFrame(
    columns=[
        "article_number", 
        "title", "title_trans", "content","content_trans",
        "keyword1" ,"keyword2" ,"keyword3" ,"keyword4" ,"keyword5",
        "keyword1_trans" ,"keyword2_trans" ,"keyword3_trans" ,"keyword4_trans" ,"keyword5_trans",
        "message",  "model", "temperature", "max_tokens", "top_p", 
        "frequency_penalty", "presence_penalty", "response"])

for idx, row in df.iterrows():
    time.sleep(3)
    article_number = row.iloc[0]
    title = row.iloc[1]
    title_trans = row.iloc[5]
    content = row.iloc[4]
    content_trans = row.iloc[6]
    keyword1 = row.iloc[7]
    keyword2 = row.iloc[8]
    keyword3 = row.iloc[9]
    keyword4 = row.iloc[10]
    keyword5 = row.iloc[11]
    keyword1_trans = row.iloc[12]
    keyword2_trans = row.iloc[13]
    keyword3_trans = row.iloc[14]
    keyword4_trans = row.iloc[15]
    keyword5_trans = row.iloc[16]
    
    response = openai.ChatCompletion.create(
      model=model,
      messages=[
        {
          "role": "user",
          "content": "다음 뉴스 기사를 3문장으로 요약해, 총 답변의 길이는 150자 이내로 제한한다."
        },
        {
          "role": "user",
          "content": content  
        },
      ],
      temperature=temperature,
      max_tokens=max_tokens,
      top_p=top_p,
      frequency_penalty=frequency_penalty,
      presence_penalty=presence_penalty
    )
    
    result = response['choices'][0]['message']['content']
    result = result.replace(",", "")  # Remove comma from the response
    result = result.replace("\n", "")
    # Update the new row with values
    new_row = pd.DataFrame([{
      "article_number": article_number,
      "score": 0,
      "keyword1" : keyword1,
      "keyword2" : keyword2,
      "keyword3" : keyword3,
      "keyword4" : keyword4,
      "keyword5" : keyword5,
      "response": result,
      "message": "The following news article is summarized in three sentences, limiting the length of the total answer to 300 characters. + content_trans",
      "model": model,
      "temperature": temperature,
      "max_tokens": max_tokens,
      "top_p": top_p,
      "frequency_penalty": frequency_penalty,
      "presence_penalty": presence_penalty,
    }])
    
    df_new = df_new._append(new_row, ignore_index=True)
# print(result)
df_new.to_csv('output.csv', index=False)

print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간
