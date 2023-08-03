import os
import sys
import urllib.request
from dotenv import load_dotenv
from insert_to_summary_translate import insert_to_summary
import json

load_dotenv()

client_id_env = os.getenv("client_id") 
client_secret_env = os.getenv("client_secret")
def papago_translate(db_article_number, db_content, cursor, connection):
    client_id = client_id_env # 개발자센터에서 발급받은 Client ID 값
    client_secret = client_secret_env # 개발자센터에서 발급받은 Client Secret 값
    encText = urllib.parse.quote(db_content)
    data = "source=en&target=ko&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id",client_id)
    request.add_header("X-Naver-Client-Secret",client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if(rescode==200):
        response_body = response.read()
        response_text = response_body.decode('utf-8')
        json_string = response_text
        data = json.loads(json_string)
        translated_text = data['message']['result']['translatedText']

        print(translated_text)
    else:
        print("Error Code:" + rescode)
    insert_to_summary(db_article_number, translated_text, cursor, connection)