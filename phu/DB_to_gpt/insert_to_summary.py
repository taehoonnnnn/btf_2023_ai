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