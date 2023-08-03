import os
import openai
from dotenv import load_dotenv
import mysql.connector

load_dotenv()
host_env = os.getenv("host") 
user_env = os.getenv("user") 
password_env = os.getenv("password") 
database_env = os.getenv("database") 

def read_data_from_mysql():
    columns = ["article_number","content"]

    try:
        connection = mysql.connector.connect(
            host=host_env,
            user=user_env,
            password=password_env,
            database=database_env
        )
        if connection.is_connected():
            cursor = connection.cursor()

            query = "SELECT {} FROM 기사;".format(", ".join(columns))

            
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                db_article_number = row[0]
                db_content = row[1]
                gpt_prompt(db_article_number,db_content,cursor, connection)
        else:
            print("MySQL 데이터베이스에 연결되어 있지 않습니다.")
    except mysql.connector.Error as err:
        print("MySQL 연결 오류: {}".format(err))

    cursor.close()
    connection.close()

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

def insert_to_summary(db_article_number, summary_result, cursor, connection):

  select_query = f"SELECT {db_article_number} FROM 기사"

  # result 변수에 조회 결과 저장
  result_list = []
  cursor.execute(select_query)
  for row in cursor.fetchall():
      result_list.append(row[0])
  update_query = f"UPDATE 기사 SET summary = %s WHERE article_number = %s"
  cursor.execute(update_query, (summary_result, db_article_number))
  connection.commit()

read_data_from_mysql()