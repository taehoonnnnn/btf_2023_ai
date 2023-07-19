import os
import sys
import urllib.request
import json
import pandas as pd
import time

client_id = "jEPij9MsZqUVIRtH6wyh"
client_secret = "UVL7kT1zvT"

df = pd.read_csv("자본시장_금융.csv")

def translate(text):
    time.sleep(1)
    encText = urllib.parse.quote(text)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        response_body = response_body.decode('utf-8') 
        response_body = json.loads(response_body)
        return response_body["message"]["result"]["translatedText"]
    else:
        return "Error Code:" + str(rescode)

df['Translated_Text'] = df['content'].apply(translate)  # Replace 'ColumnName' with the name of the column that you want to translate
df.to_csv("자본시장_금융_add_eng.csv", index=False)
