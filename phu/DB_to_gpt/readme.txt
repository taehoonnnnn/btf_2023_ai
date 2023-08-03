1. read_data.py에서 데이터베이스에 있는 '기사' 테이블에서 columns = ["article_number","content"]를  불러옵니다.
2. gpt_prompt.py에서 read_data.py에서 가져온 DB 컬럼"content"를 사용하여 GPT가 요약을 진행한 뒤 result 변수로 생성됩니다.
3. insert_to_summary 함수가 동작하여 DB 컬럼"summary"에 저장합니다.


cursor.execute(select_query)
  for row in cursor.fetchall():
      result_list.append(row[0])
update_query = f"UPDATE 기사 SET summary = %s WHERE article_number = %s"
cursor.execute(update_query, (summary_result, db_article_number))

DB를 조회하여 article_number를 비교한 뒤 번호가 같다면,
데이터베이스 "기사"에서 "summary" 컬럼에 summary_result 변수에 있는 데이터를 DB에 덮어쓰기


.evn 파일이 있어야 동작합니다

GPT API
api_key = ' '

mysql db
host = ' '
user = ' '
password = ' '
database = ' '

