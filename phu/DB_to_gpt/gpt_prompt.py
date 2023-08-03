import os
import openai
from insert_to_summary import insert_to_summary 

def gpt_prompt(db_article_number, db_content, cursor, connection):
  api_key = os.getenv("api_key") 
  openai.api_key = api_key

  # 모델 및 매개변수 정의
  model = "gpt-3.5-turbo"
  temperature = 1
  max_tokens = 256
  top_p = 1
  frequency_penalty = 0
  presence_penalty = 0

  try:
    response = openai.ChatCompletion.create(
      model=model,
      messages=[
        {
          "role": "user",
          "content": """Summarize the following news article into 3 sentences, and limit the length of the total answer to 300 characters or less."""
        },
        {
          "role": "user",
          "content": db_content
        },
      ],
      temperature=temperature,
      max_tokens=max_tokens,
      top_p=top_p,
      frequency_penalty=frequency_penalty,
      presence_penalty=presence_penalty
    )
  except openai.error.OpenAIError as e:
    # API 오류 발생 시 예외 처리
    # 오류 메시지 출력
    print("OpenAI API 오류:", str(e))

  result = response['choices'][0]['message']['content']
  result = result.replace(",", "")
  result = result.replace("\n", "")      
  print(result)
  insert_to_summary(db_article_number, result, cursor, connection)