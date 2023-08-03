import os
import mysql.connector
from dotenv import load_dotenv
from db_to_papago import papago_translate

load_dotenv()
host_env = os.getenv("host") 
user_env = os.getenv("user") 
password_env = os.getenv("password") 
database_env = os.getenv("database") 

def read_data_from_mysql():
    columns = ["article_number","summary"]

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
                papago_translate(db_article_number, db_content,cursor, connection)
        else:
            print("MySQL 데이터베이스에 연결되어 있지 않습니다.")
    except mysql.connector.Error as err:
        print("MySQL 연결 오류: {}".format(err))

    cursor.close()
    connection.close()