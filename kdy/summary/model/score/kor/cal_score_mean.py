import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('add_7_keyword_konlpy.csv')

# 각 컬럼의 평균 계산하기
keyword_konlpy = df['keyword_konlpy'].mean()
koelectra = df['KoELECTRA'].mean()
kobert = df['KoBERT'].mean()
fasttext = df['FastText'].mean()
use = df['USE'].mean()
sbert = df['SBERT'].mean()
score_keyword = df['score_keyword'].mean()

# 결과를 데이터 프레임으로 저장
df_mean = pd.DataFrame({
    "description": ["한국어 default"],
    'koelectra': [koelectra],
    'kobert': [kobert],
    'fasttext': [fasttext],
    'use': [use],
    'sbert': [sbert],
    'score_keyword': [score_keyword],
    'keyword_konlpy': [keyword_konlpy],
})

# 데이터 프레임을 CSV 파일로 저장
df_mean.to_csv('averages.csv', mode='a', header=False, index=False)
