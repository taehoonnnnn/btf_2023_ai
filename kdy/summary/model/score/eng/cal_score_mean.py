import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('add_6_keyword_nltk.csv')

# 각 컬럼의 평균 계산하기
GloVe = df['GloVe'].mean()
fasttext = df['FastText'].mean()
USE = df['USE'].mean()
SBERT = df['SBERT'].mean()
score_keyword = df['score_keyword'].mean()
score_keyword_nltk = df['score_keyword_nltk'].mean()

# 결과를 데이터 프레임으로 저장
df_mean = pd.DataFrame({
    "description": ["영어 default"],
    "GloVe" : [GloVe],
    'fasttext': [fasttext],
    'USE': [USE],
    'SBERT': [SBERT],
    'score_keyword': [score_keyword],
    'keyword_nltk': [score_keyword_nltk],
})

# 데이터 프레임을 CSV 파일로 저장
df_mean.to_csv('averages.csv', mode='a', header=False, index=False)

