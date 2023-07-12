import os
import openai
from dotenv import load_dotenv
import csv

def create_response(line):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
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
                "content": line
            },
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)

# load_dotenv()
# api_key = os.getenv("OPENAI_API_KEY")
# openai.api_key = api_key

with open('data1_val_23cent.csv', 'r', encoding='utf-8') as f:
    rdr = csv.reader(f)
    for line in rdr:
        create_response(line[3])
